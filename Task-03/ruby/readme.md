# Ruby

in this md file i will explain the codes of ruby.

is_prime(num) function: This function takes an integer num and checks whether it is prime.
It returns true if num is prime and false otherwise. It uses a simple method to check for divisibility by numbers from 2 to the square root of num.

find_primes_up_to_n(n) function: This function takes an integer n as input, and it prints all prime numbers up to n.
It iterates through numbers from 2 to n and uses the is_prime function to determine if each number is prime. If it is, the number is printed to the terminal.

User input and output: The program takes user input for the number n. It checks if n is less than 2 and handles this special case because prime numbers start from 2.
If n is greater than or equal to 2, it calls the find_primes_up_to_n function to find and print the prime numbers up to n. If the user enters an invalid input (e.g., a non-integer),
it handles the ArgumentError and provides an error message.
