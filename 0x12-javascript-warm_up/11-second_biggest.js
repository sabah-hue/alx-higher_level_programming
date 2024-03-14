#!/usr/bin/node
const args = process.argv;
if (!args[2] || !args[3]) {
  console.log(0);
} else {
  let max = args[2];
  if (args[2] < args[3]) {
    max = args[3];
  }
  console.log(max);
}
