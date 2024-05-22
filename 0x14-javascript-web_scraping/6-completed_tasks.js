#!/usr/bin/node

const request = require('request');
const process = require('process');

const url = process.argv[2];
request.get(url, function (e, res) {
  const data = JSON.parse(res.body);
  const obj = {};
  data.forEach(element => {
    if (element.completed === true) {
      if (!obj[element.userId]) {
        obj[element.userId] = 0;
      }
      obj[element.userId]++;
    }
  });
  console.log(obj);
});
