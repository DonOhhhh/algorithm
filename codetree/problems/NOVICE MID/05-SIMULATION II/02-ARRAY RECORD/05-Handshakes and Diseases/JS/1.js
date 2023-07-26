// n : 개발자의 수
// k : 최대 전염횟수
// p : 제일 처음 전염병에 걸려있는 개발자의 번호
const [[n, k, p, t], ...handshakes] = `${require("fs").readFileSync(0)}`.trim()
	.split`
`.map((row) => row.trim().split` `.map(Number));
handshakes.sort((a, b) => a[0] - b[0]);
// handshakes.forEach((row) => console.log(...row));
const developers = new Array(n + 1).fill(0);
developers[p] = 1;
const infectionLeft = new Array(n + 1).fill(k);
// x가 y에게 전염병을 옮긴다.
// y도 x에게 전염병을 옮길 수 있다.
for (const [t, x, y] of handshakes) {
	const [dx, dy, ix, iy] = [
		developers[x],
		developers[y],
		infectionLeft[x],
		infectionLeft[y],
	];
	if (dx && ix) {
		developers[y] = 1;
		infectionLeft[x]--;
	}
	if (dy && iy) {
		developers[x] = 1;
		infectionLeft[y]--;
	}
	// console.log({ x, y });
	// console.log(developers.slice(1).join(""));
}
console.log(developers.slice(1).join(""));
