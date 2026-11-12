"""Los cien ejercicios de estilo, en español. Versiones de los pastiches de styles.py,
no traducciones palabra por palabra: donde el original parodia una frase célebre, la versión
parodia la frase tal como la conoce el lector en español (Cervantes, García Márquez, Rulfo, Lorca
y Borges en su propia lengua; los demás en sus traducciones más conocidas). Jugadas, casillas,
fechas y resultados son los mismos que en el original. Los nombres de los autores van en
i18n_es.AUTHOR."""

EX = {
1: """Canta, oh musa, la cólera de La Bourdonnais, rompedor de centros, que vino por el mar gris hasta Londres y se sentó frente a McDonnell, el de las piezas blancas. Treinta y siete veces alzó el brazo cada héroe. Las damas fueron arrojadas como lanzas que ya han cumplido su tarea. Y al final tres peones negros se alzaron hombro con hombro en la segunda fila, de grebas de bronce, incansables, como tres hermanos ante una puerta; y la puerta era la última fila, y ninguna torre de McDonnell pudo sostenerla. Así cayó la casa de las blancas en el año 1834.""",
2: """Me han referido que en Londres, en 1851, Adolf Anderssen entregó un alfil, luego las dos torres, luego la dama, y que con lo que le quedaba (tres piezas menores, el rumor de un ejército) dio mate a Kieseritzky en la jugada veintitrés con un alfil en e7. Sospecho que la partida no fue jugada sino recordada. En algún lugar hay una biblioteca en cuyos anaqueles está toda partida posible; en esa biblioteca esta se encuaderna en un solo volumen, y cada lector que lo abre es, durante veintitrés jugadas, Anderssen. Kieseritzky es el espejo.""",
3: """Un Gambito — del Capitán Evans —
se ofreció en Berlín —
y Dufresne lo tomó — como se toma
lo que la Cortesía deja entrar —

Se dio el Caballo — y la Torre —
la Dama al fin — a d7 —
Un Jaque Doble — es una Puerta —
que se abre — hacia el Cielo —

Dos Alfiles hicieron — lo Final —
en la Veinticuatro — se acabó —
La llaman Siempreviva — porque —
no deja — de ganarse —""",
4: """¡Es verdad! Nervioso, muy terriblemente nervioso estaba Paulsen aquella noche en Nueva York, en el año 1857, porque había pensado una hora entera sobre una sola jugada, y aun así el joven de Nueva Orleans no se movía. Y entonces, en la jugada diecisiete, Morphy tomó con la dama un caballo en f3. ¡Con la dama! Oí al peón recapturar; oí al alfil llegar a h3; oí, bajo el suelo de la posición, un sonido sordo, apagado y rápido, como el de un rey emparedado. En la jugada veintiocho cesó. El alfil estaba en e3. Paulsen abandonó.""",
5: """Perder un caballo en b5 puede considerarse generosidad; perder una torre en d7 parece extravagancia; regalar la dama en b8 es sencillamente genialidad. El señor Morphy hizo las tres cosas en un palco de la ópera de París en 1858, mientras un duque y un conde consultaban contra él y contra la soprano. La aristocracia, como de costumbre, tomó todo lo que se le ofrecía. En la jugada diecisiete una torre llegó a d8 y fue mate. Siempre habría que jugar al ajedrez en la ópera. Es la única manera de estar seguro de que alguien escucha.""",
6: """París, luz de invierno —
se abre una siciliana
como un biombo.

El caballo en b5
mira a d6. Viejo estanque;
la rana aún no salta.

El rey de Anderssen
sale a la nieve en f7.
Nadie lo sigue.

Diecisiete jugadas;
luego el ruido de una silla.
Morphy: uno–cero.""",
7: """Era la mejor de las posiciones, era la peor de las posiciones; era Londres en 1883, y el señor Zukertort, un caballero menudo y veloz compuesto enteramente de nervios y combinaciones, estaba sentado frente al señor Blackburne, a quien los periódicos llamaban la Muerte Negra y los camareros llamaban señor. El señor Blackburne tenía una torre en la séptima fila y estaba satisfecho. En la jugada veintiocho el señor Zukertort colocó su dama en b4, donde cualquiera podía tomarla; y el señor Blackburne, que reconocía una herencia con pleito incluido en cuanto la veía, la rechazó. No le sirvió de nada en absoluto. Treinta y tres jugadas; se levantó la sesión.""",
8: """—Observará usted, Watson, que el rey de Bauer solo tiene por muralla los peones de h7 y g7. Un joven llamado Lasker lo observó en Ámsterdam en 1889. Entregó un alfil por el primer peón en la jugada quince.
—¡Y perdió una pieza!
—Después entregó el segundo alfil por el segundo peón. Una vez eliminados los peones, Watson, lo que queda, por expuesto que esté, tiene que ser el rey. La dama y una torre hicieron el resto, y de paso recogieron un alfil de sobra. Treinta y ocho jugadas. Nunca se había hecho. Desde entonces lo llaman elemental.""",
9: """¿Y si les digo, señores, que Chigorin quería perder? No, no, no es que quisiera, pero había en él, en La Habana, con aquel calor, en 1892, una vocecita rencorosa que decía: que el viejo enseñe lo que tiene. Y Steinitz lo enseñó. En la jugada veinticuatro la torre tomó en h7, con jaque, una torre sencillamente tirada, y el rey negro fue arrastrado del cuello por todo el tablero, a g7, a f6, a e5, como un deudor por las calles. En la jugada veintiocho la dama tomó en d4. Chigorin se rio. Estoy seguro de que se rio.""",
10: """En la jugada veintidós apareció una torre blanca en e7, junto al rey de von Bardeleben, y no podía ser capturada. Nadie se lo explicó. La torre se desplazó por la séptima fila, a f7, a g7, dando jaque cada vez, cada vez incapturable por razones perfectamente válidas que cambiaban con cada casilla. En la jugada veinticinco tomó en h7. Von Bardeleben se levantó, se puso el abrigo y abandonó la sala de Hastings sin abandonar la partida. Era el año 1895. El reloj siguió corriendo en su ausencia, como hacen los relojes. Steinitz esperó. El mate se le demostró al público en su lugar.""",
11: """Canto al joven Pillsbury, de veintidós años, de Massachusetts, llegado a Hastings en 1895, desconocido, a pie y con el corazón ligero,
canto al Gambito de Dama, al peón ofrecido y rehusado, a la larga presión paciente de las piezas blancas,
a Tarrasch el doctor avanzando por el flanco de dama, peón tras peón, seguro de su ciencia,
y al americano yendo en la otra dirección, hacia el rey, ¡oh, hacia el rey!
Cincuenta y dos jugadas, y cada una contenía multitudes,
y al final la dama en h7, mate, la sala poniéndose en pie,
yo también soy intraducible; yo también tomo en h7 por encima de los tejados del mundo.""",
12: """Dicen que Pillsbury cargó con esa partida el resto de su vida como se carga una casa que se quemó. San Petersburgo, pleno invierno volviéndose 1896. Él tenía las blancas y tenía a Lasker apretado, y entonces bajó una torre negra y tomó el caballo de c3. Lo tomó sin más. Se entregó. Y la otra torre se deslizó a a3 y se quedó allí, a la vista, pidiendo. No podías tomarla y no podías dejarla. Así es como vuelven los muertos. Treinta y dos jugadas. La última fue un alfil en b6, y fue mate, y fue callado como un secreto guardado.""",
13: """Yo estuve en Cambridge Springs en 1904, o habría estado si me hubiera enterado, y puedo informar de que el señor Lasker y el señor Napier jugaron allí una partida de ajedrez con más ataques que unas elecciones en Misuri. Napier atacó. Lasker, en vez de defenderse como un cristiano, contraatacó. Luego atacaron los dos a la vez, cosa que yo tenía entendido que estaba prohibida. Las piezas quedaban colgando como ropa tendida. Al cabo de treinta y cinco jugadas Lasker tenía un alfil en e3 y la partida. Napier jugó la mejor partida de su vida. La perdió. Eso es el ajedrez.""",
14: """En Lodz, en 1907, había un jugador llamado Rotlewi que creía que, si no perdía peones, el Todopoderoso se ocuparía del resto. Frente a él se sentaba Akiba Rubinstein, que había estudiado para rabino y había dejado el Talmud por el Gambito de Dama, que también tiene comentarios. En la jugada veintidós Rubinstein entregó una torre en c3. En la veintitrés entregó otra en d2. La dama ya estaba colgando. Rotlewi miraba sus riquezas como un hombre que se encuentra una bolsa en sábado. En la jugada veinticinco una torre llegó en silencio a h3. Rotlewi abandonó. En Lodz decían: jugó un demonio, no un hombre.""",
15: """Durante mucho tiempo Capablanca no había perdido, y era quizá esa costumbre de no perder, más que cualquiera de las jugadas que Rubinstein hizo en San Sebastián en 1911, lo que volvió tan dolorosa para él la captura del peón de d5 en la jugada quince, una captura que había creído imposible y que un pequeño detalle táctico (tan pequeño que se parecía a esos recuerdos que solo advertimos cuando ya lo han alterado todo) hacía no solo posible sino decisiva; y a lo largo de las veintisiete jugadas que siguieron, en un final conducido con la lentitud de una tarde en la que no ocurre nada salvo la tarde, aquella fue la única partida que perdería allí.""",
16: """Ha llegado a mis oídos, oh rey afortunado, que en la ciudad de Breslau, en el año 1912, un americano llamado Marshall jugaba al ajedrez contra Levitsky, de los rusos, y en la jugada veintitrés depositó su dama en g3, en la misma boca de tres enemigos: pues dos peones podían tomarla, y una dama podía tomarla, y quien la tomara estaba perdido. Y Levitsky inclinó la cabeza. Entonces, según se cuenta, la gente de aquella ciudad hizo llover monedas de oro sobre el tablero hasta que las casillas quedaron ocultas. Pero hay quien dice que las monedas eran solo apuestas que se pagaban. Y en esto Sherezade vio que amanecía, y se calló discretamente.""",
17: """—Muevo mi dama a h7 y tienes que tomarla —dijo Lasker.
—¿Y por qué tengo que hacerlo? —dijo el rey de sir George.
—Porque es jaque, y eres el único que está en casa.
Así que el rey la tomó, y enseguida se encontró caminando: a h6, a g5, a f4, abajo y más abajo por el tablero, con un caballo o un peón diciendo «¡Jaque!» a su espalda a cada paso. «Nunca había estado tan lejos de mi propia fila», dijo en g1. «¿Dónde estoy?»
—En mi casa —dijo el rey blanco, y se apartó cortésmente a d2.
Y eso fue mate, en la jugada dieciocho, en Londres, en 1912, y lo dio un rey.""",
18: """Todas las partidas tablas se parecen; cada partida ganada se gana a su manera. Capablanca llegó al tablero en San Petersburgo en 1914 necesitando solo no perder, y Lasker, que tenía cuarenta y cinco años y entendía a los hombres mejor que las aperturas, cambió su alfil por un caballo en la cuarta jugada y quitó las damas, como diciendo: muy bien, que sean tablas. Y Capablanca le creyó. Eso fue todo. En la jugada doce un peón fue a f5, y durante treinta jugadas más el joven buscó la vida sencilla que le habían prometido. En la cuarenta y dos llegó un caballo a c5, y abandonó.""",
19: """Tarrasch, que durante veinte años les había dicho a Nimzowitsch y a todos los demás, en lengua alemana, qué era correcto y qué era incorrecto, como si el ajedrez fuera un hospital y él su médico jefe, ese mismo Tarrasch, en San Petersburgo en 1914, entregó un alfil en h2 y luego el otro alfil en g2, exactamente como lo había hecho Lasker en Ámsterdam, exactamente, un plagio, debió de pensar Nimzowitsch, un plagio correcto, la peor clase de plagio, y sacó al rey blanco por todo el tablero para darle mate en la jugada treinta y dos con un alfil en b5, con un alfil, naturalmente, y Nimzowitsch nunca se lo perdonó, naturalmente.""",
20: """Era Nueva York, 1918, y Marshall llevaba en el bolsillo un gambito que cargaba desde hacía años como un arma guardada para un solo hombre. El hombre era Capablanca. En la jugada ocho el peón fue a d5 y la sala se quedó tan callada como un banco a medianoche. El cubano lo tomó. Veía que era una trampa; lo tomó de todos modos, como uno se mete en un callejón porque es el camino más corto a casa. Durante veinte jugadas Marshall le tiró todo al rey: caballo, alfil, dama. Capablanca se quedó ahí y dejó que rebotara. En la jugada treinta y seis un alfil tomó en f7 con jaque. Marshall tiró las cartas. Algunas sorpresas envejecen mal.""",
21: """Vine a Nueva Orleans porque me dijeron que acá jugaba un muchacho, un tal Carlos Torre, mexicano. Era 1920. Hacía calor y no había nadie en las calles. En el tablero había una sola columna abierta, la columna e, y cuatro torres mirándose a través de ella como gente en un velorio. Entonces Adams empezó a ofrecer la dama. En g4. En c4. En c7. Cada vez la dama negra se iba un poquito más lejos, sin decir nada. Se le oía la respiración. En la jugada veintitrés la dama blanca tomó un peón en b7 y se acabó. Torre levantó la vista. Yo creo que ya estábamos todos muertos.""",
22: """Bogoljubov (una sílaba rolliza de hombre) tenía las blancas en Hastings en 1922, y Alekhine tenía el plan, que es lo que más conviene tener. Recuerdo la partida como se recuerda una escalera en un sueño: un peón negro desciende por la columna b, una torre es abandonada en a8 con deliciosa indiferencia, el peón corona; se conjura una segunda dama, se cambia, y un tercer peón, en la jugada cincuenta y tres, avanza a d5 con jaque, un jaque de peón pequeño y callado, la sonrisa al final del soneto. Tres damas desde un solo lado del tablero. Los problemistas se sonrojan. Bogoljubov abandonó, me gusta pensar, sonrojado también.""",
23: """Quienes estuvieron en Teplitz-Schönau en el otoño de 1922 hablarían más tarde de un curioso desasosiego. Maróczy, el gran defensor, un hombre del mundo de ayer en quien la prudencia se había convertido en una forma de cortesía, había enrocado y no quería nada. Y entonces, en la jugada diecisiete, el doctor Tartakower colocó una torre en h2. No fue un golpe; eso era lo inquietante. No siguió nada de inmediato. Había entregado una torre, una torre entera, solo por la idea de un ataque, y siguió desarrollando tranquilamente sus piezas, como quien termina una carta. Hacia la jugada treinta y cinco, un caballo en g3, el mundo de ayer había abandonado.""",
24: """Copenhague. 1923. Un tablero.
SÄMISCH: Tengo todas mis piezas.
NIMZOWITSCH: Casi todas.
SÄMISCH: Una pieza por dos peones.
NIMZOWITSCH: Sí.
(Pausa.)
SÄMISCH: Entonces muevo.
NIMZOWITSCH: Mueve.
(Sämisch no mueve.)
SÄMISCH: La dama no puede moverse. Las torres no pueden moverse. Los alfiles. El caballo.
NIMZOWITSCH: Quedan los peones.
SÄMISCH: Entonces se acabarán.
NIMZOWITSCH: Entonces se acabarán.
(Nimzowitsch juega un peón a h6. Jugada veinticinco. No ataca nada.)
SÄMISCH: Nada que hacer.
(No se mueve. Telón.)""",
25: """Muchos años después, frente al rey negro en un tablero casi vacío, José Raúl Capablanca había de recordar aquella tarde remota de 1924 en Nueva York en que dejó que Tartakower le comiera los peones. Era un final de torres y había llovido números toda la mañana. El rey blanco salió de su casa en la jugada treinta y cinco y subió por el tablero, g3, h4, g5, f6, sin equipaje, mientras detrás de él le comían los peones uno a uno, con jaque, y él no se daba vuelta. Había entendido que un rey que llega vale más que todo lo que ha abandonado. En la jugada cincuenta y dos un peón llegó a d6 y Tartakower, que era poeta, abandonó en prosa.""",
26: """Capablanca no perdía. Capablanca no perdió en ocho años. Ocho años son ocho años y no perder es no perder y entonces en Nueva York en 1924 estuvo Réti. Réti abrió con un caballo. Un caballo no es un peón. Los alfiles estaban en las líneas largas y las líneas largas eran largas. Un alfil en una línea larga es un alfil en una línea larga es un alfil. Treinta y una jugadas. Entonces una torre fue a d5 y la otra torre estaba en d6 y ahí estaba. Capablanca perdió. Perder una vez es una vez. Había un ahí ahí y era d5.""",
27: """Estás a punto de reproducir una partida de Richard Réti: Nueva York, 1924, contra Bogoljubov. Relájate. Deja que el tablero se vacíe de todo lo que esperas que contenga una partida. Aquí no hay asalto al rey, ni peón en el centro; los alfiles blancos viven en las esquinas de la ciudad y envían, por diagonales finas como cables de tranvía, mensajes que llegan veinte jugadas después. En la jugada veinticinco uno de ellos se planta en e8, una casilla en el mismísimo borde del mapa, sin atacar nada que puedas ver. Bogoljubov abandona. Pasas la página buscando el resto de la partida. Esto era el resto de la partida.""",
28: """En Baden-Baden, en la primavera de 1925, la banda tocaba todas las tardes, y Réti abrió moviendo una casilla el peón que estaba delante de su caballo, lo cual irritó a Alekhine más de lo que él habría admitido. Hacía calor. El perro de alguien se había metido en la sala. En la jugada veintiséis Alekhine puso una torre en e3, donde un peón podía tomarla, y Réti se quedó largo rato con la mano en la mejilla, pensando en la torre y también, por alguna razón, en Viena. No la tomó. Dieciséis jugadas después llegó un alfil a d5 y perdió una pieza de todos modos. La banda seguía tocando.""",
29: """En una sala de Moscú, de cuyo nombre no quiero acordarme, se sentaba en 1925 un joven hidalgo de Yucatán, don Carlos Torre, frente al viejo encantador Lasker. Y en la jugada veinticinco puso su alfil en f6 y dejó que le tomaran la dama. «Vuestra merced ha perdido el juicio», dijeron los mirones. Mas la torre tomó en g7 con jaque, y se retiró con jaque, y volvió a tomar con jaque, vuelta y vuelta como las aspas de un molino, moliendo un peón, otro peón, un alfil y por fin a la mismísima dama, hasta que al gigante no le quedó sino su dignidad. Cuarenta y tres jugadas. Y esta vez, lector, ganó el molino.""",
30: """Sun Tzu dijo: quien bloquea el camino no necesita combatir en él.
En Dresde, en 1926, Johner sostenía el centro con muchos peones. Nimzowitsch no los atacó. Se plantó delante de ellos.
Un peón que no puede avanzar es una muralla construida para el enemigo.
Entonces la dama fue por un camino pequeño, de d8 a d7, a f5, a h7, por detrás de sus propios soldados. Los hombres se rieron. La excelencia suprema es que se rían de ti en la jugada doce y te obedezcan en la cuarenta.
Cuando el ejército blanco ya no pudo moverse, fue golpeado allí donde estaba. Cuarenta jugadas. El general que vence ya ha vencido.""",
31: """Esta partida puede leerse de dos maneras. En la primera, Alekhine y Capablanca se sientan en Buenos Aires en 1927 y juegan ochenta y dos jugadas, y en la última una torre va a e7 y Capablanca, que antes era invencible, ya no es campeón del mundo. En la segunda, se empieza en la jugada treinta, donde un caballo toma en e5, luego se salta hacia atrás a la apertura, luego hacia adelante al final de torres, que dura más que varios matrimonios. De cualquier modo el lector notará que en algún momento Capablanca empezó a jugar otra partida, una en la que el que perdía era él, y que nadie le avisó que habían cambiado las piezas.""",
32: """Nada sucede dos veces, salvo en Varsovia, hacia 1929,
donde Najdorf entregó un alfil en h2,
luego otro alfil, luego un caballo, y luego el otro caballo,
es decir, todo lo que una persona podría razonablemente conservar.

Glücksberg los tomó. Uno toma lo que le dan.
Su rey salió a g4 como quien sale a ver qué tiempo hace.

El mate se dio en la jugada veintidós
con un peón, a h5, lo más pequeño del tablero.
Prefiero los peones.
Prefiero el ridículo de entregar cuatro piezas
al ridículo de no entregarlas.""",
33: """Un príncipe que quiera conservar una columna debe conservarla con todas sus fuerzas, y en el orden debido. Alekhine, en San Remo en 1930, colocó una torre en la columna c, y la segunda torre detrás de ella, y la dama detrás de ambas, disposición que los hombres llamaron después el Cañón; porque es más seguro ser temido a lo largo de una línea que amado a lo largo de varias. Nimzowitsch, que había escrito un libro sobre cómo deben impedirse tales cosas, defendió el punto c7 con todo lo que poseía, y así no le quedó nada que mover. Un príncipe que no puede moverse no es príncipe. Abandonó en la jugada treinta y dos con casi todo su ejército aún sobre el tablero, y nada de él capaz de moverse.""",
34: """El mar en Zandvoort estaba gris, y Euwe, que era maestro de escuela y pensaba en columnas, miró el tablero y pensó, qué raro, que fuera ahora, en la partida veintiséis, a finales de 1935, cuando un caballo fuera a f5 y se ofreciera, y que fuera él el elegido. Porque allí estaba Alekhine, al otro lado de la mesa, enorme, una ola a punto de romper. Los peones avanzaron, dos de ellos, uno junto al otro, como niños de la mano en un muelle. Uno no miraba hacia abajo. Llegó la jugada cuarenta y siete; un caballo dio jaque en e4; y se acabó, y el campeón, sí, antes de que terminara el invierno, sería Euwe. ¡Qué alegría!""",
35: """A la hora de la sesión de la tarde, en Rotterdam, en 1938, dos ciudadanos se sentaron ante un tablero. El primero era el cubano Capablanca, que no cometía errores; el segundo era el ingeniero Botvinnik, que no creía en lo sobrenatural. Y sin embargo, en la jugada treinta, el ingeniero tomó su alfil y lo colocó en a3, donde la dama negra podía tomarlo a cambio de nada. Los testigos declaran que hubo olor a azufre. La dama tomó. Un caballo saltó a h5 con jaque; un peón avanzó a e7 como si ninguna fuerza de este mundo pudiera detenerlo; y en la jugada cuarenta y uno el rey blanco salió del último jaque hacia h5. Los manuscritos no arden. Esa partida tampoco.""",
36: """Consideremos el alfil de a1. En 1946, en Praga, en un match entre la ciudad y Moscú, Bronstein lo capturó con su torre en la jugada veinte, entregando la calidad, y luego entregó más. Pachman, que era checo y por lo tanto creía que la historia tenía una dirección, calculó que estaba ganando material. Lo estaba. Esto es lo que yo llamo la levedad del sacrificio: el que da se vuelve ingrávido, y el que toma pasa de pronto a ser responsable de todo el tablero. Once jugadas después un peón fue a h3 con jaque. Pachman abandonó. En la India de Rey, como en el amor, el materialista siempre es el último en enterarse.""",
37: """A mitad del camino de la partida, en Zúrich, en 1953,
yo, Averbakh, hallé a mi rey en una selva
de sus propios peones, y creí el lugar seguro.

Entonces la dama de Kotov tomó en h3, con jaque;
la tomé; y una torre dijo: sígueme.
A g4 bajé, y luego a f5,

cada círculo más estrecho, un caballo en cada puerta,
mis torres y mi dama arriba, en la luz,
demasiado lejos para oír. Lo habría dado todo

por una sola casilla libre. En la cincuenta y uno una torre
llegó a g8, y depuse las armas.
Abandonad las damas, los que aquí entráis.""",
38: """—Es muy sencillo, mes amis —dijo el pequeño belga—. En Zúrich, en 1953, monsieur Geller ataca al rey. Tiene la dama, la torre, el alfil: todos los sospechosos están en el flanco de rey. ¿Y qué hace el doctor Euwe en la jugada veintidós? Coloca una torre en h8. ¡En la esquina! ¡Para que se la tomen!
—Un descuido, sin duda —dijo Hastings.
—No, no. Un señuelo. La dama blanca toma; ahora está, ¿cómo se dice?, fuera de la ciudad. Tiene coartada. Y en su ausencia la dama y la torre negras visitan al rey blanco. Cuatro jugadas. La dama llega a f3. El asesino, Hastings, era la víctima.""",
39: """. . . una torre, Keres la puso en h5
y podía ser tomada . . .

. . . unos dicen que un ejército de jinetes es lo más bello,
otros dicen que las damas; yo digo
que es aquello que uno rehúsa . . .

Smyslov miró largo rato
(Zúrich; las hojas; 1953)
y no tomó . . .

. . . el centro, dulceamargo, se abrió
y los peones pasaron como
. . .

veintiocho jugadas . . . la dama en d4, con jaque . . .
y de la torre en h5
nadie después se acordó . . .""",
40: """Oda al peón de f4

Peón de Najdorf,
pequeño diente negro
de la India de Rey,
en Zúrich, en el cincuenta y tres,
dejaste el flanco de dama
a Taimanov:
que se lo quede,
que se coma
la larga mesa entera
de la columna a.
Tú ibas caminando
hacia el rey.
f5, f4, g5, g4,
los peones bajaban
como mineros
con lámparas,
y detrás de ellos
los caballos, el alfil en h3,
la torre
llegando tarde
con el pan.
Cuarenta y tres jugadas.
Yo canto
al que regala
medio mundo
para golpear
una sola puerta.""",
41: """Es una verdad universalmente reconocida que un jugador en posesión de un centro fuerte necesita una ruptura. El señor Reshevsky, en Zúrich en 1953, poseía dos peones de excelente familia en d4 y e5, y era opinión general que avanzarían. El señor Petrosian, un joven de escasa fortuna y gran prudencia, colocó una torre en e6, justo en su camino, donde un alfil podía tomarla; y se declaró perfectamente indiferente a su pérdida. La torre fue tomada; un caballo se instaló en d5 de por vida; y al cabo de cuarenta y una jugadas las partes acordaron, con igual satisfacción y ningún afecto, unas tablas.""",
42: """Moscú, 1954. La partida catorce.
Yo estuve allí, donde estaba la gente,
en la sala de las cortinas pesadas.

Él entregó la dama. No como se da
un regalo. Como se renuncia a un nombre.
Por ella: una torre y dos alfiles.

Botvinnik contó. Hacía bien en contar.
Los tres avanzaron como el invierno en un patio.

Nadie gritó. Habíamos aprendido
a no hacerlo. En la jugada treinta y tres
un caballo fue a c6

y el campeón paró el reloj,
y Smyslov, que cantaba, no cantó.""",
43: """Si de verdad les interesa lo que pasó, lo primero que querrán saber es cómo un chico de trece años le ganó a Donald Byrne en Nueva York en 1956, y toda esa basura de la Partida del Siglo. Yo solo les voy a contar lo de la dama. En la jugada diecisiete Bobby Fischer deja la dama colgando. La deja ahí, por el amor de Dios, y juega un alfil a e6. El bueno de Byrne se la come. Tenía que hacerlo; es un adulto. Luego el caballo y el alfil empiezan a dar jaques al rey de un lado a otro como un limpiaparabrisas, y todo se cae del tablero. Me mató. Mate en la jugada cuarenta y uno, con una torre. Un crío. De verdad que sí.""",
44: """En aquellos días el Dragón yacía sobre la diagonal larga, y pocos de los que lo enfrentaban regresaban; pues su fuego era el alfil de g7, y su tesoro era el rey. Pero llegó a Portoroz, en el año 1958, un joven de quince años venido del Oeste, Fischer de nombre, que conocía la antigua sabiduría: abrir la columna h, y golpear, y golpear otra vez. Así que el peón de la columna h avanzó; y en la jugada veintidós se entregó una torre en h5, y el camino quedó abierto. Entonces Larsen el danés supo que había llegado su perdición. En la jugada treinta y uno la dama se alzaba en d6, y el Dragón ya no existía.""",
45: """En Sochi, junto al mar, el cincuenta y ocho, un día,
Polugaevsky se sentó con la espalda erguida;
su dama estaba a salvo, su centro era muralla.
El tártaro sirvió el vino: «Esperemos», decía.

Una torre tomó en f4. La dama quedó en el aire
para quien la quisiera; él la dejó, y al instante
tiró del rey blanco por la manga, hacia adelante,
desde e3, por una escalera sin luz y sin nadie.

El caballo que se mueve da jaque, y, dado el jaque,
sigue hasta c6: la treinta y tres, exacta.
Oh, Nezhmetdinov, llena otra vez la copa:
la partida es breve; el mate es lo que se guarda.""",
46: """Fue en una lúgubre tarde en Bled, en 1959, cuando Tal contempló el fruto de sus fatigas. Había reunido los instrumentos del ataque en torno al rey negro: un caballo arrojado a h6, un alfil, una torre en la columna abierta. Ninguna ciencia sensata lo avalaba. Smyslov, el más armonioso de los hombres, miró a la criatura y la juzgó incorrecta. Y entonces, en la jugada diecinueve, la dama tomó en f7, ofreciéndose, y la cosa abrió el ojo. De qué chispa vivía, no sabría decirlo. Lo persiguió siete jugadas más. En la veintiséis, un alfil en d4, abandonó, y el creador sonrió, y no tuvo miedo.""",
47: """BOTVINNIK. ¿Qué caballo es este que se planta en f4
donde cualquier peón lo toma? ¿Está loco?
TAL. Loco tan solo con el nornoroeste, mi señor. En la veintiuno
estoy apenas lo bastante loco para dar un caballo.
BOTVINNIK. Lo tomaré, entonces, y probaré que tu cuenta es falsa.
TAL. Ahí está el obstáculo: no tienes tiempo de probarlo.
El reloj es un ladrón; el alfil en g7
mira a través de tu reino como el sol de la mañana.
BOTVINNIK. (Aparte.) Un golpe, un golpe muy palpable.
(Alarmas. Cuarenta y seis jugadas. Caen las torres blancas.)
CORO. Así vio Moscú, en la primavera del sesenta,
un caballo, un caballo, un título por un caballo.""",
48: """Leningrado, 1960. El Gambito de Rey: una apertura romántica, de las que pide un hombre cuando no piensa ver la cuenta. Bronstein tomó el peón, y más tarde llevó otro hasta e2, donde se plantó en la puerta de Spassky con una torre que tomar y una corona que cobrar. Spassky lo miró con el leve interés de un hombre al que le están robando el coche mientras tiene en la mano un mejor juego de llaves. En la jugada quince su caballo fue a d6. Que el peón tome la torre, con jaque, y se convierta en dama. Lo hizo. El caballo entró en f7 como una bala atravesando un sombrero. Veintitrés jugadas. La dama llegó a e4. Tres años después alguien puso la posición en una película.""",
49: """En 1960 yo no estaba en Mar del Plata, nadie estaba, pero estaba allí un muchacho de diecisiete años llamado Fischer, y uno de veintitrés llamado Spassky, y entre ellos el Gambito de Rey, una apertura que juegan los poetas y que los mata. Spassky la jugó. El muchacho tomó el peón y se aferró a él como a un visado. Durante un rato las negras iban ganando; esto me lo contó un chileno que lo sabía por un camarero. Luego la torre del muchacho se extravió, y las piezas blancas bajaron por la columna e como un rumor. Veintinueve jugadas. Una torre en f4. Fischer lloró, dicen. Un año después publicó una refutación de la apertura entera. Eso también es literatura.""",
50: """Peoncito de Letelier, crecido demasiado,
cruzaste la mitad del tablero
con tus hermanos, e5, f4,
y nadie se quedó en casa con el rey.

Madre del centro, ¿quién te cantará?
El niño de Brooklyn espera en Leipzig,
mil novecientos sesenta, paciente como una montaña,
y te deshace hilo por hilo.

El rey sale a e3, descubierto.
Entonces la dama cae en f4 como la tarde.
Si la toma, un alfil dice su nombre;
si no la toma, es de noche.

Veintitrés jugadas, chileno mío,
y los Andes quedan muy lejos.""",
51: """En Bled en 1961 el lago estaba quieto y hacía buen tiempo. Fischer llevaba las blancas. Tenía dieciocho años. Tal estaba frente a él y Tal era el mejor que había en lo que Tal hacía. Era una siciliana. Tal cometió un error pronto. Fue uno pequeño. Fischer lo vio y no se apresuró. Tomó un peón y luego ganó la calidad y luego vino la parte larga, cuando lo tienes ganado y todavía tienes que ganarlo. Lo hizo limpiamente. Le llevó cuarenta y siete jugadas. Tal le tendió la mano. Era la primera vez que Fischer le ganaba. Tal sonrió al hacerlo. Era de los que podían. Fue algo hermoso de ver.""",
52: """Cosas silenciosas.
Una mañana de nieve. Una carta que no se envió. La apertura de Petrosian en Bled, en 1961, donde durante muchas jugadas nada toca nada.

Cosas que sobresaltan.
Un gorrión que levanta el vuelo. La dama tomando un alfil en f6, con jaque, en la jugada diecinueve, cuando uno creía que este jugador nunca regalaba nada.

Cosas más silenciosas que el silencio.
Cuando la dama ya no está y el rey negro ha sido arrastrado hasta g5, un alfil que se mueve una casilla, a g7. Sin jaque. Veintiuna jugadas.
Pachman abandonó. Es encantador que una persona de buen gusto comprenda enseguida.""",
53: """Escuchen: Mikhail Tal ha quedado desprendido del material.
En Varna, en 1962, en la jugada diecinueve, le atacaron la dama. También el caballo. Así fue. En lugar de salvarlos tomó un caballo en f6, y ahora colgaban los dos, y en la jugada veintiuno añadió un alfil en f5 por si acaso.
Hans-Joachim Hecht era un hombre amable de Alemania. Podía tomar la dama. Podía tomar el caballo. Podía tomar el alfil. Lo que no podía era tomarlos todos, por cómo funciona el ajedrez, que es una jugada cada vez.
Tomó la dama. Perdió en la jugada cuarenta y nueve de todos modos.
Un pájaro, afuera, dijo: «¿Pío-pi-pit?»""",
54: """Estaban en el hotel de Nueva York. Era el Campeonato de Estados Unidos, a finales de 1963. Robert Byrne llevaba las blancas. Tenía una buena posición. Todo el mundo lo decía.
En la otra sala dos grandes maestros se la explicaban al público. «Las blancas están ganando», dijo uno. El otro asintió.
Fischer entregó un caballo en f2. Luego movió unas cuantas veces más. Puso la dama en d7.
Byrne miró el tablero un rato. Alargó la mano.
—Ha abandonado —dijo alguien en la otra sala.
—¿Quién?
—Byrne.
Nadie dijo nada. Veintiuna jugadas. Nevaba un poco. Uno de ellos encendió un cigarrillo.""",
55: """y ahí estábamos en Nueva York en el sesenta y tres, Bobby Fischer y Pal Benko y todo el loco campeonato americano, Bobby ganando todas las partidas, todas, once a cero, y aquí está Benko con la Pirc agazapado detrás de sus peones pensando que el peón f va a f5 y estoy a salvo tío estoy a salvo, y Bobby con esas manos largas levanta la TORRE, no el peón, la torre, y la pone en f6, ahí mismo, plof, delante del peón, una torre que nadie puede tomar y nadie puede pasar, la santa torre intocable de Manhattan, jugada diecinueve, y dos jugadas después un caballo se desliza de vuelta a e2 suave como escobillas sobre un tambor y Benko lo pilla y abandona, sí, sí.""",
56: """Érase una vez, en Bled, un caballo que deseaba muchísimo ir a d5. «No puedes ir allí», le dijeron los peones, «porque te capturarán, y nadie ha calculado lo que pasa después». Pero el caballo pertenecía a un mago de Riga llamado Tal, que nunca calculaba nada hasta el final, y en la jugada dieciséis, en la última partida del match, en 1965, fue. Y lo capturaron. Larsen el danés tenía la pieza de más en la mano, y le pesaba cada vez más, como pasa con el oro en estos cuentos. En la jugada treinta y siete la dama blanca llegó a f7. Y el caballito, en la caja, era perfectamente feliz.""",
57: """Esta es una historia sobre un sacrificio de dama en Santa Mónica, y empieza con el tiempo que hacía. Era el verano de 1966. El Santa Ana todavía no había llegado. Petrosian era campeón del mundo, lo que significaba que no perdía y, concretamente, que nadie le sacrificaba damas, del mismo modo que nadie vendía mapas de su casa. Larsen, un danés, tomó un peón en g6 con la dama en la jugada veinticinco. Quiero ser precisa en esto. No fue una apuesta. Una torre ya se había elevado a la tercera fila; lo conté. Cinco jugadas después la otra fue a g3. Nos contamos historias para poder abandonar.""",
58: """En la décima partida del match de Moscú, en la primavera de 1966, el Campeón Petrosian, de trato tan reservado que la gente lo comparaba con la luna tras una nube fina, entregó la calidad y luego, como si una sola de esas delicadezas no bastara, la entregó otra vez. Spassky, el joven aspirante, de quien todos hablaban con tanto afecto, no pudo sino sentir la tristeza de las cosas. En la jugada treinta la dama del Campeón apareció en h8, ofreciéndose con un jaque; si el rey la aceptaba, un caballo visitaría f7 y lo recuperaría todo, con intereses. Spassky se inclinó. Qué breve fue, decían las damas de la corte, y qué perfectamente compuesto.""",
59: """En Sousse, junto al mar, alzo mi copa:
un huésped ha venido de la lejana Mongolia.
El peón avanza a e5 y el centro se cierra
como una puerta al anochecer.

Los caballos blancos vagan junto al río.
El peón h sube solo hasta h5.
Treinta jugadas; el alfil espera en la diagonal larga
como la luna espera en el agua.

Entonces la dama salta a h7: ¡una estrella fugaz!
Si el rey la toma, un peón y un alfil lo terminan.
Myagmarsuren mira el tablero y no la toma.
Brindo por Fischer; 1967; la lámpara se apaga.""",
60: """¡Camarada torre!
          ¡A c7!
                    Jugada dieciséis:
¡toma
     el alfil de c6,
                    la otra torre,
                                   y no expliques nada!
Montecarlo,
            mil novecientos sesenta y ocho,
                                 la ruleta al lado:
Botvinnik
         no apuesta.
                         Botvinnik
                                  PLANIFICA.
¡Torre toma f7!
              Portisch,
                       cuenta tus piezas:
muchas.
       Cuenta tus casillas:
                          ninguna.
Un caballo en e5,
               un alfil en h6:
                               ¡JAQUE!
Veintiséis jugadas.
                 El casino
                           perdió.""",
61: """En Moscú, en el sesenta y nueve,
partida diecinueve, Spassky, con las blancas,
desarmó la Najdorf sin tregua breve
y halló esa noche al rey tras sus barricadas.
Petrosian, el cauto, el profundo,
que no cedía un palmo en este mundo,
vio venir los peones, la e y la f,
como invitados que no se marchan, hasta que, sordas
a cada defensa que sabía,
sus torres miraban y no hablaban.
Entró el caballo. La casilla era débil.
En la veinticuatro voló a g5, ágil.
¿Has visto alguna vez, lector, el disparate
de ver al hombre prudente recibir mate?""",
62: """Problema

Larsen jugó b3 en la primera jugada. Jugaba en el primer tablero del Resto del Mundo. Esto fue en Belgrado, en 1970.

Spassky puso un peón en el centro y lo empujó. La apertura de Larsen no trataba del centro.

En la jugada catorce Spassky ofreció una torre en h1. Larsen no había pensado en esto. Lo pensó entonces.

El peón h tomó en g3, avanzó a g2, luego tomó en f1, convirtiéndose en dama, con jaque.

Era la jugada diecisiete. Larsen llevaba jugando más o menos lo que se tarda en hervir unas patatas.

Abandonó. Siguió jugando b3 en la primera jugada, en otras partidas, durante años.""",
63: """La séptima partida se jugó en Buenos Aires en 1971. O quizá fue la sexta; el calor vuelve inciertas estas cosas. Fischer tenía un caballo en c5, y todos estaban de acuerdo en que era la mejor pieza del tablero. El alfil de Petrosian en d7 era malo. En la jugada veintidós Fischer tomó el alfil malo con el caballo bueno. La gente en la sala hizo un ruido. Hay que imaginárselo indiferente. Un caballo bueno no es más que una idea; una columna abierta es un hecho, y las torres bajaron por ella como el sol del mediodía. En la jugada treinta y cuatro un alfil fue a c4. Petrosian abandonó. Nadie le preguntó qué sentía.""",
64: """Había un hombre llamado Robert, hijo de Regina, al que llamaban Fischer; vino a Islandia en el verano del año 1972. Siempre había abierto con el peón de rey. Los hombres decían que no conocía otra manera.
En la sexta partida empujó el peón a c4. Boris, al que llamaban Spassky, era entonces campeón; un hombre justo y muy querido. No dijo nada, pero jugó la vieja defensa de Tartakower, que los hombres tenían por muy segura.
Los peones avanzaron por el flanco de rey. En la jugada treinta y ocho una torre tomó en f6, y aquello no pudo ser vengado.
Tras la jugada cuarenta y uno Boris se levantó y aplaudió a su enemigo. Aquello se tuvo por bien hecho. No eran amigos antes de esto.""",
65: """sí porque él nunca había jugado eso antes la Alekhine el caballo afuera a f6 y de vuelta y dando la vuelta por b6 en Reikiavik la decimotercera partida y Spassky empujando los peones detrás sí y luego la larga tarde y el aplazamiento y la jugada secreta en su sobre como una carta que no abres y cinco peones pasados contra una torre oh y su propia torre encerrada en h8 como una monja todo el rato detrás del alfil y el rey blanco yendo y viniendo setentaicuatro jugadas las conté y el peoncito f en f2 al final a un paso de ser dama y Spassky mirándolo y mirándolo y sus ojos preguntaban y sí dijo sí abandono Sí.""",
66: """En la isla de las sesenta y cuatro casillas, la vieja historia dice que para dominar a un dragón hay que conocer su nombre verdadero. Korchnoi llevó el Dragón a Moscú en el otoño de 1974, y era uno grande, y confiaba en él. Pero Karpov, que era joven y hablaba poco, había ido antes solo a los lugares tranquilos y había aprendido el nombre, sílaba a sílaba, hasta la jugada diecinueve y más allá. No alzó la voz. Un caballo a e2. Una torre a d5. En la jugada veintisiete la dama se alzaba en h8, y el Dragón yacía inmóvil. No fue una batalla. Lo que está bien nombrado no necesita ser combatido.""",
67: """Fue en Niza, en el año 1974, en el curso de una Partida Española del más irreprochable linaje, cuando Anatoly Karpov, un joven pálido y escrupuloso cuya constitución nadie habría creído a la altura de la crueldad, colocó en la jugada veinticuatro su alfil en a7; una casilla, nótese bien, en la que esa pieza no atacaba nada ni defendía nada, sino que simplemente estaba, como un médico en el umbral de una puerta, impidiendo a las torres de herr Unzicker salir por la columna a mientras las blancas se reunían detrás a sus anchas. El paciente resistió veinte jugadas. No hubo crisis; solo hubo, como en la montaña, cada vez menos aire.""",
68: """Ciudad de Baguio, octubre de 1978. El marcador estaba cinco a cinco, lo que equivale a decir que nadie se fiaba de nadie. La delegación soviética tenía un parapsicólogo en la cuarta fila de butacas; la gente de Korchnoi quería que lo movieran. Había habido el asunto del yogur. Había habido las gafas de espejo. Ahora solo quedaba la partida treinta y dos, y Korchnoi, el desertor, había elegido una apertura que casi nunca jugaba, lo que el Centro de Moscú habría llamado una provocación. Karpov hizo aquello para lo que lo habían entrenado. Se quedó muy quieto y dejó hablar al otro. Para la jugada cuarenta y uno había una torre en b7 y no quedaba nada que decir. Korchnoi no acudió a la ceremonia de clausura. Envió una nota.""",
69: """No sé si alguna vez han visto a un campeón del mundo al que acaban de servirle una gamba por el lado equivocado, pero así estaba Karpov en Skara en 1980 cuando Tony Miles contestó a su peón de rey con a6. ¡Vamos, a6! ¡En la primera jugada! Es el tipo de cosa que juega un fulano tras la tercera copa de oporto. «Rarísimo, Jeeves», dije. «Muy irregular, señor. Creo que se llama la San Jorge.» Pues bien, el campeón se irguió como un obispo que encuentra una rana en la mitra, apretó de más, soltó un peón y en la jugada cuarenta y seis se le observó abandonando. Jeeves, al enterarse, alzó una ceja un dieciseisavo de pulgada, lo que en él equivale a un desfile con confeti.""",
70: """Niksic, el ochenta y tres, señor,
Portisch con el rey bien escondido.
Dice: Kasparov, ni lo intentes, por favor.
Y el chico sonríe, veinte años, decidido.

    Alfil toma en h7: ¡jaque!
    Uno menos.
    Alfil toma en g7: ¡qué ataque!
    Dos menos.

Tengo el blues cansado de los dos alfiles,
ni un peón me queda frente a la puerta.
Lasker lo tocó allá en el ochenta y nueve,
y desde entonces sigue la puerta abierta.

Treinta y cinco jugadas, la dama dice b3,
el rey sale a pasear sin saber a dónde.
Señor, ese chico que vino de Bakú
se va a llevar el mundo, y nadie le responde.""",
71: """Dejo constancia de estas notas con la esperanza de que ningún otro jugador abra la decimosexta partida del match de Moscú de 1985. Fue en la jugada dieciséis cuando la Cosa llegó a d3: un caballo negro, hinchado, tentacular, agazapado en las mismísimas entrañas de la posición blanca, tocando ocho casillas a la vez. Karpov, un hombre racional, creyó que podría desalojarlo. No pudo. Durante dieciocho jugadas sus piezas se arrastraron por la primera fila, incapaces de cruzar la tercera, mientras el innombrable caballo seguía allí sentado. Cuando por fin fue eliminado, en la jugada treinta y cuatro, ya era demasiado tarde; seis jugadas después una torre dio jaque en e1. He visto el diagrama. No duermo.""",
72: """Y aconteció en el día noveno del mes undécimo, en el año mil novecientos ochenta y cinco, que Garry hijo de Kim subió contra Anatoly en la ciudad de Moscú, en la partida vigésima cuarta. Y Anatoly tenía necesidad de victoria, y Garry tenía necesidad tan solo de no caer. Y Anatoly envió sus peones contra el rey, aun el peón de f y el peón de g. Mas Garry se mantuvo firme, y su caballo salió en la jugada trigésima segunda, e hirió. Y en la jugada cuadragésima segunda el caballo se paró sobre d4, con jaque. Y Anatoly entregó la corona. Y era Garry de veintidós años cuando comenzó a reinar.""",
73: """La Defensa India de Rey se parece un poco a la Voraz Bestia Bugblatter de Traal: alucinantemente peligrosa, y convencida de que si tú no ves a su rey, no le pueden dar mate. En Wijk aan Zee, en 1985, el doctor John Nunn, matemático, lo puso a prueba contra Beliavsky por el sencillo método de colocar un caballo donde un peón podía tomarlo y luego, antes de que nadie terminara de decir «pero si eso es una pieza», entregar una torre en f3 y luego entregarla otra vez en f2. En el oficio esto se conoce como No Entrar en Pánico. El rey blanco, que había planeado una tarde tranquila en el flanco de dama, fue encontrado en d1 en la jugada veintisiete por un alfil. La respuesta, por si se lo preguntaban, era veintisiete.""",
74: """Leningrado, 1986. Decimosexta partida. Noche.
A un lado del tablero, un caballo en d3, negro, enterrado en el campo blanco como un cañón arrastrado dentro de una catedral: el de Karpov. Al otro lado, un rey y una tormenta: los de Kasparov. ¿Quién llega primero? Eso es todo el ajedrez. Eso es toda la historia.
Un hombre toma un flanco de dama. El otro toma un riesgo. La aritmética está a la izquierda; el destino, a la derecha.
Jugada treinta y cinco: una torre se entrega en g6. Jugada treinta y ocho: el rey negro está en la calle, en d5, con la cabeza descubierta.
Jugada cuarenta y uno: un caballo toma en f7.
Karpov para el reloj. Waterloo tuvo menos testigos.""",
75: """Sevilla. A las cinco de la tarde.
Era la jugada cuarenta en todos los relojes.
Kasparov un punto por detrás, y la última partida,
a las cinco de la tarde.

Verde que te quiero verde, casilla verde de f2.
La dama en la diagonal larga.
Karpov apurado de tiempo, un peón ya perdido,
y el sobre cerrado como una herida.

Toda la noche los segundos con sus lámparas.
Nadie durmió en el Lope de Vega.

Por la mañana el alfil siguió trabajando, despacio,
una guitarra de una sola cuerda.
Sesenta y cuatro jugadas. El rey va a g2.
Doce a doce. La corona se queda donde estaba.
¡Ay, Sevilla, mil novecientos ochenta y siete!""",
76: """—Por favor —dijo el caballito de g5—, tómame.
Era la vigésima partida, en Lyon, en 1990, y las personas mayores del público contaban piezas, porque a las personas mayores les gustan las cifras. Ya se había entregado un caballo en h6. Ahora aquí estaba otro.
—Si me tomas —dijo el caballo—, vendrá la dama.
Y en la jugada treinta y cuatro la dama vino, a h6, con jaque, y se entregó también. El rey de Karpov la miró durante mucho tiempo.
—Lo esencial —dijo el caballo— es invisible al recuento de material.
Cuarenta y una jugadas. Un alfil tomó en d5 con jaque. Solo se ve bien con el ataque.""",
77: """Estábamos más o menos por la jugada diecinueve, al borde del desempate, cuando los sacrificios empezaron a hacer efecto. Bruselas, 1991. Partidas rápidas. Ivanchuk tenía un flanco de dama como una autopista federal y Yusupov, un hombre callado, barbudo y decente, había decidido, por razones que ninguna persona cuerda podría reconstruir, tirarle todo su vestuario al rey blanco. Un caballo se metió en h4. La torre se elevó. Dios santo. Ivanchuk se comió una torre entera en la esquina, con jaque, y daba igual; tuvo que devolver la dama enseguida en g8, y el rey negro simplemente se la tragó como un portero de discoteca. Dama a g3 en la jugada treinta y nueve. Se venía el mate. Después nadie pudo probar nada de esto. Nunca se puede. De eso se trata.""",
78: """Quando octubre en la villa de Tilburg fue venido,
del anno de mill e nueuecientos e nouenta e uno cumplido,
un rey auie y era, e omne de grand valor,
que desde que primero, con mesura e con temor,
alçó su castiello, amaua mucho la paz.
Mas Short, su señor, non lo dexó en solaz:
«Id», dixo él, «en romería fasta h6.»
E fuese él por h2, por g3, sin engaños nin ardides,
por f4 e por g5, a pie e por su mano,
entre reynas e roques, por el camino llano.
E Timman, maguer toda su mesnada tenía,
nin podía mouerse, nin al romero detenía.
A treynta e quatro jugadas aqueste cuento es acabado.
Non ouo omne que viese rey assí andado.""",
79: """En la ciudad de Linares, en el año 1993, el sabio Karpov, habiendo leído en todos los mejores autores que las piezas deben desarrollarse, descubrió en la jugada veintidós que todas las suyas estaban en la primera fila, donde habían empezado. «Todo es para bien», dijo su segundo, «en la mejor de las posiciones posibles». Entretanto el joven Kasparov, que no había leído nada salvo el tablero, empujó un peón hasta la primera fila y tomó allí una torre, convirtiéndolo en dama, sin consultar a un solo filósofo. Veintisiete jugadas. Un caballo llegó a f2. Hay que cultivar nuestra primera fila.""",
80: """No se nace gran maestro: se llega a serlo. Judit Polgár había llegado a serlo a los quince años, y en Buenos Aires en 1994, en un torneo en el que todas las partidas estaban obligadas a ser sicilianas, los hombres todavía hablaban de ella como de una excepción, que es el nombre educado de una molestia. Shirov avanzó por el flanco de rey. Era su libertad hacerlo. En la jugada diez ella respondió con su propio peón g, dos casillas, en su cara; luego un caballo a e5, luego el otro caballo, y una captura con la dama en g5 que nadie había considerado porque nadie la había considerado a ella. Veintinueve jugadas. No trascendió la situación. La ganó.""",
81: """Los ancianos dicen que el hombre que mete en su choza leña infestada de hormigas no debe quejarse cuando lo visitan los lagartos. Topalov era un hombre joven en Linares en 1994, y había tomado un caballo. Karpov no era joven, y aquel año en aquel pueblo nadie podía derribarlo.
En la jugada veinte Karpov puso una torre en e6. Topalov no la tomó, pues entre los suyos un regalo de un anciano se examina primero. En la veintiuno la misma torre tomó en g6, con jaque, y ese regalo hubo que aceptarlo. Entonces todo se desmoronó: el recinto del rey estaba abierto por tres lados, y la dama entró como entra un acreedor.
Treinta y nueve jugadas. Cuando callaron los tambores, el anciano no había alzado la voz.""",
82: """Jugaban en el piso ciento siete. Se veía el tiempo que les pasaba a otras personas. Kasparov y Anand, Nueva York, 1995, una cabina de cristal, la décima partida. La jugada se había hecho días antes, en una habitación, por hombres con portátiles; eso era lo que tenía. Él solo la estaba entregando ahora. Caballo a g5 en la jugada once, una casilla conocida con información nueva dentro. Luego una torre dejada a merced del rival en a1, el alfil a h6. Jugaba rápido. Anand estaba sentado dentro de la preparación como un hombre que lee su propio expediente. Treinta y ocho jugadas. Todo estaba conectado. Las torres zumbaban.""",
83: """¿Qué es una dama cuando va a g7? Lo pregunto porque Ivanchuk la puso allí, en Wijk aan Zee en 1996, en la jugada veintiuno, donde un alfil podía simplemente tomarla, y no creo que él tampoco lo supiera, del modo en que se sabe un hecho. Lo sabía del modo en que se sabe un huevo. El peón ya estaba en el hombro de g7; si tomaban la dama, el peón se convertiría en... pero ¿en qué se convierte un peón? En sí mismo, por fin. Shirov la tomó. Tenía que hacerlo; rehusar una dama es rehusar existir. Catorce jugadas después una torre se deslizó a a1, tranquila como un domingo. Y yo, que no estaba allí, sigo dentro de ese instante anterior a la captura.""",
84: """La Primera Ley dice que una máquina no puede hacer daño a un ser humano. Nadie se lo había dicho a Deep Blue, que en febrero de 1996, en Filadelfia, era un armario del tamaño de dos neveras que examinaba cien millones de posiciones por segundo y no tenía opinión sobre ninguna de ellas. Kasparov atacó a su rey. Un humano se habría estremecido; el armario tomó un peón en b7, porque había calculado que el ataque llegaba un tiempo tarde. Así era. En la jugada treinta y siete una torre tomó en h7 con jaque, y por primera vez un campeón del mundo abandonó ante una máquina una partida a ritmo clásico. Kasparov ganó el match, cuatro a dos. Los ingenieros tomaron nota. Habría un modelo siguiente.""",
85: """Era la sexta partida, Nueva York, 1997, y Kasparov ya no sabía distinguir si la cosa que tenía enfrente era una máquina que fingía ser un hombre o una habitación llena de hombres que fingían ser una máquina. En la segunda partida había hecho una jugada tranquila, una jugada humana. Él había pedido los registros impresos. No le habían dado los registros impresos.
En la jugada siete jugó h6. Conocía el sacrificio de caballo en e6; todo el mundo lo conocía. Una máquina nunca... el caballo tomó en e6.
Su rey estaba atascado en el centro. ¿Era esto real? Miró al operador. El operador parecía un hombre.
Diecinueve jugadas. Abandonó y se fue. Después lo desmontaron. Eso no probaba nada.""",
86: """Era un final de alfiles de distinto color, de esos que siempre son tablas, como los martes. Linares, 1998. Shirov tenía dos peones de más que no importaban. Hice espaguetis y pensé en ello. En la jugada cuarenta y siete tomó su alfil y lo puso en h3, donde un peón podía tomarlo. No había ninguna razón para hacerlo. Era como un pozo al fondo de un jardín perfectamente normal.
Topalov tomó el alfil. Entonces el rey negro se abrió paso hasta el centro, exactamente un paso más rápido que antes. Para eso servía el pozo.
Cincuenta y tres jugadas. En algún lugar se estiró un gato que tuve una vez. Volví a poner el disco, pero sonaba distinto.""",
87: """De aquella primera entrega de la Torre en d4,
en Wijk aan Zee, el noventa y nueve, por la que
el Rey negro, desde su alta almena
arrojado de cabeza, en llamas, cayó por la columna a,
b6, a5, a4, nueve casillas de ruina, canta,
Musa celestial. A él el Todopoderoso Kasparov
persiguió jaque tras jaque; ni Topalov,
aunque dueño de una Torre y un Caballo, pudo detener
el descenso: pues en la jugada treinta y seis
un Alfil, callado, se volvió en f1,
y toda su hueste fue vana. En la cuarenta y cuatro
la Dama ascendió a a7. Así cayó,
no sin gloria, el que tomó, y tomando
hizo posible lo que nadie había visto.""",
88: """Era un día luminoso y frío de octubre, en Londres, en el año 2000, y los relojes estaban en marcha. Kasparov llevaba quince años de campeón. Eso era lo primero que había que entender. No es que ganara habitualmente; es que su victoria era un hecho de la naturaleza, como el precio del pan. En la segunda partida Kramnik, un joven alto y apacible, tomó un peón en b7 en la jugada once y se lo quedó. No hay nada heroico en quedarse un peón. Es simplemente lo que funciona. Más tarde se cambiaron las damas, y el peón seguía allí, y también la simple aritmética del asunto. Cuarenta jugadas. Un alfil fue a d5. Los periódicos informaron del asunto como de un cambio de régimen.""",
89: """Puedes anotarme en tus bases de datos
como la chica que iba a romperse en la rueda.
Decías que el juego de una mujer era de encajes.
Moscú, 2002. Vine a repartir las cartas.

¿Te molesta mi Ruy López?
Elegiste la Berlinesa, ese viejo muro gris.
Puse mis torres en séptima, las dos
juntas, y lo vi caer.

    Desde el dolor paciente del final,
    tomo.
    Desde un pasado de que me enseñaran,
    tomo g7, y es mío.

Cuarenta y dos jugadas. El rey corre a c8.
Paraste el reloj.
Soy el sueño y la esperanza del peón.
Corono.""",
90: """Un salón de hotel, Wijk aan Zee. Enero de 2004. Nieve en las ventanas.
ERNST. Tienes trece años.
CARLSEN. (Sin levantar la vista.) Sí.
ERNST. He jugado esta Caro-Kann toda mi vida. Es una casa sólida.
CARLSEN. Hay algo detrás del muro. En g6. (Coloca allí un caballo.)
ERNST. Si tomo eso, la columna e...
CARLSEN. Tómalo.
(Lo toma.)
CARLSEN. Entonces el alfil toma en h6.
ERNST. ¿Y si tomo ese?
CARLSEN. La torre toma en h6. Con jaque.
ERNST. (En voz baja.) Todos estos años creí que los peones la sostenían.
(La dama va a d7. Jugada veintinueve. Mate.)
ERNST. Tengo que salir. A la nieve.""",
91: """En Brissago, sobre el lago, donde los bosques de castaños bajan hasta el agua, Kramnik se encontró en el otoño de 2004 un punto por detrás con una sola partida por jugar. Había sido campeón; había estado, lo veía ahora, dormido. Leko jugaba la Caro-Kann como quien cierra una verja. Y Kramnik, que siempre había buscado la seguridad, comprendió en esa última mañana que el camino no rodeaba el peligro sino que lo atravesaba. Dejó ir las damas. Envió a su rey a pie, tablero arriba, a g5 y f6, solo, como un peregrino. En la jugada cuarenta y uno un caballo dio jaque en f7. El match quedó empatado y el título, conservado. Se había perdido a sí mismo y estaba, por fin, despierto.""",
92: """Cabalgaron hacia la Semieslava en Wijk aan Zee en el invierno de 2008 y en la jugada doce el caballo tomó el peón de f7 y nadie habló. No estaba en los libros. Cheparinov lo había encontrado mucho antes en una habitación de hotel y lo habían llevado consigo desde entonces como una cosa envuelta en hule. Kramnik tomó el caballo. Tenía la pieza y los alfiles y la larga teoría de su gente y nada de ello le sirvió. Los peones blancos bajaron por el centro de aquel país como el mal tiempo. Miró el reloj y el reloj le devolvió la mirada. Cuarenta y cinco jugadas. Un caballo en e6. Lo que en la apertura existe sin mi conocimiento existe sin mi consentimiento.""",
93: """Donde el caballo está sin temor y el alfil se mantiene en alto en b7;
donde la Merano no ha sido rota en fragmentos por estrechos análisis caseros;
donde la columna g está abierta, Señor mío, y la torre se alza en ella a la luz de la mañana en Bonn;
donde Kramnik, con las piezas blancas y el material de más, vaga por la arena lúgubre del desierto de su propio material de más;
donde en la jugada treinta y tres se equivoca, y la dama y el alfil negros descienden como la primera lluvia;
donde el último jaque se da desde b1, en la jugada cuarenta y uno, en el año 2008:
en ese cielo de las piezas negras, Padre mío, haz que despierte Anand.""",
94: """Era la duodécima partida, la última partida, la partida-de-las-partidas, en Sofía, en 2010, y Topalov-el-héroe-local solo necesitaba quedarse quieto, que era la única cosa en todos los Balcanes que nunca había aprendido a hacer. Anand, que había llegado tras cuarenta horas por carretera porque un volcán de nombre impronunciable había cerrado el cielo (esto es verdad; en mis historias las partes increíbles son siempre las verdaderas), jugó la Defensa Lasker, vieja como las abuelas. En la jugada treinta y uno Topalov tomó un peón que debería haber dejado. Zas: la diagonal larga se abrió como un bazar. ¡Torre toma g4! Dama, dama, dama. Cincuenta y seis jugadas; la dama se sentó en g7; el título se quedó, chutneificado pero entero.""",
95: """Era enero en Wijk aan Zee y el viento venía del mar como un rumor. La partida empezó como empiezan estas partidas: con una eslava, con Pequeñas Cosas. Un peón. Un alfil guardado en su cuarto.
Entonces, en la jugada quince, Anand colocó un alfil en c5 donde podían tomarlo. Y en la dieciséis un caballo en e5 donde también podían tomarlo. Dos Cosas Queridas, olvidadas en la galería bajo la lluvia.
Aronian podía quedarse con cualquiera de las dos. No con ambas. No con ninguna.
Para entonces la casa del rey ya no tenía paredes. Solo ventanas.
En la jugada veintitrés un alfil llegó a e3, y se acabó como se acaba un monzón. De repente. Todo a la vez. En 2013.""",
96: """Me desperté a las siete e hice café. Era noviembre de 2013; en Chennai había empezado la novena partida. Me quedé junto a la ventana con la taza. Carlsen tenía veintidós años y llevaba las negras e iba por delante en el match, y Anand tenía que ganar, había empujado sus peones hasta el rey, f4, f5, f6, como alguien que por fin dice lo que piensa. Pensé en mi padre. Carlsen simplemente llevó su propio peón por la columna b y se hizo una segunda dama, en b1, con jaque, como si no pasara nada más. Entonces Anand movió el caballo a f1. Era la pieza equivocada. Tendría que haber sido el alfil. Veintiocho jugadas. La dama llegó a e1. Enjuagué la taza. Eso fue todo.""",
97: """Era el vigésimo sexto cumpleaños de Carlsen, y toda Nueva York había sido invitada, o al menos la parte de Nueva York que podía quedarse detrás del cristal en el Seaport y susurrar. El match se había ido a los desempates, partidas rápidas y brillantes como cócteles. En la cuarta no necesitaba nada; le bastaban unas tablas. Ya era campeón en todos los sentidos salvo el del minutero. Y entonces, en la jugada cincuenta, porque era joven y las luces lo enfocaban y estaba ahí, puso la dama en h6 con jaque, para que la tomara el rey o el peón, y mate en ambos casos. Y así seguimos adelante, torres contra la última fila, arrastrados sin cesar hacia el premio de belleza.""",
98: """Consulté los viejos manuales de ajedrez. En cada página estaba escrito: «protege al rey, valora las piezas». No podía dormir, y leí con atención media noche, hasta que vi, entre líneas, otras dos palabras: «entrégalas».
En la Liga China, en 2017, Bai Jinshi jugaba con blancas contra Ding Liren. En la jugada quince Ding dejó su dama para que la tomaran y en su lugar tomó un caballo. En la jugada veinte una torre fue a d4, a la vista de todos. El rey blanco fue llevado de la mano, e2, f3, g3, h4, h5, g4, como se lleva a un hombre a la plaza mientras los vecinos miran.
Treinta y dos jugadas. Un caballo dio jaque en e5.
Quizá todavía haya niños que no han aprendido a contar el material. Salvad a los niños.""",
99: """Inventario de la sexta partida, Dubái, 3 de diciembre de 2021:
1 tablero; 32 piezas al principio, 7 al final;
136 jugadas (un récord para el campeonato), de las que 136 de las blancas y 135 de las negras;
casi 8 horas; 1 medianoche, rebasada;
1 dama (la blanca) cambiada en la jugada 26 por 2 torres;
1 dama (la negra) que se quedó, y dio 15 jaques, ninguno suficiente;
2 peones blancos, e y f, avanzando de 1 casilla en 1 casilla;
1 caballo, que llega a g7 en la jugada 136;
0 mates; 1 abandono; 1 apretón de manos;
1 aspirante que no volvió a ganar una partida;
varios vasos de agua, sin comentarios.""",
100: """Notaciones. En el desempate, en Astaná, hacia finales de abril de 2023. Un jugador de unos treinta años, Ding, gafas, con las piezas negras, muy poco tiempo en el reloj. Enfrente, un hombre con moño, Nepomniachtchi, que ha ido por delante tres veces. La posición es de tablas; la gente sube y baja. A Ding le ofrecen una repetición de jugadas. La rechaza en un tono que pretende ser agresivo: pone su torre en g6, clavándola él mismo contra su propio rey. Luego se lanza sobre un peón pasado.
Veintidós jugadas más tarde, en la sesenta y ocho, un alfil toma en f4. Un amigo le está diciendo: «Deberías hacerte poner una corona ahí». Le muestra dónde (en la cabeza) y por qué.""",
}
assert len(EX) == 100
