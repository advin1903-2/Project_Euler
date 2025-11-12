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

list = get_prime_numbers_list(1000000)
max_code=0
max_num = 0

for j in range(len(list)):
    current_num = 0
    for i in range(j,len(list)):
        current_num=current_num+list[i]
        # If number is to big, we should break the loop
        if(current_num>1e6):
            break
        # Check if length is big enough before starting check process
        if(max_code>=i-j+1):
            continue
        if(current_num in list):
            code=i-j+1
            max_code=code
            print(code)
            print(current_num)
            
print(code)
print(current_num)