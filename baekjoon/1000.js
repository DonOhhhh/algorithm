const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

let input;

rl.on("line", (line) => {
	input = line;
}).on("close", () => {
	const [a, b] = input.split(" ").map((e) => parseInt(e));
	console.log(a + b);
	process.exit();
});
