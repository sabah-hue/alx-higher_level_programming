#!/usr/bin/node
const args = process.argv;
const number = Math.floor(Number(args[2]));
if (args[2] && Number.isInteger(number)) {
  for (let i = 0; i < number; i++) {
    console.log('x'.repeat(number));
  }
} else {
  console.log('Missing size');
}
