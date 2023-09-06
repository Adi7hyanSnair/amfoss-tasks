# Haskell

The isPrime function checks if a given number num is prime. 
It returns True if num is prime and False otherwise.

The findPrimesUpToN function takes an integer n as input and 
prints all prime numbers up to n using a list comprehension.

In the main function, we use putStr to print a prompt asking the user to enter a number n.

We read the user's input as a string using getLine and then convert it to an Int.

We check if n is less than 2. If n is less than 2, we print a message 
indicating that prime numbers start from 2.

If n is greater than or equal to 2, we call findPrimesUpToN to find and print the prime numbers up to n.
