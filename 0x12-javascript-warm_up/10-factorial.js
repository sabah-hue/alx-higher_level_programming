#!/usr/bin/node
const args = process.argv;
function factorial (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}
console.log(factorial(parseInt(args[2])));
