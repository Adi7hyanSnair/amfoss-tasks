# Go

isPrime(num) function: This function takes an integer num and checks whether it is prime. 
It returns true if num is prime and false otherwise. It uses a simple method to check for divisibility by numbers from 2 to the square root of num.

In the main function, we use fmt to print messages and take user input for the number n.

We check if the input is a valid integer and if n is less than 2. If so, we print a message indicating that prime numbers start from 2.

If n is greater than or equal to 2, we print the prime numbers up to n by iterating through numbers from 2 to n 
and using the isPrime function to determine if each number is prime. If it is, we print the prime number to the terminal.

To run this Go program, follow these steps:

Save the code to a .go file (e.g., prime_numbers.go).

Open a terminal and navigate to the directory where the Go file is located.
