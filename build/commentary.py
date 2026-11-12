"""Play-by-play in two voices: a breathless football (soccer) announcer and a
laconic baseball radio man. One line per ply, built from the facts in features.py."""
import random

SHORT = {"Louis de La Bourdonnais": "La Bourdonnais", "Duke Karl & Count Isouard": "Duke Karl",
         "Curt von Bardeleben": "von Bardeleben", "Deep Blue": "Deep Blue", "Bai Jinshi": "Bai",
         "Ding Liren": "Ding", "Glücksberg": "Glücksberg"}


def short(name):
    return SHORT.get(name, name.split()[-1])


def ordinal(n):
    return f"{n}{'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"


S = {  # ------------------------------------------------------------------ SOCCER
 'intro': [
  "Good evening and welcome to {site}, {year}! In the white shirts, {W}; in the black, {B}. They call this one “{nick}” — stay right where you are and find out why.",
  "Hello, hello, hello from {site}! The year is {year}, the fixture is {W} against {B}, and history has a name for it already: “{nick}.” The players are out. Here we go!",
  "{site}, {year}. Sixty-four squares of perfect turf, thirty-two players, two managers: {W} and {B}. The match they will call “{nick}” is moments away.",
  "Welcome along! {W} versus {B}, live from {site} in {year}. The opening on the team sheet is the {opening}. They call it “{nick}.” The referee checks the clock...",
 ],
 'first': ["And we're underway! {P} rolls it forward — {san}.", "The whistle goes! {san} from {P} and this match is alive.",
           "Kick-off! {P} taps it out: {san}."],
 'reply': ["{P} answers straight from the restart: {san}.", "{san} comes back from {P}. No nerves there.",
           "And {P} meets it with {san}. We have a game."],
 'pawn': [
  "{P} nudges a pawn up to {sq}. Short pass, keeps the shape.", "Pawn to {sq}. {P} pushing the line a few yards higher.",
  "A little toe-poke forward, {san}. Patient build-up from {P}.", "{P} works it {flank}: pawn to {sq}.",
  "{san}. {P} squeezing the pitch, pawn by pawn.", "The pawn steps to {sq}. Who's marking that?",
  "Tidy from {P}. Pawn to {sq} — nothing fancy, nothing wrong.", "{san}. The back line creeps up behind it.",
  "{P} recycles possession, pawn to {sq}.", "Pawn to {sq}, {flank}. That's a marker put down.",
  "One more yard of grass claimed: {san}.", "{P} plays it simple. {san}. The crowd wants more; the manager does not.",
 ],
 'knight': [
  "The knight hops to {sq} — that little L-shaped run nobody ever tracks.", "{P} sends the knight {flank}; it lands on {sq}.",
  "Knight to {sq}. Tricky feet, awkward angles. Defenders hate marking that one.", "{san}! The knight ghosts into {sq}, unmarked.",
  "A dart from the knight, {sq}. {P} is probing.", "Round the corner goes the knight — {sq}. Lovely movement off the ball.",
  "{san}. The knight checks its run, then goes. Clever.", "Knight to {sq}. It never runs in a straight line and it never will.",
  "{P} finds the knight between the lines on {sq}.", "Up pops the knight on {sq}. Where did that come from?",
 ],
 'bishop': [
  "Long diagonal ball from {P}! The bishop sweeps to {sq}.", "Bishop to {sq} — a raking cross-field pass.",
  "{P} slides the bishop to {sq}. You can see the whole pitch from there.", "The bishop cuts in off the wing: {sq}.",
  "{san}. A diagonal switch of play. The bishop loves open grass.", "Bishop to {sq}. That's a sniper finding a window.",
  "{P} opens the angle — {san}. Somebody on the far side should be nervous.", "The bishop drops to {sq}, pulling strings from deep.",
  "{san}. Inch-perfect along the diagonal from {P}.",
 ],
 'rook': [
  "The rook lumbers across to {sq}. Big centre-half coming up for the set piece.", "Rook to {sq}. Heavy artillery moving up the touchline.",
  "{san}. The big unit shuffles into position.", "The rook takes the open channel — {sq}. That is a lot of grass to run into.",
  "{P} loads the file: rook to {sq}.", "Rook to {sq}. Not pretty, not meant to be.",
  "{san}. {P} brings a tower forward and the back line takes a breath.", "The rook swings over to {sq}. That's muscle arriving late in the box.",
  "{P} shifts the rook to {sq}. Quiet now. Not for long.",
 ],
 'queen': [
  "Here comes the number ten! The queen glides to {sq}.", "{P} brings the queen to {sq} — the playmaker wants the ball.",
  "Queen to {sq}. Every defender just took one step back.", "{san}. The star turns, looks up, picks a square.",
  "The queen drifts {flank}, {sq}. Danger wherever she goes.", "{san}! Different class. The queen finds a pocket of space.",
  "Queen to {sq}. She's been quiet. She's not quiet now.", "{P} moves the queen to {sq}, and the temperature in the stadium changes.",
  "The queen drops off to {sq}, asking for it to feet.",
 ],
 'king': [
  "The king steps to {sq}. The keeper is off the line!", "{P}'s king shuffles to {sq} — a keeper who likes to sweep.",
  "King to {sq}. Brave, coming out of the box like that.", "{san}. A little adjustment between the posts from {P}.",
  "The king sidesteps to {sq}. Calm hands, we hope.",
 ],
 'king_end': [
  "The king marches up to {sq}. Late on, even the keeper goes forward!", "King to {sq} — the goalkeeper is up for the corner!",
  "{san}. With the pitch this empty the king plays like a midfielder.", "{P}'s king strides to {sq}. No fear left, nothing to hide from.",
  "Forward comes the king, {sq}. This is extra-time football now.",
 ],
 'castle': [
  "{P} castles {side}! Keeper tucked behind the back four, rook into the middle.", "Castles {side}. That's the defensive wall set — good luck getting through that.",
  "And {P} castles {side}. Parking the bus? Maybe just the minibus.", "Safety first: {P} castles {side}. The king is behind the wall and the rook joins the party.",
 ],
 'cap': [
  "{P} wins the ball! The {pc} takes the {cap} on {sq}.", "Crunching tackle on {sq} — the {cap} is off the pitch.",
  "{san}! The {pc} steams in and the {cap} is dispossessed.", "Clean as you like. {pc_c} takes {cap}, {sq}. Play on, says the referee.",
  "Off goes the {cap}! Straight red, no arguments. {P}'s {pc} did the damage on {sq}.", "Intercepted! {P}'s {pc} reads it and picks off the {cap} at {sq}.",
  "{san}. That {cap} never saw the challenge coming.", "{P} goes through the back of the {cap} on {sq} — and gets away with it!",
  "The {pc} nicks it on {sq}. One {cap} fewer for {O}.", "Robbed! {san}. {O} loses a {cap} in a dangerous area.",
 ],
 'recap': [
  "And {P} wins it straight back — {pc} takes on {sq}. Fifty-fifty, honours even.", "Tit for tat! {san}; the {cap} goes into the book too.",
  "Immediate response: the {pc} recaptures on {sq}. End-to-end stuff.", "{P} mops up on {sq}. A fair exchange of shirts.",
  "{san}. Tackle answered with tackle.", "Back it comes! {P}'s {pc} settles the account on {sq}.",
 ],
 'capq': ["THE QUEEN IS DOWN! {P}'s {pc} takes her on {sq} — the star player is stretchered off!",
          "{san}!! The number ten is GONE! {O} has lost the queen!"],
 'qtrade': ["And the queens come off together. Both number tens substituted — this is a different match now.",
            "{san}. Queens exchanged. The artists leave the pitch; the grafters take over."],
 'check': [
  "SHOT! {san} — {P} tests the keeper from {sq}!", "Check on {sq}! {O}'s king has to scramble.",
  "{P} lets fly — {san}! On target!", "Oh, that's stinging the palms! {pc_c} to {sq}, check.",
  "Check! The {pc} arrives in the box and {O} is under siege.", "{san}! Straight at the king. {O} must deal with it.",
  "A dig from distance — {san}. Check!", "The {pc} shoots from {sq}! The king is rattled.",
 ],
 'capcheck': ["Takes and shoots in one movement! {san}! {P}'s {pc} flattens the {cap} and it's check!",
              "{san}! Wins the ball AND gets the shot away. {O} is reeling.",
              "The {cap} is swept aside on {sq} — and it's check as well! Ruthless from {P}."],
 'runcheck': ["Another one! {san}! {P} is peppering the goal — that's {run} shots in a row!",
              "{san}! Check again! {run} on the spin. {O}'s king is being chased around the six-yard box.",
              "And again! {san}! This is a siege — {run} consecutive checks."],
 'ev_king': ["Parried! {P}'s king dives to {sq}.", "The keeper scrambles — king to {sq}. Still alive.",
             "Off the line and away to {sq}. Heart-in-mouth defending from {P}.", "{san}. The king wriggles clear. Just.",
             "King to {sq}. Palmed round the post!"],
 'ev_king_cap': ["The king deals with it personally — takes the {cap} on {sq}!", "{san}! The keeper comes out and claims the {cap}. Brave!"],
 'ev_block': ["Blocked! The {pc} throws itself in the way on {sq}.", "Body on the line! {san} — {P} survives.",
              "{pc_c} to {sq}, a last-ditch block.", "Cleared! {san}. The {pc} gets a boot in the way."],
 'ev_take': ["Saved and held! The {pc} takes the {cap} on {sq}. Danger over — for now.", "{san}! The shooter is taken out. {P} breathes again."],
 'sac': [
  "WHAT IS THIS? {P} leaves the {pc} right there on {sq} — gift or trap?", "Given away! No — wait — {P} MEANT that. The {pc} is offered on {sq}!",
  "A dummy! {P} lets the {pc} go on {sq} and the whole stadium gasps.", "Audacious! {san} — {P} throws the {pc} forward and dares {O} to take it.",
  "That's a nutmeg in broad daylight. {P} sacrifices the {pc} on {sq}!", "{san}!! The {pc} goes in where it hurts. {P} is gambling the house!",
  "Oh my word. {P} has just put the {pc} en prise on {sq} — deliberately!",
 ],
 'qsac': ["THE QUEEN! THE QUEEN! {P} leaves the queen hanging on {qsq}! Somebody check the rulebook — is this allowed?!",
          "Unbelievable scenes! {san} — and {P}'s queen can simply be taken! That is either madness or genius!",
          "{san}!!! {P} offers the QUEEN. I have watched this game all my life and my hands are shaking."],
 'hang': ["{P} ignores the threat! The {hp} on {hsq} is simply left to its fate — and {P} plays {san}!",
          "Hold on — the {hp} on {hsq} is there to be taken! {P} doesn't care: {san}.",
          "{san}! Never mind the {hp} hanging on {hsq}; {P} has bigger ideas. This is fearless football!",
          "{P} leaves the {hp} unmarked on {hsq} and pours forward anyway. {san}!"],
 'accept': ["{P} takes the bait — {pc} takes {cap} on {sq}. Brave. Or hungry.", "{san}. {P} says thank you very much and pockets the {cap}. But at what price?",
            "Accepted! The {cap} comes off. Now {P} has to survive what's coming."],
 'decline': ["{P} wants nothing to do with it! Leaves the {offered} alone and plays {san}.",
             "No thank you, says {P}. {san} — the {offered} stays on the pitch.", "{san}. {P} smells the trap and steps around it."],
 'promo': ["SUBSTITUTION! Pawn off, queen on — {P} promotes on {sq}! Fresh legs, and what legs!",
           "{san}! The little pawn has run the length of the pitch and comes back a QUEEN!"],
 'under': ["Substitution on {sq} — and it's a {promo}, not a queen! {P} knows something we don't."],
 'adv7': ["The pawn is through on {sq}! One-on-one with the back line!", "{san}! That pawn is on the shoulder of the last defender.",
          "{P}'s pawn charges to {sq} — one step from the byline!"],
 'adv6': ["{P}'s pawn breaks into the final third — {sq}.", "{san}. That pawn is a runner in behind now.", "The pawn keeps going! {sq}. Somebody track that run."],
 'fork': ["A fork! The knight on {sq} is marking two players at once and loving it.", "{san}! The knight has two of them in its pocket."],
 'mate': [
  "GOOOOOOOOOL! GOL! GOL! GOL DE {PU}! {san} — CHECKMATE! The king has nowhere to go, the net is bulging, and {site} will talk about this for a hundred years!",
  "GOOOOOOOOOOOL! {san}! CHECKMATE! {PU}! {PU}! Take a bow — that is one for the museum!",
  "IT'S THERE! GOOOOOOL! {san}, and it is MATE! {P} has done it in {site}! Listen to that crowd!",
  "GOOOOOOOL DE {PU}! {san}! No keeper on earth stops that. Checkmate, full time, history!",
 ],
 'half': ["HALF-TIME in {site}. Possession: {W} {poss}%, {B} {possb}%. Shots on target: {shw}–{shb}. {matline}",
          "That's the half. {matline} Shots {shw}–{shb}; tackles {tkw}–{tkb}. Get the kettle on."],
 'resign': ["And that's it! {L} has seen enough — the referee blows for full time. {WIN} wins it in {site}. Final score: {WIN} 1, {L} 0.",
            "{L} offers the hand. It's over! {WIN} takes it, one–nil, and “{nick}” goes into the history books.",
            "Full time! {L} resigns — no way back from there. {WIN} one, {L} nil. What a match in {site}."],
 'draw': ["Full time. Nobody blinks, nobody breaks: the points are shared in {site}. Nil–nil, and not a dull second in it.",
          "And they shake hands on a draw. Honours even between {W} and {B}."],
 'aftermate': ["Final score from {site}: {WIN} 1, {L} 0. They will be replaying that one forever."],
}

B = {  # ---------------------------------------------------------------- BASEBALL
 'intro': [
  "Good afternoon, everybody, from {site}. It's {year}, a fine day for it. {W} bats first with the white pieces; {B} has the home half. Folks call this one “{nick}.” Settle in.",
  "Hello again, everybody. We're in {site}, {year}. {W} and {B}, nine innings or as many as it takes. You may have heard this one called “{nick}.” Let's see about that.",
  "Well, pull up a chair. {site}, {year}: {W} with the white pieces, {B} with the black, and the {opening} on the lineup card. They call it “{nick}.”",
  "From the booth in {site}, a pleasant good day to you. {year}. {W}, {B}. The game they named “{nick}.” Here's the first pitch.",
 ],
 'first': ["And we're underway. First pitch: {san}.", "{P} deals. {san}. Ballgame's on.", "Here's the windup — {san}. We're playing chess."],
 'reply': ["{P} answers in the bottom half: {san}.", "{san} from {P}. Count's even.", "And {P} steps in. {san}."],
 'pawn': [
  "Bunt. Pawn to {sq}, and {P} lays it down soft.", "{san}. Ball one, just outside. {P} is in no hurry.",
  "{P} moves a runner over: pawn to {sq}.", "Little dribbler up the line. Pawn to {sq}.",
  "Pawn to {sq}. Small ball from {P}. Nothing wrong with small ball.", "{san}. Taken for a strike.",
  "{P} chokes up and pokes one: pawn, {sq}.", "{san}. Just a fella doing his job, that pawn.",
  "Pawn to {sq}. Fouled back. We wait.", "Low and away. {san}. {P} is working the count.",
  "{P} takes a little off: pawn to {sq}.", "{san}. Infield in, pawn up a step.",
 ],
 'knight': [
  "Curveball! Knight breaks late and lands on {sq}.", "Knight to {sq}. That thing moves like a knuckler — nobody knows where it's going, catcher included.",
  "{P} sends the knight to {sq}. Hop, skip, and there's a man on.", "{san}. Slow hook on the outside corner.",
  "The knight takes a lead off {frm} and slides into {sq}.", "Knight, {sq}. Around the horn it goes.",
  "{san}. Tricky little hopper from {P}.", "Knight to {sq}. Bad hop for somebody.",
  "There's the breaking ball. {san}.", "{P} brings the knight around to {sq}. Stolen base, no throw.",
 ],
 'bishop': [
  "Slider. Bishop cuts across to {sq}.", "Bishop to {sq} — a rope down the diagonal.",
  "{P} goes to the long reliever: bishop, {sq}.", "{san}. Frozen rope, corner to corner.",
  "The bishop stretches it out to {sq}. Long arm on that one.", "Bishop to {sq}. Sidearm delivery, paints the corner.",
  "{san}. That bishop's got a cannon from the outfield.", "{P} throws the cutter — bishop to {sq}.",
  "Bishop, {sq}. Line drive, one hop.",
 ],
 'rook': [
  "Fastball, straight down the pipe: rook to {sq}.", "The rook moves over to {sq}. Big fella. Takes a while to get going.",
  "{san}. Heavy lumber in the on-deck circle.", "{P} lines up the rook on {sq}. That's the heart of the order.",
  "Rook to {sq}. Nothing cute about it.", "{san}. The big first baseman lumbers over to cover.",
  "Rook, {sq}. High heat.", "{P} warms up the rook: {sq}. Bullpen's busy.",
  "{san}. Straight ball, straight file.",
 ],
 'queen': [
  "Here's the cleanup hitter. Queen to {sq}.", "The queen steps in at {sq} and the outfield backs up.",
  "{san}. The big bat is loose now.", "Queen to {sq}. You don't pitch around her, folks. You just pray.",
  "{P} sends up the slugger: queen, {sq}.", "{san}. She digs in. Taps the plate.",
  "Queen to {sq}. Everybody in the park knows who's up.", "The queen strolls to {sq}. All the time in the world.",
 ],
 'king': [
  "The king jogs over to {sq}. Skipper's out of the dugout.", "King to {sq}. That's the manager wandering out to talk things over.",
  "{san}. Skipper adjusts his cap and moves a step.", "King, {sq}. A little visit to the mound.",
 ],
 'king_end': [
  "King to {sq}. Late innings — everybody plays the field.", "The skipper's pinch-running for himself. King to {sq}.",
  "{san}. The old man can still leg it out.", "King up to {sq}. Extra innings does this to a ballclub.",
  "{P}'s king hustles to {sq}. Player-manager, folks.",
 ],
 'castle': [
  "There's the shift. {P} castles {side} and the infield swings around.", "{P} castles {side}. King's in the dugout, rook's at the plate.",
  "Castles {side}. Skipper's safe behind the screen.", "{P} castles {side}. Double switch, nicely done.",
 ],
 'cap1': ["Base hit! {pc_c} takes pawn on {sq}. A clean single.", "{san}. Singles the other way — a pawn comes in.",
          "{P} slaps one through the hole: takes the pawn on {sq}.", "Pawn's gone on {sq}. Texas leaguer; they all count.",
          "{san}. One run across for {P}.", "Knocked down on {sq}. Scratch a pawn."],
 'cap3': ["Double! {pc_c} takes the {cap} on {sq} — off the wall, standing up.", "{san}! Into the gap. The {cap} is out of the game and three runs score.",
          "Line drive, {sq}! Say goodbye to the {cap}.", "{P} tags the {cap} at {sq}. Yer out!",
          "{san}. That's a three-run shot off the {cap}.", "Got all of that one. {pc_c} takes {cap}, {sq}."],
 'cap5': ["Triple into the corner! {pc_c} takes the rook on {sq}!", "{san}! The rook is gone — five runs on the play!",
          "Way back, off the fence — {P} takes a ROOK on {sq}."],
 'capq': ["GOING, GOING — GONE! {pc_c} takes the QUEEN on {sq}! That ball is out on the street!",
          "{san}!! Grand slam and then some. {O}'s queen leaves the yard!"],
 'recap': ["And {P} throws right back — {pc} takes on {sq}. Double play, we're even.", "Answered. {san}. They trade runs.",
           "{P} gets it right back: takes on {sq}.", "{san}. Tit for tat. Good ballgame.",
           "Four-six-three. {pc_c} recaptures on {sq}.", "Back comes {P}. {san}. The scoreboard operator is busy today."],
 'qtrade': ["And both sluggers hit the showers. Queens are off. It's a pitchers' duel now.",
            "{san}. Queens traded, even up. Small ball the rest of the way."],
 'check': [
  "High and tight! {san} — check, and {O}'s king hits the dirt.", "Check on {sq}. That's chin music, folks.",
  "Runner in scoring position: {pc} to {sq}, check.", "{P} comes inside with the heater: {san}.",
  "Check. {O}'s skipper won't care for that one.", "{san}! Brushback. Check.",
  "The {pc} fires one under the chin from {sq}. Check.", "{san}. That'll back a king off the plate.",
 ],
 'capcheck': ["Hit and run! {san} — takes the {cap} and gives check!", "{san}! Extra bases AND the king's in trouble.",
              "{P} rips the {cap} on {sq} — check. That's a rally."],
 'runcheck': ["Check again. That's {run} straight. {P} is living on the inside corner.", "{san}. {run} checks in a row — the king's in a rundown.",
              "Another one. {san}. {run} straight, and nobody's warming up for {O}."],
 'ev_king': ["King ducks to {sq}. Brushed back but still standing.", "{P} steps out of the box — king to {sq}.",
             "{san}. Skipper scrambles. Safe.", "King to {sq}. Safe at first, by an eyelash.", "The king slides into {sq}, spikes high. Safe."],
 'ev_king_cap': ["The skipper handles it himself. King takes the {cap} on {sq}.", "{san}. King fields it barehanded and the {cap} is out."],
 'ev_block': ["The {pc} covers the bag on {sq}. Check's blocked.", "Blocked. {san}. Good glove work.", "{pc_c} to {sq}. Knocked down in the hole.",
              "{san}. The {pc} takes one for the team."],
 'ev_take': ["Thrown out! The {pc} takes the {cap} on {sq} and the threat is over.", "{san}. Picked off. So much for that runner."],
 'sac': [
  "Sacrifice! {P} gives up the {pc} on {sq} to move the runners along.", "That's a sacrifice fly, deep — the {pc} is gone, but somebody's coming home.",
  "{san}. {P} lays down the {pc}. Old-time baseball: give one up to get one in.", "Squeeze play! The {pc} is offered on {sq}!",
  "Well now. {P} just left the {pc} hanging over the plate on {sq}. On purpose, I think.", "{san}. That's a sacrifice, and a pretty one.",
  "{P} puts the {pc} right in the wheelhouse on {sq} and dares {O} to swing.",
 ],
 'qsac': ["Oh, my. {P} has left the QUEEN on {qsq} with nobody covering. You don't see that in this ballpark or any other.",
          "Well, I have watched a lot of ball, and I have not seen that. {san} — the queen is there for the taking!",
          "{san}! The queen's hung out to dry on {qsq}! Either {P} knows something or we're all going home early."],
 'hang': ["{san}. And {P} leaves the {hp} on {hsq} with nobody covering. Didn't even look over.",
          "Now there's a {hp} hung out on {hsq}, and {P} plays {san} like it isn't there. Gutsy.",
          "{P} lets the {hp} on {hsq} go. {san}. That's giving yourself up to move the runner.",
          "{san}. The {hp} on {hsq} is caught in a pickle and {P} just waves it goodbye."],
 'accept': ["{P} swings at it — {pc} takes the {cap} on {sq}. We'll see if that was a strike.", "{san}. {P} takes the free pass. Nothing's free, folks.",
            "Accepted. The {cap} comes off the board. Now pitch your way out of it, {P}."],
 'decline': ["{P} takes the pitch. Leaves the {offered} right there and plays {san}.", "No swing. {san}. {P} isn't biting on the {offered}.",
             "{san}. Laid off it. Good eye, maybe."],
 'promo': ["Called up to the big club! Pawn reaches {sq} and comes back a queen!", "{san}! Came up a rookie, goes home a queen. Only in this game."],
 'under': ["Pawn reaches {sq} — and {P} calls for a {promo}. A pinch-hitter nobody expected."],
 'adv7': ["Runner on third! Pawn to {sq}, ninety feet from home.", "{san}. That pawn's dancing off third base.", "Pawn to {sq}. One good single brings it in."],
 'adv6': ["Pawn to {sq}. It's rounding second.", "{san}. Runner's in scoring position.", "That pawn stretches it to {sq}. Head-first slide."],
 'fork': ["Knight on {sq}, and it's got two men caught in a rundown.", "{san}. Knight fork — somebody's out on this play."],
 'mate': [
  "IT'S OUTTA HERE! {san} — CHECKMATE! A walk-off for {P}! Touch 'em all, this ballgame is OVER!",
  "SWUNG ON AND BELTED! {san}! That's mate, that's the ballgame, and {P} wins it in {site}!",
  "{san}! CHECKMATE! Walk-off winner! They're pouring out of the dugout for {P}!",
  "High fly ball, deep, way back — GONE! {san}, checkmate. Put it in the books: {P} wins it.",
 ],
 'half': ["That's the seventh-inning stretch, folks. Runs on material: {W} {rw}, {B} {rb}. Checks: {shw} and {shb}.",
          "Everybody up — stretch time in {site}. On the board it's {W} {rw}, {B} {rb}. Board ain't the ballgame, though."],
 'resign': ["And {L} tips the cap and heads for the clubhouse. Resigns. {WIN} wins it here in {site}.",
            "That'll do it. {L} waves it off — no sense playing it out. Ballgame to {WIN}.",
            "{L} takes the long walk. Resignation. Put it in the books: {WIN}, in the game they call “{nick}.”"],
 'draw': ["And they'll call it right there, all tied up. A draw in {site}. Nobody goes home happy, nobody goes home hurt.",
          "Called on account of nothing left to play for. Draw. {W} and {B} split it."],
 'box_irony': [" Don't look at the box score, folks — {WIN} trails {lo}–{hi} on material and wins the only thing that counts.",
               " {WIN} loses the box score {lo} to {hi}. In this league they only count the king."],
 'box': [" On material it finishes {WIN} {hi}, {L} {lo}.", " The line: {WIN} {hi} runs, {L} {lo}."],
}


class Voice:
    def __init__(self, bank, rng):
        self.bank, self.rng, self.recent = bank, rng, {}

    def pick(self, key):
        opts = self.bank[key]
        used = self.recent.setdefault(key, [])
        free = [i for i in range(len(opts)) if i not in used] or list(range(len(opts)))
        i = self.rng.choice(free)
        used.append(i)
        if len(used) > max(1, len(opts) - 2):
            del used[0]
        return opts[i]


def flank(d):
    f = d['file'] if d['white'] else 7 - d['file']
    side = "down the left" if f <= 2 else "down the right" if f >= 5 else "through the middle"
    return side


def choose_key(d, sport, endgame):
    """Priority list of what is worth shouting about on this ply."""
    if d['mate']: return 'mate'
    if d['promo']: return 'promo' if d['promo'] == 'queen' else 'under'
    if d['qoffer']: return 'qsac'
    if d['sac']: return 'sac'
    if d['hang']: return 'hang'
    if d['accept']: return 'accept'
    if d['evade'] and not d['check']:
        if d['evade'] == 'king': return 'ev_king_cap' if d['cap'] else 'ev_king'
        if d['evade'] == 'take': return 'ev_take'
        if not d['cap']: return 'ev_block'
    if d['check'] and d['run'] >= 3: return 'runcheck'
    if d['check'] and d['cap']: return 'capcheck'
    if d['check']: return 'check'
    if d['qtrade']: return 'qtrade'
    if d['cap'] == 'queen': return 'capq'
    if d['recap']: return 'recap'
    if d['cap']:
        if sport == 'b': return 'cap1' if d['capv'] == 1 else 'cap3' if d['capv'] == 3 else 'cap5'
        return 'cap'
    if d['decline']: return 'decline'
    if d['castle']: return 'castle'
    if d['fork']: return 'fork'
    if d['advanced']: return 'adv7' if d['rel_rank'] == 7 else 'adv6'
    if d['piece'] == 'king': return 'king_end' if endgame else 'king'
    return d['piece']


def cap1(s):
    """Capitalise a sentence, unless it opens with a pawn move like 'e4'."""
    if not s or (len(s) > 1 and s[0] in 'abcdefgh' and s[1] in '12345678x'):
        return s
    return s[0].upper() + s[1:]


def narrate(game, plies, opening):
    """Returns (intro, lines, outro) for each sport: {'s': ..., 'b': ...}."""
    W, Bk = short(game['white']), short(game['black'])
    res = game['result']
    win = W if res == '1-0' else Bk if res == '0-1' else None
    lose = Bk if res == '1-0' else W if res == '0-1' else None
    base = dict(W=W, B=Bk, site=game['site'], year=game['year'], nick=game['nick'], opening=opening, WIN=win, L=lose)
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
            ctx = dict(base, P=P, O=O, PU=P.upper(), san=d['san'], sq=d['to'], frm=d['frm'], pc=d['piece'],
                       pc_c=d['piece'].capitalize(), cap=d['cap'] or '', flank=flank(d), run=d['run'],
                       side='kingside' if d['castle'] == 'K' else 'queenside', offered=d['offered'] or 'piece',
                       promo=d['promo'] or '', qsq=d['qsq'],
                       hp=d['hang'][0] if d['hang'] else '', hsq=d['hang'][1] if d['hang'] else '')
            text = cap1(v.pick(key).format(**ctx))
            if d['i'] == half_at and n >= 30 and not d['mate']:
                bal = d['bal']
                mat = "All square on material." if bal == 0 else f"{W if bal > 0 else Bk} {abs(bal)} {'point' if abs(bal)==1 else 'points'} up on material."
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
                outro = f"Final from {game['site']}: {b2['WIN']} wins it."
            outro += (v.pick('box_irony') if hi < lo else v.pick('box')).format(**b2)
        out[sport] = dict(intro=intro, lines=lines, outro=outro)
    return out
