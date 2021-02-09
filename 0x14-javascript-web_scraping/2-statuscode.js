#!/usr/bin/node

const request = require('request');

const req = request.get(process.argv[2]);

request(req, function (error, response) {
  if (error) return console.log(error);
  console.log('code:', response.statusCode);
});
