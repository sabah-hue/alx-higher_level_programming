#!/usr/bin/node

const request = require('request');
const process = require('process');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(url, function (e, res) {
  const data = JSON.parse(res.body);
  console.log(data.title);
});
