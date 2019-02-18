#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
  get width () {
    return this._width;
  }
  set width (w) {
    if (w <= 0 || w == null) {
      return;
    }
    this._width = w;
  }
  get height () {
    return this._height;
  }
  set height (h) {
    if (h <= 0 || h == null) {
      delete this._width;
    } else if (this._width) {
      this._height = h;
    }
  }
}
module.exports = Rectangle;
