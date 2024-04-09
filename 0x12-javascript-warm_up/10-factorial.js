#!/usr/bin/node
function factorial (x) {
  return x === 0 || isNaN(x) ? 1 : x * factorial(x - 1);
}

console.log(factorial(parseInt(process.argv[2], 10)));
