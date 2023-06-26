const input = `${require("fs").readFileSync(0)}`
	.trim()
	.split("\n")
	.map((e) => e.split(" ").map(Number));

const [n] = input.shift();
const [m] = input.shift();

const graph = [...Array(n + 1)].map((e) => []);

input.forEach(([s, e]) => {
	graph[s].push(e);
	graph[e].push(s);
});

const visited = Array(n + 1).fill(false);
const result = [];

const dfs = (node) => {
	if (visited[node]) return;
	visited[node] = true;
	result.push(node);
	for (let i = 0; i < graph[node].length; i++) {
		dfs(graph[node][i]);
	}
};

dfs(1);

console.log(result.length - 1);
