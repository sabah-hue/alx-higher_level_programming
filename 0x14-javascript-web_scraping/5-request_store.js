#!/usr/bin/node

const request = require('request');
const process = require('process');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, function (e, res) {
  fs.writeFile(filePath, res.body, function (e) {
    if (e) {
      console.log(e);
    }
  });
});
