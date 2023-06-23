function solution(input) {
	const [h, w] = input
		.shift()
		.split(" ")
		.map((e) => parseInt(e));
	const visited = new Array(h).fill(0).map((_) => new Array(w).fill(-1));
	const matrix = input.map((row) => row.split("").map((e) => parseInt(e)));
	const isInside = (y, x) => h > y && y >= 0 && w > x && x >= 0;
	const dxy = [
		[-1, 0],
		[0, 1],
		[1, 0],
		[0, -1],
	];
	const bfs = (y, x) => {
		const queue = [[y, x]];
		visited[y][x] = 1;
		while (queue.length) {
			const [curY, curX] = queue.shift();
			dxy.forEach(([dy, dx]) => {
				const [ny, nx] = [curY + dy, curX + dx];
				if (
					isInside(ny, nx) &&
					visited[ny][nx] === -1 &&
					matrix[ny][nx] === 1
				) {
					queue.push([ny, nx]);
					visited[ny][nx] = visited[curY][curX] + 1;
				}
			});
		}
	};
	bfs(0, 0);
	console.log(visited[h - 1][w - 1]);
}

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
	input.push(line);
}).on("close", () => {
	solution(input);
	process.exit();
});
