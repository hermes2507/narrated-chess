"""Spanish names for everything that is not prose: game nicknames, places, events, openings,
authors, and Spanish algebraic notation (R D T A C for K Q R B N)."""
import re

NICK = {
    1: "Los tres peones", 2: "La Inmortal", 3: "La Siempreviva", 4: "El sacrificio de dama de Nueva York",
    5: "Una noche en la ópera", 6: "Diecisiete jugadas en París", 7: "La inmortal de Zukertort", 8: "Los dos alfiles",
    9: "La Habana, cuarta partida", 10: "La batalla de Hastings", 11: "Llega Pillsbury", 12: "La brillante de San Petersburgo",
    13: "A golpes en Cambridge Springs", 14: "La inmortal de Rubinstein", 15: "La sorpresa de San Sebastián",
    16: "La partida de las monedas de oro", 17: "La cacería del rey", 18: "El cambio de San Petersburgo",
    19: "Los dos alfiles de Tarrasch", 20: "El estreno del Ataque Marshall", 21: "El ballet de la última fila",
    22: "La obra maestra de Hastings", 23: "La torre ofrecida en Teplitz", 24: "El zugzwang inmortal",
    25: "La marcha del rey", 26: "El fin de ocho años", 27: "La brillante hipermoderna",
    28: "Fuegos artificiales en Baden-Baden", 29: "El molino", 30: "El bloqueo", 31: "La corona cambia de manos",
    32: "La inmortal polaca", 33: "El cañón de Alekhine", 34: "La perla de Zandvoort", 35: "El alfil en a3",
    36: "Trueno entre Praga y Moscú", 37: "La dama por un paseo del rey", 38: "La torre a h8", 39: "La torre rehusada",
    40: "Avalancha india de rey", 41: "La calidad en e6", 42: "La dama a cambio", 43: "La partida del siglo",
    44: "Matar al dragón", 45: "La inmortal de Nezhmetdinov", 46: "Hechicería en Bled", 47: "El caballo a f4",
    48: "Desde Rusia con amor", 49: "Gambito de rey en Mar del Plata", 50: "La dama en f4", 51: "Revancha en Bled",
    52: "El asesino silencioso", 53: "Malabares en Varna", 54: "La brillante que nadie vio", 55: "La torre a f6",
    56: "El caballo en d5", 57: "Sacrificio de dama en Santa Mónica", 58: "La décima partida",
    59: "Ataque indio de rey", 60: "Asalto de torres en Montecarlo", 61: "La decimonovena partida",
    62: "Diecisiete jugadas en Belgrado", 63: "La séptima partida", 64: "Reikiavik, sexta partida",
    65: "Reikiavik, decimotercera partida", 66: "Matadragones en Moscú", 67: "El alfil en a7",
    68: "Baguio, la última partida", 69: "1... a6", 70: "Doble alfil en Niksic", 71: "El caballo pulpo",
    72: "El decimotercer campeón", 73: "La inmortal de Nunn", 74: "Caos en Leningrado",
    75: "Sevilla, vigesimocuarta partida", 76: "Sacrificio de dama en Lyon", 77: "Locura en Bruselas",
    78: "El paseo del rey", 79: "Linares: todos en la primera fila", 80: "Los caballos de Judit",
    81: "Tormenta de torres en Linares", 82: "Décima partida, piso 107", 83: "La dama en g7",
    84: "La máquina gana una", 85: "La sexta partida", 86: "El alfil a h3", 87: "La inmortal de Kasparov",
    88: "Se levanta el muro en Londres", 89: "Judit vence al jefe", 90: "El chico de Lommedalen",
    91: "Ganar o nada en Brissago", 92: "El caballo toma f7", 93: "Bonn, tercera partida",
    94: "Sofía, la última partida", 95: "La inmortal de Anand", 96: "Chennai, novena partida", 97: "Dama a h6",
    98: "La inmortal china", 99: "El maratón de Dubái", 100: "El desempate de Astaná",
}

SITE = {"London": "Londres", "New York": "Nueva York", "St. Petersburg": "San Petersburgo", "Havana": "La Habana",
        "Moscow": "Moscú", "Warsaw": "Varsovia", "Prague": "Praga", "Zürich": "Zúrich", "Copenhagen": "Copenhague",
        "Belgrade": "Belgrado", "Seville": "Sevilla", "Brussels": "Bruselas", "Nice": "Niza", "Sofia": "Sofía",
        "Reykjavik": "Reikiavik", "Leningrad": "Leningrado", "Philadelphia": "Filadelfia", "Dresden": "Dresde",
        "Monte Carlo": "Montecarlo", "Baguio City": "Ciudad de Baguio", "Dubai": "Dubái", "Amsterdam": "Ámsterdam",
        "Berlin": "Berlín", "Paris": "París", "New Orleans": "Nueva Orleans", "Santa Monica": "Santa Mónica",
        "Astana": "Astaná"}

EVENT = {"Match": "Match", "Casual game": "Partida amistosa", "Candidates": "Torneo de Candidatos",
         "Candidates playoff": "Desempate de Candidatos", "First American Chess Congress": "Primer Congreso Americano de Ajedrez",
         "A box at the opera": "Un palco en la ópera", "German Chess Congress": "Congreso Alemán de Ajedrez",
         "St. Petersburg 1895–96": "San Petersburgo 1895–96", "St. Petersburg, final": "San Petersburgo, final",
         "St. Petersburg, preliminary": "San Petersburgo, preliminar", "Prague–Moscow match": "Match Praga–Moscú",
         "AVRO": "AVRO", "Portoroz Interzonal": "Interzonal de Portoroz", "Sousse Interzonal": "Interzonal de Sousse",
         "USSR Championship": "Campeonato de la URSS", "Olympiad": "Olimpiada", "US Championship": "Campeonato de EE. UU.",
         "USSR vs. Rest of the World": "URSS contra el Resto del Mundo", "European Team Championship": "Campeonato Europeo por Equipos",
         "Hoogovens tournament": "Torneo Hoogovens", "Corus tournament": "Torneo Corus", "Corus C": "Torneo Corus, grupo C",
         "Sicilian theme tournament": "Torneo temático de la Siciliana", "Man vs. Machine": "Hombre contra máquina",
         "PCA World Championship": "Campeonato del Mundo de la PCA", "Russia vs. Rest of the World": "Rusia contra el Resto del Mundo",
         "Tata Steel": "Torneo Tata Steel", "Chinese League": "Liga China", "Rosenwald Memorial": "Memorial Rosenwald",
         "World Championship tiebreak": "Desempate del Campeonato del Mundo"}

OPENING = {"Irregular Opening": "Apertura irregular", "Nimzo-Larsen Attack": "Ataque Nimzo-Larsen", "Bird Opening": "Apertura Bird",
           "Réti Opening": "Apertura Réti", "English Opening": "Apertura Inglesa", "Queen's Pawn Game": "Apertura de peón de dama",
           "Old Benoni": "Benoni Antigua", "Torre Attack": "Ataque Torre", "Indian Game": "Defensa India",
           "Budapest Gambit": "Gambito Budapest", "Old Indian Defence": "Defensa India Antigua", "Benoni Defence": "Defensa Benoni",
           "Dutch Defence": "Defensa Holandesa", "King's Pawn Opening": "Apertura de peón de rey", "Scandinavian Defence": "Defensa Escandinava",
           "Alekhine Defence": "Defensa Alekhine", "Modern Defence": "Defensa Moderna", "Pirc Defence": "Defensa Pirc",
           "Caro-Kann Defence": "Defensa Caro-Kann", "Sicilian Defence": "Defensa Siciliana", "Sicilian Sveshnikov": "Siciliana Sveshnikov",
           "Sicilian Accelerated Dragon": "Siciliana, Dragón Acelerado", "Sicilian Dragon": "Siciliana, Variante del Dragón",
           "Sicilian Scheveningen": "Siciliana Scheveningen", "Sicilian Najdorf": "Siciliana Najdorf", "French Defence": "Defensa Francesa",
           "King's Pawn Game": "Apertura de peón de rey", "Centre Game": "Apertura del Centro", "Bishop's Opening": "Apertura de Alfil",
           "Vienna Game": "Partida Vienesa", "King's Gambit": "Gambito de Rey", "King's Knight Opening": "Apertura de caballo de rey",
           "Philidor Defence": "Defensa Philidor", "Petrov Defence": "Defensa Petrov", "Scotch Gambit": "Gambito Escocés",
           "Scotch Game": "Apertura Escocesa", "Three Knights Game": "Apertura de los Tres Caballos",
           "Four Knights Game": "Apertura de los Cuatro Caballos", "Italian Game": "Apertura Italiana", "Evans Gambit": "Gambito Evans",
           "Giuoco Piano": "Giuoco Piano", "Two Knights Defence": "Defensa de los Dos Caballos", "Ruy Lopez": "Apertura Española",
           "Berlin Defence": "Defensa Berlinesa", "Exchange Ruy Lopez": "Española, Variante del Cambio", "Marshall Attack": "Ataque Marshall",
           "Queen's Gambit": "Gambito de Dama", "Slav Defence": "Defensa Eslava", "Queen's Gambit Accepted": "Gambito de Dama Aceptado",
           "Queen's Gambit Declined": "Gambito de Dama Rehusado", "Tarrasch Defence": "Defensa Tarrasch", "Semi-Slav Defence": "Defensa Semieslava",
           "Grünfeld Defence": "Defensa Grünfeld", "Catalan Opening": "Apertura Catalana", "Bogo-Indian Defence": "Defensa Bogoindia",
           "Queen's Indian Defence": "Defensa India de Dama", "Nimzo-Indian Defence": "Defensa Nimzoindia",
           "King's Indian Defence": "Defensa India de Rey", "St. George Defence": "Defensa San Jorge",
           "King's Fianchetto Opening": "Apertura del fianchetto de rey"}

AUTHOR = {"Homer": "Homero", "Fyodor Dostoevsky": "Fiódor Dostoievski", "Leo Tolstoy": "León Tolstói", "Scheherazade": "Sherezade",
          "Anton Chekhov": "Antón Chéjov", "Niccolò Machiavelli": "Nicolás Maquiavelo", "Mikhail Bulgakov": "Mijaíl Bulgákov",
          "Sappho": "Safo", "Anna Akhmatova": "Anna Ajmátova", "Omar Khayyam": "Omar Jayam", "Vladimir Nabokov": "Vladímir Nabokov",
          "Vladimir Mayakovsky": "Vladímir Maiakovski", "Alexander Pushkin": "Alexandr Pushkin",
          "The Icelandic Sagas": "Las sagas islandesas", "The King James Bible": "La Biblia Reina-Valera", "Victor Hugo": "Víctor Hugo"}

PIECE = {'K': 'R', 'Q': 'D', 'R': 'T', 'B': 'A', 'N': 'C'}


def san(s):
    """English SAN -> Spanish SAN: Nf3 -> Cf3, Qxh7# -> Dxh7#, e8=Q -> e8=D."""
    if s[0] in PIECE:
        s = PIECE[s[0]] + s[1:]
    return re.sub(r'=([QRBN])', lambda m: '=' + PIECE[m.group(1)], s)


def site(s):
    return SITE.get(s, s)


def event(ev, site_en):
    if ev in EVENT:
        return EVENT[ev]
    m = re.match(r'World Championship, game (\d+)$', ev)
    if m:
        return f"Campeonato del Mundo, partida {m.group(1)}"
    if ev.endswith(' tournament'):
        return 'Torneo de ' + site(ev[:-len(' tournament')])
    raise KeyError(f"no Spanish name for event {ev!r}")


def opening(o):
    return OPENING[o]


def author(a):
    return AUTHOR.get(a, a)
