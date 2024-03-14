#!/usr/bin/node
const square = require('./5-square.js');
class Square extends square {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
