# What is the smallest number evenly divisible by all numbers from 1 to 20?
# Ok, so I need to guarantee it is divisble by all numbers from 1 to 20, maybe it is easier to decompose the 20 numbers in the primes
# The prime numbers are:
# 19,17,13,11,7,5,3,2
# So two arrays, one to store the primes, and other to store the times it repeats

# Define list of number and initial weights
list_numbers = [19,17,13,11,7,5,3,2]
list_weight = [1] * len(list_numbers)

# Decompose in primes for all numbers, than check if weight list satisifies 
for i in range(1,21):
    for j in range(len(list_numbers)):
        n = 0
        prime = list_numbers[j]
        while(i % (prime ** (n+1)) == 0):
            n = n + 1
        if list_weight[j] < n:
            list_weight[j] = n

# Calculate the number
n = 1
for i in range(len(list_numbers)):
    n = n * list_numbers[i] ** list_weight[i]