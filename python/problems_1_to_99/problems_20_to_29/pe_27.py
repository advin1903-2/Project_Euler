import math

def get_number_from_formula(a,b,n:int)->int:
    num=n*n+a*n+b
    return num

def check_if_prime(n:int)->bool:
    if n<=1:
        return False
    sqrt_n=int(math.floor(math.sqrt(n)))
    for i in range(2,sqrt_n):
        if(n%i==0):
            return False
    return True

n_max=0
mult=0

for b in range(2,1000+1):
    if(check_if_prime(b)!=True):
        continue
    for a in range(-1000,1000):
        n=0
        while(check_if_prime(get_number_from_formula(a,b,n))==True):
            n=n+1
        if(n_max<n):
            n_max=n
            mult=a*b
print(mult)





