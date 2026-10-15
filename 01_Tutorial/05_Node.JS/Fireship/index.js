const { readFile, readFileSync } = require("fs").promises;

const file = await readFile("./hello.txt", "utf8", (err, txt) => {
  console.log(txt);
});

const txt = readFileSync("./hello.txt", "utf8");

console.log(txt);

console.log("finish");
