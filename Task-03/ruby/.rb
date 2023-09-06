# Function to check if a number is prime
def is_prime(num)
    return false if num <= 1
  
    (2..Math.sqrt(num)).each do |i|
      return false if (num % i).zero?
    end
  
    true
  end
  
  # Function to find and print prime numbers up to n
  def find_primes_up_to_n(n)
    puts "Prime numbers up to #{n}:"
    (2..n).each do |num|
      puts num if is_prime(num)
    end
  end
  
  begin
    print "Enter a number (n): "
    n = gets.chomp.to_i
  
    if n < 2
      puts "Prime numbers start from 2."
    else
      find_primes_up_to_n(n)
    end
  rescue ArgumentError
    puts "Please enter a valid integer."
  end
