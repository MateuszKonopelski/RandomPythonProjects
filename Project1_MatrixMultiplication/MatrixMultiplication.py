# This program multiplicates two matrices of any number of rows and columns.
# The matrix elements are filled by User
# The result is set up and saved as list

print('''
MATRIX MULTIPLICATION\n
''')

# Ask user for
r = int(input("Matrix1: Number of rows?: "))
c = int(input("Matrix1: Number of columns?: "))

# Print design matrix with user dimensions to easier visualize M11, M13 etc
print('''\nElements of matrix1:''')
element = ''
for vr in range(0, r):                  # vr - variable row
    for vc in range(0, c):              # vc - variable column
        element += 'M' + str(vr + 1) + str(vc + 1) + ' '
    print('|', element, '\b|')
    element = ''

# Ask User for matrix elements and create lists
Matrix1 = [[] for vr in range(0, r)]
for vr in range(0, r):
    Matrix1[vr] = [0 for vc in range(0, c)]

for vr in range(0, r):
    for vc in range(0, c):
        Matrix1[vr][vc] = int(input('M' + str(vr + 1) + str(vc + 1) + ': '))

# Matrix2:
v = int(input("Matrix2: Number of columns?: "))
print('''\nElements of matrix Matrix2:''')
element = ''
for vr in range(0, c):                  # vr in c because Matrix 2 must have the same number of rows as Matrix1 columns.
    for vc in range(0, v):
        element += 'M' + str(vr + 1) + str(vc + 1) + ' '
    print('|', element, '\b|')
    element = ''

# Ask User for matrix elements and create lists
Matrix2 = [[] for vr in range(0, c)]
for vr in range(0, c):
    Matrix2[vr] = [0 for vc in range(0, v)]

for vr in range(0, c):
    for vc in range(0, v):
        Matrix2[vr][vc] = int(input('M' + str(vr + 1) + str(vc + 1) + ': '))

# Create Empty Table for Product of Matrix and Vector
Product = [[] for vr in range(0, r)]
for vr in range(0, r):
    Product[vr] = [0 for columns in range(v)]
print(Product)
# Calculate the Product of two tables

Products = 0
for vv in range(0, v):
    for vr in range(0, r):
        for vc in range(0, c):
            Products += Matrix1[vr][vc] * Matrix2[vc][vv]
        Product[vr][vv] = Products
        Products = 0


print('Matrix1: ', Matrix1)
print('Matrix2: ', Matrix2)
print('Result of Matrix Multiplication:', Product)

print('\n\n\ncreated by: MK')

input('Press "Enter" to Exit')
