# Looking at the problem, if one decomposes the square sum according to (a+b)**2=a**2+b**2+2*a*b
# And noting that on the other and subtracting b ** 2 until the point where a=0
# Then is just summing sums

value = 0

for i in range(1,101):
    sum = 0
    for j in range(1,i):
        sum = sum + j
    sum = 2 * i * sum

    value = value + sum

print(value) 