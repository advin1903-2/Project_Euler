a_max=100
a_min=2
b_max=100
b_min=2
list=[]

for a in range(a_min,a_max+1):
    for b in range(b_min,b_max+1):
        val = a**b
        if(val in list):
            continue
        else:
            list.append(val)

print(len(list))