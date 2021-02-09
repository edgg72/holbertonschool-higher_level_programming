#!/usr/bin/node

const request = require('request');
const movie = process.argv[2];
const req = 'https://swapi-api.hbtn.io/api/films/' + movie;

request(req, function (error, response, body) {
  if (error) return console.log(error);
  const characters = JSON.parse(body).characters;
  for (const i in characters) {
    request(characters[i], function (error, response, body) {
      if (error) return console.log(error);
      console.log(JSON.parse(body).name);
    });
  }
});
