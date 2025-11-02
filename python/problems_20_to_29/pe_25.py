FN2=1
FN1=1
FN=FN2+FN1
Index=3
n=10**999
check=0

while(check==0):
    Index=Index+1
    FN2=FN1
    FN1=FN
    FN=FN1+FN2
    check=FN//n
    print(Index)
    print(FN)

print(Index)