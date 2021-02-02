#!/usr/bin/node

const a = parseInt(process.argv[2], 10);
let square = '';
if (a) {
  if (!isNaN(a) && a > 0) {
    for (let i = 0; i < a; i++) {
      square += 'X';
    }
    for (let i = 0; i < a; i++) {
      console.log(square);
    }
  }
} else console.log('Missing size');
