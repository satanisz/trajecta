"""Save textual HTML editions of the two openly available web books.

Images, interactive widgets and styles may still require internet access.
Only same-book HTML documents are collected; this is not an offline site mirror.
"""
import concurrent.futures
from html import escape
from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
from urllib.parse import urljoin, urlparse, urldefrag
from urllib.request import Request, urlopen

ROOT=Path(__file__).resolve().parents[1]

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]
    def handle_starttag(self, tag, attrs):
        if tag=='a':
            href=dict(attrs).get('href')
            if href: self.links.append(href)

def get(url):
    with urlopen(Request(url,headers={'User-Agent':'TRAJECTA-Research-Library/0.1'}),timeout=30) as r:
        return r.read(8_000_000).decode('utf-8')

def save_book(book, seeds, prefix, recursive):
    directory=ROOT/'publications/files/books'/book
    directory.mkdir(parents=True,exist_ok=True)
    visited=set(); todo=set(seeds); records=[]; failures=[]
    while todo:
        batch=sorted(todo-visited); todo=set()
        if not batch: break
        if len(visited)+len(batch)>250: raise RuntimeError('book page limit exceeded')
        def fetch(url):
            try: return url,get(url),None
            except Exception as e: return url,None,str(e)
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            results=list(pool.map(fetch,batch))
        for url,body,error in results:
            visited.add(url)
            if error:
                failures.append({'url':url,'error':error}); continue
            if len(body)<500 or '<html' not in body.lower() and '<section' not in body.lower() and '<div' not in body.lower():
                failures.append({'url':url,'error':'No substantial HTML document'}); continue
            name=urlparse(url).path.rsplit('/',1)[-1] or 'preface.html'
            # Preserve source attribution and resolve remote illustrations from the source.
            body='<!doctype html><meta charset="utf-8"><base href="'+escape(url,quote=True)+'"><p>Source: <a href="'+escape(url,quote=True)+'">'+escape(url)+'</a></p>\n'+body
            path=directory/name; path.write_text(body,encoding='utf-8')
            records.append({'url':url,'file':name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
            if recursive:
                parser=Links(); parser.feed(body)
                for href in parser.links:
                    dest=urldefrag(urljoin(url,href))[0]
                    if dest.startswith(prefix) and urlparse(dest).path.endswith('.html') and not urlparse(dest).query:
                        todo.add(dest)
    items='\n'.join('<li><a href="'+r['file']+'">'+r['file']+'</a></li>' for r in records)
    (directory/'index.html').write_text('<!doctype html><meta charset="utf-8"><h1>'+book+'</h1><p>Local text edition. Illustrations and interactive resources may need internet.</p><ul>'+items+'</ul>',encoding='utf-8')
    (directory/'manifest.json').write_text(json.dumps({'records':records,'failures':failures},indent=2),encoding='utf-8')
    print(f'{book}: {len(records)} HTML documents; {len(failures)} failures')

if __name__=='__main__':
    save_book('forecasting-book',['https://otexts.com/fpppy/'],'https://otexts.com/fpppy/',True)
    save_book('network-book',[f'https://www.networksciencebook.com/translations/en/partials/ch-{i}.html' for i in range(12)],'https://www.networksciencebook.com/',False)
