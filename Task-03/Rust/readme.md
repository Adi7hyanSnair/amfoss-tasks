# Rust

The is_prime function checks if a given number num is prime. It returns true if num is prime and false otherwise.

In the main function, we use println! to print a prompt asking the user to enter a number n.

We read the user's input as a string and then parse it as a u32 (an unsigned 32-bit integer). If parsing fails, we handle the error and print a message.

We check if n is less than 2. If n is less than 2, we print a message indicating that prime numbers start from 2.

If n is greater than or equal to 2, we print "Prime numbers up to n" and then iterate through numbers from 2 to n. For each number,
we call the is_prime function to check if it's prime. If it's prime, we use println! to print the number to the terminal.

I ones an online compiler Replit 
I will also add the Screen Shot

![WhatsApp Image 2023-09-06 at 20 01 46](https://github.com/Adi7hyanSnair/amfoss-tasks/assets/143208653/1b39159b-240b-4127-8873-167a457a42fa)
