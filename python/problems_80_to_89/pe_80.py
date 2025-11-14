import math
from decimal import *

getcontext().prec = 110 # Set the desired precision

n_digits=99
n=100
sum=0
for i in range(2,n+1):
    if(math.sqrt(i)%1==0):
        continue
    else:
        num_current=Decimal(i).sqrt()
        #print(num_current)
        sum=sum+num_current//1
        for j in range(n_digits):
            num_current=num_current*10
            num_current=num_current%10
            sum=sum+num_current//1
print(sum)