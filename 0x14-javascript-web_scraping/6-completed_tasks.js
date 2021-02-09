#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) return console.log(error);
  const newDict = {};
  const aux = JSON.parse(body);
  for (const i in aux) { // checking every position in body
    if (aux[i].completed === true) {
      if (newDict[aux[i].userId] === undefined) {
        newDict[aux[i].userId] = 1;
      } else {
        newDict[aux[i].userId]++;
      }
    }
  }
  console.log(newDict);
});
