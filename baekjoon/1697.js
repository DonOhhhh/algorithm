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
		if (this.size) {
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
	const [n, k] = input.split(" ").map((e) => parseInt(e));
	if (n === k) return 0;
	const arr = new Array(200000).fill(0);
	const dx = [(x) => x + 1, (x) => x - 1, (x) => x * 2];
	const isInside = (x) => arr.length > x && x >= 0;
	const bfs = () => {
		const queue = new Queue();
		const visited = new Array(arr.length).fill(false);
		const elapsedTime = new Array(arr.length).fill(0);
		queue.push(n);
		while (queue.size) {
			const cx = queue.shift();
			dx.forEach((dx) => {
				const nx = dx(cx);
				if (isInside(nx) && !visited[nx]) {
					queue.push(nx);
					visited[nx] = true;
					elapsedTime[nx] = elapsedTime[cx] + 1;
				}
			});
		}
		return elapsedTime;
	};
	const timeMatrix = bfs();
	return timeMatrix[k];
}

let input;
require("readline")
	.createInterface(process.stdin, process.stdout)
	.on("line", (line) => {
		input = line;
	})
	.on("close", () => {
		console.log(solution(input));
		process.exit();
	});
