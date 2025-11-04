# Define matrix size
n=1001


## Intiate the matrix 
matrix = [[0 for _ in range(n)] for _ in range(n)]

n_i=int((n-1)/2)
n_j=n_i
n_b=n_i
num=1
matrix[n_i][n_j]=num

##Loop to create a matrix with the values
for i in range(n_j+1):
    ## Move to the right
    for j in range(i*2+1):
        #print(n_j)
        #print(n_i)
        n_j=n_j+1
        if(n_j==n):
            break
        num=num+1
        matrix[n_i][n_j]=num
    if(i==n_b):
        break;
    ## Move down
    for j in range(i*2+1):
        n_i=n_i+1
        num=num+1
        matrix[n_i][n_j]=num
    ## Move to the left
    for j in range(i*2+1+1):
        n_j=n_j-1
        num=num+1
        matrix[n_i][n_j]=num
    ## Move up
    for j in range(i*2+1+1):
        n_i=n_i-1
        num=num+1
        matrix[n_i][n_j]=num

## Sum all diagonal values
sum=0
for i in range(1001):
    sum = sum + matrix[i][i]
for i in range(1001):
    sum = sum + matrix[1000-i][i]

print(sum-1)