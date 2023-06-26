const [[n, m], ...edges] = `${require("fs").readFileSync(0)}`
	.trim()
	.split("\n")
	.map((row) => row.split(" ").map(Number));

const graph = [...Array(n + 1)].map((_) => []);
edges.forEach(([s, e]) => {
	graph[s].push(e);
	graph[e].push(s);
});

const visited = Array(n + 1).fill(false);
const dfs = (node) => {
	if (visited[node]) return;
	visited[node] = true;
	graph[node].forEach((e) => dfs(e));
};

let ccNum = 0;

for (let i = 1; i <= n; i++) {
	if (!visited[i]) {
		dfs(i);
		ccNum++;
	}
}

console.log(ccNum);
