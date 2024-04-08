#!/usr/bin/node
const args = process.argv;
if (args[2] === undefined || args[3] === undefined) {
  console.log(0);
}
if (args[2] > args[3]) {
  console.log(args[2]);
} else {
  console.log(args[3]);
}
