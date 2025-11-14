# Create a list of numbers from 2 to 2 million
numbers = list(range(2, 2000001))

# Initialize the sum of primes
sum_of_primes = 0

# Loop to find primes using Sieve of Eratosthenes
for i in range(len(numbers)):
    prime = numbers[i]
    
    # If prime is 0, skip it (it's already marked as non-prime)
    if prime == 0:
        continue
    
    # Mark multiples of the prime as zero, starting from prime^2
    for j in range(prime * prime, 2000001, prime):
        numbers[j - 2] = 0  # Mark as non-prime

# Sum up all the non-zero numbers (which are the primes)
sum_of_primes = sum(filter(lambda x: x != 0, numbers))

# Print the result
print(f"Sum of primes up to 2 million: {sum_of_primes}")
