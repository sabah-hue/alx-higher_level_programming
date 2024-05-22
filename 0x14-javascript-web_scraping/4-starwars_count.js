#!/usr/bin/node

const request = require('request');
const process = require('process');

const url = process.argv[2];
request.get(url, function (e, res) {
  const data = JSON.parse(res.body).results;
  const result = data.filter(
    e => e.characters.find(elm => elm.includes('/18/'))
  );
  console.log(result.length);
});
