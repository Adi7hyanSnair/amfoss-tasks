// Function to check if a number is prime
function isPrime(num) {
  if (num <= 1) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) {
      return false;
    }
  }
  return true;
}

// Function to find and print prime numbers up to n
function findPrimesUpToN(n) {
  console.log(`Prime numbers up to ${n}:`);
  for (let i = 2; i <= n; i++) {
    if (isPrime(i)) {
      console.log(i);
    }
  }
}

// Get user input for n
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('Enter a number (n): ', (input) => {
  const n = parseInt(input);
  if (isNaN(n) || n < 2) {
    console.log('Prime numbers start from 2.');
  } else {
    findPrimesUpToN(n);
  }
  readline.close();
});
