#!/usr/bin/node
const x = require('./5-square');
class Square extends x {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        console.log(c.repeat(this.size));
      }
    }
  }
}
module.exports = Square;
