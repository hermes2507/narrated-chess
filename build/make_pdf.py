"""Typeset the book as a print-ready interior (7 x 10 in, black and white, no bleed,
mirrored margins) plus a wrap-around cover sized for the page count.
Each game is one spread: verso = the score as a concrete poem, recto = the game told
in the manner of a different author (see styles.py)."""
import json, math, os, sys
from PIL import Image, ImageDraw, ImageFont
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import stringWidth as sw
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.platypus import Paragraph

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUP = '/System/Library/Fonts/Supplemental/'
for name, f, i in [('Serif', 'Baskerville.ttc', 0), ('SerifB', 'Baskerville.ttc', 4), ('SerifI', 'Baskerville.ttc', 2),
                   ('Didot', 'Didot.ttc', 0), ('DidotI', 'Didot.ttc', 1),
                   ('TypeB', 'AmericanTypewriter.ttc', 2),
                   ('Mono', 'Courier New.ttf', 0), ('MonoB', 'Courier New Bold.ttf', 0)]:
    pdfmetrics.registerFont(TTFont(name, SUP + f, subfontIndex=i))
SYMBOLS = '/System/Library/Fonts/Apple Symbols.ttf'

IN = 72
PW, PH = 7 * IN, 10 * IN              # trim size
INSIDE, OUTSIDE, TOP, BOTTOM = 0.875 * IN, 0.6 * IN, 0.75 * IN, 0.8 * IN
INK, MOVE, GREY, FAINT, HOTC = black, HexColor('#3d3d3d'), HexColor('#8a8a8a'), HexColor('#cfcfcf'), black
GLYPH = {'king': '♚', 'queen': '♛', 'rook': '♜', 'bishop': '♝', 'knight': '♞', 'pawn': '♟'}
RES = {'1-0': '1–0', '0-1': '0–1', '1/2-1/2': '½–½'}
HOT = set('x+#=')


def tokens(g):
    out = []
    for i, p in enumerate(g['plies']):
        if i % 2 == 0:
            out += [(ch, 'n') for ch in f"{i // 2 + 1}."]
        out += [(ch, 'h' if ch in HOT else 'w') for ch in p['san']]
        out.append((' ', 's'))
    return out[:-1]


def colour(kind):
    return {'n': GREY, 'h': HOTC, 'w': MOVE, 's': MOVE}[kind]


def rich(c, x, y, s, font, fs, col=MOVE, align='l', hotfont='MonoB'):
    """Draw a move; the marks of contact (x + # =) are set heavier and blacker."""
    w = sw(s, font, fs)
    x = x - w if align == 'r' else x - w / 2 if align == 'c' else x
    for ch in s:
        hot = ch in HOT
        c.setFillColor(HOTC if hot else col)
        c.setFont(hotfont if hot and font.startswith('Mono') else font, fs)
        c.drawString(x, y, ch)
        x += sw(ch, font, fs)


# ------------------------------------------------------------------ the six forms
_mask_cache = {}


def glyph_mask(piece):
    if piece not in _mask_cache:
        im = Image.new('L', (1000, 1000), 0)
        ImageDraw.Draw(im).text((100, 60), GLYPH[piece], font=ImageFont.truetype(SYMBOLS, 760), fill=255)
        _mask_cache[piece] = im.crop(im.getbbox())
    return _mask_cache[piece]


def form_calligram(c, g, box, text=None, piece=None, cap=8.6):
    """The notation poured into the silhouette of the piece that made the last move."""
    x0, y0, W, H = box
    piece = piece or g['plies'][-1]['piece']
    mask = glyph_mask(piece)
    toks = text or tokens(g)
    asp = mask.width / mask.height
    w, h = (W, W / asp) if W / asp <= H else (H * asp, H)

    def grid(w, h, fs):
        cols, rows = max(1, int(w / (0.6 * fs))), max(1, int(h / (fs * 0.98)))
        small = mask.resize((cols, rows), Image.BOX)
        return [(r, q) for r in range(rows) for q in range(cols) if small.getpixel((q, r)) > 120]
    fs = cap
    cells = grid(w, h, fs)
    if len(cells) < len(toks):                      # long game: smaller type
        while fs > 2.5 and len(cells) < len(toks):
            fs -= 0.15; cells = grid(w, h, fs)
    else:                                           # short game: smaller figure, then an echo
        k = 1 if text else max(0.74, math.sqrt(len(toks) / len(cells)) * 1.02)
        w, h = w * k, h * k
        cells = grid(w, h, fs)
    ox, oy = x0 + (W - w) / 2, y0 + (H - h) / 2
    for k, (r, q) in enumerate(cells):
        if text and k >= len(toks):
            break
        ch, kind = toks[k % len(toks)]
        if ch == ' ':
            continue
        ghost = k >= len(toks) and text is None
        c.setFont('MonoB', fs)
        c.setFillColor(FAINT if ghost else colour(kind))
        c.drawString(ox + q * 0.6 * fs, oy + h - (r + 1) * fs * 0.98, ch)
    return f"calligram: {piece}"


def form_spiral(c, g, box):
    """One line of notation wound inward; the last move arrives at the centre."""
    x0, y0, W, H = box
    cx, cy = x0 + W / 2, y0 + H / 2
    toks = tokens(g)
    R, r_in = min(W, H) / 2 - 2, 30
    fs = min(16.5, math.sqrt(math.pi * (R * R - r_in * r_in) / (1.22 * 0.6 * len(toks))))
    pitch, adv = 1.22 * fs, 0.6 * fs
    r = math.sqrt(r_in * r_in + len(toks) * adv * pitch / math.pi)
    th = math.pi / 2
    for ch, kind in toks:
        if ch != ' ':
            c.saveState()
            c.translate(cx + r * math.cos(th), cy + r * math.sin(th))
            c.rotate(math.degrees(th) - 90)
            c.setFont('MonoB', fs); c.setFillColor(colour(kind))
            c.drawString(0, 0, ch)
            c.restoreState()
        dth = adv / r
        th -= dth
        r -= pitch * dth / (2 * math.pi)
    c.setFillColor(INK); c.setFont('TypeB', 19)
    c.drawCentredString(cx, cy - 6, RES[g['result']])
    return "spiral"


def form_board(c, g, box):
    """Every move written on the square where it landed: the geography of the game."""
    x0, y0, W, H = box
    cell = min(W, H) / 8
    bx, by = x0 + (W - 8 * cell) / 2, y0 + (H - 8 * cell) / 2
    sq = {}
    for i, p in enumerate(g['plies']):
        sq.setdefault(p['to'], []).append((i, p))
    for f in range(8):
        for r in range(8):
            name = 'abcdefgh'[f] + str(r + 1)
            X, Y = bx + f * cell, by + r * cell
            if (f + r) % 2 == 0:
                c.setFillColor(HexColor('#ececec')); c.rect(X, Y, cell, cell, stroke=0, fill=1)
            ms = sq.get(name, [])
            if not ms:
                continue
            cols = (len(ms) + 5) // 6
            rows = math.ceil(len(ms) / cols)
            longest = max(len(p['san']) for _, p in ms)
            fs = min(9, (cell - 3) / (rows * 1.06), (cell - 3) / (cols * (longest + 0.4) * 0.6))
            for k, (i, p) in enumerate(ms):
                col, row = k // rows, k % rows
                tx = X + (col + 0.5) * cell / cols
                ty = Y + cell - (cell - rows * fs * 1.06) / 2 - (row + 0.8) * fs * 1.06
                if i == len(g['plies']) - 1:          # the last move: reversed out
                    wd = sw(p['san'], 'MonoB', fs)
                    c.setFillColor(INK); c.rect(tx - wd / 2 - 1.5, ty - fs * 0.25, wd + 3, fs * 1.05, stroke=0, fill=1)
                    c.setFillColor(white); c.setFont('MonoB', fs); c.drawCentredString(tx, ty, p['san'])
                else:
                    rich(c, tx, ty, p['san'], 'MonoB' if p['white'] else 'Mono', fs, INK if p['white'] else MOVE, 'c')
    c.setFont('Mono', 6); c.setFillColor(GREY)
    for k in range(8):
        c.drawCentredString(bx + (k + 0.5) * cell, by - 10, 'abcdefgh'[k])
        c.drawRightString(bx - 5, by + (k + 0.5) * cell - 2, str(k + 1))
    c.setStrokeColor(INK); c.setLineWidth(0.5); c.rect(bx, by, 8 * cell, 8 * cell, stroke=1, fill=0)
    return "sixty-four squares"


def form_rain(c, g, box):
    """Files as columns, time as gravity. A thread follows the play from square to square."""
    x0, y0, W, H = box
    n = len(g['plies'])
    colw = W / 8
    top = y0 + H - 34
    rowh = (top - y0) / n
    fs = max(4.6, min(10, rowh * 1.2))
    for k in range(8):
        c.setFont('Didot', 20); c.setFillColor(INK); c.drawCentredString(x0 + (k + 0.5) * colw, y0 + H - 16, 'abcdefgh'[k])
        c.setStrokeColor(FAINT); c.setLineWidth(0.3)
        c.line(x0 + (k + 0.5) * colw, top, x0 + (k + 0.5) * colw, y0)
    pts = [(x0 + ('abcdefgh'.index(p['to'][0]) + 0.5) * colw, top - (i + 0.7) * rowh) for i, p in enumerate(g['plies'])]
    c.setStrokeColor(GREY); c.setLineWidth(0.4)
    path = c.beginPath(); path.moveTo(*pts[0])
    for pt in pts[1:]:
        path.lineTo(*pt)
    c.drawPath(path)
    for (x, y), p in zip(pts, g['plies']):
        w = sw(p['san'], 'MonoB', fs)
        c.setFillColor(white); c.rect(x - w / 2 - 1, y - fs * 0.22, w + 2, fs * 0.95, stroke=0, fill=1)
        rich(c, x, y, p['san'], 'MonoB' if p['white'] else 'Mono', fs, INK if p['white'] else MOVE, 'c')
    return "rain"


def form_sunburst(c, g, box):
    """A clock of moves. Each ray stands as far from the centre as the move was loud."""
    x0, y0, W, H = box
    cx, cy = x0 + W / 2, y0 + H / 2
    n = len(g['plies'])
    fs = max(5.0, min(12.5, 2 * math.pi * 80 / n))
    r0 = max(70, n * fs * 0.98 / (2 * math.pi))
    reach = min(W, H) / 2 - r0 - 7 * 0.6 * fs
    c.setStrokeColor(FAINT); c.setLineWidth(0.3); c.circle(cx, cy, r0 - 4, stroke=1, fill=0)
    for i, p in enumerate(g['plies']):
        th = math.pi / 2 - 2 * math.pi * i / n
        rr = r0 + max(0, reach) * min(p['ex'], 14) / 14
        c.saveState(); c.translate(cx, cy)
        c.setStrokeColor(INK if p['ex'] >= 6 else FAINT); c.setLineWidth(0.4)
        c.line((r0 - 4) * math.cos(th), (r0 - 4) * math.sin(th), (rr - 1.5) * math.cos(th), (rr - 1.5) * math.sin(th))
        font, col = ('MonoB', INK) if p['white'] else ('Mono', MOVE)
        if math.cos(th) >= 0:
            c.rotate(math.degrees(th)); rich(c, rr, -fs * 0.3, p['san'], font, fs, col, 'l')
        else:
            c.rotate(math.degrees(th) + 180); rich(c, -rr, -fs * 0.3, p['san'], font, fs, col, 'r')
        c.restoreState()
    c.setFillColor(INK); c.setFont('TypeB', min(26, r0 * 0.5))
    c.drawCentredString(cx, cy - min(26, r0 * 0.5) * 0.33, RES[g['result']])
    return "sunburst"


def form_river(c, g, box):
    """White on the left bank, Black on the right. The river bends toward whoever is ahead."""
    x0, y0, W, H = box
    pl = g['plies']
    nm = (len(pl) + 1) // 2
    rowh = min(H / nm, 26)
    y_top = y0 + H - (H - rowh * nm) / 2
    base = min(12.5, rowh * 0.92)
    cx0 = x0 + W / 2
    pts = []
    for m in range(nm):
        w = pl[2 * m]; b = pl[2 * m + 1] if 2 * m + 1 < len(pl) else None
        cx = cx0 + max(-80, min(80, (b or w)['bal'] * 8.5))
        y = y_top - (m + 0.75) * rowh
        pts.append((cx, y + base * 0.3))
        rich(c, cx - 7, y, w['san'], 'SerifB', base * (1 + min(w['ex'], 12) / 21), INK, 'r')
        if b:
            rich(c, cx + 7, y, b['san'], 'SerifI', base * (1 + min(b['ex'], 12) / 21), INK, 'l')
        if (m + 1) % 5 == 0 or m == 0:
            c.setFont('Mono', 5.5); c.setFillColor(GREY); c.drawRightString(x0 + 8, y, str(m + 1))
    c.setStrokeColor(GREY); c.setLineWidth(0.5)
    path = c.beginPath(); path.moveTo(*pts[0])
    for pt in pts[1:]:
        path.lineTo(*pt)
    c.drawPath(path)
    return "river"


FORMS = [form_calligram, form_spiral, form_river, form_board, form_rain, form_sunburst]
ANY_LENGTH = [form_calligram, form_spiral, form_board]


def choose_form(g):
    n = len(g['plies'])
    f = FORMS[(g['id'] - 1) % 6]
    limit = {form_river: 110, form_rain: 110, form_sunburst: 104, form_board: 170}.get(f, 9999)
    if n > limit:
        f = ANY_LENGTH[g['id'] % 2] if n > 170 else ANY_LENGTH[g['id'] % 3]
    return f


# ------------------------------------------------------------------ pages
class Book:
    def __init__(self, path):
        self.c = canvas.Canvas(path, pagesize=(PW, PH), initialFontName='Serif')
        self.c.setTitle('Play by Play: One Hundred Chess Games, One Hundred Voices'); self.c.setAuthor('Chess Narrator')
        self.n = 1

    @property
    def recto(self):
        return self.n % 2 == 1

    def left(self):      # x of the text block's left edge on this page
        return INSIDE if self.recto else OUTSIDE

    def width(self):
        return PW - INSIDE - OUTSIDE

    def folio(self, text=''):
        c = self.c
        c.setFillColor(GREY)
        x = PW - OUTSIDE if self.recto else OUTSIDE
        spaced(c, x, 0.45 * IN, str(self.n), 'MonoB', 7, 1.2, 'r' if self.recto else 'l')
        if text:
            spaced(c, INSIDE if self.recto else PW - INSIDE, 0.45 * IN, text.upper(), 'Mono', 5.8, 1.3, 'l' if self.recto else 'r')

    def next(self):
        self.c.showPage(); self.n += 1


def fit(text, font, size, width):
    while sw(text, font, size) > width and size > 6:
        size -= 0.5
    return size


def spaced(c, x, y, s, font, fs, gap=1.2, align='l'):
    w = sum(sw(ch, font, fs) + gap for ch in s) - gap
    x = x - w if align == 'r' else x - w / 2 if align == 'c' else x
    c.setFont(font, fs)
    for ch in s:
        c.drawString(x, y, ch); x += sw(ch, font, fs) + gap


def markup(text):
    """Plain text -> reportlab paragraphs; keeps verse lines and stepped indents."""
    lines = []
    for ln in text.replace('&', '&amp;').replace('<', '&lt;').split('\n'):
        lead = len(ln) - len(ln.lstrip(' '))
        lines.append('&nbsp;' * lead + ln.lstrip(' '))
    return '<br/>'.join(lines)


def game_spread(b, g):
    c = b.c
    assert not b.recto
    # ---- verso: the poem
    form = choose_form(g)
    label = form(c, g, (b.left(), BOTTOM + 14, b.width(), PH - TOP - BOTTOM - 14))
    b.folio(label)
    b.next()
    # ---- recto: the telling
    L, width = b.left(), b.width()
    y = PH - TOP - 6
    c.setFillColor(INK)
    spaced(c, L, y, f"Exercise {g['id']}  ·  {g['site']}, {g['year']}".upper(), 'Mono', 6.8, 1.5)
    y -= 38
    ts = fit(g['nick'], 'DidotI', 30, width)
    c.setFont('DidotI', ts); c.drawString(L, y, g['nick'])
    y -= 22
    who = f"{g['white']}  —  {g['black']}"
    c.setFont('SerifB', fit(who, 'SerifB', 11.5, width)); c.drawString(L, y, who)
    y -= 14
    sub = f"{g['event']}  ·  {g['opening']}  ·  {RES[g['result']]}"
    c.setFillColor(GREY); c.setFont('SerifI', fit(sub, 'SerifI', 9.5, width)); c.drawString(L, y, sub)
    y -= 30
    c.setFillColor(INK); c.setFont('SerifI', 12); c.drawString(L, y, "in the manner of")
    c.setFont('Didot', 12); spaced(c, L + sw("in the manner of ", 'SerifI', 12) + 2, y, g['author'].upper(), 'Serif', 10.5, 1.4)
    y -= 10
    c.setStrokeColor(INK); c.setLineWidth(0.6); c.line(L, y, L + 30, y)
    y -= 20
    text = g['exercise']
    verse = text.count('\n') >= 3
    size = 12.2
    while True:
        st = ParagraphStyle('p', fontName='Serif', fontSize=size, leading=size * (1.36 if verse else 1.46), textColor=INK,
                            alignment=TA_LEFT if verse else TA_JUSTIFY)
        blocks = [Paragraph(markup(t), st) for t in (text.split('\n\n') if verse else text.split('\n'))]
        hs = [p.wrap(width, 2000)[1] for p in blocks]
        gap = size * (0.9 if verse else 0.45)
        if sum(hs) + gap * (len(hs) - 1) <= y - BOTTOM - 40 or size <= 8.5:
            break
        size -= 0.25
    for p, h in zip(blocks, hs):
        y -= h
        p.drawOn(c, L, y)
        y -= gap
    pl = g['plies']
    c.setFillColor(GREY)
    spaced(c, L, BOTTOM + 4, f"{(len(pl) + 1) // 2} moves  ·  {sum(p['cap'] for p in pl)} captures  ·  {sum(p['check'] for p in pl)} checks".upper(), 'Mono', 5.8, 1.3)
    b.folio()
    b.next()


def front_matter(b, book):
    c = b.c
    # p1 title
    L = b.left()
    c.setFillColor(INK); spaced(c, L, PH - 2.2 * IN, "ONE HUNDRED CHESS GAMES · ONE HUNDRED VOICES", 'Mono', 7, 1.8)
    c.setFont('DidotI', 64); c.drawString(L - 3, PH - 3.3 * IN, "Play")
    c.setFont('Didot', 64); c.drawString(L - 3, PH - 4.2 * IN, "by Play")
    c.setLineWidth(0.8); c.line(L, PH - 4.55 * IN, L + 40, PH - 4.55 * IN)
    st = ParagraphStyle('t', fontName='Serif', fontSize=13, leading=19.5, textColor=INK)
    p = Paragraph("The scores of a hundred historic games,<br/>set as concrete poetry.<br/>The games themselves, told a hundred ways:<br/>"
                  "<font name='SerifI'>exercises in style, after Raymond Queneau.</font>", st)
    w, h = p.wrap(b.width(), 300); p.drawOn(c, L, PH - 4.85 * IN - h)
    c.setFillColor(GREY); spaced(c, L, BOTTOM, "1834 — 2023", 'Mono', 7, 1.8)
    b.next()
    # p2 colophon
    st = ParagraphStyle('n', fontName='Serif', fontSize=9.2, leading=13.4, textColor=INK, spaceAfter=7)
    y = BOTTOM + 2.6 * IN
    for t in ["<font name='SerifB'>Play by Play</font><br/>One Hundred Chess Games, One Hundred Voices",
              "The hundred games in this book were really played. Their scores are reproduced complete in standard algebraic notation and every move was checked for legality.",
              "The hundred prose pieces and poems are pastiches written for this book. Each imitates the manner of a named author; none quotes from any author's work, and none was written, seen or approved by the author it imitates. Scenes, weather, dialogue and inner thoughts are invented.",
              "Set in Baskerville, Didot and Courier New.",
              "First edition."]:
        p = Paragraph(t, st); w, h = p.wrap(b.width() - 60, 500); y -= h; p.drawOn(c, b.left(), y); y -= 7
    b.next()
    # p3 how to read
    st = ParagraphStyle('n', fontName='Serif', fontSize=10.4, leading=15, alignment=TA_JUSTIFY, textColor=INK)
    y = PH - TOP - 10
    for t in [
        "<font name='DidotI' size='22'>How to read this book</font>", "",
        "<font name='SerifB'>On the left</font> of every opening is the complete score of a game and nothing else. No move has been added or taken away; only the typesetting changes. "
        "The marks of contact, <font name='MonoB'>x</font> for a capture, <font name='MonoB'>+</font> for a check, <font name='MonoB'>#</font> for mate, are set blacker than the moves around them. The score takes one of six forms.",
        "<font name='SerifI'>Calligram.</font> The score is poured into the silhouette of the piece that made the final move. A short game echoes in grey until the figure is full.",
        "<font name='SerifI'>Spiral.</font> One unbroken line, wound clockwise and inward. The last move arrives at the centre, where the result waits.",
        "<font name='SerifI'>River.</font> White's moves on the left bank, Black's on the right. The channel bends toward the side that is ahead in material, and moves grow with their violence.",
        "<font name='SerifI'>Sixty-four squares.</font> Each move is written on the square where it landed. Empty squares were never visited. The last move is reversed out of black.",
        "<font name='SerifI'>Rain.</font> The files are columns and time is gravity. A thread follows the play from one destination to the next, like a ball being passed.",
        "<font name='SerifI'>Sunburst.</font> A clock of moves, read clockwise from noon. The louder the move, the farther it stands from the centre.", "",
        "<font name='SerifB'>On the right</font> the same game is told in words, each time in the manner of a different writer: an epic poet, a hard-boiled novelist, a court diarist, a playwright of the absurd. "
        "The method is borrowed from Raymond Queneau, who in <font name='SerifI'>Exercises in Style</font> told one small story ninety-nine ways. Here the story changes too, and it is always the same story: two people, sixty-four squares, one result.",
        "The voices range over some twenty-seven centuries and most of the inhabited world. The games run in order of date, from London in 1834 to Astana in 2023."]:
        if not t:
            y -= 8; continue
        p = Paragraph(t, st); w, h = p.wrap(b.width(), 600); y -= h; p.drawOn(c, b.left(), y); y -= 8
    b.next()
    # p4-5 contents
    for start in (0, 50):
        c.setFillColor(INK); c.setFont('DidotI', 20); c.drawString(b.left(), PH - TOP - 8, "Contents" if start == 0 else "Contents, continued")
        for k, g in enumerate(book[start:start + 50]):
            y = PH - TOP - 40 - k * 11.6
            x = b.left()
            c.setFillColor(GREY); c.setFont('MonoB', 6.2); c.drawString(x, y, f"{g['id']:03d}")
            c.setFillColor(INK); c.setFont('SerifI', 8.8); c.drawString(x + 20, y, g['nick'])
            c.setFont('Serif', 8.2); c.drawString(x + 178, y, f"{g['ws']} – {g['bs']}, {g['year']}"[:44])
            c.setFillColor(GREY); c.setFont('Serif', 8.2); c.drawRightString(x + b.width() - 22, y, g['author'])
            c.setFillColor(INK); c.setFont('Mono', 6.2); c.drawRightString(x + b.width(), y, str(6 + 2 * (g['id'] - 1) + 1))
        b.folio(); b.next()


def back_matter(b, book):
    c = b.c
    c.setFillColor(INK); c.setFont('DidotI', 20); c.drawString(b.left(), PH - TOP - 8, "The Voices")
    names = sorted(book, key=lambda g: g['author'].split()[-1] if not g['author'].startswith('The ') else g['author'][4:])
    for k, g in enumerate(names):
        col, row = k // 50, k % 50
        x = b.left() + col * (b.width() / 2); y = PH - TOP - 40 - row * 11.6
        c.setFillColor(INK); c.setFont('Serif', 8.6); c.drawString(x, y, g['author'])
        c.setFillColor(GREY); c.setFont('Mono', 6.2); c.drawRightString(x + b.width() / 2 - 18, y, str(6 + 2 * (g['id'] - 1) + 1))
    b.folio(); b.next()


PAPERWHITE = HexColor('#f4f1ea')


def _cover_ink(on):
    """Covers are white on black: swap the palette while drawing them."""
    global MOVE, GREY, FAINT, HOTC, INK
    if on:
        _cover_ink.keep = (MOVE, GREY, FAINT, HOTC, INK)
        MOVE, GREY, HOTC, INK = PAPERWHITE, HexColor('#8d8a84'), PAPERWHITE, PAPERWHITE
    else:
        MOVE, GREY, FAINT, HOTC, INK = _cover_ink.keep


def draw_front(c, book, fx, fy):
    """Front cover artwork with its trim box at (fx, fy)."""
    _cover_ink(True)
    names = ' '.join(f"{g['nick']}." for g in book).replace(' ', '·')
    form_calligram(c, None, (fx + 0.9 * IN, fy + 0.9 * IN, PW - 1.8 * IN, PH - 4.6 * IN),
                   text=[(ch, 'n' if ch == '·' else 'w') for ch in names], piece='knight', cap=7.4)
    c.setFillColor(INK)
    c.setFont('DidotI', 60); c.drawString(fx + 0.7 * IN, fy + PH - 1.55 * IN, "Play")
    c.setFont('Didot', 60); c.drawString(fx + 0.7 * IN + sw("Play ", 'DidotI', 60), fy + PH - 1.55 * IN, "by Play")
    spaced(c, fx + 0.72 * IN, fy + PH - 1.95 * IN, "ONE HUNDRED CHESS GAMES · ONE HUNDRED VOICES", 'Mono', 7.6, 1.9)
    spaced(c, fx + 0.72 * IN, fy + 0.6 * IN, "CONCRETE POEMS & EXERCISES IN STYLE", 'Mono', 7, 1.9)
    _cover_ink(False)


def draw_back(c, bx, by, barcode=True):
    st = ParagraphStyle('b', fontName='Serif', fontSize=12, leading=18, textColor=PAPERWHITE)
    p = Paragraph("A hundred of the most famous chess games ever played, from London in 1834 to Astana in 2023.<br/><br/>"
                  "On every left-hand page, the moves themselves, typeset as concrete poetry: spirals, rivers, rain, the silhouette of the piece that struck the last blow.<br/><br/>"
                  "On every right-hand page, the game retold in the manner of a different writer, from Homer to Sei Shōnagon to Raymond Chandler. "
                  "<font name='SerifI'>Exercises in style</font> for sixty-four squares.", st)
    w, h = p.wrap(PW - 1.8 * IN, 600); p.drawOn(c, bx + 0.9 * IN, by + PH - 1.4 * IN - h)
    if barcode:
        c.setFillColor(white); c.rect(bx + PW - 2.75 * IN, by + 0.5 * IN, 2 * IN, 1.2 * IN, stroke=0, fill=1)


def cover(book, pages):
    """Print wrap: back + spine + front, with 0.125in bleed, spine sized for white paper."""
    spine = pages * 0.002252 * IN
    bleed = 0.125 * IN
    W, Hh = 2 * PW + spine + 2 * bleed, PH + 2 * bleed
    out = os.path.join(ROOT, 'book', 'Play_by_Play_cover.pdf')
    c = canvas.Canvas(out, pagesize=(W, Hh), initialFontName='Serif')
    c.setFillColor(black); c.rect(0, 0, W, Hh, stroke=0, fill=1)
    draw_front(c, book, bleed + PW + spine, bleed)
    c.setFillColor(PAPERWHITE)
    c.saveState(); c.translate(bleed + PW + spine / 2 - 3.5, bleed + PH - 0.7 * IN); c.rotate(-90)
    c.setFont('DidotI', 11); c.drawString(0, 0, "Play by Play"); c.restoreState()
    draw_back(c, bleed, bleed)
    c.save()
    print(out, f"spine {spine / IN:.3f} in for {pages} pages")


def build(book, out, only=(), with_cover=False):
    """with_cover=False: the print interior. True: the reading edition, cover-to-cover in one file."""
    b = Book(out)
    c = b.c
    if with_cover:
        c.setFillColor(black); c.rect(0, 0, PW, PH, stroke=0, fill=1)
        draw_front(c, book, 0, 0); c.showPage()
    if not only:
        front_matter(b, book)
    else:
        b.next()
    for g in book:
        if not only or g['id'] in only:
            game_spread(b, g)
    if not only:
        back_matter(b, book)
        if b.n % 2 == 0:       # b.n is the next page number; keep the interior even
            b.next()
    pages = b.n - 1
    if with_cover:
        c.setFillColor(black); c.rect(0, 0, PW, PH, stroke=0, fill=1)
        draw_back(c, 0, 0, barcode=False); c.showPage()
    c.save()
    print(out, pages, 'interior pages', '+ covers' if with_cover else '', os.path.getsize(out) // 1024, 'KB')
    return pages


def main():
    book = json.load(open(os.path.join(ROOT, 'data/book.json')))
    only = [int(a) for a in sys.argv[1:]]
    if only:
        build(book, os.path.join(ROOT, 'book', 'sample.pdf'), only)
        return
    pages = build(book, os.path.join(ROOT, 'book', 'Play_by_Play.pdf'))                      # for the printer
    cover(book, pages)                                                                      # for the printer
    build(book, os.path.join(ROOT, 'web', 'Play_by_Play.pdf'), with_cover=True)              # for readers


if __name__ == '__main__':
    main()
