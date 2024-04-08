#!/usr/bin/node
const args = process.argv;
if (args[2] === undefined) {
  console.log('No argument');
}
for (let i = 2; i < args.length; i++) {
  console.log(args[i]);
}
