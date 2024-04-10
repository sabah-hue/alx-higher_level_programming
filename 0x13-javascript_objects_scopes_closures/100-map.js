#!/usr/bin/node
const arr = require('./100-data');
console.log(arr.list);
const newArr = arr.list.map((e, index) => e * index);
console.log(newArr);
