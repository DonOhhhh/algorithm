const [[w, h], ...matrix] = `${require("fs").readFileSync(0)}`
	.trim()
	.split("\n")
	.map((row) => row.split(" ").map(Number));

const isInside = (y, x) => h > y && y >= 0 && w > x && x >= 0;
const dxy = [
	[-1, 0],
	[0, 1],
	[1, 0],
	[0, -1],
];
const queue = matrix
	.flatMap((row, i) => row.map((value, j) => (value === 1 ? [i, j] : null)))
	.filter((coord) => coord);

let days = 0;
let pointer = 0;
while (pointer < queue.length) {
	const [cy, cx] = queue[pointer++];
	dxy.forEach(([dy, dx]) => {
		const [ny, nx] = [cy + dy, cx + dx];
		if (isInside(ny, nx) && matrix[ny][nx] === 0) {
			queue.push([ny, nx]);
			matrix[ny][nx] = matrix[cy][cx] + 1;
			if (matrix[cy][cx] > days) days = matrix[cy][cx];
		}
	});
}

console.log(matrix.flat().includes(0) ? -1 : days);
