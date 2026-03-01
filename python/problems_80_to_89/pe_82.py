
filename="0082_matrix.txt"

matrix = []

# Read the file
with open(filename, "r") as file:
    for line in file:
        row = [int(x) for x in line.strip().split(",")]
        matrix.append(row)

# Create matrix to store the paths values
matrix_paths= [[0 for _ in range(80)] for _ in range(80)]

# Only can go right,down or up
# Can start whenever I want on the left

# Create the [i][0]
for i in range(80):
    matrix_paths[i][0]=matrix[i][0]

# Have to create a method to evaluate all the paths from the left to the right
# Have to do this column wise
# The idea is to eighty times evaluate in neighbour plus own value is smaller than own value

# For all columns
for j in range(1,80):
    # For all lines do default
    for i in range(80):
        matrix_paths[i][j]=matrix[i][j]+matrix_paths[i][j-1]
    # Do eighty times, to check optimal
    for n in range(80):
        # Do for all lines the optimal
        ## For first line
        i=0
        if (matrix[i][j]+matrix_paths[i+1][j])<matrix_paths[i][j]:
            matrix_paths[i][j]=matrix[i][j]+matrix_paths[i+1][j]
        ## For last line
        i=79
        if (matrix[i][j]+matrix_paths[i-1][j])<matrix_paths[i][j]:
            matrix_paths[i][j]=matrix[i][j]+matrix_paths[i-1][j]
        ## For rest of lines
        for i in range(1,79):
            # For cell bellow
            if (matrix[i][j]+matrix_paths[i+1][j])<matrix_paths[i][j]:
                matrix_paths[i][j]=matrix[i][j]+matrix_paths[i+1][j]
            # For top cell
            if (matrix[i][j]+matrix_paths[i-1][j])<matrix_paths[i][j]:
                matrix_paths[i][j]=matrix[i][j]+matrix_paths[i-1][j]

# Print lowest value on the right
results=[]
for i in range(80):
    results.append(matrix_paths[i][79])

print(min(results))
   