"""One hundred exercises in style, after Queneau: each game told once, each in the manner
of a different author. Pastiches written for this book; no line is quoted from anyone.
Keyed by game id (chronological order of data/games.json)."""

EX = {
1: ("Homer", """Sing, Muse, of the wrath of La Bourdonnais, breaker of centres, who came over the grey sea to London and sat down before McDonnell of the white pieces. Thirty-seven times each hero raised his arm. Queens were flung away like spears that have done their work. And at the last three black pawns stood shoulder to shoulder on the second rank, bronze-greaved, unwearied, like three brothers before a gate; and the gate was the last rank, and no rook of McDonnell could hold it. So fell the house of White in the year 1834."""),
2: ("Jorge Luis Borges", """I have been told that in London, in 1851, Adolf Anderssen gave away a bishop, then both rooks, then the queen, and that with what remained (three minor pieces, a rumour of an army) he mated Kieseritzky on the twenty-third move with a bishop on e7. I suspect the game was not played but remembered. Somewhere there is a library in which every possible game is shelved; in that library this one is bound in a single volume, and each reader who opens it becomes, for twenty-three moves, Anderssen. Kieseritzky is the mirror."""),
3: ("Emily Dickinson", """A Gambit — Captain Evans' kind —
Was offered in Berlin —
And Dufresne took — as Persons take —
What Courtesy lets in —

The Knight was given — then the Rook —
The Queen went last — to d7 —
A Double Check — is like a Door —
That opens — into Heaven —

Two Bishops did the final Thing —
At Twenty-four — 'twas done —
They call it Evergreen — because —
It will not stop — being won —"""),
4: ("Edgar Allan Poe", """True! nervous, very dreadfully nervous was Paulsen that night in New York, in the year 1857, for he had thought an hour upon a single move, and still the young man from New Orleans did not stir. And then, upon the seventeenth move, Morphy took a knight on f3 with the queen. With the queen! I heard the pawn recapture; I heard the bishop arrive at h3; I heard, beneath the floor of the position, a low dull quick sound, as of a king enclosed. At the twenty-eighth move it ceased. The bishop stood on e3. Paulsen resigned."""),
5: ("Oscar Wilde", """To lose a knight on b5 may be regarded as generosity; to lose a rook on d7 looks like extravagance; to give away one's queen on b8 is simply genius. Mr Morphy did all three in a box at the Paris opera in 1858, while a Duke and a Count consulted against him and against the soprano. The aristocracy, as usual, took everything that was offered. On the seventeenth move a rook arrived on d8 and it was mate. One should always play chess at the opera. It is the only way to be sure that somebody is listening."""),
6: ("Matsuo Bashō", """Paris, winter light —
a Sicilian is opened
like a paper door.

The knight on b5
looks at d6. Old pond; the
frog has not yet jumped.

Anderssen's king walks
out into the snow at f7.
Nobody follows.

Seventeen moves, then
the sound of a chair pushed back.
Morphy: one–nothing."""),
7: ("Charles Dickens", """It was the best of positions, it was the worst of positions; it was London in 1883, and Mr Zukertort, a small quick gentleman composed entirely of nerves and combinations, sat opposite Mr Blackburne, whom the newspapers called the Black Death and whom the waiters called sir. Mr Blackburne had a rook upon the seventh rank and was content. On the twenty-eighth move Mr Zukertort placed his queen on b4, where it might be taken by anybody; and Mr Blackburne, who knew a legacy with a lawsuit attached when he saw one, declined it. It did him no good whatever. Thirty-three moves; the court rose."""),
8: ("Arthur Conan Doyle", """“You will observe, Watson, that Bauer's king has only the pawns on h7 and g7 for a wall. A young man named Lasker observed it at Amsterdam in 1889. He gave a bishop for the first pawn on move fifteen.”
“And lost a piece!”
“He then gave the second bishop for the second pawn. When you have eliminated the pawns, Watson, whatever remains, however exposed, must be the king. The queen and a rook did the rest, and collected a spare bishop along the way. Thirty-eight moves. It had never been done before. It has been called elementary ever since.”"""),
9: ("Fyodor Dostoevsky", """And what if I tell you, gentlemen, that Chigorin wanted to lose? No, no, not wanted, but there was in him, in Havana, in that heat, in 1892, some spiteful little voice saying: let the old man show what he has. And Steinitz showed it. On the twenty-fourth move the rook took on h7, with check, a rook simply thrown away, and the black king was dragged out by the collar across the whole board, to g7, to f6, to e5, like a debtor through the streets. On move twenty-eight the queen took on d4. Chigorin laughed. I am certain that he laughed."""),
10: ("Franz Kafka", """On the twenty-second move a white rook appeared on e7, next to von Bardeleben's king, and it could not be taken. This was explained to him by no one. The rook moved along the seventh rank, to f7, to g7, each time giving check, each time untakeable for reasons that were perfectly valid and that changed with every square. On the twenty-fifth move it took on h7. Von Bardeleben rose, put on his coat, and left the hall at Hastings without resigning. The year was 1895. The clock continued to run in his absence, as clocks do. Steinitz waited. The mate was demonstrated to the audience instead."""),
11: ("Walt Whitman", """I sing the young man Pillsbury, twenty-two, of Massachusetts, arrived at Hastings in 1895 unknown, afoot, light-hearted,
I sing the Queen's Gambit, the pawn offered and declined, the long patient pressure of the white pieces,
Tarrasch the doctor advancing on the queenside, pawn after pawn, sure of his science,
And the American going the other way, toward the king, O toward the king!
Fifty-two moves, each one contained multitudes,
And at the last the queen upon h7, mate, the hall rising,
I too am untranslatable; I too take on h7 over the roofs of the world."""),
12: ("Toni Morrison", """They say Pillsbury carried that game the rest of his life the way you carry a house that burned. St. Petersburg, deep winter turning into 1896. He had the white pieces and he had Lasker cramped, and then a black rook came down and took the knight on c3. Just took it. Gave itself. And the other rook slid to a3 and sat there, in the open, asking. You could not take it and you could not leave it. That is what a haunting is. Thirty-two moves. The last one was a bishop on b6, and it was mate, and it was quiet as a kept secret."""),
13: ("Mark Twain", """I was at Cambridge Springs in 1904, or would have been if I'd known about it, and I can report that Mr Lasker and Mr Napier played a game of chess there that had more attacks in it than a Missouri election. Napier attacked. Lasker, instead of defending like a Christian, attacked back. Then they both attacked at once, which I had understood to be against the rules. Pieces were left hanging like wash on a line. After thirty-five moves Lasker had a bishop on e3 and the game. Napier said it was the best game he ever played. He lost it. That is chess."""),
14: ("Isaac Bashevis Singer", """In Lodz, in 1907, there was a player named Rotlewi who believed that if he lost no pawns the Almighty would look after the rest. Across from him sat Akiba Rubinstein, who had studied to be a rabbi and had left the Talmud for the Queen's Gambit, which also has commentaries. On the twenty-second move Rubinstein gave a rook on c3. On the twenty-third he gave another on d2. The queen was already hanging. Rotlewi looked at his riches like a man who has found a purse on the Sabbath. On move twenty-five a rook came quietly to h3. Rotlewi resigned. In Lodz they said: a demon played, not a man."""),
15: ("Marcel Proust", """For a long time Capablanca had not lost, and it was perhaps this habit of not losing, more than any single move that Rubinstein played at San Sebastián in 1911, which made the capture of the pawn on d5 at the fifteenth move, a capture he had believed impossible and which a small tactical detail (so small that it resembled those memories one notices only when they have already altered everything) rendered not only possible but decisive, so painful to him; and through the twenty-seven moves that followed, in a rook ending conducted with the slowness of an afternoon in which nothing happens except the afternoon, it was the only game he would lose there."""),
16: ("Scheherazade", """It has reached me, O auspicious King, that in the city of Breslau, in the year 1912, an American named Marshall played at chess against Levitsky of the Russians, and on the twenty-third move set his queen down on g3, in the very mouth of three enemies: for two pawns could take her, and a queen could take her, and whosoever took her was lost. And Levitsky bowed his head. Then, it is said, the people of that city rained gold coins upon the board until the squares were hidden. But some say the coins were only wagers being paid. And Scheherazade perceived the dawn and fell silent."""),
17: ("Lewis Carroll", """“I move my Queen to h7 and you must take it,” said Lasker.
“Why must I?” said Sir George's King.
“Because it is check, and you are the only one at home.”
So the King took it, and at once found himself walking: to h6, to g5, to f4, down and down the board, with a Knight or a pawn saying “Check!” behind him at every step. “I have never been so far from my own rank,” he said at g1. “Where am I?”
“At my place,” said the White King, and stepped politely aside to d2.
And that was mate, on the eighteenth move, in London, in 1912, by a King."""),
18: ("Leo Tolstoy", """All drawn games are alike; each won game is won in its own way. Capablanca came to the board at St. Petersburg in 1914 needing only not to lose, and Lasker, who was forty-five and understood men better than openings, exchanged his bishop for a knight on the fourth move and removed the queens, as if to say: very well, let it be a draw. And Capablanca believed him. That was the whole of it. On the twelfth move a pawn went to f5, and for thirty moves more the young man looked for the simple life he had been promised. On the forty-second, a knight came to c5, and he resigned."""),
19: ("Thomas Bernhard", """Tarrasch, who had for twenty years told Nimzowitsch and everyone else in the German language what was correct and what was incorrect, as though chess were a hospital and he its senior physician, this same Tarrasch, at St. Petersburg in 1914, gave one bishop on h2 and then the other bishop on g2, exactly as Lasker had done it in Amsterdam, exactly, a plagiarism, Nimzowitsch must have thought, a correct plagiarism, the worst kind, and drove the white king out across the entire board to be mated on the thirty-second move by a bishop on b5, by a bishop, naturally, and Nimzowitsch never forgave him, naturally."""),
20: ("Raymond Chandler", """It was New York, 1918, and Marshall had a gambit in his pocket that he'd been carrying around for years like a gun he was saving for one man. The man was Capablanca. On move eight the pawn went to d5 and the room got as quiet as a bank at midnight. The Cuban took it. He could see it was a setup; he took it anyway, the way you walk into an alley because it's the shortest way home. For twenty moves Marshall threw everything at the king: knight, bishop, queen. Capablanca stood there and let it bounce off. On move thirty-six a bishop took on f7 with check. Marshall folded. Some surprises age badly."""),
21: ("Juan Rulfo", """I went to New Orleans because they told me a boy named Carlos Torre played there, a Mexican. It was 1920. It was hot and nobody was in the streets. On the board there was only one file open, the e-file, and four rooks looking at each other across it like people at a wake. Then Adams began to offer the queen. On g4. On c4. On c7. Each time the black queen moved a little further off, saying nothing. You could hear her breathing. On the twenty-third move the white queen took a pawn on b7 and it was over. Torre looked up. I think we were all already dead."""),
22: ("Vladimir Nabokov", """Bogoljubov (a plump syllable of a man) had the white pieces at Hastings in 1922, and Alekhine had the plan, which is the better thing to have. I recall the game as one recalls a staircase in a dream: a black pawn descends the b-file, a rook is abandoned on a8 with delicious indifference, the pawn queens; a second queen is conjured, traded, and a third pawn, on move fifty-three, steps to d5 with check, a small quiet pawn check, the smile at the end of the sonnet. Three queens from one side of the board. Problemists blush. Bogoljubov resigned, I should like to think, with a blush too."""),
23: ("Stefan Zweig", """Those who were present at Teplitz-Schönau in the autumn of 1922 would later speak of a curious unease. Maróczy, the great defender, a man of the old world in whom caution had become a form of courtesy, had castled and wanted nothing. And then, on the seventeenth move, Dr Tartakower placed a rook on h2. It was not a blow; that was the uncanny thing. Nothing followed at once. He had given a rook, a whole rook, merely for the idea of an attack, and he went on quietly developing his pieces as one finishes a letter. By the thirty-fifth move, a knight on g3, the old world had resigned."""),
24: ("Samuel Beckett", """Copenhagen. 1923. A board.
SÄMISCH: I have all my pieces.
NIMZOWITSCH: Nearly all.
SÄMISCH: A piece more than you.
NIMZOWITSCH: Yes.
(Pause.)
SÄMISCH: Then I'll move.
NIMZOWITSCH: Do.
(Sämisch does not move.)
SÄMISCH: The queen cannot move. The rooks cannot move. The bishops. The knight.
NIMZOWITSCH: There are the pawns.
SÄMISCH: Then they'll be gone.
NIMZOWITSCH: Then they'll be gone.
(Nimzowitsch plays a pawn to h6. Move twenty-five. Nothing is attacked.)
SÄMISCH: Nothing to be done.
(He does not move. Curtain.)"""),
25: ("Gabriel García Márquez", """Many years later, facing the black king across an almost empty board, José Raúl Capablanca would remember the afternoon in New York in 1924 when he let Tartakower take his pawns. It was a rook ending and it had rained numbers all morning. The white king left his house on the thirty-fifth move and walked up the board, g3, h4, g5, f6, without baggage, while behind him the pawns were eaten one by one, with check, and he did not turn around. He had understood that a king who arrives is worth more than everything he has abandoned. On the fifty-second move a pawn reached d6 and Tartakower, who was a poet, resigned in prose."""),
26: ("Gertrude Stein", """Capablanca did not lose. Capablanca did not lose for eight years. Eight years is eight years and not losing is not losing and then in New York in 1924 there was Réti. Réti opened with a knight. A knight is not a pawn. The bishops were on the long lines and the long lines were long. A queen in the corner is a queen in the corner is a queen. Thirty-one moves. Then a rook went to d5 and the other rook was on d5 before and there it was. Capablanca lost. Losing once is once. There was a there there and it was d5."""),
27: ("Italo Calvino", """You are about to play over a game by Richard Réti: New York, 1924, against Bogoljubov. Relax. Let the board empty itself of everything you expect a game to contain. There is no storming of the king here, no pawn in the centre; the white bishops live in the corners of the city and send, along diagonals as thin as tram wires, messages that arrive twenty moves later. On the twenty-fifth move one of them steps to e8, a square at the very edge of the map, attacking nothing you can see. Bogoljubov resigns. You turn the page looking for the rest of the game. This was the rest of the game."""),
28: ("Anton Chekhov", """At Baden-Baden in the spring of 1925 the band played every afternoon, and Réti opened by moving the pawn in front of his knight one square, which annoyed Alekhine more than he would admit. It was a warm day. Somebody's dog had got into the hall. On the twenty-sixth move Alekhine put a rook on e3, where a pawn could take it, and Réti sat for a long time with his hand on his cheek, thinking about the rook and also about a debt and a woman in Vienna. He did not take it. Sixteen moves later a bishop came to d5 and he lost a piece anyway. The band was still playing."""),
29: ("Miguel de Cervantes", """In a hall in Moscow, whose name I do not care to recall, there sat in 1925 a young gentleman of Yucatán, Don Carlos Torre, facing the old enchanter Lasker. And on the twenty-fifth move he set his bishop on f6 and let his queen be taken. “Your worship has lost your wits,” said the onlookers. But the rook took on g7 with check, and retreated with check, and took again with check, round and round like the sails of a windmill, grinding up a bishop, a pawn, a rook, until the giant had nothing left but his dignity. Forty-three moves. And this time, reader, the windmill won."""),
30: ("Sun Tzu", """The Master said: he who blocks the road need not fight upon it.
At Dresden, in 1926, Johner held the centre with many pawns. Nimzowitsch did not attack them. He stood in front of them.
A pawn that cannot advance is a wall built for the enemy.
Then the queen went by a small road, from d8 to d7, to f5, to h7, behind her own soldiers. Men laughed. The supreme excellence is to be laughed at on the twelfth move and obeyed on the fortieth.
When the white army could no longer move, it was struck where it stood. Forty moves. The general who wins has already won."""),
31: ("Julio Cortázar", """This game can be read in two ways. In the first, Alekhine and Capablanca sit in Buenos Aires in 1927 and play eighty-two moves, and on the last one a rook goes to e7 and Capablanca, who used to be invincible, is no longer champion of the world. In the second, begin at move thirty, where a knight takes on e5, then jump back to the opening, then forward to the rook ending, which lasts longer than several marriages. Either way the reader will notice that at some point Capablanca began to play a different game, one in which he was the one who lost, and that nobody told him the pieces had been swapped."""),
32: ("Wisława Szymborska", """Nothing happens twice, except in Warsaw, around 1929,
where Najdorf gave a bishop on h2,
then another bishop, then a knight, and then the other knight,
which is to say everything a person might reasonably keep.

Glücksberg took them. One takes what one is given.
His king walked out to g4 like a man checking the weather.

The mate was delivered on move twenty-two
by a pawn, to h5, the smallest thing on the board.
I prefer pawns.
I prefer the absurdity of giving four pieces
to the absurdity of not giving them."""),
33: ("Niccolò Machiavelli", """A prince who would hold a file must hold it with all his forces, and in the right order. Alekhine, at San Remo in 1930, placed one rook on the c-file, and the second rook behind it, and the queen behind them both, which arrangement men afterwards called the Gun; for it is better to be feared along one line than loved along several. Nimzowitsch, who had written a book on how such things are to be prevented, defended the point c7 with everything he owned, and so had nothing left to move. A prince who cannot move is no prince. He resigned on the thirty-second move without a single piece having been taken from him by force."""),
34: ("Virginia Woolf", """The sea at Zandvoort was grey, and Euwe, who was a schoolmaster and thought in columns, looked at the board, and thought, how odd, that it should be now, the twenty-sixth game, December, 1935, that a knight should go to d5 and offer itself, and that he should be the one. For there was Alekhine, across the table, enormous, a wave about to break. The pawns went forward, two of them, side by side, like children holding hands on a pier. One did not look down. The forty-seventh move came; a knight checked on e4; and it was over, and the champion, yes, in a few days, would be Euwe. What a lark."""),
35: ("Mikhail Bulgakov", """At the hour of the evening session, in Rotterdam, in 1938, two citizens sat at a board. The first was the Cuban Capablanca, who did not make mistakes; the second was the engineer Botvinnik, who did not believe in the supernatural. And yet on the thirtieth move the engineer picked up his bishop and placed it on a3, where the black queen could take it for nothing. Witnesses state that there was a smell of sulphur. The queen took. A knight leapt to h5 with check; a pawn advanced to e7 as though no force on earth could detain it; and on the forty-first move the white king stepped out of the last check to h5. Manuscripts don't burn. Neither does that game."""),
36: ("Milan Kundera", """Let us consider the rook on a1. In 1946, in Prague, in a match between the city and Moscow, Bronstein captured it with his own rook on the twentieth move, giving up the exchange, and then gave more. Pachman, who was a Czech and therefore believed that history had a direction, calculated that he was winning material. He was. This is what I call the lightness of sacrifice: the one who gives becomes weightless, and the one who takes is suddenly responsible for everything on the board. Eleven moves later a pawn went to h3 with check. Pachman resigned. In the King's Indian, as in love, the materialist is always the last to know."""),
37: ("Dante Alighieri", """Midway through the game at Zürich, in the year 1953,
I, Averbakh, found my king within a wood
of his own pawns, and deemed the place secure.

Then Kotov's queen took on h3, with check;
I took her; and a rook said: follow me.
Through f4 I went down, and then g5,

each circle narrower, a knight at every gate,
my rooks and queen above me in the light,
too far to hear. I would have given them all

for one free square. At move fifty-one a rook
came to g8, and I laid down my arms.
Abandon queens, all ye who enter here."""),
38: ("Agatha Christie", """“It is quite simple, mes amis,” said the little Belgian. “At Zürich in 1953 Monsieur Geller attacks the king. He has the queen, the rook, the bishop: all the suspects are on the kingside. And what does Dr Euwe do on the twenty-second move? He places a rook on h8. In the corner! To be taken!”
“An oversight, surely,” said Hastings.
“No, no. A decoy. The white queen takes; she is now, how do you say, out of town. She has the alibi. And in her absence the black queen and rook visit the white king at c2. Four moves. The queen comes to f3. The murderer, Hastings, was the victim.”"""),
39: ("Sappho", """. . . a rook, Keres set it down on h5
and it could be taken . . .

. . . some say a host of horsemen is the finest thing,
some say queens; I say
it is whatever one declines . . .

Smyslov looked a long while
(Zürich; the leaves; 1953)
and did not take . . .

. . . the centre, sweetbitter, opened
and the pawns went through like
. . .

twenty-eight moves . . . the queen on d4, with check . . .
and of the rook on h5
no one afterward remembered . . ."""),
40: ("Pablo Neruda", """Ode to the pawn on f4

Pawn of Najdorf,
small black tooth
of the King's Indian,
in Zürich in fifty-three
you left the queenside
to Taimanov:
let him have it,
let him eat
the whole long table
of the a-file.
You were walking
toward the king.
f5, f4, g5, g4,
the pawns went down
like miners
with lamps,
and behind them
the knights, the bishop on h3,
the rook
arriving late
with bread.
Forty-three moves.
I sing
the one who gives away
half the world
to knock
on a single door."""),
41: ("Jane Austen", """It is a truth universally acknowledged, that a player in possession of a strong centre must be in want of a breakthrough. Mr Reshevsky, at Zürich in 1953, possessed two pawns of excellent family on d5 and e5, and it was generally expected that they would advance. Mr Petrosian, a young man of small fortune and great prudence, placed a rook on e6 directly in their path, where a bishop might take it; and declared himself perfectly indifferent to the loss. The rook was taken; a knight settled on d5 for life; and after forty-one moves the parties agreed, with equal satisfaction and no affection, to a draw."""),
42: ("Anna Akhmatova", """Moscow, 1954. The fourteenth game.
I was there, where the people were,
in the hall with the heavy curtains.

He gave the queen. Not as one gives
a gift. As one gives up a name.
For her: a rook, a bishop, and a knight.

Botvinnik counted. He was right to count.
The three came on like winter in a courtyard.

No one cried out. We had learned
not to. On move thirty-three
a knight went to c6

and the champion stopped the clock,
and Smyslov, who sang, did not sing."""),
43: ("J. D. Salinger", """If you really want to hear about it, the first thing you'll probably want to know is how a thirteen-year-old kid in a dopey striped shirt beat Donald Byrne in New York in 1956, and all that Game-of-the-Century kind of crap. I'll just tell you about the queen. On move seventeen Bobby Fischer leaves the queen hanging. Just leaves it there, for God's sake, and plays a bishop to e6. Old Byrne takes it. He had to; he's a grown-up. Then the knight and the bishop start checking the king back and forth like a windshield wiper, and everything falls off the board. It killed me. Mate on move forty-one, with a rook. A kid. It really was."""),
44: ("J. R. R. Tolkien", """In those days the Dragon lay upon the long diagonal, and few who came against it returned; for its fire was the bishop on g7, and its hoard was the king. But there came to Portoroz, in the year 1958, a youth of fifteen out of the West, Fischer by name, and he knew the old lore: pry open the h-file, and strike, and strike again. So the pawn of the h-file went forward; and on the twenty-second move a rook was given upon h5, and the way was open. Then Larsen the Dane knew that his doom was come. On the thirty-first move the queen stood on d6, and the Dragon was no more."""),
45: ("Omar Khayyam", """In Sochi, by the sea, in fifty-eight,
Polugaevsky sat down, calm and straight;
His queen was safe, his centre like a wall.
The Tatar poured the wine, and said: we wait.

A rook took on f4. The queen was there
To take or leave; he left her in the air,
And drew the white king forward by the sleeve
From e4 on, down an unlit stair.

The moving knight checks, and, having checked,
Moves on to c6: thirty-three, correct.
O Nezhmetdinov, fill the cup again:
The game is brief, the mate is what is kept."""),
46: ("Mary Shelley", """It was on a dreary afternoon at Bled, in 1959, that Tal beheld the accomplishment of his toils. He had collected the instruments of attack around the black king: a knight flung to h6, a bishop, a rook upon the open file. No sober science sanctioned it. Smyslov, the most harmonious of men, looked on the creature and judged it unsound. And then, on the nineteenth move, the queen took on f7, offering herself, and the thing opened its eye. By what spark it lived I cannot say. It pursued him seven moves more. At the twenty-sixth, a bishop on d4, he resigned, and the creator smiled, and was not afraid."""),
47: ("William Shakespeare", """BOTVINNIK. What knight is this that comes upon f4
Where any pawn may take it? Is he mad?
TAL. Mad north-north-west, my lord. On move twenty-one
I am but mad enough to give a horse.
BOTVINNIK. I'll take it, then, and prove thy reckoning false.
TAL. Ay, there's the rub: thou hast not time to prove it.
The clock's a thief; the bishop on g7
Looks through thy kingdom like the morning sun.
BOTVINNIK. (Aside) A hit, a very palpable hit.
(Alarums. Forty-six moves. The white rooks fall.)
CHORUS. So Moscow saw, in nineteen-sixty's spring,
A horse, a horse, a title for a horse."""),
48: ("Ian Fleming", """Spassky lit nothing; the Russians didn't, at the board. Leningrad, 1960. The King's Gambit, a romantic opening, the sort of thing a man orders when he doesn't intend to see the bill. Across the table Bronstein took a pawn on e1's doorstep, with check to come, a rook for the asking. Spassky looked at the rook with the mild interest of a man whose car is being stolen while he holds a better pair of keys. On move fifteen the knight went to d6. Let him take it, with check. The next knight went into f7 like a bullet through a hat. Twenty-three moves. The queen came to e4. Someone later put the position in a film."""),
49: ("Roberto Bolaño", """In 1960 I was not in Mar del Plata, nobody was, but a seventeen-year-old named Fischer was there, and a twenty-three-year-old named Spassky, and between them the King's Gambit, an opening that poets play and that kills them. Spassky played it. The kid took the pawn and held on to it like a visa. For a while Black was winning; I have this from a Chilean who had it from a waiter. Then the kid's rook wandered, and the white pieces came down the e-file like a rumour. Twenty-nine moves. A rook on f4. Fischer cried, they say. A year later he published a refutation of the whole opening. That is also literature."""),
50: ("Gabriela Mistral", """Little pawn of Letelier, grown too tall,
you crossed the middle of the board
with your brothers, e5, f4,
and no one stayed at home with the king.

Mother of the centre, who will sing you?
The boy from Brooklyn waits in Leipzig,
nineteen-sixty, patient as a mountain,
and undoes you thread by thread.

The king walks out to e3, uncovered.
Then the queen falls on f4 like the evening.
If he takes her, a bishop says his name;
if he does not, it is night.

Twenty-three moves, my Chilean,
and the Andes are very far."""),
51: ("Ernest Hemingway", """In Bled in 1961 the lake was flat and the weather was good. Fischer had White. He was eighteen. Tal was across from him and Tal was the best there was at the thing Tal did. It was a Sicilian. Tal made a mistake early. It was a small one. Fischer saw it and did not hurry. He took a pawn and then he took the exchange and then there was the long part, where you have it won and must still win it. He did it cleanly. It took forty-seven moves. Tal held out his hand. It was the first time. “It's hard to beat Bobby,” Tal said after. It was a fine thing to say and it was true."""),
52: ("Sei Shōnagon", """Things that are quiet.
A snowy morning. A letter left unsent. Petrosian's opening at Bled, in 1961, where for many moves nothing touches anything.

Things that startle.
A sparrow flying up. The queen taking a bishop on f6, with check, at the nineteenth move, when one had thought this player never gave anything away.

Things that are quieter than quiet.
After the queen is gone, and the black king has been drawn out to g5, a bishop moving one square, to g7. No check. Twenty-one moves.
Pachman resigned. It is delightful when a person of taste understands at once."""),
53: ("Kurt Vonnegut", """Listen: Mikhail Tal has come unstuck in material.
At Varna, in 1962, on move nineteen, his queen was attacked. So was his knight. So it goes. He took a pawn on f6 instead, and now both were hanging, and on move twenty-one he added a bishop on f5 for luck.
Hans-Joachim Hecht was a nice man from Germany. He could take the queen. He could take the knight. He could take the bishop. What he could not do was take them all, on account of how chess works, which is one move at a time.
He took the queen. He lost on move forty-nine anyway.
A bird outside said, “Poo-tee-weet?”"""),
54: ("Raymond Carver", """They were in the hotel in New York. It was the U.S. Championship, the end of 1963. Robert Byrne had White. He had a good position. Everybody said so.
In the other room two grandmasters were explaining it to the crowd. “White is winning,” one of them said. The other one nodded.
Fischer gave up a knight on f2. Then he played a few more moves. He put his queen on d7.
Byrne looked at the board for a while. He reached out his hand.
“He resigned,” somebody said in the other room.
“Who?”
“Byrne.”
Nobody said anything. Twenty-one moves. It was snowing a little. One of them lit a cigarette."""),
55: ("Jack Kerouac", """and so there we were in New York in sixty-three, Bobby Fischer and Pal Benko and the whole mad American championship, Bobby winning every game, every one, eleven and oh, and here's Benko with the Pirc all hunkered down behind his pawns thinking the f-pawn goes to f5 and I'm safe man I'm safe, and Bobby with those long hands lifts the ROOK, not the pawn, the rook, and sets it on f6, right there, plonk, in front of the pawn, a rook nobody can take and nobody can pass, the holy untouchable rook of West 81st Street, move nineteen, and two moves later a knight slides back to e2 soft as brushes on a snare and Benko digs it and resigns, yes, yes."""),
56: ("Hans Christian Andersen", """Once upon a time, in Bled, there lived a knight who wished very much to go to d5. “You cannot go there,” said the pawns, “for you will be taken, and nobody has counted what happens next.” But the knight belonged to a magician from Riga named Tal, who never counted anything to the end, and on the sixteenth move, in the last game of the match, in 1965, it went. And it was taken. Larsen the Dane held the extra piece in his hand, and it grew heavier and heavier, as gold does in such stories. On the thirty-seventh move the white queen came to f7. And the little knight, in the box, was perfectly happy."""),
57: ("Joan Didion", """This is a story about a queen sacrifice in Santa Monica, and it begins with the weather. It was the summer of 1966. The Santa Ana had not come yet. Petrosian was champion of the world, which meant that he did not lose and, specifically, that nobody sacrificed queens against him, in the way that nobody sold maps to his house. Larsen, a Dane, took a pawn on g6 with the queen on the twenty-fifth move. I want to be precise about this. It was not a gamble. The rooks were already on the third rank; I counted. Five moves later one of them went to g3. We tell ourselves stories in order to resign."""),
58: ("Murasaki Shikibu", """In the tenth game of the match at Moscow, in the spring of 1966, the Champion Petrosian, whose manner was so reserved that people compared him to the moon behind thin cloud, gave up a rook for a knight, and then, as if one such delicacy were insufficient, another. Spassky, the young challenger, of whom everyone spoke so warmly, could not but feel the sadness of things. On the thirtieth move the Champion's queen appeared on h8, offering herself with a check; should the king accept her, a knight would call at f7 and take everything back, with interest. Spassky bowed. How brief it was, the ladies said, and how perfectly composed."""),
59: ("Li Bai", """At Sousse, beside the sea, I raise my cup:
A guest has come from far Mongolia.
The pawn steps to e5 and the centre closes
Like a gate at dusk.

The white knights wander by the river.
The h-pawn climbs alone to h6.
Thirty moves; the bishop waits on the long diagonal
As the moon waits in the water.

Then the queen leaps onto h7 — a falling star!
If the king takes her, a pawn and a bishop finish it.
Myagmarsuren looks at the board and does not take.
I drink to Fischer; 1967; the lamp burns down."""),
60: ("Vladimir Mayakovsky", """Comrade rook!
          On c7!
                    Move seventeen —
take
     the pawn on c6,
                    the other rook,
                                   and don't explain!
Monte Carlo,
            nineteen sixty-eight,
                                 roulette next door —
Botvinnik
         does not gamble.
                         Botvinnik
                                  PLANS.
Rook takes f7!
              Portisch,
                       count your pieces:
plenty.
       Count your squares:
                          none.
A knight on e5,
               a bishop on h6 —
                               CHECK!
Twenty-six moves.
                 The casino
                           lost."""),
61: ("Alexander Pushkin", """In Moscow, nineteen sixty-nine,
The nineteenth game: Spassky, the White,
Unpacked the Najdorf line by line
And found the champion's king that night.
Petrosian, the cautious, the profound,
Who never gave an inch of ground,
Watched pawns come at him, e and f,
Like guests who will not go, till, deaf
To every defence that he knew,
His rooks stood by and could not speak.
The knight came in. The spot was weak.
At twenty-four, to g5 it flew.
My reader, has it been your fate
To see the careful man checkmate?"""),
62: ("Lydia Davis", """Problem

Larsen played b3 on the first move. He was on board one for the Rest of the World. This was in Belgrade, in 1970.

Spassky put his pawns in the centre. Larsen had said the centre was not important.

On move fourteen Spassky offered a rook on h1. Larsen had not thought of this. He thought of it now.

The h-pawn took on g2, then on f1, becoming a queen, with check.

It was move seventeen. Larsen had been playing for about as long as it takes to boil potatoes.

He resigned. He still thought, in general, that he was right about the centre."""),
63: ("Albert Camus", """The seventh game was played in Buenos Aires in 1971. Or perhaps it was the sixth; the heat makes these things uncertain. Fischer had a knight on c5, and everyone agreed it was the best piece on the board. Petrosian's bishop on d7 was bad. On the twenty-second move Fischer took the bad bishop with the good knight. People in the room made a noise. One must imagine him indifferent. A good knight is only an idea; an open file is a fact, and the rooks came down it like the sun at noon. On move thirty-four a bishop went to c4. Petrosian resigned. He said later that he had felt nothing in particular."""),
64: ("The Icelandic Sagas", """There was a man named Robert, son of Regina, called Fischer; he came out to Iceland in the summer of the year 1972. He had always opened with the king's pawn. Men said he knew no other way.
In the sixth game he pushed the pawn on c4. Boris, called Spassky, was champion then; a fair man and well liked. He said nothing, but played the Queen's Gambit, which he had never lost.
The pawns went forward on the king's side. On the thirty-eighth move a rook took on f6, and it could not be avenged.
After the forty-first move Boris stood up and clapped his hands for his enemy. That was thought well done. Robert said afterward that it showed a true sportsman. They were not friends before this."""),
65: ("James Joyce", """yes because he never played that before the Alekhine knight out to f6 and back and round by b6 in Reykjavik the thirteenth game and Spassky pushing the pawns after it yes and then the long afternoon and the adjournment and the sealed move in its envelope like a letter you dont open and five passed pawns against a rook O and his own rook shut up on h8 like a nun the whole time behind the bishop and the white king coming and going seventyfour moves I counted and the little f pawn on f2 at the end one step from being a queen and Spassky looking and looking at it and his eyes asked and yes he said yes I resign Yes."""),
66: ("Ursula K. Le Guin", """On the island of the sixty-four squares the old tale says that to master a dragon you must know its true name. Korchnoi brought the Dragon to Moscow in the autumn of 1974, and it was a great one, and he trusted it. But Karpov, who was young and spoke little, had gone alone to the quiet places beforehand and learned the name, syllable by syllable, to the nineteenth move and beyond. He did not raise his voice. A knight to e2. A rook to d5. On the twenty-seventh move the queen stood on h8, and the Dragon lay still. It was not a battle. A thing rightly named does not need to be fought."""),
67: ("Thomas Mann", """It was at Nice, in the year 1974, in the course of a Spanish Game of the most irreproachable pedigree, that Anatoly Karpov, a pale and scrupulous young man whose constitution one would not have thought equal to cruelty, placed upon the twenty-fourth move his bishop on a7; a square, be it noted, upon which that piece attacked nothing and defended nothing, but merely stood, like a doctor in a doorway, preventing the rooks of Herr Unzicker from leaving by the a-file while the white ones were assembled behind it at leisure. The patient lingered twenty moves. There was no crisis; there was only, as in the mountains, less and less air."""),
68: ("John le Carré", """Baguio City, October 1978. The score stood at five–five, which is to say nobody trusted anybody. The Soviet delegation had a parapsychologist in the fourth row; Korchnoi's people wanted him moved. There had been the business with the yoghurt. There had been the mirrored glasses. Now there was only game thirty-two, and Korchnoi, the defector, had chosen an opening so irregular that Moscow Centre would have called it a provocation. Karpov did what he had been trained to do. He sat very still and let the other man talk. By move forty-one a rook was on b7 and there was nothing left to say. Korchnoi did not come to the closing ceremony. He sent a note."""),
69: ("P. G. Wodehouse", """I don't know if you've ever seen a World Champion who has just been handed a prawn at the wrong end, but that was Karpov at Skara in 1980 when Tony Miles answered his king's pawn with a6. I mean to say, a6! On move one! It is the sort of thing Gussie Fink-Nottle would play after a third glass of port. “Rummy, Jeeves,” I said. “Most irregular, sir. It is called, I believe, the St. George.” Well, the champion sat up like a bishop who has found a frog in his mitre, overpressed, shed a pawn, and at move forty-six was observed to be resigning. Miles, I gather, had spent the night before on his back. Lumbago."""),
70: ("Langston Hughes", """Niksic, nineteen eighty-three,
Portisch got his king tucked in.
Says, Kasparov, you can't touch me.
Kid just grins that twenty-year grin.

    Bishop takes on h7 — check!
    One gone.
    Bishop takes on g7 — what the heck!
    Two gone.

Got them weary two-bishop blues.
Ain't got no pawns around my door.
Lasker played it in 'eighty-nine,
Folks been playing it ever more.

Thirty-five moves, the queen says b3.
King out walking with nowhere to be.
Lord, that boy from Baku town
Gonna take the whole world down."""),
71: ("H. P. Lovecraft", """I set down these notes in the hope that no other player will open the sixteenth game of the Moscow match of 1985. It was on the sixteenth move that the Thing arrived on d3: a black knight, bloated, tentacular, squatting in the very bowels of the white position, touching eight squares at once. Karpov, a rational man, believed it could be dislodged. It could not. For eighteen moves his pieces crawled about the first rank, unable to cross the third, while the unspeakable horse sat and sat. When at last it was removed, on the thirty-fourth move, it was too late; six moves later a rook gave check on e1. I have seen the diagram. I do not sleep."""),
72: ("The King James Bible", """And it came to pass in the ninth day of the eleventh month, in the year one thousand nine hundred eighty and five, that Garry the son of Kim went up against Anatoly in the city of Moscow, in the four and twentieth game. And Anatoly had need of victory, and Garry had need only that he fall not. And Anatoly sent his pawns against the king, even the f pawn and the g pawn. But Garry held fast, and his knight went forth at the two and thirtieth move, and smote. And at the two and fortieth move the knight stood upon d4, with check. And Anatoly gave up the crown. And Garry was two and twenty years old when he began to reign."""),
73: ("Douglas Adams", """The King's Indian Defence is a bit like the Ravenous Bugblatter Beast of Traal: mind-bogglingly dangerous, and convinced that if you can't see its king, it can't be mated. At Wijk aan Zee in 1985 Dr John Nunn, a mathematician, tested this against Beliavsky by the simple method of putting a knight where a pawn could take it and then, before anyone had finished saying “but that's a piece,” giving a rook on f3 and another one on f2. This is known in the trade as Not Panicking. The white king, which had planned a quiet afternoon on the queenside, was found on d1 at move twenty-seven by a bishop. The answer, in case you wondered, was twenty-seven."""),
74: ("Victor Hugo", """Leningrad, 1986. Sixteenth game. Night.
On one side of the board, a knight on d3, black, buried in the white camp like a cannon dragged into a cathedral: Karpov's. On the other side, a king and a storm: Kasparov's. Which arrives first? That is all of chess. That is all of history.
One man takes a queenside. The other takes a risk. Arithmetic is on the left; destiny is on the right.
Move thirty-five: a rook gives itself on g6. Move thirty-eight: the black king is in the street, at d5, bareheaded.
Move forty-one: a knight takes on f7.
Karpov stops the clock. Waterloo had fewer witnesses."""),
75: ("Federico García Lorca", """Seville. Five in the afternoon.
It was exactly move forty by all the clocks.
Kasparov one point behind, and the last game,
at five in the afternoon.

Green, how I want you, green square of f2.
The queen on the long diagonal.
Karpov in time trouble, a pawn already gone,
and the envelope sealed like a wound.

All night the seconds with their lamps.
No one slept in the Lope de Vega.

In the morning the bishop went on working, slowly,
a guitar with one string.
Sixty-four moves. The king steps to g2.
Twelve–twelve. The crown stays where it was.
Ay, Seville, nineteen eighty-seven!"""),
76: ("Antoine de Saint-Exupéry", """“Please,” said the little knight on g5, “take me.”
It was the twentieth game, in Lyon, in 1990, and the grown-ups in the audience were counting pieces, because grown-ups love figures. A knight had already been given on h6. Now here was another.
“If you take me,” said the knight, “the queen will come.”
And on the thirty-fourth move the queen did come, to h6, with check, and gave herself too. Karpov's king looked at her for a long time.
“What is essential,” said Kasparov, “is invisible to the material count.”
Forty-one moves. A bishop took on d5 with check. One sees clearly only with the attack."""),
77: ("Hunter S. Thompson", """We were somewhere around move nineteen on the edge of the tiebreak when the sacrifices began to take hold. Brussels, 1991. Rapid chess. Ivanchuk had a queenside like a federal highway and Yusupov, a quiet, bearded, decent man, had decided for reasons no sane person could reconstruct to throw his entire wardrobe at the white king. A knight went into h4. The rook lifted. Jesus. Ivanchuk queened a pawn, with check, a whole new queen, and it did not matter; the black king just stepped aside like a bouncer. Queen to g3 on move thirty-nine. Mate coming. Later, Yusupov admitted he couldn't prove any of it. You never can. That's the whole point."""),
78: ("Geoffrey Chaucer", """Whan that Octobre in Tilburg toune was come,
Of nynetene hundred nynety and oon the somme,
A kyng ther was, and that a worthy man,
That fro the tyme that he first bigan
To casten up his castel, loved pees.
But Short, his maister, wolde hym nat lese:
“Go forth,” quod he, “on pilgrimage to h6.”
And forth he wente, by h2, g3, withouten trikkes,
By f4 and g5, on his owene feet,
Thurgh quenes and rookes, in the open strete.
And Timman, though he hadde alle his route,
Ne koude nat stire, ne kepe the pilgrim oute.
At foure and thritty moves this tale is do.
Ther nys no man that saugh a kyng walk so."""),
79: ("Voltaire", """In the city of Linares, in the year 1993, the sage Karpov, having read in all the best authors that pieces should be developed, found on the twenty-second move that every one of his was standing on the first rank, where it had begun. “All is for the best,” said his second, “in this best of all possible positions.” Meanwhile the young Kasparov, who had read nothing but the board, pushed a pawn to the first rank and, in his haste, announced it as a queen while a knight would have done; whereupon there was a quarrel about clocks, as there is among philosophers. Twenty-seven moves. A knight came to f2. One must cultivate one's back rank."""),
80: ("Simone de Beauvoir", """One is not born a grandmaster; one becomes one. Judit Polgár had become one at fifteen, and in Buenos Aires in 1994, in a tournament where every game was obliged to be a Sicilian, the men still spoke of her as an exception, which is the polite name for an inconvenience. Shirov advanced on the kingside. It was his freedom to do so. On the tenth move she answered with her own g-pawn, two squares, into his face; then a knight to e5, then the other knight, and a queen's capture on g5 that no one had considered because no one had considered her. Twenty-nine moves. She did not transcend the situation. She won it."""),
81: ("Chinua Achebe", """The elders say that the man who brings ant-infested firewood into his hut should not complain when lizards visit. Topalov was a young man in Linares in 1994, and he had taken a pawn. Karpov was not young, and that year in that town no one could throw him.
On the twentieth move Karpov gave a rook on e6. Topalov took it, for among his people a gift is not refused. On the twenty-first the second rook took on g6, with check. Then things fell apart: the king's compound was open on three sides, and the queen walked in as a creditor walks in.
Thirty-nine moves. When the drums stopped, the old man had not raised his voice."""),
82: ("Don DeLillo", """They played on the hundred and seventh floor. You could see weather happening to other people. Kasparov and Anand, New York, 1995, a glass booth, the tenth game. The move had been made days before, in a room, by men with laptops; that was the thing about it. He was only delivering it now. Knight to g5 on move eleven, a known square with new information in it. Then a rook left en prise on a1, the bishop to h6. He played fast and went out and slammed the door. Anand sat inside the preparation like a man reading his own file. Thirty-eight moves. Everything was connected. The towers hummed."""),
83: ("Clarice Lispector", """What is a queen when she goes to g7? I ask because Ivanchuk put her there, at Wijk aan Zee in 1996, on the twenty-first move, where a bishop could simply take her, and I do not think he knew either, in the way one knows a fact. He knew it in the way one knows an egg. The pawn was already on g7's shoulder; if the queen was taken, the pawn would become — but what does a pawn become? Itself, finally. Shirov took her. He had to; refusing a queen is refusing to exist. Fourteen moves later a rook slid to a1, calm as a Sunday. And I, who was not there, am still inside that instant before the taking."""),
84: ("Isaac Asimov", """The First Law says a machine may not injure a human being. Nobody had told Deep Blue, which in February of 1996, in Philadelphia, was a cabinet the size of two refrigerators that examined a hundred million positions a second and had no opinion about any of them. Kasparov attacked its king. A human would have flinched; the cabinet took a pawn on b7, because it had calculated that the attack was one tempo slow. It was. On the thirty-seventh move a rook took on h7 with check, and for the first time a world champion resigned a regulation game to a machine. Kasparov won the match, four to two. The engineers took notes. There would be a next model."""),
85: ("Philip K. Dick", """It was the sixth game, New York, 1997, and Kasparov could no longer tell whether the thing across the board was a machine pretending to be a man or a room full of men pretending to be a machine. In game two it had played a quiet move, a human move. He had asked for the printouts. They had not given him the printouts.
On move seven he played h6. He knew the knight sacrifice on e6; everyone knew it. A machine would never — the knight took on e6.
His king was stuck in the centre. Was this real? He looked at the operator. The operator looked like a man.
Nineteen moves. He resigned and walked out. Later they dismantled it. That proved nothing."""),
86: ("Haruki Murakami", """It was a bishop ending with opposite colours, the kind that is always a draw, like Tuesdays. Linares, 1998. Shirov had two extra pawns that didn't matter. I made spaghetti and thought about it. On the forty-seventh move he picked up his bishop and put it on h3, where a pawn could take it. There was no reason for it. It was like a well at the bottom of a perfectly ordinary garden.
Topalov took the bishop. Then the black king walked through to the centre, exactly one step faster than before. That was all the well was for.
Fifty-three moves. Somewhere a cat I used to own stretched. I listened to the record again, but it sounded different."""),
87: ("John Milton", """Of that first Rook's surrender on d4,
At Wijk aan Zee, in ninety-nine, whereby
The sable King, from his high battlement
Hurled headlong, flaming, down the a-file fell,
b6, a5, a4, nine squares of ruin, sing,
Heavenly Muse. Him the Almighty Kasparov
Pursued with check on check; nor Topalov,
Though of a Rook and Knight possest, could stay
The descent: for on the six and thirtieth move
A Bishop, quiet, turned at f1,
And all his host was vain. At forty-four
The Queen ascended to a7. So fell
Not without glory he who took, and taking
Made possible the thing that none had seen."""),
88: ("George Orwell", """It was a bright cold day in October, in London, in the year 2000, and the clocks were running. Kasparov had been champion for fifteen years. That was the first thing one had to understand. It was not that he usually won; it was that his winning was a fact of nature, like the price of bread. In the second game Kramnik, a tall, mild young man, exchanged queens early. There is nothing heroic in exchanging queens. It is merely what works. Then he took a pawn. Kasparov made a mistake in time trouble, of the plain kind that clerks make. Forty moves. A bishop went to d5. The matter was reported in the newspapers as a change of regime."""),
89: ("Maya Angelou", """You may write me down in your databases
as the girl who would be broken on the wheel.
You said a woman's game was made of laces.
Moscow, 2002. I came to deal.

Does my Ruy Lopez upset you?
You chose the Berlin, that old grey wall.
I put my rooks on the seventh, two
together, and I watched it fall.

    Out of the endgame's patient ache,
    I take.
    Up from a past of being shown,
    I take g7, and it's my own.

Forty-two moves. The king runs to c8.
You shook my hand, late.
I am the dream and the hope of the pawn.
I queen."""),
90: ("Henrik Ibsen", """A hotel hall, Wijk aan Zee. January 2004. Snow at the windows.
ERNST. You are thirteen years old.
CARLSEN. (Not looking up.) Yes.
ERNST. I have played this Caro-Kann all my life. It is a solid house.
CARLSEN. There is something behind the wall. On g6. (He places a knight there.)
ERNST. I cannot take that. If I take it, the e-file —
CARLSEN. Then the bishop takes on h6.
ERNST. And if I take that?
CARLSEN. The rook takes on h6. With check.
ERNST. (Quietly.) All these years I thought the pawns were holding it up.
(The queen goes to d7. Move twenty-nine. Mate.)
ERNST. I must go out. Into the snow."""),
91: ("Hermann Hesse", """In Brissago, above the lake, where the chestnut woods come down to the water, Kramnik found himself in the autumn of 2004 one point behind with one game left. He had been a champion; he had been, he saw now, asleep. Leko played the Caro-Kann as a man shuts a gate. And Kramnik, who had always sought safety, understood on this last morning that the way led not around danger but through it. He let the queens go. He sent his king forward on foot, up the dark squares, to g5, alone, like a pilgrim. On the forty-first move a knight gave check at f7. The match was tied, and the title kept. He had lost himself and was, at last, awake."""),
92: ("Cormac McCarthy", """They rode into the Semi-Slav at Wijk aan Zee in the winter of 2008 and on the twelfth move the knight took the pawn on f7 and nobody spoke. It was not in the books. Cheparinov had found it three years before in a hotel room and they had carried it since like a thing wrapped in oilcloth. Kramnik took the knight. He had the piece and the bishops and the long theory of his people and none of it availed him. The white pawns came down the centre of that country like weather. He looked at the clock and the clock looked back. Forty-five moves. A knight on e6. Whatever in the opening exists without my knowledge, Topalov said, exists without my consent."""),
93: ("Rabindranath Tagore", """Where the knight is without fear and the bishop held high on b7;
Where the Meran has not been broken up into fragments by narrow home analysis;
Where the g-file is open, my Lord, and the rook stands upon it in the morning light at Bonn;
Where Kramnik, having the white pieces and a pawn, wanders in the dreary desert sand of his own extra material;
Where on the thirty-third move he errs, and the black queen and bishop descend like the first rain;
Where the last check is given from b1, at move forty-one, in the year 2008:
Into that heaven of the black pieces, my Father, let Anand awake."""),
94: ("Salman Rushdie", """It was the twelfth game, the last game, the game-of-games, in Sofia, in 2010, and Topalov-the-home-hero needed only to sit still, which was the one thing in all the Balkans he had never learned to do. Anand, who had arrived by a forty-hour bus because a volcano with an unpronounceable name had closed the sky (this is true; in my stories the unbelievable parts are always the true ones), played the Lasker Defence, old as grandmothers. On move thirty-one Topalov took a pawn he should have left. Whoosh: the long diagonal opened like a bazaar. Rook takes g4! Queen, queen, queen. Fifty-six moves; the queen sat on g7; the title stayed, chutnified but whole."""),
95: ("Arundhati Roy", """It was January in Wijk aan Zee and the wind came off the sea like a rumour. The game began the way these games do: with a Slav, with Small Things. A pawn. A bishop put away in its room.
Then, on the fifteenth move, Anand placed a bishop on c5 where it could be taken. And on the sixteenth a knight on e5 where it could be taken too. Two Loved Things, left on the verandah in the rain.
Aronian could have either. Not both. Not neither.
The king's house had no walls by then. Only windows.
On the twenty-third move a bishop came to e3, and it was over the way a monsoon is over. Suddenly. All at once. In 2013."""),
96: ("Karl Ove Knausgård", """I woke at seven and made coffee. It was November 2013; in Chennai the ninth game had started. I stood by the window with the cup. Carlsen was twenty-two and had Black and was ahead in the match and Anand had to win, had pushed his pawns all the way up to the king, f4, f5, f6, like someone finally saying what they mean. I thought about my father. Carlsen just ran his own pawn down the b-file and made a second queen, on b1, with check, as though nothing else was happening. Then Anand moved the knight to f1. It was the wrong piece. It should have been the bishop. Twenty-eight moves. The queen came to e1. I rinsed the cup. That was all."""),
97: ("F. Scott Fitzgerald", """It was Carlsen's twenty-sixth birthday, and all of New York had been invited, or at any rate the part of it that could stand behind glass at the Seaport and whisper. The match had come down to tiebreaks, quick bright games like cocktails. In the fourth one he needed nothing; a draw would do. He was already champion in every sense but the minute hand. And then on the fiftieth move, because he was young and the lights were on him and it was there, he put the queen on h6 with check, to be taken by the king or by the pawn, and mate either way. So we beat on, rooks against the back rank, borne ceaselessly into the brilliancy prize."""),
98: ("Lu Xun", """I looked up the old chess manuals. On every page was written: “protect the king, value the pieces.” I could not sleep, and read carefully half the night, until I saw, between the lines, two other words: “give them.”
In the Chinese League, in 2017, Bai Jinshi played white against Ding Liren. On move fifteen Ding left a knight to be taken. On move twenty a rook went to d4, in the open. Then the queen was offered. The white king was led out by the hand, e2, f3, g4, the way a man is led to the square while the neighbours watch.
Thirty-two moves. A knight checked on e5.
Perhaps there are still children who have not learned to count material. Save the children."""),
99: ("Georges Perec", """Inventory of the sixth game, Dubai, 3 December 2021:
1 board; 32 pieces at the start, 9 at the end;
136 moves (a record for the championship), of which 136 by White and 135 by Black;
7 hours and 45 minutes; 1 midnight, passed;
1 queen (White's) exchanged at move 26 for 2 rooks;
1 queen (Black's) which remained, and gave 14 checks, none of them sufficient;
2 white pawns, e and f, advancing 1 square at a time, with pauses of up to 9 moves;
1 knight, arriving on g7 at move 136;
0 mates; 1 resignation; 1 handshake;
1 challenger who did not afterwards win a game;
several glasses of water, unremarked."""),
100: ("Raymond Queneau", """Notation. In the tiebreak, in Astana, towards the end of April 2023. A player of about thirty, Ding, glasses, with the black pieces, very little time on the clock. Opposite, a man with a topknot, Nepomniachtchi, who has been ahead three times. The position is a draw; people get on and off. Ding is offered a repetition of moves. He declines it in a tone which is meant to be aggressive: he puts his rook on g6, pinning it himself against his own king. He then throws himself onto a passed pawn.
Twenty-two moves later, on the sixty-eighth, a bishop takes on f4. A friend is telling him: “You ought to get a crown put on that.” He shows him where (on the head) and why."""),
}
assert len(EX) == 100 and len({a for a, _ in EX.values()}) == 100
