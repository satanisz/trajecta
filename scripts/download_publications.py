"""Download catalogued public copies; never treat HTML as a PDF.

Run from any directory. Uses only the Python standard library.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
MAX_BYTES = 100 * 1024 * 1024


def read_url(url, system_client=False):
    if not system_client:
        request = Request(url, headers={'User-Agent': 'TRAJECTA-Research-Library/0.1'})
        with urlopen(request, timeout=35) as response:
            return response.read(MAX_BYTES + 1), response.url
    # Optional system trust store/client for servers incompatible with urllib.
    # TLS verification remains enabled; redirects must also use HTTPS.
    client = shutil.which('curl.exe') or shutil.which('curl')
    if client is None:
        raise RuntimeError('--system-client requires curl on PATH')
    with tempfile.TemporaryDirectory(prefix='trajecta-') as temporary:
        path = Path(temporary)/'download.pdf'
        result = subprocess.run([
            client, '--silent', '--show-error', '--fail', '--location',
            '--proto', '=https', '--proto-redir', '=https',
            '--max-time', '35', '--max-filesize', str(MAX_BYTES),
            '--output', str(path), '--write-out', '%{url_effective}', url,
        ], capture_output=True, text=True, timeout=40, check=True)
        return path.read_bytes(), result.stdout.strip()


def fetch(publication, system_client=False):
    p = publication
    if not re.fullmatch(r'[a-z0-9-]+', p['id']) or not re.fullmatch(r'[a-z0-9-]+', p['category']):
        raise ValueError('Unsafe catalog path')
    path = ROOT / 'publications' / 'files' / p['category'] / (p['id'] + '.pdf')
    result = {'id': p['id'], 'status': 'unavailable', 'attempts': []}
    if path.exists():
        body = path.read_bytes()
        if not body.startswith(b'%PDF-') or b'%%EOF' not in body[-4096:]:
            raise ValueError(f'Existing file is not a complete PDF: {path}')
        result.update(status='cached', path=path.relative_to(ROOT).as_posix(),
                      bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
        return result
    for url in p['download_urls']:
        try:
            if not url.startswith('https://'):
                raise ValueError('Only HTTPS downloads are accepted')
            body, resolved = read_url(url, system_client)
            if len(body) > MAX_BYTES:
                raise ValueError('Download exceeds 100 MiB')
            if not body.startswith(b'%PDF-') or b'%%EOF' not in body[-4096:]:
                raise ValueError('Response is not a complete PDF (HTML/challenge/preview?)')
            path.parent.mkdir(parents=True, exist_ok=True)
            temporary = path.with_suffix('.pdf.part')
            temporary.write_bytes(body)
            temporary.replace(path)
            result.update(status='downloaded', url=url, resolved_url=resolved,
                          path=path.relative_to(ROOT).as_posix(), bytes=len(body),
                          sha256=hashlib.sha256(body).hexdigest())
            break
        except Exception as exc:
            result['attempts'].append({'url': url, 'error': str(exc)})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--id', action='append', help='Download only this catalog ID; repeatable')
    parser.add_argument('--list', action='store_true', help='List entries without accessing the network')
    parser.add_argument('--system-client', action='store_true', help='Use installed curl with system TLS validation')
    args = parser.parse_args()
    publications = json.loads((ROOT/'publications/catalog.json').read_text(encoding='utf-8'))['publications']
    if args.id:
        unknown = set(args.id) - {p['id'] for p in publications}
        if unknown:
            parser.error(f'Unknown IDs: {sorted(unknown)}')
        publications = [p for p in publications if p['id'] in args.id]
    if args.list:
        for p in publications:
            print(f"{p['id']}: {len(p['download_urls'])} PDF source(s)")
        return
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda p: fetch(p, args.system_client), publications))
    report_path = ROOT/'local/download-report.json'
    report_path.parent.mkdir(parents=True, exist_ok=True)
    # Keep successful provenance when a rerun sees a cached file.
    previous = {}
    if report_path.exists():
        previous = {r['id']:r for r in json.loads(report_path.read_text(encoding='utf-8'))['results']}
    for result in results:
        old = previous.get(result['id'], {})
        if result['status'] == 'cached' and old.get('sha256') == result['sha256']:
            for key in ['url', 'resolved_url']:
                if key in old: result[key] = old[key]
        previous[result['id']] = result
        print(f"{result['id']}: {result['status']}")
    report_path.write_text(json.dumps({'checked_at':datetime.now(timezone.utc).isoformat(),
                                      'results':list(previous.values())}, indent=2), encoding='utf-8')
    failed = sum(r['status'] == 'unavailable' for r in results)
    print(f'{len(results)-failed}/{len(results)} available as local PDFs. HTML books use download_web_books.py. Report: local/download-report.json')


if __name__ == '__main__':
    main()
