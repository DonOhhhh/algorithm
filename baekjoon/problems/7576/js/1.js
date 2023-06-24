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

	push(element) {
		const node = new Node(element);
		if (!this.size) {
			this.head = node;
			this.head.next = this.tail;
			this.tail = node;
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
		const arr = [];
		let node = this.head;
		while (node) {
			arr.push(node.value);
			node = node.next;
		}
		console.log(JSON.stringify(arr));
	}
}

function solution(input) {
	const [w, h] = input.shift();
	const matrix = input;
	const dxy = [
		[-1, 0],
		[0, 1],
		[1, 0],
		[0, -1],
	];
	let days = 1;
	const isInside = (y, x) => h > y && y >= 0 && w > x && x >= 0;
	const bfs = () => {
		const queue = new Queue();
		matrix
			.flatMap((row, i) =>
				row
					.map((tomato, j) => (tomato === 1 ? [i, j] : false))
					.filter((e) => e)
			)
			.forEach((e) => queue.push(e));
		while (queue.size) {
			const [cy, cx] = queue.shift();
			dxy.forEach(([dy, dx]) => {
				const [ny, nx] = [cy + dy, cx + dx];
				if (isInside(ny, nx) && matrix[ny][nx] === 0) {
					queue.push([ny, nx]);
					matrix[ny][nx] = matrix[cy][cx] + 1;
					days = matrix[ny][nx] > days ? matrix[ny][nx] : days;
				}
			});
		}
	};

	bfs();
	const result = matrix.flatMap((e) => e).includes(0) ? -1 : days - 1;
	console.log(result);
}

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

const input = [];

rl.on("line", (line) => {
	input.push(line.split(" ").map((e) => parseInt(e)));
}).on("close", () => {
	solution(input);
	process.exit();
});
