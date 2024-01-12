const x = +`${require("fs").readFileSync(0)}`.trim();
const LIMIT = 10000;
let min = Infinity;
for (let i = 1; i <= LIMIT; i++) {
	let [d, v, t] = [0, 0, 0];
	while (d < x) {
		if (x - d < (v * (v + 1)) / 2) v--;
		if (t < i) v++;
		d += v;
		t++;
	}
	if (d === x && v === 1) min = Math.min(min, t);
}
console.log(min);
/*
즉, 남은 거리가 v * (v + 1) / 2 보다 크거나 같다면, 속도를 유지
*/
