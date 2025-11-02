matrix=[]

with open('pe_11_data.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        matrix.append(row)

max_val=0

num_rows = len(matrix)
num_columns = len(matrix[0])

##Check in lines
for i in range(num_rows):
    for j in range(num_columns-4+1):
        multiple=1
        for x in range(4):
            multiple=multiple*matrix[i][j+x]
        if max_val<multiple:
            max_val=multiple

##Check in columns
for i in range(num_columns):
    for j in range(num_rows-4+1):
        multiple=1
        for x in range(4):
            multiple=multiple*matrix[j+x][i]
        if max_val<multiple:
            max_val=multiple

##Check diagonals top-left bottom-right
for i in range(num_rows-4+1):
    for j in range(num_columns-4+1):
        multiple=1
        for x in range(4):
            multiple=multiple*matrix[i+x][j+x]
        if max_val<multiple:
            max_val=multiple

##Check diagonals top-right bottom-left
for i in range(num_rows-4+1):
    for j in range(3,num_columns):
        multiple=1
        for x in range(4):
            multiple=multiple*matrix[i+x][j-x]
        if max_val<multiple:
            max_val=multiple

print(max_val)