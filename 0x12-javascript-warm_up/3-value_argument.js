#!/usr/bin/node
const args = process.argv;
if (args[2] === undefined) {
  console.log('No argument');
}
let i = 2;
while (args[i] !== undefined) {
  console.log(args[i]);
  i++;
}
