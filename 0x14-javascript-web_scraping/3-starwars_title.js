#!/usr/bin/node
const request = require('request');
let id = process.argv[2];
request('http://swapi.co/api/films/' + id, function (err, response, body) {
  if (err) throw err;
  let title = JSON.parse(body);
  console.log(title.title);
});
