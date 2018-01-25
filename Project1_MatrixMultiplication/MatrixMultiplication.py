# This program multiplicates two matrices of any number of rows and columns.
# The matrix elements are filled by User
# The result is calculated and saved as list

print('MATRIX MULTIPLICATION\n')

# Ask user for dimensions of first matrix
r = int(input("Matrix1: Number of rows?: "))
c = int(input("Matrix1: Number of columns?: "))

# Print design of first Matrix for better understanding of elements' naming convention
print('''\nElements of matrix1:''')
element = ''                            # Later will be used to construct each row of the matrix
for vr in range(0, r):                  # vr - variable row
    for vc in range(0, c):              # vc - variable column
        element += 'M' + str(vr + 1) + str(vc + 1) + ' '    # +1 because matrix indications start from 0
    print('|', element, '\b|')
    element = ''

# Create empty Matrix1 and fill it with user input element by element
Matrix1 = [[] for vr in range(0, r)]
for vr in range(0, r):
    Matrix1[vr] = [0 for vc in range(0, c)]

for vr in range(0, r):
    for vc in range(0, c):
        Matrix1[vr][vc] = int(input('M' + str(vr + 1) + str(vc + 1) + ': '))

# Ask the user for dimension of second matrix
v = int(input("Matrix2: Number of columns?: "))     # Only for columns since M2 rows = M1 columns by definition
print('''\nElements of matrix Matrix2:''')

for vr in range(0, c):                  # vr in c because Matrix 2 must have the same number of rows as Matrix1 columns.
    for vc in range(0, v):
        element += 'M' + str(vr + 1) + str(vc + 1) + ' '
    print('|', element, '\b|')
    element = ''

# Create Empty Matrix2 and fill it with user input element by element
Matrix2 = [[] for vr in range(0, c)]
for vr in range(0, c):
    Matrix2[vr] = [0 for vc in range(0, v)]

for vr in range(0, c):
    for vc in range(0, v):
        Matrix2[vr][vc] = int(input('M' + str(vr + 1) + str(vc + 1) + ': '))

# Create empty Product Matrix for Result of multiplication of Matrix1 and Matrix2
Product = [[] for vr in range(0, r)]                # Number of rows defined by number of rows in Matrix1
for vr in range(0, r):
    Product[vr] = [0 for columns in range(v)]       # Number of columns defined by number of columns in Matrix2

# Calculate the Product of two tables
Products = 0            # dummy variable for calculating sum of product of each row and column
for vv in range(0, v):
    for vr in range(0, r):
        for vc in range(0, c):
            Products += Matrix1[vr][vc] * Matrix2[vc][vv]
        Product[vr][vv] = Products
        Products = 0        # clear the variable when looped for whole column of Matrix2


print('Matrix1: ', Matrix1)
print('Matrix2: ', Matrix2)
print('Result of Matrix Multiplication:', Product)

# Footnotes
print('\n\nCreated by: MK')
input('Press "Enter" to Exit')        # Easy way to Exit program If run from script

# Test PyCharmUpdate 43
