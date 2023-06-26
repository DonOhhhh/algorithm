const [a, b, c] = `${require("fs").readFileSync(0)}`
	.trim()
	.split(" ")
	.map(BigInt);

function pow(b) {
	if (b === 1n) return a % c;
	let val = pow(b / 2n);
	val = (val * val) % c;
	if (b % 2n === 0n) return val;
	return (val * (a % c)) % c;
}

console.log(parseInt(pow(b)));
