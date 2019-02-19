#!/usr/bin/node
const request = require('request');
let url = process.argv[2];
request(url, function (err, response, body) {
  if (err) throw err;
  let list = JSON.parse(body);
  let dict = {};
  for (let i = 0; i < list.length; i++) {
    if (list[i].completed) {
      if (dict[list[i].userId]) {
        dict[list[i].userId]++;
      } else {
        dict[list[i].userId] = 1;
      }
    }
  }
  console.log(dict);
});
