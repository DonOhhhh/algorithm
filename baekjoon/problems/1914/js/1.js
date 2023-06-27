let n = require("fs").readFileSync("/dev/stdin").toString().trim();
const solution = (n) => {
	if (n <= 20) {
		let l = [["1 2", "2 1", "1 3", "3 1", "2 3", "3 2"]];
		for (let i = 1; i < n; i++) {
			let q = l[i - 1];
			l.push([
				q[2] + "\n1 2\n" + q[5],
				q[4] + "\n2 1\n" + q[3],
				q[0] + "\n1 3\n" + q[4],
				q[5] + "\n3 1\n" + q[1],
				q[1] + "\n2 3\n" + q[2],
				q[3] + "\n3 2\n" + q[0],
			]);
		}
		return Math.pow(2, n) - 1 + "\n" + l[n - 1][2];
	} else {
		let x = 0;
		let res = BigInt(1);
		while (x < n) {
			res = res * BigInt(2);
			x++;
		}
		return (res - BigInt(1)).toString();
	}
};
console.log(solution(n));
