print('''
Calculate r squared and linear regression equation using
least squared errors method.

Manual approach.
''')

# set up
import math
import matplotlib.pyplot as plt

# Data
P1 = (1, 1)
P2 = (2, 2)
P3 = (2, 3)
P4 = (3, 6)

# Create a list from Data

points = []
points.extend(value for name, value in locals().items() if name.startswith('P'))

# constants, which characterize x-axis and y-axis
X = 0
Y = 1

# Calcualte Mean
sumx = 0
sumy = 0
count = len(points)

for point in points:
    sumx += point[X]
    sumy += point[Y]

meanx = sumx / count
meany = sumy / count

# Calculate Standard Deviation
sumxx = 0
sumyy = 0

for point in points:
    sumxx += (point[X] - meanx) ** 2
    sumyy += (point[Y] - meany) ** 2

sdx = math.sqrt(sumxx / (count - 1))
sdy = math.sqrt(sumyy / (count - 1))

# Calcualte R
sum = 0
for point in points:
    sum += ((point[X] - meanx)/sdx) * ((point[Y] - meany)/sdy)

r = sum / (count - 1)

print('Correlation coefficient r = ', round(r * 100, 2), '%')

# Calculate linear regression equation (y = ax + b) using least squared method

a = r * (sdy / sdx)
b = meany - a * meanx       # because this equation must intercept in mean of both

print("Linear Regression equation: ", 'y =', round(a, 2), 'x', round(b, 2))

# Scaterplot
x, y = [], []
for i in range(len(points)):
    x.append(points[i][0])
    y.append(points[i][1])

x1 = min(x)
y1 = a * x1 + b
x2 = max(x)
y2 = a * x2 + b

plt.scatter(x, y, marker="D")
plt.plot([x1, x2], [y1, y2], 'k-')
plt.text(x1, max(y1, y2), 'R = ' + str(round(r * 100, 2)) + '%')
plt.title('Linear Regression of ' + str(len(points)) + ' points.')
plt.show()
