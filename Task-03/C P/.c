#include <stdio.h>

int main() {
    int n;

    printf("Enter a number (n): ");
    scanf("%d", &n);

    if (n < 2) {
        printf("Prime numbers start from 2.\n");
    } else {
        printf("Prime numbers up to %d:\n", n);
        for (int i = 2; i <= n; i++) {
            if (isPrime(i)) {
                printf("%d\n", i);
            }
        }
    }

  
// Function to check if a number is prime
int isPrime(int num) {
    if (num <= 1) {
        return 0;
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return 0;
        }
    }
    return 1;
}

    return 0;
}
