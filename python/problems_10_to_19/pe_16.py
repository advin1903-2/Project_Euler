import math

number = 2**1000

# Calculate log base 10
log_base_10 = int(math.log10(number))
sum=0

for i in range(log_base_10+1):
    sum=sum+number%10
    number=number//10

print(number)
print(sum)
