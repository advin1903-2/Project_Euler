def collatz_sequence_advance(n):
    if n%2==0:
        return n/2
    else:
        return(3*n+1)
    
best=0
best_number=0    
for initial_number in range(2,10**6):
    number=initial_number
    count=0
    while(number!=1):
        number=collatz_sequence_advance(number)
        count=count+1
    if count>best:
        best=count
        best_number=initial_number
    print(best)

print(best_number)