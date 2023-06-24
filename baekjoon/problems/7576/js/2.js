const fs = require("fs");

const inputs = fs.readFileSync("/dev/stdin").toString().split("\n");
let cursor = 0;
const outputs = [];

const [m, n] = inputs[cursor++].split(" ").map(Number);

const field = inputs.slice(cursor).map((input) => input.split(" ").map(Number));

const q = [];

for (let y = 0; y < n; y++) {
	for (let x = 0; x < m; x++) {
		if (field[y][x] === 1) {
			q.push(x, y);
		}
	}
}

let result = 0;

const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

for (let i = 0, days = 1; i < q.length; days++) {
	for (const { length } = q; i < length; ) {
		const ox = q[i++];
		const oy = q[i++];

		for (let j = 0; j < 4; j++) {
			const x = ox + dx[j];
			const y = oy + dy[j];

			if (x < 0 || x >= m || y < 0 || y >= n) continue;
			if (field[y][x] !== 0) continue;

			field[y][x] = 1;
			result = days;

			q.push(x, y);
		}
	}
}

for (let y = 0; y < n; y++) {
	for (let x = 0; x < m; x++) {
		if (field[y][x] === 0) result = -1;
	}
}

outputs.push(result);

fs.writeFileSync("/dev/stdout", outputs.join("\n"));
