const { log } = require("console");

const [mn, ...rest] = `${require("fs").readFileSync(0)}`.trim().split`
`;
const [m, n] = mn.split` `.map(Number);
const matrix = rest.map((row) => row.split``);
log(m, n);
matrix.forEach((row) => log(...row));
