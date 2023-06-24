const fs = require("fs");

function solution(input) {
	const [h, w] = input.shift().map((e) => parseInt(e));
	const matrix = input.map((row) => row.map((value) => parseInt(value)));
	let [picCnt, largestWidth] = [0, 0];
	const dxy = [
		[1, 0],
		[0, 1],
		[-1, 0],
		[0, -1],
	];
	const isInside = (y, x) => 0 <= y && y < h && 0 <= x && x < w;
	const visited = new Array(h).fill(0).map((_) => new Array(w).fill(false));
	const bfs = (y, x) => {
		const queue = [[y, x]];
		visited[y][x] = true;
		let width = 1;
		while (queue.length) {
			const [curY, curX] = queue.shift();
			dxy.forEach(([dy, dx]) => {
				const [ny, nx] = [curY + dy, curX + dx];
				if (
					isInside(ny, nx) &&
					!visited[ny][nx] &&
					matrix[ny][nx] === 1
				) {
					queue.push([ny, nx]);
					visited[ny][nx] = true;
					width++;
				}
			});
		}
		return width;
	};

	for (let i = 0; i < h; i++) {
		for (let j = 0; j < w; j++) {
			if (matrix[i][j] === 1 && !visited[i][j]) {
				picCnt++;
				const width = bfs(i, j);
				largestWidth = largestWidth < width ? width : largestWidth;
			}
		}
	}
	console.log(picCnt);
	console.log(largestWidth);
}

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
	solution(input);
	process.exit();
});
