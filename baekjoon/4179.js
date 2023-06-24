const logMatrix = (matrix) => {
	matrix.forEach((row) => console.log(...row));
	console.log();
};

class Node {
	constructor(value) {
		this.prev = null;
		this.value = value;
		this.next = null;
	}
}

class Queue {
	constructor() {
		this.head = null;
		this.tail = null;
		this.size = 0;
	}

	push(value) {
		const node = new Node(value);
		if (!this.size) {
			this.head = node;
			this.tail = node;
			this.head.next = this.tail;
			this.tail.prev = this.head;
		} else {
			this.tail.next = node;
			node.prev = this.tail;
			this.tail = node;
		}
		this.size++;
	}

	shift() {
		if (this.head) {
			const tmp = this.head;
			this.head = this.head.next;
			this.size--;
			return tmp.value;
		}
		return null;
	}

	print() {
		let node = this.head;
		const arr = [];
		while (node) {
			arr.push(node);
			node = node.next;
		}
		console.log(JSON.stringify(arr));
	}
}

function solution(input) {
	const [h, w] = input
		.shift()
		.split(" ")
		.map((e) => parseInt(e));
	const matrix = input.map((row) => row.split(""));
	const isInside = (y, x) => h > y && y >= 0 && w > x && x >= 0;
	const dxy = [
		[-1, 0],
		[0, 1],
		[1, 0],
		[0, -1],
	];

	const fire = input.map((row) => row.split("").map((_) => -1)); // 불 전파 시간
	const fireQueue = new Queue();
	const jihoon = structuredClone(fire); // 지훈이 이동 시간
	const jihoonQueue = new Queue();

	for (let i = 0; i < h; i++) {
		for (let j = 0; j < w; j++) {
			if (matrix[i][j] === "F") {
				fireQueue.push([i, j]);
				fire[i][j] = 0;
			} else if (matrix[i][j] === "J") {
				jihoonQueue.push([i, j]);
				jihoon[i][j] = 0;
			}
		}
	}

	while (fireQueue.size) {
		const [cy, cx] = fireQueue.shift();
		for (let i = 0; i < 4; i++) {
			const [dy, dx] = dxy[i];
			const [ny, nx] = [cy + dy, cx + dx];
			if (
				isInside(ny, nx) &&
				fire[ny][nx] === -1 &&
				matrix[ny][nx] !== "#"
			) {
				fireQueue.push([ny, nx]);
				fire[ny][nx] = fire[cy][cx] + 1;
			}
		}
	}

	let answer;

	while (jihoonQueue.size) {
		const [cy, cx] = jihoonQueue.shift();
		for (let i = 0; i < 4; i++) {
			const [dy, dx] = dxy[i];
			const [ny, nx] = [cy + dy, cx + dx];
			if (!isInside(ny, nx)) {
				return jihoon[cy][cx] + 1;
			}
			if (jihoon[ny][nx] !== -1 || matrix[ny][nx] === "#") continue;
			if (fire[ny][nx] !== -1 && fire[ny][nx] <= jihoon[cy][cx] + 1)
				continue;
			jihoonQueue.push([ny, nx]);
			jihoon[ny][nx] = jihoon[cy][cx] + 1;
		}
	}
	return "IMPOSSIBLE";
}

const input = [];
require(`readline`)
	.createInterface(process.stdin, process.stdout)
	.on("line", (line) => {
		input.push(line);
	})
	.on("close", () => {
		console.log(solution(input));
		process.exit();
	});
