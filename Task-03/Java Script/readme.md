# Javan Script

isPrime(num) function: This function takes an integer num and checks whether it is prime. It returns true if num is prime and false otherwise. 
It uses a simple method to check for divisibility by numbers from 2 to the square root of num.

findPrimesUpToN(n) function: This function takes an integer n as input and prints all prime numbers up to n. 
It iterates through numbers from 2 to n and uses the isPrime function to determine if each number is prime. If it is, the number is printed to the console.

User input: The program gets user input for the number n using the readline module, which allows you to interact with the command-line interface. 
It checks if n is less than 2 or if it's not a valid integer, and handles these special cases accordingly.

Running the program: To run this JavaScript program, you need to execute it in a Node.js environment. Save the code to a .js file and run it using the node command. 
For example, if you save the program as find_primes.js, you can run it by typing node find_primes.js in your terminal.
