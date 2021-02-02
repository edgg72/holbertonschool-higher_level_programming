#!/usr/bin/node

if (isNaN(process.argv[2]) || process.argv.length < 4) {
  console.log(0);
} else {
  let numList = [];
  for (let i = 2; i < process.argv.length; i++) {
    numList.push(parseInt(process.argv[i]));
  }
  const maxNum = Math.max(...numList);
  let secMax = numList[0];
  for (let i = 1; i < numList.length; i++) {
    if (numList[i] > secMax && numList[i] < maxNum) {
      secMax = numList[i];
    }
  }
  console.log(secMax);
}
