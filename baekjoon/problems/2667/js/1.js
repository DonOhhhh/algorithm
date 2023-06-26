const input = `${require("fs").readFileSync(0)}`.trim().split("\n");

const n = Number(input.shift());
const matrix = input.map((row) => row.split("").map(Number));

const isInside = (y, x) => n > y && y >= 0 && n > x && x >= 0;
const dxy = [
	[-1, 0],
	[0, 1],
	[1, 0],
	[0, -1],
];
const visited = Array.from(Array(n + 1), () => Array(n + 1).fill(false));

const dfs = (coord) => {
	const stack = [coord];
	visited[coord[0]][coord[1]] = true;
	let width = 1;
	while (stack.length) {
		const [cy, cx] = stack.pop();
		dxy.forEach(([dy, dx]) => {
			const [ny, nx] = [cy + dy, cx + dx];
			if (isInside(ny, nx) && !visited[ny][nx] && matrix[ny][nx] !== 0) {
				visited[ny][nx] = true;
				stack.push([ny, nx]);
				width++;
			}
		});
	}
	return width;
};

const result = [];

for (let i = 0; i < n; i++) {
	for (let j = 0; j < n; j++) {
		if (matrix[i][j] !== 0 && !visited[i][j]) {
			result.push(dfs([i, j]));
		}
	}
}

console.log(result.length);
if (result.length) result.sort((a, b) => a - b).forEach((e) => console.log(e));
