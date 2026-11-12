# Narrated Chess

One hundred historic chess games (1834–2023), in two forms and two languages, English and Spanish.

Idea and concept by **Sergio Santiago Rentería Aguilar**, co-created with **Claude Code** (Claude Fable 5.2; Spanish edition with Claude Opus 5.5).

## Web: Bureau for Chess Narration
Open `web/index.html` in a browser (no server needed), or visit the GitHub Pages site.
Each game is called move by move by a football announcer or a baseball announcer
(board becomes a pitch, or turns 45° into a diamond). Optional spoken voice and
synthesised crowd. Each game page also carries its "exercise in style", and the
menu has download links for both books.

**EN / ES** in the top bar switches everything to Spanish: the page, the hundred exercises, the
commentary (written anew in Spanish, not machine-translated: a goal-calling football narrator and a
Caribbean-radio baseball man), Spanish algebraic notation (R D T A C), and the spoken voice
(es-ES voice for football, es-MX/es-US for baseball, whatever the browser has). The choice is
remembered; `?lang=es` in the address forces it; Spanish-language browsers start in Spanish.
The Spanish texts live in `web/games_es.js`, loaded only when needed.

## Book: Play by Play / Jugada a jugada
- `kdp/` — **print-ready files for Amazon KDP**, both languages: `*_KDP_interior.pdf` (7 × 10 in, 206 pages,
  black and white, no bleed, mirrored margins, all fonts embedded) and `*_KDP_cover.pdf` (wrap cover with
  0.125 in bleed and a 0.464 in spine). `kdp/KDP_SETUP.md` has the exact KDP settings and the text to paste in.
- `web/Play_by_Play.pdf` — reading edition for download: front cover + interior + back cover
  in one file (208 pages). This is what the site links to.
- `web/Jugada_a_jugada.pdf` — the Spanish reading edition, same layout and page count, scores in Spanish notation.

**Edition:** both books are the *first edition, November 2026*, printed on the title page, colophon,
front and back covers. To issue a new edition, change `EDITION` / `EDITION_MONTH` in `build/make_pdf.py`
and `EDITION` in `web/app.js`, then rebuild.

## Rebuild
    .venv/bin/python3 build/build_data.py     # analysis + commentary -> web/games.js, data/book.json
    .venv/bin/python3 build/make_pdf.py       # both languages: kdp/ print interior + cover, web/ reading edition
    .venv/bin/python3 build/make_pdf.py es 2 17   # quick sample of a few games -> kdp/sample.pdf

- `data/hundred.pgn`, `data/games.json` — the 100 validated games
- `build/styles.py` — the 100 author pastiches (edit text here); `build/styles_es.py` — their Spanish versions
- `build/commentary.py` — football and baseball phrase banks; `build/commentary_es.py` — the Spanish booths
- `build/i18n_es.py` — Spanish game names, places, events, openings, authors and notation
- `build/index_raw.py`, `build/select_games.py` — only needed to re-pick games from
  pgnmentor.com player archives (the raw downloads were removed).

## Credits and licence
- Website design inspired by the [Bureau for Listening](https://bureauforlistening.com). Not affiliated.
- Method after Raymond Queneau, *Exercices de style* (1947). Game scores from public archives, mainly pgnmentor.com.
- **Copy it, remix it, pass it on.** Code: MIT License (`LICENSE`). Book text and PDFs:
  [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), so anything is allowed, even selling, as long as you credit
  Sergio Santiago Rentería Aguilar and say what you changed. `NOTICE.md` has the details and a ready-made credit line.
