#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this._width = w;
    this._height = h;
  }
  get _width () {
    return this.width;
  }
  set _width (w) {
    if (w <= 0 || w == null) {
      return;
    }
    this.width = w;
  }
  get _height () {
    return this.height;
  }
  set _height (h) {
    if (h <= 0 || h == null) {
      delete this.width;
    } else if (this.width) {
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
  double () {
    this.width *= 2;
    this.height *= 2;
  }
  rotate () {
    this.width = this.width + this.height;
    this.height = this.width - this.height;
    this.width = this.width - this.height;
  }
}
module.exports = Rectangle;
