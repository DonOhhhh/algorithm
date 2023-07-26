const [[n, m], ...ops] = `${require("fs").readFileSync(0)}`.trim().split`
`.map((row) => row.trim().split` `.map((e) => (!isNaN(+e) ? +e : e)));
const [a, b] = [ops.slice(0, n), ops.slice(n)];
const SIZE = 1000001;
const time1 = new Array(SIZE).fill(0);
const time2 = new Array(SIZE).fill(0);
let offset = 0;
for (const [t, d] of a) {
	for (let i = 1; i <= t; i++) {
		time1[offset + i] = time1[offset + i - 1] + (d === "R" ? 1 : -1);
	}
	offset += t;
}
time1.fill(time1[offset], offset + 1);
offset = 0;
for (const [t, d] of b) {
	for (let i = 1; i <= t; i++) {
		time2[offset + i] = time2[offset + i - 1] + (d === "R" ? 1 : -1);
	}
	offset += t;
}
time2.fill(time2[offset], offset + 1);
// console.log(time1.lastIndexOf(0));
// console.log(time2.slice(0, 168).join(" "));
let prevSign = Math.sign(time1[1] - time2[1]);
let cnt = 0;
for (let i = 1; i <= SIZE; i++) {
	const curSign = Math.sign(time1[i] - time2[i]);
	// console.log({ i, prevSign, curSign, cnt });
	if (curSign === 0 && prevSign !== curSign) {
		cnt++;
	}
	prevSign = curSign;
}
console.log(cnt);
