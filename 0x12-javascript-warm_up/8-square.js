#!/usr/bin/node
const args = process.argv;
if (isNaN(Number(args[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args[2]; i++) {
    console.log('X'.repeat(args[2]));
  }
}
