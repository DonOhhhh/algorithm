const N = +`${require("fs").readFileSync(0)}`.trim();

function hanoi(N, start, end, via) {
	if (N === 1) return `${start} ${end}\n`;
	return `${hanoi(N - 1, start, via, end)}${start} ${end}\n${hanoi(
		N - 1,
		via,
		end,
		start
	)}`;
}

console.log((1 << N) - 1);
console.log(hanoi(N, 1, 3, 2).trim());
