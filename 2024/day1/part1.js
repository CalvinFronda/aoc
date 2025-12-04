/*
 AOC day 1
*/
// import { data } from "./1.1_daydata.js";

import { readFileSync } from "fs";

function answer(a, b) {
  const sortA = a.sort((a, b) => a - b);
  const sortB = b.sort((a, b) => a - b);

  let result = 0;
  for (let i = 0; i < a.length; i++) {
    result = result + Math.abs(sortA[i] - sortB[i]);
  }
  return result;
}

function cleanData(d) {
  const rows = d.trim().split("\n");

  const column1 = [];
  const column2 = [];

  rows.forEach((row) => {
    const [col1, col2] = row.trim().split(/\s+/).map(Number);
    column1.push(col1);
    column2.push(col2);
  });
  return [column1, column2];
}

const sample = "./sample.txt";
const real = "./input.txt";

function result() {
  const input = readFileSync(real, "latin1");
  const [a, b] = cleanData(input);
  return answer(a, b);
}

console.log(result());
