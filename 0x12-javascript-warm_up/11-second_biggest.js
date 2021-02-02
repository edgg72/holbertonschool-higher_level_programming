#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv.length < 4) {
  console.log(0);
} else {
  const maxNum = Math.max(process.argv);
  let secMax = process.argv[2];
  for (let i = 3; i < process.argv.length; i++) {
    if (process.argv[i] > secMax && secMax < maxNum) {
      secMax = process.argv[i];
    }
  }
  console.log(secMax);
}
