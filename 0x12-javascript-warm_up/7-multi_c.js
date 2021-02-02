#!/usr/bin/node

const a = parseInt(process.argv[2], 10);

if (a) {
  if (!isNaN(a) && a > 0) {
    for (let i = 0; i < a; i++) {
      console.log('C is fun');
    }
  }
} else console.log('Missing number of occurrences');
