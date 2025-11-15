import math

# Function to get sum of divisors
def get_sum_divisors(n:int)->int:
    sum=1
    n_max=int(math.sqrt(n))
    for i in range(2,n_max+1):
        if(n%i==0):
            sum=sum+i
            if(n//i!=i):
                sum= sum+n//i
    return sum

# Function to check if it is an abundant number
def check_if_abundant(n:int)->bool:
    sum_divs=get_sum_divisors(n)
    if(sum_divs>n):
        return True
    else:
        return False

# Function to create list of abundant numbers up to a certain number
def get_list_abundant_numbers(max_num:int)->list:
    list=[]
    for num in range(12,max_num+1):
        if(check_if_abundant(num)):
            list.append(num)
    return list


# Main code
# First of all create list with abundant numbers
n_max=28123
list_abundant_numbers=get_list_abundant_numbers(n_max)
# Now create list with all numbers
list_of_numbers=[0]*n_max
# Now make combinations of sums and if in list of abundant numbers, delete
for j in range(len(list_abundant_numbers)):
    for i in range(j,len(list_abundant_numbers)):
        sum=list_abundant_numbers[i]+list_abundant_numbers[j]
        if(sum>n_max):
            break
        list_of_numbers[sum-1]=1

# Now that we have the numbers, sum them up
sum=0
for i in range(n_max):
    if(list_of_numbers[i]==0):
        sum=sum+i+1

print(sum)