from decimal import Decimal, getcontext

# If not working for numbers try to change this values, these are settings
# This one defines precision
getcontext().prec = 3000
# This one defines the initial places to jump
jump_places=100

# Here define the max value of d, and store values
max_num=1000
n_max=0
d_max=0

for d in range(3,max_num+1):
    div_result=Decimal('1') / Decimal(str(d))
    div_result=(div_result*10**jump_places)%(1)
    if((div_result*1000)%1==0):
        continue
    else:
        n=0
        while(True):
            n=n+1
            # Create numbers and provide displacemte
            comp_1=div_result*(10**n)
            comp_2=div_result*100**n
            comp_1=comp_1//1
            comp_2=comp_2//1
            ## Time to create numbers that should be equal
            comp_1=comp_1*(10**n+1)
            if(int(comp_1)==int(comp_2)):
                break
    if(n_max<n):
        n_max=n
        d_max=d

# Print results
print(f"Maximum d value:{d_max}")
print(f"Maximum number of places:{n_max}")