// 여러 줄 입력
const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

let input;

rl.on("line", (line) => {
	input = line.split("");
}).on("close", () => {
	const convert = {
		"(": 2,
		")": 2,
		"[": 3,
		"]": 3,
	};
	let [ans, tmp] = [0, 1];
	const stack = [];
	let flag = true;
	for (let i = 0; i < input.length; i++) {
		// console.log(stack, ans, tmp);
		switch (input[i]) {
			case "(":
			case "[":
				tmp *= convert[input[i]];
				stack.push(input[i]);
				break;
			case ")":
				if (!stack.length || stack.at(-1) !== "(") {
					ans = 0;
					flag = false;
					break;
				}
				if (input[i - 1] === "(") {
					ans += tmp;
				}
				tmp /= convert[input[i]];
				stack.pop();
				break;
			case "]":
				if (!stack.length || stack.at(-1) !== "[") {
					ans = 0;
					flag = false;
					break;
				}
				if (input[i - 1] === "[") {
					ans += tmp;
				}
				tmp /= convert[input[i]];
				stack.pop();
				break;
		}
		if (!flag) break;
	}
	if (stack.length) ans = 0;
	console.log(ans);
	process.exit();
});
