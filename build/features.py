"""Turn a validated game into a list of per-ply facts the narrators can talk about."""
import chess

VAL = {chess.PAWN: 1, chess.KNIGHT: 3, chess.BISHOP: 3, chess.ROOK: 5, chess.QUEEN: 9, chess.KING: 100}
NAME = {chess.PAWN: 'pawn', chess.KNIGHT: 'knight', chess.BISHOP: 'bishop', chess.ROOK: 'rook',
        chess.QUEEN: 'queen', chess.KING: 'king'}

ECO_TABLE = [
    ('A00', 'A00', "Irregular Opening"), ('A01', 'A01', "Nimzo-Larsen Attack"), ('A02', 'A03', "Bird Opening"),
    ('A04', 'A09', "Réti Opening"), ('A10', 'A39', "English Opening"), ('A40', 'A41', "Queen's Pawn Game"),
    ('A42', 'A44', "Old Benoni"), ('A45', 'A45', "Queen's Pawn Game"), ('A46', 'A46', "Torre Attack"),
    ('A47', 'A50', "Indian Game"), ('A51', 'A52', "Budapest Gambit"), ('A53', 'A55', "Old Indian Defence"),
    ('A56', 'A79', "Benoni Defence"), ('A80', 'A99', "Dutch Defence"), ('B00', 'B00', "King's Pawn Opening"),
    ('B01', 'B01', "Scandinavian Defence"), ('B02', 'B05', "Alekhine Defence"), ('B06', 'B06', "Modern Defence"),
    ('B07', 'B09', "Pirc Defence"), ('B10', 'B19', "Caro-Kann Defence"), ('B20', 'B32', "Sicilian Defence"),
    ('B33', 'B33', "Sicilian Sveshnikov"), ('B34', 'B39', "Sicilian Accelerated Dragon"), ('B40', 'B69', "Sicilian Defence"),
    ('B70', 'B79', "Sicilian Dragon"), ('B80', 'B89', "Sicilian Scheveningen"), ('B90', 'B99', "Sicilian Najdorf"),
    ('C00', 'C19', "French Defence"), ('C20', 'C20', "King's Pawn Game"), ('C21', 'C22', "Centre Game"),
    ('C23', 'C24', "Bishop's Opening"), ('C25', 'C29', "Vienna Game"), ('C30', 'C39', "King's Gambit"),
    ('C40', 'C40', "King's Knight Opening"), ('C41', 'C41', "Philidor Defence"), ('C42', 'C43', "Petrov Defence"),
    ('C44', 'C44', "Scotch Gambit"), ('C45', 'C45', "Scotch Game"), ('C46', 'C46', "Three Knights Game"),
    ('C47', 'C49', "Four Knights Game"), ('C50', 'C50', "Italian Game"), ('C51', 'C52', "Evans Gambit"),
    ('C53', 'C54', "Giuoco Piano"), ('C55', 'C59', "Two Knights Defence"), ('C60', 'C66', "Ruy Lopez"),
    ('C67', 'C67', "Berlin Defence"), ('C68', 'C69', "Exchange Ruy Lopez"), ('C70', 'C88', "Ruy Lopez"),
    ('C89', 'C89', "Marshall Attack"), ('C90', 'C99', "Ruy Lopez"), ('D00', 'D05', "Queen's Pawn Game"),
    ('D06', 'D09', "Queen's Gambit"), ('D10', 'D19', "Slav Defence"), ('D20', 'D29', "Queen's Gambit Accepted"),
    ('D30', 'D31', "Queen's Gambit Declined"), ('D32', 'D34', "Tarrasch Defence"), ('D35', 'D42', "Queen's Gambit Declined"),
    ('D43', 'D49', "Semi-Slav Defence"), ('D50', 'D69', "Queen's Gambit Declined"), ('D70', 'D99', "Grünfeld Defence"),
    ('E00', 'E09', "Catalan Opening"), ('E10', 'E10', "Indian Game"), ('E11', 'E11', "Bogo-Indian Defence"),
    ('E12', 'E19', "Queen's Indian Defence"), ('E20', 'E59', "Nimzo-Indian Defence"), ('E60', 'E99', "King's Indian Defence"),
]
OPENING_OVERRIDE = {"One... a6": "St. George Defence", "Baden-Baden Fireworks": "King's Fianchetto Opening",
                    "The King Hunt": "Dutch Defence", "The Back Rank Ballet": "Philidor Defence",
                    "Hypermodern Brilliancy": "Réti Opening", "The Polish Immortal": "Dutch Defence"}


def opening_name(eco, nick):
    if nick in OPENING_OVERRIDE:
        return OPENING_OVERRIDE[nick]
    for lo, hi, name in ECO_TABLE:
        if lo <= eco <= hi:
            return name
    return "Queen's Pawn Game"


def en_prise(board, sq, color):
    """Is the piece of `color` on sq capturable at a profit (cheaply attacked or undefended)?"""
    p = board.piece_at(sq)
    if not p:
        return False
    att = board.attackers(not color, sq)
    if not att:
        return False
    dfd = board.attackers(color, sq)
    vals = [VAL[board.piece_at(a).piece_type] for a in att]
    if dfd:
        vals = [v for v in vals if v < 100]      # a king cannot take a defended piece
        return bool(vals) and min(vals) < VAL[p.piece_type]
    return True


def mobility(board):
    me = board.legal_moves.count()
    if board.is_check() or board.is_game_over():
        return me, None
    board.push(chess.Move.null())
    other = board.legal_moves.count()
    board.pop()
    return me, other


def analyse(game):
    """game: dict with 'ucis'. Returns list of ply dicts and game-level summary."""
    board = chess.Board()
    plies = []
    run = {True: 0, False: 0}          # consecutive checks given
    last_mob = {True: 20, False: 20}
    prev_hang = {True: {}, False: {}}
    n = len(game['ucis'])
    prev = None
    for i, u in enumerate(game['ucis']):
        mv = chess.Move.from_uci(u)
        color = board.turn
        piece = board.piece_at(mv.from_square).piece_type
        was_check = board.is_check()
        cap = None
        if board.is_capture(mv):
            cap = chess.PAWN if board.is_en_passant(mv) else board.piece_at(mv.to_square).piece_type
        castle = 'K' if board.is_kingside_castling(mv) else 'Q' if board.is_queenside_castling(mv) else ''
        san = board.san(mv)
        board.push(mv)
        d = dict(i=i, n=i // 2 + 1, white=color, san=san, uci=u, piece=NAME[piece],
                 frm=chess.square_name(mv.from_square), to=chess.square_name(mv.to_square),
                 cap=NAME[cap] if cap else None, capv=VAL[cap] if cap else 0,
                 check=board.is_check(), mate=board.is_checkmate(), castle=castle,
                 promo=NAME[mv.promotion] if mv.promotion else None, was_check=was_check)
        landed = board.piece_at(mv.to_square).piece_type
        # sacrifice: lands on a square where it can be taken at a loss
        loss = VAL[piece] - d['capv']
        d['sac'] = (not d['mate'] and piece not in (chess.PAWN, chess.KING) and not mv.promotion
                    and loss >= 2 and en_prise(board, mv.to_square, color))
        # leaves another piece hanging on purpose (or not): newly en prise since this side's last move
        cur = {sq: board.piece_at(sq).piece_type for pt in (chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN)
               for sq in board.pieces(pt, color) if en_prise(board, sq, color)}
        fresh = {sq: pt for sq, pt in cur.items() if prev_hang[color].get(sq) != pt and sq != mv.to_square}
        prev_hang[color] = cur
        d['hang'] = None
        if fresh and not d['check'] and not d['mate']:
            sq = max(fresh, key=lambda x: VAL[fresh[x]])
            if d['capv'] < VAL[fresh[sq]]:
                d['hang'] = (NAME[fresh[sq]], chess.square_name(sq))
        d['qoffer'] = bool((piece == chess.QUEEN and d['sac']) or (d['hang'] and d['hang'][0] == 'queen'))
        d['qsq'] = d['hang'][1] if (d['hang'] and d['hang'][0] == 'queen') else d['to']
        # recapture / reactions to the previous ply
        d['recap'] = bool(cap and prev and prev['cap'] and prev['to'] == d['to'])
        d['accept'] = bool(prev and cap and ((prev['sac'] and prev['to'] == d['to']) or
                                             (prev['hang'] and prev['hang'][1] == d['to'])))
        d['decline'] = bool(prev and (prev['sac'] or prev['qoffer']) and not d['accept'] and not was_check)
        d['offered'] = ('queen' if prev['qoffer'] else prev['piece']) if prev and (prev['sac'] or prev['qoffer']) else None
        d['qtrade'] = bool(d['recap'] and cap == chess.QUEEN and prev['cap'] == 'queen')
        d['evade'] = ''
        if was_check:
            d['evade'] = 'king' if piece == chess.KING else ('take' if cap and prev and prev['to'] == d['to'] else 'block')
        # consecutive checks
        run[color] = run[color] + 1 if d['check'] else 0
        d['run'] = run[color]
        # fork by knight
        d['fork'] = False
        if landed == chess.KNIGHT and not en_prise(board, mv.to_square, color):
            heavy = [s for s in board.attacks(mv.to_square)
                     if board.piece_at(s) and board.piece_at(s).color != color
                     and board.piece_at(s).piece_type in (chess.KING, chess.QUEEN, chess.ROOK)]
            d['fork'] = len(heavy) >= 2
        # far-advanced pawn
        rr = chess.square_rank(mv.to_square) if color else 7 - chess.square_rank(mv.to_square)
        d['rel_rank'] = rr + 1
        d['advanced'] = piece == chess.PAWN and rr >= 5 and not mv.promotion
        d['file'] = chess.square_file(mv.to_square)
        d['queens'] = bool(board.queens)
        d['pieces'] = len(board.piece_map())
        # material and "possession"
        bal = sum(VAL[p.piece_type] * (1 if p.color else -1) for p in board.piece_map().values() if p.piece_type != chess.KING)
        d['bal'] = bal
        me, other = mobility(board)      # board.turn is now the opponent
        last_mob[board.turn] = me
        if other is not None:
            last_mob[not board.turn] = other
        w, b = last_mob[True], last_mob[False]
        d['poss'] = round(100 * w / max(1, w + b))
        # excitement
        e = 1 + d['capv'] * 0.6 + (3 if d['check'] else 0) + (7 if d['sac'] else 0) + (4 if d['qoffer'] else 0) + (5 if d['hang'] else 0) \
            + (6 if d['promo'] else 0) + (12 if d['mate'] else 0) + (2 if d['fork'] else 0) + (1.5 if d['advanced'] else 0)
        if d['recap']:
            e -= d['capv'] * 0.4
        d['ex'] = round(e, 1)
        plies.append(d)
        prev = d
    return plies, board
