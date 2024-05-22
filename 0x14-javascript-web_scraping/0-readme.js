#!/usr/bin/node
const process = require('process');
const fs = require('fs');

const filePath = process.argv[2];
fs.readFile(filePath, function (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
