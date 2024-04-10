#!/usr/bin/node
const fs = require('fs');

const a = process.argv[2];
const b = process.argv[3];
const c = process.argv[4];

const stream = fs.createWriteStream(c);

stream.write(fs.readFileSync(a));
stream.write(fs.readFileSync(b));

stream.end();
