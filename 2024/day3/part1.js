/*

	AOC day 3
	The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
*/

import { day3Data } from "../day2/2.1_daydata.js";

function processedRows(d) {
  return d
    .trim()
    .split("\n")
    .map((row) => row.trim().split(/\s+/).map(Number));
}

function isSafe(arr) {
  let increasing = true;
  let decreasing = true;

  for (let i = 0; i < arr.length - 1; i++) {
    const diff = arr[i + 1] - arr[i];

    // Check if the difference is within the allowed range
    if (Math.abs(diff) < 1 || Math.abs(diff) > 3) {
      return false; // Not safe if the difference is outside [1, 3]
    }

    // Update the flags based on the direction of the difference
    if (diff > 0) decreasing = false; // Increasing means not decreasing
    if (diff < 0) increasing = false; // Decreasing means not increasing

    // If neither increasing nor decreasing, break early
    if (!increasing && !decreasing) {
      return false;
    }
  }

  // The array is safe if it is consistently increasing or decreasing
  return true;
}

function answer(arr) {
  let result = 0;

  for (let i = 0; i < arr.length; i++) {
    if (isSafe(arr[i])) {
      result++;
    }
  }
  return result;
}

const test = `
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
`;
const clean = processedRows(day3Data);

console.log(answer(clean));
