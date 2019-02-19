#!/usr/bin/node
const request = require('request');
let url = process.argv[2];
request(url, function (err, response, body) {
  if (err) throw err;
  let r = JSON.parse(body);
  let newURL = r.results[0].characters[15];
  request(newURL, function (err, response, body) {
    if (err) throw err;
    let films = JSON.parse(body);
    console.log(films.films.length);
  });
});
