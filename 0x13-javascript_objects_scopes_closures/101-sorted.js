#!/usr/bin/node
const dict = require('./101-data').dict;
let newDict = {};
for (var k in dict) {
  if (newDict[dict[k]]) {
    newDict[dict[k]].push(k);
  } else {
    newDict[dict[k]] = [k];
  }
}
console.log(newDict);
