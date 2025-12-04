/*
	AOC day 2
Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.
*/
import { readFileSync } from "fs";

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

function answer(col1, col2) {
  const hash = {};
  let result = 0;
  for (let i = 0; i < col2.length; i++) {
    if (!hash[col2[i]]) {
      hash[col2[i]] = 1;
    } else {
      hash[col2[i]] = hash[col2[i]] + 1;
    }
  }

  for (let i = 0; i < col1.length; i++) {
    if (hash[col1[i]]) {
      result = result + col1[i] * hash[col1[i]];
    }
  }

  return result;
}

const sample = "./sample.txt";
const real = "./input.txt";

function result() {
  const input = readFileSync(real, "latin1");
  const [col1, col2] = cleanData(input);
  return answer(col1, col2);
}

console.log(result());
