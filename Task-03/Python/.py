def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for current_num in range(2, int(n ** 0.5) + 1):
        if is_prime[current_num]:
            for multiple in range(current_num * current_num, n + 1, current_num):
                is_prime[multiple] = False

    prime_numbers = [num for num in range(2, n + 1) if is_prime[num]]
    return prime_numbers

try:
    n = int(input("Enter a number (n): "))
    if n < 2:
        print("Prime numbers start from 2.")
    else:
        prime_numbers = sieve_of_eratosthenes(n)
        print(f"Prime numbers up to {n}:")
        print(prime_numbers)
except ValueError:
    print("Please enter a valid integer.")
