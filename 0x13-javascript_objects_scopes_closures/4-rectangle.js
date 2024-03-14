#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    let x = this.width;
    this.width = 2 * x;
    let y = this.height;
    this.height = 2 * y;
  }
}
module.exports = Rectangle;
