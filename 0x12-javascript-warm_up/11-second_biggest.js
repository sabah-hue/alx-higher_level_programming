#!/usr/bin/node
const args = process.argv;
const arrCopy = args.slice(2);
if (args[2] === undefined || args[3] === undefined) {
  console.log(0);
} else {
  arrCopy.sort((a, b) => {
    return b - a;
  });
  console.log(arrCopy[1]);
  // let max = args[2];
  // for (let i = 2; i < args.length; i++) {
  //   if (args[i] > max) {
  //     max = args[i];
  //   }
  // }
  // console.log(max);
  // let secMax = 0;
  // for (let i = 2; i < args.length; i++) {
  //   if (args[i] > secMax && args[i] !== max) {
  //     secMax = args[i];
  //   }
  // }
  // console.log(secMax);
}
