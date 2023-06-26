const input = `${require("fs").readFileSync(0)}`.trim().split`
`.map((row) => row.split(" ").map(Number));

const dxy = [
	[-1, -1],
	[-1, 0],
	[-1, 1],
	[0, 1],
	[1, 1],
	[1, 0],
	[1, -1],
	[0, -1],
];

while (true) {
	const [w, h] = input.shift();
	if (h === 0) break;
	const matrix = input.splice(0, h);
	const isInside = (y, x) => h > y && y >= 0 && w > x && x >= 0;
	const isLand = (y, x) => matrix[y][x] === 1;
	const visited = Array(h)
		.fill()
		.map((_) => Array(w).fill(0));
	const dfs = (y, x) => {
		const stack = [[y, x]];
		visited[y][x] = 1;
		while (stack.length) {
			const [cy, cx] = stack.pop();
			dxy.forEach(([dy, dx]) => {
				const [ny, nx] = [cy + dy, cx + dx];
				if (isInside(ny, nx) && !visited[ny][nx] && isLand(ny, nx)) {
					visited[ny][nx] = 1;
					stack.push([ny, nx]);
				}
			});
		}
	};

	let islands = 0;

	for (let i = 0; i < h; i++) {
		for (let j = 0; j < w; j++) {
			if (isLand(i, j) && !visited[i][j]) {
				dfs(i, j);
				islands++;
			}
		}
	}
	console.log(islands);
}
