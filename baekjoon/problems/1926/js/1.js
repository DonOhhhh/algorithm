const [[h, w], ...matrix] = `${require("fs").readFileSync(0)}`.trim().split`
`.map((row) => row.split` `.map(Number));

const isInside = (y, x) => h > y && y >= 0 && w > x && x >= 0;
const dxy = [
	[-1, 0],
	[0, 1],
	[1, 0],
	[0, -1],
];

const visited = new Array(h).fill(0).map((_) => new Array(w).fill(false));
const bfs = (y, x) => {
	const queue = [[y, x]];
	visited[y][x] = true;
	let width = 1;
	let pointer = 0;
	while (pointer < queue.length) {
		const [cy, cx] = queue[pointer++];
		dxy.forEach(([dy, dx]) => {
			const [ny, nx] = [cy + dy, cx + dx];
			if (isInside(ny, nx) && !visited[ny][nx] && matrix[ny][nx] === 1) {
				queue.push([ny, nx]);
				visited[ny][nx] = true;
				width++;
			}
		});
	}
	return width;
};

let totalPicture = 0,
	maxWidth = 0;

for (let i = 0; i < h; i++) {
	for (let j = 0; j < w; j++) {
		if (matrix[i][j] === 1 && !visited[i][j]) {
			totalPicture++;
			const tmpWidth = bfs(i, j);
			maxWidth = maxWidth > tmpWidth ? maxWidth : tmpWidth;
		}
	}
}

console.log(totalPicture);
console.log(maxWidth);
