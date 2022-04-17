m = [[1, 2, 3], [4, 5, 6]]

row = int(input("Enter number of Rows:"))
column = int(input("Enter number of Columns:"))

matrix = []
print("Enter the values in row:")

# TODO Take input from user
for i in range(row):
    a = []
    for j in range(column):
        a.append(int(input("Enter Values:")))
    matrix.append(a)

# TODO print the matrix

for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=" ")
    print()