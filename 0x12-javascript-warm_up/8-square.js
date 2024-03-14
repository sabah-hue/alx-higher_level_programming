#!/usr/bin/node
const args = process.argv;
const number = Number(args[2]);
if (args[2] && Number.isInteger(number)) {
  for (let i = 0; i < number; i++) {
    console.log('X'.repeat(number));
  }
} else {
  console.log('Missing size');
}
