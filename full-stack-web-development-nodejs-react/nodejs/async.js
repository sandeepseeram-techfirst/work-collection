const fs = require("fs");

fs.readFile("sandeep.txt", "utf8", (err, data) => {
  console.log(data);
});

console.log("Hello Node.js!");
