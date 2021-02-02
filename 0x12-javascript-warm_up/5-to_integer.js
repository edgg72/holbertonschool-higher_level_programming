#!/usr/bin/node

const a = parseInt(process.argv[2], 10);

if (a) {
  if (!isNaN(a)) console.log(a);
} else console.log('Not a number');
