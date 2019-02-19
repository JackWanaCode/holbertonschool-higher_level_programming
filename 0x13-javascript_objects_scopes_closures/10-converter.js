#!/usr/bin/node
exports.converter = function (base) {
  function func1 (a) {
    if (base === 10) {
      return a;
    } else {
      return a.toString(base);
    }
  }
  return func1;
};
