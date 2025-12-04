import fs from "fs";

export function readFile(file, callback) {
  fs.readFile(file, "utf-8", (err, data) => {
    if (err) {
      console.error("Error reading file", err);
      callback(err, null);
      return;
    }
    callback(null, data);
  });
}
