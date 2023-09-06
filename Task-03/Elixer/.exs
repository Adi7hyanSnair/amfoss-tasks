defmodule PrimeNumbers do
  # Function to generate a list of prime numbers up to n using Sieve of Eratosthenes
  def sieve_of_eratosthenes(n) when n < 2, do: []
  def sieve_of_eratosthenes(n) do
    sieve(2..n, [2], MapSet.new())
  end

  defp sieve([], primes, _marked), do: Enum.reverse(primes)
  defp sieve([current | rest], primes, marked) do
    if MapSet.member?(current, marked) do
      sieve(rest, primes, marked)
    else
      sieve(rest, [current | primes], mark_multiples(current, rest, marked))
    end
  end

  defp mark_multiples(_current, [], marked), do: marked
  defp mark_multiples(current, [num | rest], marked) do
    marked_numbers = Enum.reduce(1..(div(n, num) - 1), marked, fn i, set ->
      MapSet.put(set, current * i + num)
    end)
    mark_multiples(current, rest, marked_numbers)
  end
end

# Input function
defmodule Main do
  def run do
    IO.puts("Enter a number (n):")
    input = IO.gets() |> String.trim() |> String.to_integer()

    primes = PrimeNumbers.sieve_of_eratosthenes(input)
    IO.puts("Prime numbers up to #{input}:")
    Enum.each(primes, &IO.puts/1)
  end
end

# Run the program
Main.run()
