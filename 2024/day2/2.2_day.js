/**
 
    AOC 2.2
 
 */
import { day2_2data } from "./2.2daydata.js";
function processedRows(d) {
  return d
    .trim()
    .split("\n")
    .map((row) => row.trim().split(/\s+/).map(Number));
}
function isSafe(arr) {
  // Helper function to check if the array is safe
  const checkSafe = (array) => {
    let increasing = true;
    let decreasing = true;

    for (let i = 0; i < array.length - 1; i++) {
      const diff = array[i + 1] - array[i];

      if (Math.abs(diff) < 1 || Math.abs(diff) > 3) {
        return false; // Not safe if the difference is outside [1, 3]
      }

      if (diff > 0) decreasing = false; // Increasing means not decreasing
      if (diff < 0) increasing = false; // Decreasing means not increasing

      if (!increasing && !decreasing) return false; // Break early
    }

    return true;
  };

  // Check if the array is already safe
  if (checkSafe(arr)) return true;

  // Try removing each element one by one and check again
  for (let i = 0; i < arr.length; i++) {
    const modifiedArray = arr.slice(0, i).concat(arr.slice(i + 1));
    if (checkSafe(modifiedArray)) return true;
  }

  // If no single removal makes the array safe, return false
  return false;
}

function answer(row) {
  let result = 0;
  for (let i = 0; i < row.length; i++) {
    if (isSafe(row[i])) {
      result++;
    }
  }
  return result;
}

const test = `7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9`;
const testData = processedRows(day2_2data);
console.log(answer(testData));
