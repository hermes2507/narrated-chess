"""Scan the downloaded PGN collections and build a light index (headers + movetext)."""
import re, glob, pickle, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
games = []
seen = set()
for f in sorted(glob.glob(os.path.join(ROOT, 'data/raw/*.pgn'))):
    txt = open(f, encoding='latin-1').read().replace('\r', '')
    for chunk in re.split(r'\n(?=\[Event )', txt):
        hdr = dict(re.findall(r'\[(\w+) "([^"]*)"\]', chunk))
        body = re.sub(r'\[[^\]]*\]\n', '', chunk).strip()
        if not hdr.get('White') or not body: continue
        body = re.sub(r'\{[^}]*\}', '', body)
        body = ' '.join(body.split())
        key = re.sub(r'\d+\.|\s|1-0|0-1|1/2-1/2|\*', '', body)[:400] + hdr.get('White','')[:4]
        if key in seen: continue
        seen.add(key)
        nmoves = len(re.findall(r'\d+\.', body))
        games.append(dict(h=hdr, body=body, n=nmoves, src=os.path.basename(f)))
pickle.dump(games, open(os.path.join(ROOT, 'data/index.pkl'), 'wb'))
print(len(games), 'unique games')
