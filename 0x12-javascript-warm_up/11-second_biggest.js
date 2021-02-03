#!/usr/bin/node

let secMax = 0;
let numList = process.argv.slice(2);

if (numList.length > 1) {
  numList.sort(function(a, b){return a - b});
  secMax = numList[numList.length - 2];
}

console.log(secMax);
