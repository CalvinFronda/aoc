/**
    AoC


 */
import { readFile } from "../day2/helper.js";
function answer() {
  readFile("3_daydata.txt", (err, data) => {
    if (err) {
      console.error("Failed to read file");
    } else {
      //   const data = `xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))`;
      const pattern = /mul\((\d{1,3}),(\d{1,3})\)/g; // Match 'mul(#,#)' with 1-3 digit numbers

      let result = 0;
      let match;

      while ((match = pattern.exec(data)) != null) {
        result = result + parseInt(match[1], 10) * parseInt(match[2], 10);
      }

      console.log(result);
    }
  });
}

function answer2() {
  readFile("3_day2data.txt", (err, input) => {
    if (err) {
      console.error("Failed to read file");
    } else {
      // const input = `xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`;
      const mulPattern = /^mul\((\d{1,3}),(\d{1,3})\)/; // Matches valid mul() calls at the current position

      let isEnabled = true; // Starts enabled
      let results = 0;
      let index = 0;

      while (index < input.length) {
        // Check for `do()` at the current position
        if (input.slice(index).startsWith("do()")) {
          isEnabled = true;
          index += 4; // Move past `do()`
          continue;
        }

        // Check for `don't()` at the current position
        if (input.slice(index).startsWith("don't()")) {
          isEnabled = false;
          index += 7; // Move past `don't()`
          continue;
        }

        // Check for `mul()` at the current position using a regex match
        if (isEnabled) {
          const mulMatch = input.slice(index).match(mulPattern);
          if (mulMatch) {
            const [fullMatch, arg1, arg2] = mulMatch;
            results = results + parseInt(arg1, 10) * parseInt(arg2, 10);

            index += fullMatch.length; // Move past the matched `mul()` call
            continue;
          }
        }

        // Move to the next character if no match
        index++;
      }

      console.log(results);
    }
  });
}

answer2();
