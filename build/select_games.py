"""Pick the 100 historic games out of the raw index, validate every move with
python-chess, and write data/hundred.pgn + data/games.json."""
import pickle, os, io, json, re
import chess, chess.pgn
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# whiteKey|blackKey|fileYear|result|moves|White|Black|Nickname|Site|displayYear
SPEC = """
McDonnell|Bourdonnais|1834|0-1|37|Alexander McDonnell|Louis de La Bourdonnais|The Three Pawns|London|1834
Anderssen|Kieseritzky|1851|1-0|23|Adolf Anderssen|Lionel Kieseritzky|The Immortal Game|London|1851
Anderssen|Dufresne|1852|1-0|24|Adolf Anderssen|Jean Dufresne|The Evergreen Game|Berlin|1852
Paulsen|Morphy|1857|0-1|28|Louis Paulsen|Paul Morphy|The Queen Sacrifice in New York|New York|1857
Morphy|Duke|1858|1-0|17|Paul Morphy|Duke Karl & Count Isouard|A Night at the Opera|Paris|1858
Morphy|Anderssen|1858|1-0|17|Paul Morphy|Adolf Anderssen|Seventeen Moves in Paris|Paris|1858
Zukertort|Blackburne|1883|1-0|33|Johannes Zukertort|Joseph Blackburne|Zukertort's Immortal|London|1883
Lasker|Bauer|1889|1-0|38|Emanuel Lasker|Johann Bauer|The Two Bishops|Amsterdam|1889
Steinitz|Chigorin|1892|1-0|28|Wilhelm Steinitz|Mikhail Chigorin|Havana, Game Four|Havana|1892
Steinitz|Bardeleben|1895|1-0|25|Wilhelm Steinitz|Curt von Bardeleben|The Battle of Hastings|Hastings|1895
Pillsbury|Tarrasch|1895|1-0|52|Harry Pillsbury|Siegbert Tarrasch|Pillsbury Arrives|Hastings|1895
Pillsbury|Lasker|1895|0-1|32|Harry Pillsbury|Emanuel Lasker|St. Petersburg Brilliancy|St. Petersburg|1896
Lasker|Napier|1904|1-0|35|Emanuel Lasker|William Napier|Cambridge Springs Slugfest|Cambridge Springs|1904
Rotlewi|Rubinstein|1907|0-1|25|Georg Rotlewi|Akiba Rubinstein|Rubinstein's Immortal|Lodz|1907
Rubinstein|Capablanca|1911|1-0|42|Akiba Rubinstein|José Raúl Capablanca|San Sebastián Upset|San Sebastián|1911
Levitsky|Marshall|1912|0-1|23|Stepan Levitsky|Frank Marshall|The Gold Coins Game|Breslau|1912
MEM1
Lasker|Capablanca|1914|1-0|42|Emanuel Lasker|José Raúl Capablanca|The Exchange in St. Petersburg|St. Petersburg|1914
Nimzowitsch|Tarrasch|1914|0-1|32|Aron Nimzowitsch|Siegbert Tarrasch|Tarrasch's Two Bishops|St. Petersburg|1914
Capablanca|Marshall|1918|1-0|36|José Raúl Capablanca|Frank Marshall|The Marshall Attack Debut|New York|1918
MEM2
Bogoljubow|Alekhine|1922|0-1|53|Efim Bogoljubov|Alexander Alekhine|Hastings Masterpiece|Hastings|1922
Maroczy|Tartakower|1922|0-1|35|Géza Maróczy|Savielly Tartakower|The Rook Offer at Teplitz|Teplitz-Schönau|1922
Saemisch|Nimzowitsch|1923|0-1|25|Friedrich Sämisch|Aron Nimzowitsch|The Immortal Zugzwang|Copenhagen|1923
Capablanca|Tartakower|1924|1-0|52|José Raúl Capablanca|Savielly Tartakower|The King Marches In|New York|1924
Reti|Capablanca|1924|1-0|31|Richard Réti|José Raúl Capablanca|The End of Eight Years|New York|1924
Reti|Bogoljubow|1924|1-0|25|Richard Réti|Efim Bogoljubov|Hypermodern Brilliancy|New York|1924
Reti|Alekhine|1925|0-1|42|Richard Réti|Alexander Alekhine|Baden-Baden Fireworks|Baden-Baden|1925
Torre|Lasker|1925|1-0|43|Carlos Torre|Emanuel Lasker|The Windmill|Moscow|1925
Johner|Nimzowitsch|1926|0-1|40|Paul Johner|Aron Nimzowitsch|The Blockade|Dresden|1926
Alekhine|Capablanca|1927|1-0|82|Alexander Alekhine|José Raúl Capablanca|The Crown Changes Hands|Buenos Aires|1927
Glucksberg|Najdorf|1935|0-1|22|Glücksberg|Miguel Najdorf|The Polish Immortal|Warsaw|1929
Alekhine|Nimzowitsch|1930|1-0|32|Alexander Alekhine|Aron Nimzowitsch|Alekhine's Gun|San Remo|1930
Euwe|Alekhine|1935|1-0|47|Max Euwe|Alexander Alekhine|The Pearl of Zandvoort|Zandvoort|1935
Botvinnik|Capablanca|1938|1-0|41|Mikhail Botvinnik|José Raúl Capablanca|The Bishop on a3|Rotterdam|1938
Pachman|Bronstein|1946|0-1|31|Ludek Pachman|David Bronstein|Prague-Moscow Thunder|Prague|1946
Averbakh|Kotov|1953|0-1|51|Yuri Averbakh|Alexander Kotov|The Queen for a King Walk|Zürich|1953
Geller|Euwe|1953|0-1|26|Efim Geller|Max Euwe|The Rook to h8|Zürich|1953
Keres|Smyslov|1953|0-1|28|Paul Keres|Vasily Smyslov|The Rook Declined|Zürich|1953
Taimanov|Najdorf|1953|0-1|43|Mark Taimanov|Miguel Najdorf|King's Indian Avalanche|Zürich|1953
Reshevsky|Petrosian|1953|1/2-1/2|41|Samuel Reshevsky|Tigran Petrosian|The Exchange on e6|Zürich|1953
Botvinnik|Smyslov|1954|0-1|33|Mikhail Botvinnik|Vasily Smyslov|The Queen Trade-In|Moscow|1954
Byrne, D|Fischer|1956|0-1|41|Donald Byrne|Bobby Fischer|The Game of the Century|New York|1956
Fischer|Larsen|1958|1-0|31|Bobby Fischer|Bent Larsen|Slaying the Dragon|Portoroz|1958
Polugaevsky|Nezhmetdinov|1958|0-1|33|Lev Polugaevsky|Rashid Nezhmetdinov|Nezhmetdinov's Immortal|Sochi|1958
Tal|Smyslov|1959|1-0|26|Mikhail Tal|Vasily Smyslov|Bled Sorcery|Bled|1959
Botvinnik|Tal|1960|0-1|46|Mikhail Botvinnik|Mikhail Tal|The Knight to f4|Moscow|1960
Spassky|Bronstein|1960|1-0|23|Boris Spassky|David Bronstein|From Russia with Love|Leningrad|1960
Spassky|Fischer|1960|1-0|29|Boris Spassky|Bobby Fischer|King's Gambit at Mar del Plata|Mar del Plata|1960
Letelier|Fischer|1960|0-1|23|René Letelier|Bobby Fischer|The Queen on f4|Leipzig|1960
Fischer|Tal|1961|1-0|47|Bobby Fischer|Mikhail Tal|Revenge at Bled|Bled|1961
Petrosian|Pachman|1961|1-0|21|Tigran Petrosian|Ludek Pachman|The Quiet Killer|Bled|1961
Tal|Hecht|1962|1-0|49|Mikhail Tal|Hans-Joachim Hecht|Varna Juggling Act|Varna|1962
Byrne, R|Fischer|1963|0-1|21|Robert Byrne|Bobby Fischer|The Brilliancy Nobody Saw|New York|1963
Fischer|Benko|1963|1-0|21|Bobby Fischer|Pal Benko|The Rook to f6|New York|1963
Tal|Larsen|1965|1-0|37/B82|Mikhail Tal|Bent Larsen|The Knight on d5|Bled|1965
Larsen|Petrosian|1966|1-0|30|Bent Larsen|Tigran Petrosian|Santa Monica Queen Sacrifice|Santa Monica|1966
Petrosian|Spassky|1966|1-0|30|Tigran Petrosian|Boris Spassky|The Tenth Game|Moscow|1966
Fischer|Myagmarsuren|1967|1-0|31|Bobby Fischer|Lhamsuren Myagmarsuren|King's Indian Attack|Sousse|1967
Botvinnik|Portisch|1968|1-0|26|Mikhail Botvinnik|Lajos Portisch|Monte Carlo Rook Raid|Monte Carlo|1968
Spassky|Petrosian|1969|1-0|24|Boris Spassky|Tigran Petrosian|The Nineteenth Game|Moscow|1969
Larsen|Spassky|1970|0-1|17|Bent Larsen|Boris Spassky|Seventeen Moves in Belgrade|Belgrade|1970
Fischer|Petrosian|1971|1-0|34|Bobby Fischer|Tigran Petrosian|The Seventh Game|Buenos Aires|1971
Fischer|Spassky|1972|1-0|41|Bobby Fischer|Boris Spassky|Reykjavik, Game Six|Reykjavik|1972
Spassky|Fischer|1972|0-1|74|Boris Spassky|Bobby Fischer|Reykjavik, Game Thirteen|Reykjavik|1972
Karpov|Kortschnoj|1974|1-0|27|Anatoly Karpov|Viktor Korchnoi|Dragon Slayer in Moscow|Moscow|1974
Karpov|Unzicker|1974|1-0|44|Anatoly Karpov|Wolfgang Unzicker|The Bishop on a7|Nice|1974
Karpov|Kortschnoj|1978|1-0|41|Anatoly Karpov|Viktor Korchnoi|Baguio, the Last Game|Baguio City|1978
Karpov|Miles|1980|0-1|46|Anatoly Karpov|Tony Miles|One... a6|Skara|1980
Kasparov|Portisch|1983|1-0|35|Garry Kasparov|Lajos Portisch|Niksic Double Bishop|Niksic|1983
Karpov|Kasparov|1985|0-1|40|Anatoly Karpov|Garry Kasparov|The Octopus Knight|Moscow|1985
Karpov|Kasparov|1985|0-1|42|Anatoly Karpov|Garry Kasparov|The Thirteenth Champion|Moscow|1985
Beliavsky|Nunn|1985|0-1|27|Alexander Beliavsky|John Nunn|Nunn's Immortal|Wijk aan Zee|1985
Kasparov|Karpov|1986|1-0|41/r16|Garry Kasparov|Anatoly Karpov|Leningrad Chaos|Leningrad|1986
Kasparov|Karpov|1987|1-0|64|Garry Kasparov|Anatoly Karpov|Seville, Game Twenty-Four|Seville|1987
Kasparov|Karpov|1990|1-0|41|Garry Kasparov|Anatoly Karpov|Lyon Queen Sacrifice|Lyon|1990
Ivanchuk|Jussupow|1991|0-1|39|Vasyl Ivanchuk|Artur Yusupov|Brussels Mayhem|Brussels|1991
Short|Timman|1991|1-0|34|Nigel Short|Jan Timman|The King Walk|Tilburg|1991
Karpov|Kasparov|1993|0-1|27|Anatoly Karpov|Garry Kasparov|Linares: Everyone on the Back Rank|Linares|1993
Shirov|Polgar|1994|0-1|29|Alexei Shirov|Judit Polgár|Judit's Knights|Buenos Aires|1994
Karpov|Topalov|1994|1-0|39|Anatoly Karpov|Veselin Topalov|Linares Rook Storm|Linares|1994
Kasparov|Anand|1995|1-0|38|Garry Kasparov|Viswanathan Anand|Tenth Game, 107th Floor|New York|1995
Ivanchuk|Shirov|1996|1-0|35|Vasyl Ivanchuk|Alexei Shirov|The Queen on g7|Wijk aan Zee|1996
Deep Blue|Kasparov|1996|1-0|37|Deep Blue|Garry Kasparov|The Machine Wins One|Philadelphia|1996
Deep Blue|Kasparov|1997|1-0|19|Deep Blue|Garry Kasparov|Game Six|New York|1997
Topalov|Shirov|1998|0-1|53|Veselin Topalov|Alexei Shirov|The Bishop to h3|Linares|1998
Kasparov|Topalov|1999|1-0|44|Garry Kasparov|Veselin Topalov|Kasparov's Immortal|Wijk aan Zee|1999
Kramnik|Kasparov|2000|1-0|40|Vladimir Kramnik|Garry Kasparov|The Wall Goes Up in London|London|2000
Polgar|Kasparov|2002|1-0|42|Judit Polgár|Garry Kasparov|Judit Beats the Boss|Moscow|2002
Carlsen|Ernst|2004|1-0|29|Magnus Carlsen|Sipke Ernst|The Boy from Lommedalen|Wijk aan Zee|2004
Kramnik|Leko|2004|1-0|41|Vladimir Kramnik|Peter Leko|Must-Win in Brissago|Brissago|2004
Topalov|Kramnik|2008|1-0|45|Veselin Topalov|Vladimir Kramnik|The Knight Takes f7|Wijk aan Zee|2008
Kramnik|Anand|2008|0-1|41|Vladimir Kramnik|Viswanathan Anand|Bonn, Game Three|Bonn|2008
Topalov|Anand|2010|0-1|56|Veselin Topalov|Viswanathan Anand|Sofia, the Last Game|Sofia|2010
Aronian|Anand|2013|0-1|23|Levon Aronian|Viswanathan Anand|Anand's Immortal|Wijk aan Zee|2013
Anand|Carlsen|2013|0-1|28|Viswanathan Anand|Magnus Carlsen|Chennai, Game Nine|Chennai|2013
Carlsen|Karjakin|2016|1-0|50|Magnus Carlsen|Sergey Karjakin|Queen to h6|New York|2016
Bai|Ding|2017|0-1|32|Bai Jinshi|Ding Liren|The Chinese Immortal|China|2017
Carlsen|Nepomniachtchi|2021|1-0|136|Magnus Carlsen|Ian Nepomniachtchi|The Dubai Marathon|Dubai|2021
Nepomniachtchi|Ding|2023|0-1|68|Ian Nepomniachtchi|Ding Liren|Astana Tiebreak|Astana|2023
""".strip().split('\n')

MEM = {
 'MEM1': dict(white='Edward Lasker', black='George Thomas', nick='The King Hunt', site='London', year=1912, result='1-0', eco='A40', event='Casual game',
   body='1.d4 e6 2.Nf3 f5 3.Nc3 Nf6 4.Bg5 Be7 5.Bxf6 Bxf6 6.e4 fxe4 7.Nxe4 b6 8.Ne5 O-O 9.Bd3 Bb7 10.Qh5 Qe7 11.Qxh7+ Kxh7 12.Nxf6+ Kh6 13.Neg4+ Kg5 14.h4+ Kf4 15.g3+ Kf3 16.Be2+ Kg2 17.Rh2+ Kg1 18.Kd2# 1-0'),
 'MEM2': dict(white='Edwin Adams', black='Carlos Torre', nick='The Back Rank Ballet', site='New Orleans', year=1920, result='1-0', eco='C62', event='Casual game',
   body='1.e4 e5 2.Nf3 d6 3.d4 exd4 4.Qxd4 Nc6 5.Bb5 Bd7 6.Bxc6 Bxc6 7.Nc3 Nf6 8.O-O Be7 9.Nd5 Bxd5 10.exd5 O-O 11.Bg5 c6 12.c4 cxd5 13.cxd5 Re8 14.Rfe1 a5 15.Re2 Rc8 16.Rae1 Qd7 17.Bxf6 Bxf6 18.Qg4 Qb5 19.Qc4 Qd7 20.Qc7 Qb5 21.a4 Qxa4 22.Re4 Qb5 23.Qxb7 1-0'),
}
EVENT_FIX = {'Candidats':'Candidates','World Championship':'World Championship','Hoogovens':'Hoogovens','Corus A':'Corus','WCh':'World Championship',
             'USA-ch':'US Championship','URS-ch27':'USSR Championship','Varna olm':'Olympiad','Nice olm fin-A':'Olympiad','EU-chT':'European Team Championship',
             'Leipzig olm prel':'Olympiad','Warsaw ol':'Warsaw','Belgrade URS-World':'USSR vs. Rest of the World','PCA-World Championship':'PCA World Championship',
             'Braingames WCC':'World Championship','New York man vs machine':'Man vs. Machine','Philadelphia m':'Man vs. Machine','RUS vs. ROW':'Russia vs. Rest of the World',
             'GMC':'Corus C','75th Tata Steel GpA':'Tata Steel','TCh-CHN 2017':'Chinese League','Candidats qf3 rapid60':'Candidates playoff','Paris it':'Italian Opera House',
             'London m4':'Match','Paris m1':'Match','USA-01.Congress':'First American Chess Congress','DSB-18.Kongress':'German Chess Congress','AVRO':'AVRO'}
def clean_event(e):
    for k,v in EVENT_FIX.items():
        if e.startswith(k): return v
    e = re.sub(r"\s*'.*'", '', e)
    e = re.sub(r'\b(Interzonal)\+', r'\1', e)
    return e.strip()

G = pickle.load(open(os.path.join(ROOT,'data/index.pkl'),'rb'))
out = []
for line in SPEC:
    if line in MEM:
        m = MEM[line]; body = m['body']; meta = dict(m); del meta['body']; meta['round']=''
    else:
        wk,bk,fy,res,n,W,B,nick,site,dy = line.split('|')
        c = [g for g in G if wk.lower() in g['h']['White'].lower() and bk.lower() in g['h']['Black'].lower()
             and g['h'].get('Date','')[:4]==fy and g['h'].get('Result')==res and g['n']==int(n.split('/')[0])
             and ('/' not in n or n.split('/')[1] in (g['h'].get('ECO'), 'r'+g['h'].get('Round','')))]
        if wk=='Lasker' and bk=='Bauer': c=c[:1]
        assert len(c)==1, (line, len(c))
        g=c[0]; body=g['body']; h=g['h']
        meta = dict(white=W, black=B, nick=nick, site=site, year=int(dy), result=res, eco=h.get('ECO',''),
                    event=clean_event(h.get('Event','')), round=h.get('Round','').replace('?',''))
    game = chess.pgn.read_game(io.StringIO(body))
    assert not game.errors, (meta, game.errors)
    board = game.board(); sans=[]; ucis=[]
    for mv in game.mainline_moves():
        sans.append(board.san(mv)); ucis.append(mv.uci()); board.push(mv)
    meta['sans']=sans; meta['ucis']=ucis; meta['mate']=board.is_checkmate()
    out.append(meta)
out.sort(key=lambda m: m['year'])   # stable
for i,m in enumerate(out): m['id']=i+1
assert len(out)==100, len(out)
json.dump(out, open(os.path.join(ROOT,'data/games.json'),'w'), ensure_ascii=False)
with open(os.path.join(ROOT,'data/hundred.pgn'),'w') as f:
    for m in out:
        f.write(f'[Event "{m["event"]}"]\n[Site "{m["site"]}"]\n[Date "{m["year"]}.??.??"]\n[Round "{m["round"] or "?"}"]\n[White "{m["white"]}"]\n[Black "{m["black"]}"]\n[Result "{m["result"]}"]\n[ECO "{m["eco"]}"]\n[Title "{m["nick"]}"]\n\n')
        s=''
        for k,san in enumerate(m['sans']):
            s += (f'{k//2+1}. ' if k%2==0 else '') + san + ' '
        f.write(s + m['result'] + '\n\n')
print(len(out), 'games;', sum(len(m['sans']) for m in out), 'plies; mates:', sum(m['mate'] for m in out))
for m in out: print(m['id'], m['year'], m['white'],'-',m['black'],'|',m['event'],'|',m['round'],'|',len(m['sans']), m['sans'][-1])
