# The goal of this problem is to find the first four consecutive numbers, with three distinct prime factors
# Maybe the best approach is create a list with the prime numbers up to 1000, then check if the number has four distinct prime factors
# Then check if the three previous also fill the condition

# Get a list with prime numbers up to a certain number
def get_prime_numbers_list(n_max:int):
    list=[]
    list.append(2)
    for i in range(3,n_max+1):
        check=1
        for j in list:
            if(i%j==0):
                check=0
                break
        if(check==1):
            list.append(i)
    return list

# Check if number has four distinct prime factors
# Have to provide a list of primes and the number itself
def check_number_condition(numb,list):
    count=0
    for i in list:
        if(numb%i==0):
            count=count+1
        if(count==4):
            return 1
    return 0


list = get_prime_numbers_list(1000000)
#print(list)
num_max = 1000000
count=0
for i in range(2*3*5*7,num_max+1):
    print(i)
    if (check_number_condition(i,list)==1):
        count=count+1
    else:
        count=0
    if(count==4):
        print(i-3)
        break