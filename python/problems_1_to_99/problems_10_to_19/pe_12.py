def get_number_divisors(n):
    count=0
    for i in range(1,int(n)):
        if n%i==0:
            count=count+1
    return count

n=1
divisors=get_number_divisors(n)*get_number_divisors((n+1)/2)
number=0

while(divisors<=501):
    n=n+1
    if n%2==0:
        divisors=get_number_divisors(n/2)*get_number_divisors(n+1)
    else:
        divisors=get_number_divisors(n)*get_number_divisors((n+1)/2)
    number=n*(n+1)/2
    print(n)
    
print(number)