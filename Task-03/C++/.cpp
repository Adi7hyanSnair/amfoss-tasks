#include <iostream>
#include <vector>

using namespace std;

// Function to check if a number is prime
bool isPrime(int num) {
    if (num <= 1) {
        return false;
    }
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    int n;

    cout << "Enter a number (n): ";
    cin >> n;

    if (n < 2) {
        cout << "Prime numbers start from 2." << endl;
    } else {
        cout << "Prime numbers up to " << n << ":" << endl;
        for (int i = 2; i <= n; i++) {
            if (isPrime(i)) {
                cout << i << endl;
            }
        }
    }

    return 0;
}

