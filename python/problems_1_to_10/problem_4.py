# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91*99
# Find the largest palindrome made from the product of two 3-digit numbers.

def palindrome_test(number: int)->bool:
    # Get number of digits
    original = number
    inverted = 0
    while(number > 0):
        digit = number % 10
        inverted = inverted * 10 + digit

        number = number // 10

    return original == inverted

big_palindrome = 0

for j in range(100,1000):
    for i in range(100,1000):
        candidate = i*j
        if candidate <= big_palindrome:
            continue
        elif palindrome_test(candidate) == True:
            big_palindrome = candidate
            print(big_palindrome)

print(big_palindrome)
