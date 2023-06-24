// 여러 줄 입력
const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
	input.push(line);
}).on("close", () => {
	input.forEach((e) => {
		if (e === ".") return;
		const stack = [];
		const words = Array.from(e);
		let flag = true;
		for (const word of words) {
			if (word === "(" || word === "[") {
				stack.push(word);
			} else if (word === ")" || word === "]") {
				const tmp = stack.pop();
				if (
					!(
						(tmp === "(" && word === ")") ||
						(tmp === "[" && word === "]")
					)
				) {
					flag = false;
					break;
				}
			}
		}
		console.log(flag && !stack.length ? "yes" : "no");
	});
	process.exit();
});
