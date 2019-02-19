#!/usr/bin/node
const request = require('request');
let next = '';
let url = 'http://swapi.co/api/people/';
let check = 'https://swapi.co/api/films/' + process.argv[2] + '/';
function func (n = next, u = url) {
  request.get(u + n, function (err, response, body) {
    if (err) {
      console.log(err);
    }
    let characters = JSON.parse(body).results;
    next = JSON.parse(body).next;
    for (let i = 0; i < characters.length; i++) {
      let film = characters[i].films;
      if (film.indexOf(check) !== -1) {
        console.log(characters[i].name);
      }
    }
    if (next != null) {
      func(next, '');
    }
  });
}
func();
