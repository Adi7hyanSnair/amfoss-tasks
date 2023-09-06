# Elixer

it is the explanation of elixer

We define a module called PrimeNumbers that contains functions for generating prime numbers using the Sieve of Eratosthenes algorithm.
The main function is sieve_of_eratosthenes(n) which generates a list of prime numbers up to n.

We also define a module called Main that handles user input and output. The run/0 function takes user input,
calls sieve_of_eratosthenes/1 from the PrimeNumbers module, and prints the prime numbers.

In the PrimeNumbers module, the sieve_of_eratosthenes/1 function initializes a sieve with the numbers from 2 to n 
and uses helper functions to mark non-prime numbers and generate the list of prime numbers.

The mark_multiples/3 function marks the multiples of a given number, and the sieve/3 function processes the list of numbers and filters out non-prime numbers.

Finally, we run the program by calling Main.run(), which takes user input, computes the prime numbers, and prints them to the terminal.

I ones an online compiler Replit 
I will also add the Screen Shot

![WhatsApp Image 2023-09-06 at 19 54 37](https://github.com/Adi7hyanSnair/amfoss-tasks/assets/143208653/8a194e7b-a5b0-4e91-b545-5b2404db1f9f)
