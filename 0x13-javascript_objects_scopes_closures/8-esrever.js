#!/usr/bin/node
exports.esrever = function (list) {
  let temp;
  for (let i = 0, j = list.length - 1; i < j; i++, j--) {
    temp = list[i];
    list[i] = list[j];
    list[j] = temp;
  }
  return list;
};
