number=1
sum_of_digits=0

for i in range(1,101):
    number=number*i
    while(number%10==0):
        number=number//10

while(number!=0):
    sum_of_digits=sum_of_digits+number%10
    number=number//10

print(sum_of_digits)