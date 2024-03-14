#!/usr/bin/node
const args = process.argv;
const number = Number(args[2]);
function f (n) {
  if (n === 1) {
    return 1;
  }
  return n * f(n - 1);
}
if (args[2]) {
  console.log(f(number));
} else {
  console.log(1);
}
