# Find the 10001 prime number
# Ok, so maybe find if a number is prime and keep increasing, just need to check on the list of other primes

def is_prime(n:int,list_of_primes)->bool:
    for num in list_of_primes:
        if n % num == 0:
            return False
    return True

list_of_primes = [2,3,5,7,11,13,17,19]
num = 20

while(len(list_of_primes)<10001):
    num = num + 1
    if is_prime(num,list_of_primes) == True:
        list_of_primes.append(num)
        print(num)

print(num)
