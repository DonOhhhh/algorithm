const fs = require("fs");
const input = +fs.readFileSync("/dev/stdin").toString().trim();
let output = "";

const hanoi = (n, start, end) => {
	if (n === 1) output += start + " " + end + "\n";
	else {
		hanoi(n - 1, start, 6 - start - end);
		output += start + " " + end + "\n";
		hanoi(n - 1, 6 - start - end, end);
	}
};

output += `${2 ** input - 1}\n`;
hanoi(input, 1, 3);

console.log(output);
