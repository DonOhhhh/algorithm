const [[M, N], ...a] = `${require("fs").readFileSync(0)}`.split`
`.map((n) => n.split` `.map(Number));
const m = a.flat();
m.length = M * N;

let q = [];
for (let i = 0; i < m.length; i++) if (m[i] === 1) q.push(i);

let d = -1;
while (q.length) {
	for (let ii = 0; ii < q.length; ii++) m[q[ii]] = 1;
	const s = new Set();
	for (let ii = 0; ii < q.length; ii++) {
		const i = q[ii];
		const y = (i / M) | 0;
		const x = i % M;
		if (y - 1 >= 0 && m[i - M] === 0) s.add(i - M);
		if (y + 1 < N && m[i + M] === 0) s.add(i + M);
		if (x - 1 >= 0 && m[i - 1] === 0) s.add(i - 1);
		if (x + 1 < M && m[i + 1] === 0) s.add(i + 1);
	}
	q = [...s];
	d++;
}
console.log(m.some((o) => o === 0) ? -1 : d);
