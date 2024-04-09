#!/usr/bin/node
const Square = require('./5-square');
class Square extends Square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.size));
      }
    }
  }
}
module.exports = Square;
