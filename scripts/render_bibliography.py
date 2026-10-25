"""Render the Markdown bibliography from the audited catalog; no network access."""
from collections import Counter
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GROUPS = {
    'markov-and-master-equation': 'Procesy Markowa, Master Equation i trajektorie',
    'process-and-temporal-models': 'Modele zdarzeń, procesów i grafów czasowych',
    'economics-and-applications': 'Sieci gospodarcze, handel i zastosowania',
    'books': 'Książki i materiały przekrojowe',
}


def main():
    catalog = json.loads((ROOT/'publications/catalog.json').read_text(encoding='utf-8'))
    entries = catalog['publications']
    counts = Counter(p['snapshot']['status'] for p in entries)
    lines = [
        '# Bibliografia TRAJECTA', '',
        'Źródło: czat „Pragma i Master Equation”. Audyt i lokalny stan plików: **2026-10-25**.', '',
        f"**{len(entries)} pozycji: {counts['pdf']} PDF-ów, {counts['html_text']} książki jako tekst HTML, {counts['unavailable']} braków pełnego tekstu.**", '',
        'Pliki publikacji są ignorowane przez Git. Poniższy stan opisuje bibliotekę lokalną w dniu audytu; samo sklonowanie repozytorium ich nie pobiera.', '',
        'Krótkie opisy wskazują rolę materiału w projekcie. Nie są recenzją naukową ani potwierdzeniem wyników. Zasady audytu: [README](README.md).', '',
        '## Brakujące pełne teksty', '',
        '| ID | Publikacja | Przyczyna |', '| --- | --- | --- |',
    ]
    for p in entries:
        if p['snapshot']['status']=='unavailable':
            lines.append(f"| `{p['id']}` | [{p['title']}]({p['source_url']}) | {p['snapshot']['reason']} |")
    for category, title in GROUPS.items():
        lines += ['', f'## {title}', '']
        for p in entries:
            if p['category'] != category: continue
            s=p['snapshot']
            lines += [f"<a id=\"{p['id']}\"></a>", '', f"### {p['title']} ({p['year']})", '',
                      f"ID: `{p['id']}` · [Źródło]({p['source_url']}) · Weryfikacja: `{p['verification']}`.", '']
            if p.get('authors'): lines += ['Autorzy: '+ '; '.join(p['authors'])+'.', '']
            lines += [p['summary_pl'], '']
            if s['status']=='pdf':
                lines += [f"Lokalnie: `{s['path']}` · {s['pages']} stron · [Pobrana kopia]({s['download_url']}).", '',
                          f"SHA-256: `{s['sha256']}`.", '']
            elif s['status']=='html_text':
                lines += [f"Lokalnie: `{s['path']}` · {s['documents']} dokumentów HTML; multimedia mogą wymagać internetu.", '']
            else: lines += ['**Brak pełnego tekstu:** '+s['reason'], '']
            for note in p['notes']: lines += ['Uwaga: '+note, '']
    (ROOT/'publications/BIBLIOGRAPHY.md').write_text('\n'.join(lines).rstrip()+'\n',encoding='utf-8')
    print(f'Rendered {len(entries)} entries.')


if __name__ == '__main__':
    main()
