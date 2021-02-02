#!/usr/bin/node

function factorial (number) {
  if (isNaN(number) || number === 1 || number === 0) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

console.log(factorial(process.argv[2]));
