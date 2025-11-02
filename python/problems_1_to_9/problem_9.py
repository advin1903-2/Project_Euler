total=1000

for a in range(1,total-1):
    a_square=a**2
    for b in range(a+1,total-a):
        b_square=b**2
        sum_square_ab=a_square+b_square
        c=1000-a-b
        c_square=c**2
        if sum_square_ab==c_square:
            print(a*b*c)
            