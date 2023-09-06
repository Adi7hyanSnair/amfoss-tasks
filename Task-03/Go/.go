package main

import (
	"fmt"
	"math"
)

// Function to check if a number is prime
func isPrime(num int) bool {
	if num <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	var n int
	fmt.Print("Enter a number (n): ")
	_, err := fmt.Scanf("%d", &n)

	if err != nil || n < 2 {
		fmt.Println("Prime numbers start from 2.")
	} else {
		fmt.Printf("Prime numbers up to %d:\n", n)
		for i := 2; i <= n; i++ {
			if isPrime(i) {
				fmt.Println(i)
			}
		}
	}
}
