import java.util.Scanner;

public class PrimeNumbers {
    // Function to check if a number is prime
    public static boolean isPrime(int num) {
        if (num <= 1) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number (n): ");
        int n = scanner.nextInt();
        scanner.close();

        if (n < 2) {
            System.out.println("Prime numbers start from 2.");
        } else {
            System.out.println("Prime numbers up to " + n + ":");
            for (int i = 2; i <= n; i++) {
                if (isPrime(i)) {
                    System.out.println(i);
                }
            }
        }
    }
}
