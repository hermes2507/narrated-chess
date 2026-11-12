# Narrated Chess

One hundred historic chess games (1834–2023), in two forms.

Idea and concept by **Santiago Rentería**, co-created with **Claude Code** (Claude Fable 5.2).

## Web: Bureau for Chess Narration
Open `web/index.html` in a browser (no server needed), or visit the GitHub Pages site.
Each game is called move by move by a football announcer or a baseball announcer
(board becomes a pitch, or turns 45° into a diamond). Optional spoken voice and
synthesised crowd. Each game page also carries its "exercise in style", and the
menu has a download link for the book.

## Book: Play by Play
- `book/Play_by_Play.pdf` — print-ready interior: 7 × 10 in, 206 pages, black and white,
  no bleed, mirrored margins (inside 0.875 in), all fonts embedded.
- `book/Play_by_Play_cover.pdf` — wrap cover with 0.125 in bleed and a 0.464 in spine
  (KDP white paper, 206 pages). The white box on the back is the barcode zone.

Left pages: the score as concrete poetry (calligram, spiral, river, sixty-four squares,
rain, sunburst). Right pages: the game retold in the manner of a different author.

- `web/Play_by_Play.pdf` — reading edition for download: front cover + interior + back cover
  in one file (208 pages). This is what the site links to.

## Rebuild
    .venv/bin/python3 build/build_data.py     # analysis + commentary -> web/games.js, data/book.json
    .venv/bin/python3 build/make_pdf.py       # print interior, print cover, and web/ reading edition

- `data/hundred.pgn`, `data/games.json` — the 100 validated games
- `build/styles.py` — the 100 author pastiches (edit text here)
- `build/commentary.py` — football and baseball phrase banks
- `build/index_raw.py`, `build/select_games.py` — only needed to re-pick games from
  pgnmentor.com player archives (the raw downloads were removed).

## Credits and licence
- Website design inspired by the [Bureau for Listening](https://bureauforlistening.com). Not affiliated.
- Method after Raymond Queneau, *Exercices de style* (1947). Game scores from public archives, mainly pgnmentor.com.
- **Copy it, remix it, pass it on.** Code: MIT License (`LICENSE`). Book text and PDFs:
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), so anything is allowed, even selling, as long as you credit
  Santiago Rentería and say what you changed. `NOTICE.md` has the details and a ready-made credit line.
