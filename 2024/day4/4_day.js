import { readFile } from "../day2/helper.js";

readFile("4_daydata.txt", (err, data) => {
  if (err) {
    return "Error getting data";
  }

  const result = data.match(
    /(?=(M|S).(M|S).{139}A.{139}(?!\2)(M|S).(?!\1)(M|S))/dgs
  ).length;
  console.log(result);
});
