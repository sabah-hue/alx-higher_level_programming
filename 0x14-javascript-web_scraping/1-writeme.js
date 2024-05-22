#!/usr/bin/node
const process = require('process');
const fs = require('fs');

const filePath = process.argv[2];
const fileContent = process.argv[3];

fs.writeFile(filePath, fileContent, function (e) {
  if (e) {
    console.log(e);
  }
});
