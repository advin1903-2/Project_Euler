filename="0081_matrix.txt"

matrix = []

# Read the file
with open(filename, "r") as file:
    for line in file:
        row = [int(x) for x in line.strip().split(",")]
        matrix.append(row)

# Create matrix to store the paths values
matrix_paths= [[0 for _ in range(80)] for _ in range(80)]

# Only can go right or down
# This way I can make a rule to create the values by line or column
# Simply create the line, where values are the smaller between top and left and sum the value of cell

# Create the [0][0]
matrix_paths[0][0]=matrix[0][0]
# Create line 0
for j in range(1,80):
    matrix_paths[0][j]=matrix[0][j]+matrix_paths[0][j-1]
# Create column 0
for j in range(1,80):
    matrix_paths[j][0]=matrix[j][0]+matrix_paths[j-1][0]

# for all lines
for i in range(1,80):
    # For all columns:
    for j in range(1,80):
        matrix_paths[i][j]=matrix[i][j]+min(matrix_paths[i-1][j],matrix_paths[i][j-1])

print(matrix_paths[79][79])      