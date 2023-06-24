const { log } = require("console");

function solution(input) {
	input = input.trim().split("\n");
	const [h, w] = input.shift().split(" ").map(Number);
	const matrix = input.map((row) => row.split(""));
	const isInside = (y, x) => h > y && y >= 0 && w > x && x >= 0;
	const [dy, dx] = [
		[1, 0, -1, 0],
		[0, 1, 0, -1],
	];
	const findLoc = (alpha) =>
		matrix
			.flatMap((row, i) =>
				row.map((value, j) => (value === alpha ? [i, j] : null))
			)
			.filter((e) => e);
	const fireQueue = findLoc("F");
	const fireMatrix = new Array(h).fill().map((_) => new Array(w).fill(-1));
	fireQueue.forEach(([i, j]) => {
		fireMatrix[i][j] = 0;
	});

	let pointer = 0;
	while (pointer < fireQueue.length) {
		const [cy, cx] = fireQueue[pointer++];
		for (let i = 0; i < 4; i++) {
			const [ny, nx] = [cy + dy[i], cx + dx[i]];
			if (
				!isInside(ny, nx) ||
				fireMatrix[ny][nx] !== -1 ||
				matrix[ny][nx] === "#"
			)
				continue;
			fireQueue.push([ny, nx]);
			fireMatrix[ny][nx] = fireMatrix[cy][cx] + 1;
		}
	}

	const jihoonQueue = findLoc("J");
	const jihoonMatrix = new Array(h).fill().map((_) => new Array(w).fill(-1));
	jihoonQueue.forEach(([i, j]) => {
		jihoonMatrix[i][j] = 0;
	});

	pointer = 0;
	while (pointer < jihoonQueue.length) {
		const [cy, cx] = jihoonQueue[pointer++];
		for (let i = 0; i < 4; i++) {
			const [ny, nx] = [cy + dy[i], cx + dx[i]];
			if (!isInside(ny, nx)) {
				return jihoonMatrix[cy][cx] + 1;
			}
			if (
				matrix[ny][nx] === "#" ||
				jihoonMatrix[ny][nx] !== -1 ||
				jihoonMatrix[cy][cx] + 1 >= fireMatrix[ny][nx]
			)
				continue;
			jihoonQueue.push([ny, nx]);
			jihoonMatrix[ny][nx] = jihoonMatrix[cy][cx] + 1;
		}
	}

	return "IMPOSSIBLE";
}

const input = `${require("fs").readFileSync(0)}`;
log(solution(input));
