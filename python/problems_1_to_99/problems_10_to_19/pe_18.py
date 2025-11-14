matrix=[]

with open('pe_18_data.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        matrix.append(row)

num_rows = len(matrix)
number1=0
number2=0

for row in range(1,num_rows):
    #print(row)
    num_columns = len(matrix[row])
    #print(num_columns)
    for column in range(0,num_columns):
        #print(column)
        if column==0:
            matrix[row][column]=matrix[row][column]+matrix[row-1][column]
        elif column==(num_columns-1):
            matrix[row][column]=matrix[row][column]+matrix[row-1][column-1]
        else:
            number1=matrix[row-1][column-1]
            number2=matrix[row-1][column]
            if number1>number2:
                matrix[row][column]=matrix[row][column]+number1
            else:
                matrix[row][column]=matrix[row][column]+number2

##Get_final_row
final_line=matrix[num_rows-1]
max_value=max(final_line)
print(max_value)