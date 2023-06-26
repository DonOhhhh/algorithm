const input = `${require("fs").readFileSync(0)}`.split`
`.map((row) => row.split` `.map(Number));

const [tc] = input.shift();
const dxy = [
	[-1, 0],
	[0, 1],
	[1, 0],
	[0, -1],
];

for (let i = 0; i < tc; i++) {
	const [w, h, k] = input.shift();
	const edges = input.splice(0, k);
	const matrix = Array(h)
		.fill()
		.map((_) => Array(w).fill(0));
	edges.forEach(([x, y]) => (matrix[y][x] = 1));
	const visited = Array(h)
		.fill()
		.map((_) => Array(w).fill(0));
	const isInside = (y, x) => h > y && y >= 0 && w > x && x >= 0;
	const isCabbage = (y, x) => matrix[y][x] === 1;
	const dfs = (y, x) => {
		const stack = [[y, x]];
		visited[y][x] = 1;
		while (stack.length) {
			const [cy, cx] = stack.pop();
			dxy.forEach(([dy, dx]) => {
				const [ny, nx] = [cy + dy, cx + dx];
				if (isInside(ny, nx) && !visited[ny][nx] && isCabbage(ny, nx)) {
					visited[ny][nx] = true;
					stack.push([ny, nx]);
				}
			});
		}
	};
	let cnt = 0;
	for (let i = 0; i < h; i++) {
		for (let j = 0; j < w; j++) {
			if (!visited[i][j] && isCabbage(i, j)) {
				dfs(i, j);
				cnt++;
			}
		}
	}
	console.log(cnt);
}
