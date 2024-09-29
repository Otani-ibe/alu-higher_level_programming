#!/usr/bin/node
function factorial(n) {
  if (isNaN(n)) {
    return 1; // Return 1 for NaN
  }
  if (n <= 1) {
    return 1; // Base case: factorial(0) and factorial(1) are 1
  }
  return n * factorial(n - 1); // Recursive case
}

const input = process.argv[2]; // First argument from command line
const num = parseInt(input, 10); // Cast the argument to an integer

console.log(factorial(num));
