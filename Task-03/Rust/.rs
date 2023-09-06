use std::io;

// Function to check if a number is prime
fn is_prime(num: u32) -> bool {
    if num <= 1 {
        return false;
    }
    for i in 2..=num / 2 {
        if num % i == 0 {
            return false;
        }
    }
    true
}

fn main() {
    println!("Enter a number (n):");

    let mut n = String::new();
    io::stdin()
        .read_line(&mut n)
        .expect("Failed to read line");

    let n: u32 = match n.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Invalid input. Please enter a valid number.");
            return;
        }
    };

    if n < 2 {
        println!("Prime numbers start from 2.");
    } else {
        println!("Prime numbers up to {}:", n);
        for i in 2..=n {
            if is_prime(i) {
                println!("{}", i);
            }
        }
    }
}
