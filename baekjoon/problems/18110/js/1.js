const { log } = require("console");
const [n, ...levels] = `${require("fs").readFileSync(0)}`.trim().split`
`.map(Number);
levels.sort((a, b) => a - b);
const solution = () => {
	if (!n) return 0;
	const cut = Math.round(n * 0.15);
	return Math.round(
		levels.slice(cut, n - cut).reduce((a, c) => a + c) / (n - cut * 2)
	);
};
log(solution());

/*
아직 아무 의견이 없다면 문제의 난이도는 0으로 결정한다.
의견이 하나 이상 있다면, 문제의 난이도는 모든 사람의 난이도 의견의 30% 절사평균으로 결정한다.
절사 -> 반올림
평균 -> 반올림
*/
