#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return (1);
  }

  return (n * factorial(n - 1));
}

const argv = process.argv;
console.log(factorial(parseInt(argv[2])));
