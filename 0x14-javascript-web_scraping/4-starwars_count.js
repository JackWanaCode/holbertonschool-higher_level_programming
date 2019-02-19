#!/usr/bin/node
const request = require('request');
let url = process.argv[2];
let check = 'https://swapi.co/api/people/18/';
let count = 0;
request(url, function (err, response, body) {
  if (err) throw err;
  let result = JSON.parse(body).results;
  for (let i = 0; i < result.length; i++) {
    if (result[i].characters.indexOf(check) !== -1) {
      count++;
    }
  }
  console.log(count);
});
