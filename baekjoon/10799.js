// 여러 줄 입력
const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

let input;

rl.on("line", (line) => {
	input = line;
}).on("close", () => {
	const bar = input.split("");
	let [ans, cnt] = [0, 0];
	for (let i = 0; i < bar.length; i++) {
		if (bar[i] === "(") cnt++;
		if (bar[i] === ")") {
			cnt--;
			if (bar[i - 1] === "(") ans += cnt;
			if (bar[i - 1] === ")") ans++;
		}
	}
	console.log(ans);
	process.exit();
});
