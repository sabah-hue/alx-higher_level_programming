#!/usr/bin/node
const args = process.argv;
if (args[2] === undefined || args[3] === undefined) {
  console.log('0');
} else {
  let max = args[2];
  for (let i = 2; i < args.length; i++) {
    if (args[i] > max) {
      max = args[i];
    }
  }
  console.log(max);
  let secMax = 0;
  for (let i = 2; i < args.length; i++) {
    if (args[i] > secMax && args[i] !== max) {
      secMax = args[i];
    }
  }
  console.log(secMax);
}
