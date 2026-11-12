# Publishing on Amazon KDP (paperback)

Four print-ready files, two books. Each book is set up as its own paperback in KDP
(Bookshelf → + Create → Paperback).

| Book | Interior (upload as "Manuscript") | Cover (upload as "Book Cover", *Upload a cover you already have*) |
|---|---|---|
| *Play by Play* (English) | `Play_by_Play_KDP_interior.pdf` | `Play_by_Play_KDP_cover.pdf` |
| *Jugada a jugada* (Spanish) | `Jugada_a_jugada_KDP_interior.pdf` | `Jugada_a_jugada_KDP_cover.pdf` |

## Print options: choose exactly these
The files are built for these settings. Change any of them and the cover no longer fits.

- **Ink and paper:** Black & white interior with **white** paper
- **Trim size:** 7 × 10 in (17.78 × 25.4 cm)
- **Bleed settings:** **No bleed**
- **Paperback cover finish:** Matte (suits the black cover; Glossy also works)
- **Page count:** 206 (KDP reads it from the PDF)

What the files already meet (checked when they were built):
- Interior: 206 pages of 7 × 10 in, every font embedded, inks in black-only greys, no ink within 0.25 in
  of the outer edges or 0.5 in of the spine (KDP's minimums for this length), no blank pages. Prose and labels
  are at least 7 pt; only the score-poems go smaller, as artwork (long games pack hundreds of moves into one figure).
- Cover: one page of 14.714 × 10.25 in = 0.125 in bleed + 7 in back + 0.464 in spine + 7 in front + 0.125 in bleed.
  The spine width is KDP's white-paper figure (206 × 0.002252 in). Spine text keeps clear of the spine edges.
  The white box at the bottom right of the back cover is where KDP prints the barcode.

## Details: paste these in

### English
- **Language:** English
- **Book title:** Play by Play
- **Subtitle:** One Hundred Chess Games, One Hundred Voices
- **Author:** Sergio Santiago Rentería Aguilar
- **Edition number:** 1
- **Description:**
  > A hundred of the most famous chess games ever played, from London in 1834 to Astana in 2023.
  > On every left-hand page, the moves themselves, typeset as concrete poetry: spirals, rivers, rain,
  > the silhouette of the piece that struck the last blow. On every right-hand page, the game retold
  > in the manner of a different writer, from Homer to Sei Shōnagon to Raymond Chandler.
  > Exercises in style for sixty-four squares.
- **Keywords (up to 7):** chess history; famous chess games; concrete poetry; exercises in style; Queneau;
  literary parody; chess gift
- **Categories (suggestions):** Games & Activities › Chess; Poetry › Subjects & Themes; Humor › Parodies

### Spanish
- **Language:** Spanish
- **Book title:** Jugada a jugada
- **Subtitle:** Cien partidas de ajedrez, cien voces
- **Author:** Sergio Santiago Rentería Aguilar
- **Edition number:** 1
- **Description:**
  > Cien de las partidas de ajedrez más famosas de la historia, de Londres en 1834 a Astaná en 2023.
  > En cada página izquierda, las jugadas mismas, compuestas como poesía concreta: espirales, ríos, lluvia,
  > la silueta de la pieza que dio el último golpe. En cada página derecha, la partida contada a la manera
  > de un escritor distinto, de Homero a Sei Shōnagon y Raymond Chandler. Ejercicios de estilo para
  > sesenta y cuatro casillas.
- **Keywords:** historia del ajedrez; partidas famosas de ajedrez; poesía concreta; ejercicios de estilo;
  Queneau; parodia literaria; regalo ajedrez
- **Categories (suggestions):** the same three as the English book.

### Questions KDP will ask
- **AI-generated content:** answer **Yes**. KDP asks this on every new title. The text, code and typesetting
  were co-created with Claude Code (the colophon says so), so the honest answer is yes for text.
  This is disclosed to Amazon only; it is not shown on the store page.
- **Public domain content:** No. The text is original (pastiches and parody), and the game scores are facts.
- **Adult content:** No.
- **Low-content book:** No.

## ISBN
Each book (English and Spanish) needs its own ISBN. The simplest option is KDP's **free ISBN**
("Get a free KDP ISBN"). It makes Independently published the imprint and works only for Amazon distribution.
After KDP assigns them, you can print them on the copyright page:
1. Put them in `ISBN = {'en': '…', 'es': '…'}` near the top of `build/make_pdf.py`.
2. Run `.venv/bin/python3 build/make_pdf.py`.
3. Upload the new interiors.

This is optional: KDP prints the ISBN on the barcode either way.

## Pricing
KDP shows the printing cost and the minimum price on the Pricing page after the files upload. For a
206-page black-and-white paperback the printing cost is a few dollars per copy. Use KDP's own figure;
their rates change.

## Before publishing
1. Upload both files and open **Launch Previewer**. Fix anything it flags. It should flag nothing.
2. Order a **printed proof** of each book. It costs about the printing price and is the only way to see the
   greys and the tiny type in the score-poems on real paper.
3. The book is CC BY 4.0. Anyone may also print and sell it, as long as they credit you.

## Rebuilding
    .venv/bin/python3 build/build_data.py
    .venv/bin/python3 build/make_pdf.py      # writes these four files and the two web reading editions

If the page count ever changes, the build widens or narrows the spine to match, but KDP must also be told
the new page count (re-upload both files). A new edition: change `EDITION`/`EDITION_MONTH` in
`build/make_pdf.py` and `EDITION` in `web/app.js`.
