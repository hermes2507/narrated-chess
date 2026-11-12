/* Bureau for Chess Narration — one hundred historic games, called aloud as sport. */
(() => {
const G = window.GAMES, $ = s => document.querySelector(s);
const content = $('#content'), toc = $('#toc'), menu = $('#menu');
const GLY = { K: '♔', Q: '♕', R: '♖', B: '♗', N: '♘', P: '♙', k: '♚', q: '♛', r: '♜', b: '♝', n: '♞', p: '♟' };
const RES = { '1-0': '1–0', '0-1': '0–1', '1/2-1/2': '½–½' };
const S = { g: null, step: 0, sport: 's', playing: false, speed: 1, voice: false, crowd: false, timer: null, pos: [] };
const pad = n => String(n).padStart(3, '0');
const esc = t => t.replace(/&/g, '&amp;').replace(/</g, '&lt;');

/* ---------- positions: replay the UCI moves once per game */
function positions(g) {
  let pcs = [], id = 0;
  'RNBQKBNR'.split('').forEach((t, f) => {
    pcs.push({ id: id++, t, sq: f }, { id: id++, t: 'P', sq: 8 + f }, { id: id++, t: 'p', sq: 48 + f }, { id: id++, t: t.toLowerCase(), sq: 56 + f });
  });
  const out = [pcs];
  const sq = s => s.charCodeAt(0) - 97 + 8 * (+s[1] - 1);
  for (const p of g.plies) {
    const u = p[1], a = sq(u.slice(0, 2)), b = sq(u.slice(2, 4));
    pcs = pcs.map(x => ({ ...x }));
    const m = pcs.find(x => x.sq === a);
    let victim = pcs.find(x => x.sq === b);
    if (!victim && /p/i.test(m.t) && (a % 8) !== (b % 8)) victim = pcs.find(x => x.sq === (a - a % 8) + b % 8); // en passant
    if (victim) pcs = pcs.filter(x => x !== victim);
    if (/k/i.test(m.t) && Math.abs(a % 8 - b % 8) === 2) {                                                   // castling
      const rook = pcs.find(x => x.sq === (b % 8 === 6 ? a + 3 : a - 4)); rook.sq = b % 8 === 6 ? a + 1 : a - 1;
    }
    m.sq = b;
    if (u[4]) m.t = m.t === 'P' ? u[4].toUpperCase() : u[4];
    out.push(pcs);
  }
  return out;
}

/* ---------- table of contents */
function buildToc(filter = '') {
  const f = filter.toLowerCase();
  toc.innerHTML = G.filter(g => !f || `${g.nick} ${g.white} ${g.black} ${g.site} ${g.year} ${g.author} ${g.opening}`.toLowerCase().includes(f))
    .map(g => `<a class="sub${S.g === g ? ' on' : ''}" href="#${g.id}">${pad(g.id)} ${esc(g.nick)}<small>${esc(g.ws)}–${esc(g.bs)}, ${g.year}</small></a>`).join('');
}
$('#search').addEventListener('input', e => buildToc(e.target.value));
$('#menu-trigger').onclick = () => menu.classList.toggle('is-active');
menu.querySelectorAll('[data-sport]').forEach(a => a.onclick = e => { e.preventDefault(); setSport(a.dataset.sport); });

/* ---------- pages */
function front() {
  stop(); S.g = null; buildToc($('#search').value);
  const g = G[Math.floor(Math.random() * G.length)];
  content.innerHTML = `
  <div class="gap"></div>
  <div class="row"><div class="column"><p>A FRONT PAGE BROADCAST.</p><p>THE SOUND OF A QUEEN BEING LEFT ON f6, CALLED AS A GOAL.</p></div>
    <div class="column"><p><a href="#2">Listen: The Immortal Game, London, 1851.</a></p></div></div>
  <div class="gap"></div>
  <div class="row"><div class="column">
    <p>This is our front page.</p><p>&nbsp;</p><p>We thank you for finding it.</p><p>&nbsp;</p>
    <p>The Bureau narrates historic chess games as if they were sport. A football announcer and a baseball announcer take turns in the booth. Nobody in the booth has been told that it is chess.</p><p>&nbsp;</p>
    <p>We have one hundred ongoing games. Explore them under ‘table of contents’.</p><p>&nbsp;</p>
    <p>Each game has also been written down once, in the manner of a different author, as an exercise in style. The exercises are collected in a book, with the scores set as concrete poetry.</p>
    <p><a href="Play_by_Play.pdf" download>Download the book (PDF, cover to cover, 208 pages).</a></p>
  </div><div class="column"></div></div>
  <div class="gap"></div>
  <h1>Today's fixture</h1>
  <p><a href="#${g.id}">${esc(g.nick)}. ${esc(g.white)} — ${esc(g.black)}, ${esc(g.site)}, ${g.year}.</a></p>
  <div class="gap"></div>
  <h6 class="caption">Shots are checks. Tackles and hits are captures. Possession is mobility. Runs are material. The patter is invented; the moves are not.</h6>
  <div class="gap s"></div>
  <h6 class="caption">Idea and concept by Santiago Rentería, co-created with Claude Code (Claude Fable 5.2). Design after the <a class="u" href="https://bureauforlistening.com">Bureau for Listening</a>. Free to copy and adapt, with credit: book text under <a class="u" href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>, code under the MIT License.</h6>`;
  document.title = 'Bureau for Chess Narration';
}

function gamePage(g) {
  stop(); S.g = g; S.step = 0; S.pos = positions(g); buildToc($('#search').value);
  document.title = `${g.nick} — Bureau for Chess Narration`;
  let sq = '';
  for (let r = 7; r >= 0; r--) for (let f = 0; f < 8; f++) sq += `<div class="${(r + f) % 2 ? '' : 'd'}" data-s="${r * 8 + f}"></div>`;
  content.innerHTML = `
  <h6>Game ${pad(g.id)} — ${esc(g.site)}, ${g.year} — ${esc(g.event)}</h6>
  <h1>${esc(g.nick)}</h1>
  <p>${esc(g.white)} — ${esc(g.black)}. ${esc(g.opening)}. ${RES[g.result]}.</p>
  <div class="gap s"></div>
  <div class="row">
    <div class="column"><div class="figure">
      <div class="board" id="board"><div class="squares">${sq}</div>
        <svg class="lines" viewBox="0 0 80 80"><line x1="0" y1="40" x2="80" y2="40"/><circle cx="40" cy="40" r="11"/><rect x="17" y="0" width="46" height="15"/><rect x="29" y="0" width="22" height="6"/><rect x="17" y="65" width="46" height="15"/><rect x="29" y="74" width="22" height="6"/></svg>
        <div class="bases"><i></i><i></i><i></i><i></i></div><div id="pieces"></div></div>
      <h6 class="caption" id="figcap"></h6>
      <div class="momentum" id="momentum"></div>
      <div class="controls">
        <button id="play">Play</button><button id="back">← Back</button><button id="fwd">Forward →</button><button id="first">From the start</button>
        <button id="speed">Speed 1×</button><button id="voice">Voice: off</button><button id="crowd">Crowd: off</button>
      </div></div></div>
    <div class="column">
      <h6 class="switch"><button data-sp="s">Football</button> / <button data-sp="b">Baseball</button> &nbsp; <span id="stamp"></span></h6>
      <div class="call" id="call"></div>
      <div id="score"></div>
      <div class="transcript" id="transcript"></div>
    </div>
  </div>
  <div class="gap"></div>
  <div class="exercise">
    <h6>Exercise in style No. ${g.id} — the same game, in the manner of ${esc(g.author)}</h6>
    <div class="gap s"></div>
    ${g.exercise.split('\n\n').map(t => `<p>${esc(t)}</p>`).join('')}
    <h6 class="caption">A pastiche written for the Bureau. It may borrow a famous phrase, as parody; it was not written by ${esc(g.author)}. Players' words and thoughts are invented.</h6>
  </div>
  <div class="gap s"></div>
  <p><a href="Play_by_Play.pdf" download>Download the book (PDF, with cover).</a></p>
  <p>${g.id > 1 ? `<a href="#${g.id - 1}">← Previous game</a> &nbsp; ` : ''}${g.id < 100 ? `<a href="#${g.id + 1}">Next game →</a>` : ''}</p>
  <div class="gap"></div>`;
  // momentum bars
  const N = g.plies.length;
  $('#momentum').innerHTML = `<svg viewBox="0 0 ${N} 20" preserveAspectRatio="none">${g.plies.map((p, i) => {
    const h = Math.min(10, .8 + p[5] * .7); return `<rect x="${i + .15}" y="${i % 2 ? 10 : 10 - h}" width=".7" height="${h}" fill="#141414"/>`; }).join('')}</svg><div class="needle"></div>`;
  $('#momentum').onclick = e => { const r = e.currentTarget.getBoundingClientRect(); go(Math.round((e.clientX - r.left) / r.width * N)); };
  $('#play').onclick = toggle; $('#back').onclick = () => { stop(); go(S.step - 1); }; $('#fwd').onclick = () => { stop(); go(S.step + 1); };
  $('#first').onclick = () => { stop(); go(0); };
  $('#speed').onclick = () => { S.speed = { 1: 2, 2: .5, .5: 1 }[S.speed]; ui(); };
  $('#voice').onclick = () => { S.voice = !S.voice; if (!S.voice) speechSynthesis.cancel(); ui(); };
  $('#crowd').onclick = () => { S.crowd = !S.crowd; crowd.set(S.crowd); ui(); };
  content.querySelectorAll('[data-sp]').forEach(b => b.onclick = () => setSport(b.dataset.sp));
  new ResizeObserver(() => $('#board') && $('#board').style.setProperty('--sq', $('#board').clientWidth / 8 + 'px')).observe($('#board'));
  window.scrollTo(0, 0);
  render(false);
}

/* ---------- rendering one step. step 0 = intro, 1..N = plies, N+1 = sign-off */
const maxStep = () => S.g.plies.length + (S.g.outro[S.sport] ? 1 : 0);
function stamp(i, N) {            // i = ply index
  if (S.sport === 's') return Math.max(1, Math.ceil((i + 1) / N * 90)) + "'";
  const inn = Math.min(9, Math.floor(i * 9 / N) + 1); return (i % 2 ? 'Bot ' : 'Top ') + inn;
}
function textAt(step) {
  const g = S.g, N = g.plies.length;
  if (step === 0) return g.intro[S.sport];
  if (step > N) return g.outro[S.sport];
  return g.plies[step - 1][S.sport === 's' ? 6 : 7];
}
function render(animate = true) {
  const g = S.g, N = g.plies.length, k = Math.min(S.step, N), ply = k ? g.plies[k - 1] : null;
  document.body.classList.toggle('baseball', S.sport === 'b');
  // pieces
  const box = $('#pieces'), seen = new Set();
  for (const p of S.pos[k]) {
    let el = box.querySelector(`[data-id="${p.id}"]`);
    if (!el) { el = document.createElement('div'); el.className = 'pc'; el.dataset.id = p.id; el.innerHTML = '<span></span>'; box.appendChild(el); }
    el.classList.remove('gone'); el.firstChild.textContent = GLY[p.t] + '︎';
    el.style.left = (p.sq % 8) * 12.5 + '%'; el.style.top = (7 - (p.sq >> 3)) * 12.5 + '%';
    seen.add(String(p.id));
  }
  box.querySelectorAll('.pc').forEach(el => { if (!seen.has(el.dataset.id)) el.classList.add('gone'); });
  // highlights
  content.querySelectorAll('.squares div').forEach(d => d.classList.remove('hl', 'chk'));
  if (ply) {
    const sq = s => s.charCodeAt(0) - 97 + 8 * (+s[1] - 1);
    [ply[1].slice(0, 2), ply[1].slice(2, 4)].forEach(s => content.querySelector(`[data-s="${sq(s)}"]`).classList.add('hl'));
    if (ply[2].includes('c')) { const kg = S.pos[k].find(p => p.t === (k % 2 ? 'k' : 'K')); content.querySelector(`[data-s="${kg.sq}"]`).classList.add('chk'); }
  }
  // stats so far
  const st = { sh: [0, 0], tk: [0, 0], runs: [Array(9).fill(0), Array(9).fill(0)] };
  for (let i = 0; i < k; i++) { const p = g.plies[i], c = i % 2; if (p[2].includes('c')) st.sh[c]++; if (p[3]) { st.tk[c]++; st.runs[c][Math.min(8, Math.floor(i * 9 / N))] += p[3]; } }
  const over = S.step >= N && (ply && ply[2].includes('m') || S.step > N || !g.outro[S.sport]);
  const won = over ? (g.result === '1-0' ? 0 : g.result === '0-1' ? 1 : -1) : -1;
  $('#figcap').textContent = `Fig. ${g.id}. ` + (k ? `Position after ${Math.ceil(k / 2)}${k % 2 ? '.' : '…'}${ply[0]}` : 'The teams line up') + `. ${S.sport === 's' ? 'A football pitch' : 'A baseball diamond'}, seen from above.`;
  $('#stamp').textContent = k ? `— ${stamp(k - 1, N)}${over ? ' — final' : ''}` : '— before the start';
  if (S.sport === 's') {
    const poss = ply ? ply[4] : 50;
    $('#score').innerHTML = `<table class="sb"><tr><th></th><th>Goals</th><th>Possession</th><th>Shots on target</th><th>Tackles won</th></tr>` +
      [0, 1].map(c => `<tr><td>${esc(c ? g.bs : g.ws)}</td><td>${won === c ? 1 : 0}</td><td>${c ? 100 - poss : poss}%</td><td>${st.sh[c]}</td><td>${st.tk[c]}</td></tr>`).join('') + `</table>`;
  } else {
    const inn = k ? Math.min(8, Math.floor((k - 1) * 9 / N)) : -1;
    $('#score').innerHTML = `<table class="sb"><tr><th></th>${[1,2,3,4,5,6,7,8,9].map(n => `<th>${n}</th>`).join('')}<th>R</th><th>H</th><th>K</th><th></th></tr>` +
      [0, 1].map(c => `<tr><td>${esc(c ? g.bs : g.ws)}</td>${st.runs[c].map((r, n) => `<td class="${n === inn ? 'now' : ''}">${n <= inn ? r : ''}</td>`).join('')}<td>${st.runs[c].reduce((a, b) => a + b, 0)}</td><td>${st.tk[c]}</td><td>${st.sh[c]}</td><td>${won === c ? 'W' : ''}</td></tr>`).join('') +
      `</table><h6 class="caption">R: material won. H: captures. K: checks. W: the king, which is the only thing that counts.</h6>`;
  }
  // the call
  const text = textAt(S.step), parts = text.split('\n');
  const loud = ply && S.step <= N && /[mq]/.test(ply[2]);
  $('#call').innerHTML = parts.map((t, i) => `<p class="${i ? 'aside' : loud ? 'loud' : ''}">${esc(t)}</p>`).join('');
  // transcript (most recent first)
  let tr = '';
  for (let s = Math.min(S.step - 1, N); s >= 1 && s > S.step - 40; s--) {
    const p = g.plies[s - 1]; tr += `<button data-step="${s}"><span>${stamp(s - 1, N)}</span><span>${Math.ceil(s / 2)}${s % 2 ? '.' : '…'}${p[0]}</span><span>${esc(p[S.sport === 's' ? 6 : 7].split('\n')[0])}</span></button>`;
  }
  $('#transcript').innerHTML = tr;
  $('#transcript').querySelectorAll('button').forEach(b => b.onclick = () => { stop(); go(+b.dataset.step); });
  // momentum
  $('#momentum').querySelectorAll('rect').forEach((r, i) => r.classList.toggle('future', i >= k));
  $('#momentum .needle').style.left = k / N * 100 + '%';
  ui();
  if (animate && ply && S.step <= N) crowd.roar(ply[5]);
  if (animate && S.voice) say(text, ply);
}
function ui() {
  if (!S.g) return;
  $('#play').textContent = S.playing ? 'Pause' : (S.step >= maxStep() ? 'Play again' : 'Play');
  $('#speed').textContent = `Speed ${S.speed}×`; $('#voice').textContent = `Voice: ${S.voice ? 'on' : 'off'}`; $('#crowd').textContent = `Crowd: ${S.crowd ? 'on' : 'off'}`;
  content.querySelectorAll('[data-sp]').forEach(b => b.classList.toggle('on', b.dataset.sp === S.sport));
  menu.querySelectorAll('[data-sport]').forEach(a => a.classList.toggle('on', a.dataset.sport === S.sport));
}
function go(step) { S.step = Math.max(0, Math.min(maxStep(), step)); render(true); }
function setSport(sp) { S.sport = sp; if (S.g) { S.step = Math.min(S.step, maxStep()); render(false); } else { document.body.classList.toggle('baseball', sp === 'b'); ui(); menu.querySelectorAll('[data-sport]').forEach(a => a.classList.toggle('on', a.dataset.sport === sp)); } }

/* ---------- playback */
function toggle() { S.playing ? stop() : start(); }
function start() { if (S.step >= maxStep()) S.step = 0, render(false); S.playing = true; ui(); if (S.step === 0) { render(true); wait(); } else advance(); }
function stop() { S.playing = false; clearTimeout(S.timer); if (window.speechSynthesis) speechSynthesis.cancel(); if (S.g && $('#play')) ui(); }
function advance() { if (!S.playing) return; if (S.step >= maxStep()) return stop(); go(S.step + 1); wait(); }
function wait() {
  const len = textAt(S.step).length;
  if (S.voice && window.speechSynthesis) { S.onend = () => { S.timer = setTimeout(advance, 350 / S.speed); }; S.timer = setTimeout(advance, 20000); }  // safety net
  else S.timer = setTimeout(advance, (900 + len * 42) / S.speed);
}

/* ---------- the announcer (browser speech) */
const SPOKEN = { K: 'king', Q: 'queen', R: 'rook', B: 'bishop', N: 'knight' };
function sayMove(san) {
  if (san.startsWith('O-O-O')) return 'castles long'; if (san.startsWith('O-O')) return 'castles';
  let s = san.replace(/[+#]/g, '').replace(/=([QRBN])/, (_, p) => ' promotes to ' + SPOKEN[p]).replace('x', ' takes ');
  return s.replace(/^[KQRBN]/, m => SPOKEN[m] + ' ');
}
function say(text, ply) {
  if (!window.speechSynthesis) return;
  speechSynthesis.cancel();
  let t = text.replace(/\n/g, ' ');
  if (ply) t = t.split(ply[0]).join(sayMove(ply[0]));
  t = t.replace(/GO{3,}L/g, 'GOAL').replace(/([A-Za-z])\1{3,}/g, '$1$1');
  const u = new SpeechSynthesisUtterance(t), vs = speechSynthesis.getVoices();
  const want = S.sport === 's' ? ['en-GB', 'en-IE', 'en-AU'] : ['en-US'];
  u.voice = vs.find(v => want.includes(v.lang) && /Daniel|Fred|Alex|Google/.test(v.name)) || vs.find(v => want.includes(v.lang)) || null;
  u.rate = (S.sport === 's' ? 1.12 : .96) * Math.min(1.6, Math.max(.8, S.speed)); u.pitch = S.sport === 's' ? 1.1 : .85;
  u.onend = () => { if (S.playing && S.onend) { clearTimeout(S.timer); const f = S.onend; S.onend = null; f(); } };
  speechSynthesis.speak(u);
}

/* ---------- a crowd that is not there (filtered noise, swelling with the game) */
const crowd = {
  ctx: null, gain: null,
  set(on) {
    if (on && !this.ctx) {
      const c = this.ctx = new (window.AudioContext || window.webkitAudioContext)();
      const buf = c.createBuffer(1, c.sampleRate * 4, c.sampleRate), d = buf.getChannelData(0);
      let last = 0; for (let i = 0; i < d.length; i++) { last = (last + .02 * (Math.random() * 2 - 1)) / 1.02; d[i] = last * 3.5; }
      const src = c.createBufferSource(); src.buffer = buf; src.loop = true;
      const bp = c.createBiquadFilter(); bp.type = 'bandpass'; bp.frequency.value = 700; bp.Q.value = .5;
      this.gain = c.createGain(); this.gain.gain.value = 0;
      src.connect(bp).connect(this.gain).connect(c.destination); src.start();
    }
    if (this.ctx) { this.ctx.resume(); this.gain.gain.setTargetAtTime(on ? .12 : 0, this.ctx.currentTime, .3); }
  },
  roar(ex) {
    if (!S.crowd || !this.ctx) return;
    const t = this.ctx.currentTime, peak = Math.min(1, .12 + ex * .07);
    this.gain.gain.cancelScheduledValues(t); this.gain.gain.setTargetAtTime(peak, t, .08); this.gain.gain.setTargetAtTime(.12, t + .6 + ex * .12, .9);
  }
};

/* ---------- routing and keys */
function route() { const id = +location.hash.slice(1); menu.classList.remove('is-active'); (id >= 1 && id <= G.length) ? gamePage(G[id - 1]) : front(); }
addEventListener('hashchange', route);
addEventListener('keydown', e => {
  if (e.target.tagName === 'INPUT' || !S.g) return;
  if (e.key === ' ') { e.preventDefault(); toggle(); }
  else if (e.key === 'ArrowRight') { stop(); go(S.step + 1); }
  else if (e.key === 'ArrowLeft') { stop(); go(S.step - 1); }
  else if (e.key.toLowerCase() === 's') setSport(S.sport === 's' ? 'b' : 's');
});
menu.querySelector('[data-sport="s"]').classList.add('on');
route();
})();
