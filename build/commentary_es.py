"""Los mismos dos locutores, en español: un narrador de fútbol que canta los goles
y un cronista de béisbol de radio caribeña. Mismas reglas que commentary.py; las frases
se escriben de nuevo, no se traducen línea por línea.

Marcadores con género: {el_pc} 'el caballo' / 'la torre', {El_pc} con mayúscula, {un_pc},
{o_pc} 'o' / 'a' para concordar. Igual para {cap}, {hp}, {offered}, {promo}.
'a el' y 'de el' se contraen solos en 'al' y 'del'."""
import random, re
from commentary import Voice, choose_key, short
import i18n_es

GEN = {'pawn': ('peón', 'm'), 'knight': ('caballo', 'm'), 'bishop': ('alfil', 'm'),
       'rook': ('torre', 'f'), 'queen': ('dama', 'f'), 'king': ('rey', 'm')}

S = {  # ------------------------------------------------------------------ FÚTBOL
 'intro': [
  "¡Buenas noches y bienvenidos a {site}, {year}! De blanco, {W}; de negro, {B}. A este partido lo llaman «{nick}»: no se muevan de ahí y descubran por qué.",
  "¡Hola, hola, hola desde {site}! Estamos en {year}, el partido es {W} contra {B}, y la historia ya le puso nombre: «{nick}». Salen los jugadores. ¡Vamos allá!",
  "{site}, {year}. Sesenta y cuatro casillas de césped perfecto, treinta y dos jugadores, dos entrenadores: {W} y {B}. Falta un suspiro para el partido que llamarán «{nick}».",
  "¡Bienvenidos! {W} contra {B}, en directo desde {site}, {year}. En la pizarra, {opening}. Lo llaman «{nick}». El árbitro mira el reloj...",
 ],
 'first': ["¡Y arranca el partido! {P} la pone en juego: {san}.", "¡Suena el silbato! {san} de {P} y esto ya está vivo.",
           "¡Saque de centro! {P} la toca hacia adelante: {san}."],
 'reply': ["{P} responde desde el reinicio: {san}.", "{san} de vuelta por parte de {P}. Sin nervios.",
           "Y {P} contesta con {san}. Tenemos partido."],
 'pawn': [
  "{P} adelanta un peón a {sq}. Pase corto, mantiene el dibujo.", "Peón a {sq}. {P} adelanta la línea unos metros.",
  "Un toquecito hacia adelante, {san}. Elaboración paciente de {P}.", "{P} juega {flank}: peón a {sq}.",
  "{san}. {P} va estrechando el campo, peón a peón.", "El peón avanza a {sq}. ¿Quién marca a ese?",
  "Ordenado el juego de {P}. Peón a {sq}: nada lujoso, nada equivocado.", "{san}. La defensa sube detrás de él.",
  "{P} recicla la posesión: peón a {sq}.", "Peón a {sq}, {flank}. Ahí queda la marca.",
  "Un metro más de césped conquistado: {san}.", "{P} lo hace sencillo. {san}. La grada quiere más; el entrenador, no.",
 ],
 'knight': [
  "El caballo salta a {sq}: esa carrerita en L que nadie sigue nunca.", "{P} manda el caballo {flank}; aterriza en {sq}.",
  "Caballo a {sq}. Pies rápidos, ángulos raros. Los defensas odian marcarlo.", "¡{san}! El caballo aparece en {sq}, solo, sin marca.",
  "Una arrancada del caballo, {sq}. {P} está tanteando.", "Dobla la esquina el caballo: {sq}. Qué buen desmarque.",
  "{san}. El caballo frena, amaga y se va. Muy listo.", "Caballo a {sq}. Nunca corre en línea recta y nunca lo hará.",
  "{P} encuentra al caballo entre líneas, en {sq}.", "Asoma el caballo en {sq}. ¿De dónde salió eso?",
 ],
 'bishop': [
  "¡Balón largo en diagonal de {P}! El alfil barre hasta {sq}.", "Alfil a {sq}: un cambio de orientación de lado a lado.",
  "{P} desliza el alfil a {sq}. Desde ahí se ve todo el campo.", "El alfil se mete desde la banda: {sq}.",
  "{san}. Cambio de juego en diagonal. Al alfil le encanta el espacio.", "Alfil a {sq}. Un francotirador que encuentra la ventana.",
  "{P} abre el ángulo: {san}. Alguien en el otro lado debería estar nervioso.", "El alfil baja a {sq} y mueve los hilos desde atrás.",
  "{san}. Milimétrico por la diagonal, el de {P}.",
 ],
 'rook': [
  "La torre cruza pesada hasta {sq}. El central grandote sube para el balón parado.", "Torre a {sq}. Artillería pesada subiendo por la banda.",
  "{san}. La mole se acomoda en su sitio.", "La torre toma el pasillo libre: {sq}. Cuánto césped por delante.",
  "{P} carga la columna: torre a {sq}.", "Torre a {sq}. No es bonito ni pretende serlo.",
  "{san}. {P} adelanta una torre y la defensa respira hondo.", "La torre se cambia a {sq}. Músculo que llega tarde al área.",
  "{P} pasa la torre a {sq}. Ahora todo tranquilo. No por mucho tiempo.",
 ],
 'queen': [
  "¡Aquí viene la número diez! La dama se desliza a {sq}.", "{P} lleva la dama a {sq}: la estrella pide el balón.",
  "Dama a {sq}. Todos los defensas acaban de dar un paso atrás.", "{san}. La estrella gira, levanta la cabeza y elige casilla.",
  "La dama se va {flank}, {sq}. Peligro por donde pasa.", "¡{san}! Otra categoría. La dama encuentra un hueco.",
  "Dama a {sq}. Estaba callada. Ya no lo está.", "{P} mueve la dama a {sq}, y cambia la temperatura del estadio.",
  "La dama baja a {sq} y pide el balón al pie.",
 ],
 'king': [
  "El rey se mueve a {sq}. ¡El portero sale del arco!", "El rey de {P} se acomoda en {sq}: un portero al que le gusta salir.",
  "Rey a {sq}. Qué valor, salir así del área.", "{san}. Pequeño ajuste bajo palos de {P}.",
  "El rey se aparta a {sq}. Manos seguras, esperemos.",
 ],
 'king_end': [
  "El rey sube hasta {sq}. ¡A estas alturas hasta el portero va al ataque!", "Rey a {sq}: ¡el portero sube a rematar el córner!",
  "{san}. Con el campo tan vacío, el rey juega de mediocampista.", "El rey de {P} avanza a {sq}. Ya no hay miedo ni dónde esconderse.",
  "Adelante el rey, {sq}. Esto ya es fútbol de prórroga.",
 ],
 'castle': [
  "¡{P} enroca {side}! Portero detrás de la línea de cuatro, torre al medio.", "Enroque {side}. La barrera está lista: a ver quién la atraviesa.",
  "Y {P} enroca {side}. ¿Aparca el autobús? Quizá solo la furgoneta.", "Primero la seguridad: {P} enroca {side}. El rey tras el muro y la torre se suma a la fiesta.",
 ],
 'cap': [
  "¡{P} recupera el balón! {El_pc} toma {el_cap} en {sq}.", "Entrada durísima en {sq}: {el_cap} se va del campo.",
  "¡{san}! {El_pc} entra fuerte y {el_cap} pierde el balón.", "Limpísimo. {El_pc} toma {el_cap}, {sq}. Siga, siga, dice el árbitro.",
  "¡Fuera {el_cap}! Roja directa, sin discusión. {El_pc} de {P} hizo el daño en {sq}.", "¡Interceptado! {El_pc} de {P} lee la jugada y se lleva {el_cap} en {sq}.",
  "{san}. {El_cap} ni vio venir la entrada.", "¡{P} entra por detrás sobre {el_cap} en {sq}... y no le pitan nada!",
  "{El_pc} se la roba en {sq}. {Un_cap} menos para {O}.", "¡Robo! {san}. {O} pierde {un_cap} en zona peligrosa.",
 ],
 'recap': [
  "Y {P} la recupera enseguida: {el_pc} toma en {sq}. Balón dividido, nadie gana el duelo.", "¡Toma y daca! {san}; {el_cap} también va al acta.",
  "Respuesta inmediata: {el_pc} recaptura en {sq}. Ida y vuelta.", "{P} limpia en {sq}. Intercambio justo de camisetas.",
  "{san}. Entrada respondida con entrada.", "¡Y vuelve! {El_pc} de {P} salda la cuenta en {sq}.",
 ],
 'capq': ["¡CAE LA DAMA! {El_pc} de {P} la toma en {sq}: ¡la estrella sale en camilla!",
          "¡¡{san}!! ¡La número diez SE FUE! ¡{O} ha perdido la dama!"],
 'qtrade': ["Y se van las damas juntas. Sustituidas las dos números diez: esto es otro partido.",
            "{san}. Damas cambiadas. Se van los artistas; entran los obreros."],
 'check': [
  "¡DISPARO! {san}: ¡{P} prueba al portero desde {sq}!", "¡Jaque en {sq}! El rey de {O} tiene que estirarse.",
  "¡{P} saca el zapatazo: {san}! ¡Entre los tres palos!", "¡Uf, cómo le quema las manos! {El_pc} a {sq}, jaque.",
  "¡Jaque! {El_pc} llega al área y el arco de {O} está sitiado.", "¡{san}! Directo al rey. {O} tiene que resolverlo.",
  "Un disparo desde lejos: {san}. ¡Jaque!", "¡{El_pc} remata desde {sq}! El rey tiembla.",
 ],
 'capcheck': ["¡Roba y dispara en un solo movimiento! ¡{san}! {El_pc} de {P} arrolla a {el_cap}, ¡y es jaque!",
              "¡{san}! Gana el balón Y saca el tiro. {O} se tambalea.",
              "¡{El_cap} barrid{o_cap} en {sq}... y encima es jaque! Implacable, {P}."],
 'runcheck': ["¡Otro más! ¡{san}! {P} acribilla la portería: ¡{run} disparos seguidos!",
              "¡{san}! ¡Jaque otra vez! {run} seguidos. Al rey de {O} lo persiguen por el área chica.",
              "¡Y otra vez! ¡{san}! Esto es un asedio: {run} jaques consecutivos."],
 'ev_king': ["¡Despeja! El rey de {P} se lanza a {sq}.", "El portero se las arregla: rey a {sq}. Sigue vivo.",
             "Sale de la línea y se va a {sq}. Defensa con el corazón en la boca, la de {P}.", "{san}. El rey se escurre. Por poco.",
             "Rey a {sq}. ¡La manda al córner!"],
 'ev_king_cap': ["El rey lo resuelve en persona: ¡toma {el_cap} en {sq}!", "¡{san}! El portero sale y atrapa {el_cap}. ¡Qué valor!"],
 'ev_block': ["¡Bloqueado! {El_pc} se tira al suelo en {sq}.", "¡Cuerpo en la línea! {san}: {P} sobrevive.",
              "{El_pc} a {sq}, un bloqueo desesperado.", "¡Despejada! {san}. {El_pc} mete la pierna."],
 'ev_take': ["¡Atajada y retenida! {El_pc} toma {el_cap} en {sq}. Peligro superado... por ahora.", "¡{san}! Eliminan al tirador. {P} vuelve a respirar."],
 'sac': [
  "¿PERO QUÉ ES ESTO? {P} deja {el_pc} ahí mismo, en {sq}: ¿regalo o trampa?", "¡Regalado! No, esperen: {P} lo hizo A PROPÓSITO. ¡{El_pc} se ofrece en {sq}!",
  "¡Un amague! {P} suelta {el_pc} en {sq} y todo el estadio se queda sin aire.", "¡Qué atrevimiento! {san}: {P} lanza {el_pc} hacia adelante y reta a {O} a tomarl{o_pc}.",
  "Es un caño a plena luz del día. ¡{P} sacrifica {el_pc} en {sq}!", "¡¡{san}!! {El_pc} se mete donde duele. ¡{P} se juega la casa!",
  "Dios mío. {P} acaba de dejar {el_pc} colgad{o_pc} en {sq}... ¡a propósito!",
 ],
 'qsac': ["¡LA DAMA! ¡LA DAMA! ¡{P} deja la dama colgada en {qsq}! Que alguien revise el reglamento: ¿esto se puede?",
          "¡Escenas increíbles! {san}... ¡y la dama de {P} se puede capturar sin más! ¡O es locura o es genialidad!",
          "¡¡¡{san}!!! {P} ofrece la DAMA. Llevo toda la vida viendo este deporte y me tiemblan las manos."],
 'hang': ["¡{P} ignora la amenaza! {El_hp} de {hsq} queda a su suerte... ¡y {P} juega {san}!",
          "Un momento: ¡{el_hp} de {hsq} está ahí para quien l{o_hp} quiera! A {P} no le importa: {san}.",
          "¡{san}! Da igual {el_hp} colgad{o_hp} en {hsq}; {P} tiene ideas más grandes. ¡Esto es fútbol sin miedo!",
          "{P} deja {el_hp} sin marca en {hsq} y se vuelca al ataque igual. ¡{san}!"],
 'accept': ["{P} muerde el anzuelo: {el_pc} toma {el_cap} en {sq}. Valentía. O hambre.", "{san}. {P} dice muchas gracias y se guarda {el_cap}. Pero ¿a qué precio?",
            "¡Aceptado! Se va {el_cap}. Ahora {P} tiene que sobrevivir a lo que viene."],
 'decline': ["¡{P} no quiere saber nada! Ni toca {el_offered} y juega {san}.",
             "No, gracias, dice {P}. {san}: {el_offered} sigue en el campo.", "{san}. {P} huele la trampa y la esquiva."],
 'promo': ["¡CAMBIO! Sale el peón, entra una dama: ¡{P} corona en {sq}! Piernas frescas, ¡y qué piernas!",
           "¡{san}! El peoncito recorrió todo el campo y vuelve convertido en DAMA."],
 'under': ["Cambio en {sq}... ¡y entra {un_promo}, no una dama! {P} sabe algo que nosotros no."],
 'adv7': ["¡El peón se escapa a {sq}! ¡Mano a mano con la última línea!", "¡{san}! Ese peón va al hombro del último defensa.",
          "¡El peón de {P} se lanza a {sq}, a un paso de la línea de fondo!"],
 'adv6': ["El peón de {P} entra en el último tercio: {sq}.", "{san}. Ese peón ya está a la espalda de la defensa.", "¡El peón sigue! {sq}. Que alguien siga esa carrera."],
 'fork': ["¡Una horquilla! El caballo en {sq} marca a dos jugadores a la vez y lo disfruta.", "¡{san}! El caballo tiene a dos en el bolsillo."],
 'mate': [
  "¡GOOOOOOOOOL! ¡GOL! ¡GOL! ¡GOL DE {PU}! {san}: ¡JAQUE MATE! El rey no tiene adónde ir, la red se infla, ¡y en {site} hablarán de esto durante cien años!",
  "¡GOOOOOOOOOOOL! ¡{san}! ¡JAQUE MATE! ¡{PU}! ¡{PU}! Una reverencia, por favor: ¡esto va directo al museo!",
  "¡AHÍ ESTÁ! ¡GOOOOOOL! {san}, ¡y es MATE! ¡{P} lo consiguió en {site}! ¡Escuchen a esa afición!",
  "¡GOOOOOOOL DE {PU}! ¡{san}! No hay portero en el mundo que pare eso. Jaque mate, final, historia.",
 ],
 'half': ["DESCANSO en {site}. Posesión: {W} {poss}%, {B} {possb}%. Tiros a puerta: {shw}–{shb}. {matline}",
          "Termina la primera parte. {matline} Tiros {shw}–{shb}; entradas {tkw}–{tkb}. Pongan el agua para el mate, el de beber."],
 'resign': ["¡Y se acabó! {L} ya vio suficiente: el árbitro pita el final. {WIN} se lo lleva en {site}. Resultado final: {WIN} 1, {L} 0.",
            "{L} tiende la mano. ¡Terminó! {WIN} gana uno a cero, y «{nick}» entra en los libros de historia.",
            "¡Final! {L} abandona: ya no había vuelta atrás. {WIN} uno, {L} cero. Qué partidazo en {site}."],
 'draw': ["Final. Nadie parpadea, nadie se rompe: reparto de puntos en {site}. Cero a cero, y ni un segundo aburrido.",
          "Y se dan la mano: tablas. Empate entre {W} y {B}."],
 'aftermate': ["Resultado final desde {site}: {WIN} 1, {L} 0. Esto lo van a repetir para siempre."],
}

B = {  # ---------------------------------------------------------------- BÉISBOL
 'intro': [
  "Muy buenas tardes, amigos, desde {site}. Estamos en {year}, un día precioso para jugar. {W} batea primero con las blancas; {B} tiene la parte baja. A este juego le dicen «{nick}». Acomódense.",
  "Hola otra vez, amigos. Estamos en {site}, {year}. {W} y {B}, nueve entradas o las que hagan falta. Quizá lo hayan oído llamar «{nick}». A ver si es para tanto.",
  "Pues acerquen una silla. {site}, {year}: {W} con las blancas, {B} con las negras, y {opening} en la alineación. Le dicen «{nick}».",
  "Desde la cabina en {site}, muy buen día tengan ustedes. {year}. {W}, {B}. El juego que bautizaron «{nick}». Ahí va el primer lanzamiento.",
 ],
 'first': ["Y arrancamos. Primer lanzamiento: {san}.", "{P} lanza. {san}. Se juega pelota.", "Se prepara, lanza... {san}. Estamos jugando ajedrez."],
 'reply': ["{P} responde en la parte baja: {san}.", "{san} de {P}. La cuenta está pareja.", "Y {P} se para en la caja de bateo. {san}."],
 'pawn': [
  "Toque de bola. Peón a {sq}, y {P} la deja muertita.", "{san}. Bola uno, apenas afuera. {P} no tiene prisa.",
  "{P} adelanta al corredor: peón a {sq}.", "Rodadito por la línea. Peón a {sq}.",
  "Peón a {sq}. Pelota chiquita de {P}. Nada de malo con la pelota chiquita.", "{san}. Strike cantado.",
  "{P} recorta el bate y la toca: peón, {sq}.", "{san}. Un muchacho haciendo su trabajo, ese peón.",
  "Peón a {sq}. Foul hacia atrás. Seguimos esperando.", "Bajita y afuera. {san}. {P} está trabajando la cuenta.",
  "{P} le quita un poquito de velocidad: peón a {sq}.", "{san}. El cuadro jugando adentro, peón un pasito adelante.",
 ],
 'knight': [
  "¡Curva! El caballo rompe tarde y cae en {sq}.", "Caballo a {sq}. Eso se mueve como una nudillera: nadie sabe adónde va, ni el receptor.",
  "{P} manda el caballo a {sq}. Brinco, salto, y hay hombre en base.", "{san}. Curva lenta por la esquina de afuera.",
  "El caballo se despega de {frm} y se barre en {sq}.", "Caballo, {sq}. Y le dan la vuelta al cuadro.",
  "{san}. Brinquito tramposo de {P}.", "Caballo a {sq}. Mal bote para alguien.",
  "Ahí está el lanzamiento quebrado. {san}.", "{P} trae el caballo a {sq}. Base robada, sin tiro.",
 ],
 'bishop': [
  "Slider. El alfil corta hasta {sq}.", "Alfil a {sq}: un lineazo por la diagonal.",
  "{P} va al relevista largo: alfil, {sq}.", "{san}. Línea tendida, de esquina a esquina.",
  "El alfil se estira hasta {sq}. Qué brazo tan largo.", "Alfil a {sq}. Lanzamiento de costado, pinta la esquina.",
  "{san}. Ese alfil tiene un cañón desde los jardines.", "{P} tira la cortada: alfil a {sq}.",
  "Alfil, {sq}. Línea, de un bote.",
 ],
 'rook': [
  "Recta, por el mismo centro: torre a {sq}.", "La torre se cambia a {sq}. Grandulona. Le cuesta arrancar.",
  "{san}. Madera pesada en el círculo de espera.", "{P} alinea la torre en {sq}. Ese es el corazón del lineup.",
  "Torre a {sq}. Nada de adornos.", "{san}. La primera base grandota va a cubrir.",
  "Torre, {sq}. Recta alta.", "{P} calienta la torre: {sq}. Hay movimiento en el bullpen.",
  "{san}. Pelota recta, columna recta.",
 ],
 'queen': [
  "Aquí viene el cuarto bate. Dama a {sq}.", "La dama se para en {sq} y los jardineros se van hacia atrás.",
  "{san}. El bate grande ya está suelto.", "Dama a {sq}. A ella no se le pitchea con cuidado, amigos. Se le reza.",
  "{P} manda a la toletera: dama, {sq}.", "{san}. Se acomoda en la caja. Toca el plato.",
  "Dama a {sq}. Todo el estadio sabe quién está al bate.", "La dama pasea hasta {sq}. Con todo el tiempo del mundo.",
 ],
 'king': [
  "El rey trota hasta {sq}. El mánager sale de la caseta.", "Rey a {sq}. Es el mánager, que va a conversar un rato.",
  "{san}. El mánager se acomoda la gorra y da un pasito.", "Rey, {sq}. Una visita a la lomita.",
 ],
 'king_end': [
  "Rey a {sq}. Últimas entradas: aquí todos se ponen el guante.", "El mánager corre de emergente por sí mismo. Rey a {sq}.",
  "{san}. El viejo todavía puede correr.", "Rey hasta {sq}. Las entradas extra le hacen esto a un equipo.",
  "El rey de {P} corre a {sq}. Jugador y mánager a la vez, amigos.",
 ],
 'castle': [
  "Ahí está el shift. {P} enroca {side} y el cuadro gira.", "{P} enroca {side}. El rey a la caseta, la torre al plato.",
  "Enroque {side}. El mánager, a salvo detrás de la malla.", "{P} enroca {side}. Doble cambio, muy bien hecho.",
 ],
 'cap1': ["¡Hit! {El_pc} toma el peón en {sq}. Un sencillo limpio.", "{san}. Sencillo al lado contrario: entra un peón.",
          "{P} la pasa por el hueco: toma el peón en {sq}.", "Se va el peón en {sq}. Un hit de pelotita; todos cuentan.",
          "{san}. Una carrera que entra para {P}.", "Derribado en {sq}. Un peón menos."],
 'cap3': ["¡Doble! {El_pc} toma {el_cap} en {sq}: contra la pared, llega de pie.", "¡{san}! Por la brecha. {El_cap} sale del juego y entran tres carreras.",
          "¡Lineazo en {sq}! Que se despida {el_cap}.", "{P} pone out a {el_cap} en {sq}. ¡Está out!",
          "{san}. Jonrón de tres carreras a costa de {el_cap}.", "Le dio con todo. {El_pc} toma {el_cap}, {sq}."],
 'cap5': ["¡Triple a la esquina! ¡{El_pc} toma la torre en {sq}!", "¡{san}! ¡Se fue la torre: cinco carreras en la jugada!",
          "Atrás, atrás, contra la cerca: ¡{P} se lleva una TORRE en {sq}!"],
 'capq': ["¡SE VA, SE VA, SE VA... Y SE FUE! ¡{El_pc} toma la DAMA en {sq}! ¡Esa pelota cayó en la calle!",
          "¡¡{san}!! Jonrón con las bases llenas y más. ¡La dama de {O} se va del parque!"],
 'recap': ["Y {P} devuelve el golpe: {el_pc} toma en {sq}. Doble play, quedamos parejos.", "Respondido. {san}. Se cambian carreras.",
           "{P} la recupera enseguida: toma en {sq}.", "{san}. Tú me das, yo te doy. Buen juego.",
           "Cuatro-seis-tres. {El_pc} recaptura en {sq}.", "Vuelve {P}. {san}. El de la pizarra trabaja hoy."],
 'qtrade': ["Y las dos toleteras se van a las duchas. Fuera las damas. Ahora es un duelo de pitcheo.",
            "{san}. Damas cambiadas, mano a mano. Pelota chiquita de aquí al final."],
 'check': [
  "¡Pegada y adentro! {san}: jaque, y el rey de {O} se tira al suelo.", "Jaque en {sq}. Ese pasó rozando la barbilla, amigos.",
  "Corredor en posición de anotar: {el_pc} a {sq}, jaque.", "{P} pitchea adentro con la recta: {san}.",
  "Jaque. Al mánager de {O} no le va a gustar esa.", "¡{san}! Para que se aparte del plato. Jaque.",
  "{El_pc} tira una pegada a la barbilla desde {sq}. Jaque.", "{san}. Eso aleja a cualquier rey del plato.",
 ],
 'capcheck': ["¡Bateo y corrido! {san}: ¡toma {el_cap} y da jaque!", "¡{san}! Extrabase Y el rey en apuros.",
              "{P} le pega duro a {el_cap} en {sq}: jaque. Eso es un rally."],
 'runcheck': ["Jaque otra vez. Ya van {run} seguidos. {P} vive en la esquina de adentro.", "{san}. {run} jaques al hilo: el rey está atrapado entre bases.",
              "Otro más. {san}. {run} seguidos, y nadie calienta en el bullpen de {O}."],
 'ev_king': ["El rey se agacha hacia {sq}. Lo apartaron, pero sigue en pie.", "{P} sale de la caja: rey a {sq}.",
             "{san}. El mánager se escabulle. Safe.", "Rey a {sq}. Safe en primera, por un pelito.", "El rey se barre en {sq}, con los spikes por delante. Safe."],
 'ev_king_cap': ["El mánager lo resuelve en persona. El rey toma {el_cap} en {sq}.", "{san}. El rey la fildea a mano limpia y {el_cap} queda out."],
 'ev_block': ["{El_pc} cubre la almohadilla en {sq}. Jaque bloqueado.", "Bloqueado. {san}. Buen trabajo de guante.", "{El_pc} a {sq}. La paran en el hueco.",
              "{san}. {El_pc} se sacrifica por el equipo."],
 'ev_take': ["¡Out en el tiro! {El_pc} toma {el_cap} en {sq} y se acabó la amenaza.", "{san}. Lo sorprendieron fuera de la base. Adiós a ese corredor."],
 'sac': [
  "¡Sacrificio! {P} entrega {el_pc} en {sq} para adelantar a los corredores.", "Eso es un elevado de sacrificio, profundo: {el_pc} se va, pero alguien viene a home.",
  "{san}. {P} entrega {el_pc}. Pelota a la antigua: das una para meter una.", "¡Squeeze play! ¡{El_pc} se ofrece en {sq}!",
  "Vaya, vaya. {P} acaba de dejar {el_pc} colgad{o_pc} sobre el plato en {sq}. A propósito, creo.", "{san}. Eso es un sacrificio, y uno bonito.",
  "{P} pone {el_pc} justo en la zona de poder, en {sq}, y reta a {O} a hacerle swing.",
 ],
 'qsac': ["Ay, caramba. {P} dejó la DAMA en {qsq} sin nadie que la cubra. Eso no se ve en este parque ni en ningún otro.",
          "Pues miren, he visto mucha pelota, y eso no lo había visto. {san}: ¡la dama está ahí para quien la quiera!",
          "¡{san}! ¡La dama colgada en {qsq}! O {P} sabe algo, o nos vamos todos temprano a casa."],
 'hang': ["{san}. Y {P} deja {el_hp} de {hsq} sin nadie que l{o_hp} cubra. Ni siquiera miró.",
          "Ahí hay {un_hp} colgad{o_hp} en {hsq}, y {P} juega {san} como si no existiera. Con agallas.",
          "{P} deja ir {el_hp} de {hsq}. {san}. Es entregarse para adelantar al corredor.",
          "{san}. {El_hp} de {hsq} está atrapad{o_hp} entre bases y {P} le dice adiós con la mano."],
 'accept': ["{P} le hace swing: {el_pc} toma {el_cap} en {sq}. Veremos si era strike.", "{san}. {P} acepta la base por bolas. Nada es gratis, amigos.",
            "Aceptado. {El_cap} sale del tablero. Ahora a pitchear para salir del lío, {P}."],
 'decline': ["{P} deja pasar el lanzamiento. Ni toca {el_offered} y juega {san}.", "No hay swing. {san}. {P} no muerde con {el_offered}.",
             "{san}. La dejó pasar. Buen ojo, quizá."],
 'promo': ["¡Subido al equipo grande! El peón llega a {sq} ¡y vuelve convertido en dama!", "¡{san}! Llegó de novato y se va a casa como dama. Solo en este juego."],
 'under': ["El peón llega a {sq}... y {P} pide {un_promo}. Un emergente que nadie esperaba."],
 'adv7': ["¡Corredor en tercera! Peón a {sq}, a noventa pies de home.", "{san}. Ese peón baila en la tercera base.", "Peón a {sq}. Con un buen sencillo, entra."],
 'adv6': ["Peón a {sq}. Va doblando por segunda.", "{san}. Corredor en posición de anotar.", "Ese peón la estira hasta {sq}. Barrida de cabeza."],
 'fork': ["Caballo en {sq}, y tiene a dos atrapados entre bases.", "{san}. Horquilla de caballo: alguien queda out en esta jugada."],
 'mate': [
  "¡SE VA, SE VA, SE FUE! {san}: ¡JAQUE MATE! ¡Jonrón para dejar en el terreno a {O}! ¡Este juego SE ACABÓ!",
  "¡LE TIRA Y LA DESAPARECE! ¡{san}! Eso es mate, eso es el juego, ¡y {P} gana en {site}!",
  "¡{san}! ¡JAQUE MATE! ¡Lo dejan en el terreno! ¡Salen todos de la caseta por {P}!",
  "Elevado, profundo, atrás, atrás... ¡SE FUE! {san}, jaque mate. Anótenlo en los libros: gana {P}.",
 ],
 'half': ["Llegó la séptima entrada, amigos: a estirar las piernas. Carreras en material: {W} {rw}, {B} {rb}. Jaques: {shw} y {shb}.",
          "Todos de pie: estiramiento en {site}. En la pizarra van {W} {rw}, {B} {rb}. Pero la pizarra no es el juego."],
 'resign': ["Y {L} se toca la gorra y se va al clubhouse. Abandona. {WIN} gana aquí en {site}.",
            "Hasta ahí llegó. {L} hace un gesto con la mano: no tiene sentido seguir. Juego para {WIN}.",
            "{L} emprende la larga caminata. Abandono. Anótenlo en los libros: {WIN}, en el juego que llaman «{nick}»."],
 'draw': ["Y lo van a suspender ahí, empatados. Tablas en {site}. Nadie se va feliz, nadie se va herido.",
          "Suspendido por falta de algo que jugar. Tablas. {W} y {B} se reparten el juego."],
 'box_irony': [" No miren el box score, amigos: {WIN} pierde {lo}–{hi} en material y gana lo único que cuenta.",
               " {WIN} pierde el box score {lo} a {hi}. En esta liga solo cuenta el rey."],
 'box': [" En material termina {WIN} {hi}, {L} {lo}.", " La línea: {WIN} {hi} carreras, {L} {lo}."],
}


def flank(d):
    f = d['file'] if d['white'] else 7 - d['file']
    return "por la izquierda" if f <= 2 else "por la derecha" if f >= 5 else "por el centro"


def art(piece, cap=False, indef=False):
    if not piece:
        return ''
    noun, g = GEN[piece]
    a = ('un' if g == 'm' else 'una') if indef else ('el' if g == 'm' else 'la')
    return (a.capitalize() if cap else a) + ' ' + noun


def end(piece):
    return 'a' if piece and GEN[piece][1] == 'f' else 'o'


def contract(s):
    s = re.sub(r'\b([Aa]) el\b', r'\1l', s)
    return re.sub(r'\b([Dd])e el\b', r'\1el', s)


def cap1(s):
    """Mayúscula inicial (también tras ¡ o ¿), salvo si abre con una jugada de peón como 'e4'."""
    i = 0
    while i < len(s) and s[i] in '¡¿«':
        i += 1
    if i >= len(s) or (len(s) > i + 1 and s[i] in 'abcdefgh' and s[i + 1] in '12345678x'):
        return s
    return s[:i] + s[i].upper() + s[i + 1:]


def narrate(game, plies, opening, site, nick):
    """Igual que commentary.narrate, en español. opening, site y nick ya traducidos."""
    W, Bk = short(game['white']), short(game['black'])
    res = game['result']
    win = W if res == '1-0' else Bk if res == '0-1' else None
    lose = Bk if res == '1-0' else W if res == '0-1' else None
    base = dict(W=W, B=Bk, site=site, year=game['year'], nick=nick, opening=opening, WIN=win, L=lose)
    out = {}
    n = len(plies)
    for sport, bank in (('s', S), ('b', B)):
        v = Voice(bank, random.Random(game['id'] * 7 + (1 if sport == 's' else 2)))
        intro = v.pick('intro').format(**base)
        lines = []
        sh = {True: 0, False: 0}; tk = {True: 0, False: 0}; runs = {True: 0, False: 0}
        half_at = n // 2 if sport == 's' else (n * 6) // 9
        for d in plies:
            P, O = (W, Bk) if d['white'] else (Bk, W)
            if d['check']: sh[d['white']] += 1
            if d['cap']: tk[d['white']] += 1; runs[d['white']] += d['capv']
            endgame = d['pieces'] <= 12 or not d['queens']
            key = 'first' if d['i'] == 0 else 'reply' if d['i'] == 1 else choose_key(d, sport, endgame)
            hp = d['hang'][0] if d['hang'] else None
            off = d['offered'] or 'knight'
            ctx = dict(base, P=P, O=O, PU=P.upper(), san=i18n_es.san(d['san']), sq=d['to'], frm=d['frm'],
                       el_pc=art(d['piece']), El_pc=art(d['piece'], True), o_pc=end(d['piece']),
                       el_cap=art(d['cap']), El_cap=art(d['cap'], True), un_cap=art(d['cap'], indef=True),
                       Un_cap=art(d['cap'], True, True), o_cap=end(d['cap']),
                       flank=flank(d), run=d['run'], side='corto' if d['castle'] == 'K' else 'largo',
                       el_offered=art(off) if d['offered'] else 'la pieza', un_promo=art(d['promo'], indef=True),
                       qsq=d['qsq'], el_hp=art(hp), El_hp=art(hp, True), un_hp=art(hp, indef=True), o_hp=end(hp),
                       hsq=d['hang'][1] if d['hang'] else '')
            text = cap1(contract(v.pick(key).format(**ctx)))
            if d['i'] == half_at and n >= 30 and not d['mate']:
                bal = d['bal']
                mat = "Igualados en material." if bal == 0 else \
                    f"{W if bal > 0 else Bk}, {abs(bal)} {'punto' if abs(bal) == 1 else 'puntos'} arriba en material."
                text += "\n" + v.pick('half').format(**dict(base, poss=d['poss'], possb=100 - d['poss'], shw=sh[True], shb=sh[False],
                                                           tkw=tk[True], tkb=tk[False], rw=runs[True], rb=runs[False], matline=mat))
            lines.append(text)
        last = plies[-1]
        if last['mate']:
            mw = last['white']
            b2 = dict(base, WIN=W if mw else Bk, L=Bk if mw else W)
            outro = S['aftermate'][0].format(**b2) if sport == 's' else ''
        elif win:
            outro = v.pick('resign').format(**base)
        else:
            outro = v.pick('draw').format(**base)
        if sport == 'b' and (win or last['mate']):
            winner_white = (res == '1-0')
            hi, lo = runs[winner_white], runs[not winner_white]
            b2 = dict(base, WIN=W if winner_white else Bk, L=Bk if winner_white else W, hi=hi, lo=lo)
            if not outro:
                outro = f"Final desde {site}: gana {b2['WIN']}."
            outro += (v.pick('box_irony') if hi < lo else v.pick('box')).format(**b2)
        out[sport] = dict(intro=intro, lines=lines, outro=outro)
    return out
