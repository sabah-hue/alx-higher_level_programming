#!/usr/bin/node
const rectangle = require('./4-rectangle.js');
class Square extends rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        console.log('C'.repeat(this.size));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
