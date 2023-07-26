const n = +`${require("fs").readFileSync(0)}`.trim();
let fact = 1n;
for (let i = 1n; i <= n; i++) {
	fact *= i;
}
const divider = 10n;
let cnt = 0;
while (fact % divider === 0n) {
	cnt++;
	fact /= divider;
}
console.log(cnt);
