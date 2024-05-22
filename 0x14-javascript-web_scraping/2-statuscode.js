#!/usr/bin/node

const request = require('request');
const process = require('process');

const url = process.argv[2];
request.get(url, function (e, res) {
  const code = res.statusCode;
  console.log(`code: ${code}`);
});
