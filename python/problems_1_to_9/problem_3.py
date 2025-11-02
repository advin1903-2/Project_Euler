# Biggest prime factor of 600851475143

num = 600851475143
i = 1

while(num > 1):
    i = i+1
    while(num % i == 0):
        num = num / i

print(i)