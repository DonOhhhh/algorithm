// 여러 줄 입력
const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
	input.push(line.split(" "));
}).on("close", () => {
	process.exit();
});
