const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m, v] = input[0].split(" ").map(Number);
const graph = Array.from(Array(n + 1), () => []);
for (let i = 1; i <= m; i++) {
	const [u, v] = input[i].split(" ").map(Number);
	graph[u].push(v);
	graph[v].push(u);
}

graph.forEach((edges) => edges.sort((a, b) => a - b));

const dfsVisited = Array(n + 1).fill(false);
const dfsResult = [];
const dfs = (node) => {
	dfsVisited[node] = true;
	dfsResult.push(node);
	for (let i = 0; i < graph[node].length; i++) {
		const next = graph[node][i];
		if (!dfsVisited[next]) {
			dfs(next);
		}
	}
};

dfs(v);
console.log(dfsResult.join(" "));

const bfsVisited = Array(n + 1).fill(false);
const bfsResult = [];
const queue = [v];
bfsVisited[v] = true;
while (queue.length) {
	const node = queue.shift();
	bfsResult.push(node);
	for (let i = 0; i < graph[node].length; i++) {
		const next = graph[node][i];
		if (!bfsVisited[next]) {
			bfsVisited[next] = true;
			queue.push(next);
		}
	}
}

console.log(bfsResult.join(" "));
