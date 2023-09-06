# Python

In this md file i will explain what i coded.

in this md file i am explaining the steps of python language to solve
the given problem

Define the sieve_of_eratosthenes function: This function takes an integer n as input and returns a list of prime numbers up to n.

Initialize a boolean list is_prime: We create a list is_prime of size n+1 where each element is initially set to True. This list will be used to mark numbers as prime or non-prime.

Mark 0 and 1 as non-prime: Since 0 and 1 are not prime numbers, we set is_prime[0] and is_prime[1] to False.

Iterate through numbers from 2 to the square root of n: We start iterating from 2 (the smallest prime number) up to the square root of n. For each current number, if it's marked as prime (is_prime[current_num] is True), we proceed to mark its multiples as non-prime.

Mark multiples as non-prime: For each prime number found (starting with 2), we mark all its multiples as non-prime. We start from current_num * current_num because any smaller multiple would have already been marked as non-prime by a smaller prime number.

Generate a list of prime numbers: After completing the above steps, the is_prime list will have True for prime numbers and False for non-prime numbers. We then generate a list of prime numbers by iterating through the range from 2 to n and adding numbers with True in the is_prime list to the prime_numbers list.

User input and output: The program takes user input for the number n. It checks if n is less than 2 and handles this special case because prime numbers start from 2. If n is greater than or equal to 2, it calls the sieve_of_eratosthenes function to find prime numbers up to n and prints the result.

I ones an online compiler Replit 
I will also add the Screen Shot

![WhatsApp Image 2023-09-06 at 19 52 23](https://github.com/Adi7hyanSnair/amfoss-tasks/assets/143208653/80b03af5-0ea5-46d4-9d33-e25b61be9483)
