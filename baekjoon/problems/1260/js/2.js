const input = `${require("fs").readFileSync(0)}`;

const [[n, m, v], ...edges] = input
	.trim()
	.split("\n")
	.map((row) => row.split(" ").map(Number));

const graph = Array.from(Array(n + 1), () => []);
for (let i = 0; i < m; i++) {
	const [u, v] = edges[i];
	graph[u].push(v);
	graph[v].push(u);
}

graph.forEach((edges) => edges.sort((a, b) => a - b));

const dfsVisited = Array(n + 1).fill(false);
const dfsResult = [];
const dfs = (node) => {
	if (dfsVisited[node]) return;
	dfsVisited[node] = true;
	dfsResult.push(node);
	for (let i = 0; i < graph[node].length; i++) {
		const next = graph[node][i];
		dfs(next);
	}
};
dfs(v);
console.log(...dfsResult);

const bfsVisited = Array(n + 1).fill(false);
const bfsResult = [];
const queue = [v];
bfsVisited[v] = true;
let pointer = 0;
while (pointer < queue.length) {
	const node = queue[pointer++];
	bfsResult.push(node);
	for (let i = 0; i < graph[node].length; i++) {
		const next = graph[node][i];
		if (!bfsVisited[next]) {
			bfsVisited[next] = true;
			queue.push(next);
		}
	}
}

console.log(...bfsResult);
