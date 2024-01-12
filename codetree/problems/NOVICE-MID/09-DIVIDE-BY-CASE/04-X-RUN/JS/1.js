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
		this.length = 0;
	}

	push(value) {
		const node = new Node(value);
		if (!this.tail) {
			this.head = node;
			this.tail = node;
			this.head.next = this.tail;
			this.tail.prev = this.head;
		} else {
			node.prev = this.tail;
			this.tail.next = node;
			this.tail = node;
		}
		this.length++;
	}

	shift() {
		if (this.head) {
			let tmp = this.head;
			this.head = this.head.next;
			this.length--;
			return tmp.value;
		}
		return null;
	}

	print() {
		let node = this.head;
		let values = [];
		while (node) {
			values.push(node.value);
			node = node.next;
		}
		console.log(values.join` `);
	}
}

const x = +`${require("fs").readFileSync(0)}`.trim();
const dvs = [-1, 0, 1];
const visited = [];
let min = Infinity;
const bfs = (d, v, t) => {
	const queue = [];
	queue.push([d, v, t]);
	while (queue.length) {
		const [cd, cv, ct] = queue.shift();
		for (const dv of dvs) {
			let nv = cv + dv;
			let nd = cd + nv;
			let nt = ct + 1;
			if (nd === x && nv === 1) {
				min = Math.min(min, nt);
				break;
			}
			if (
				!visited.includes(JSON.stringify([nd, nv, nt])) &&
				nv > 0 &&
				nd < x
			) {
				queue.push([nd, nv, nt]);
				visited.push(JSON.stringify([nd, nv, nt]));
				// console.log({ t: nt, d: nd, v: nv, min })
			}
		}
	}
};
bfs(0, 0, 0);
console.log(min);
