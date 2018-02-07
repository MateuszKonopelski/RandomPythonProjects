'''Generating Random Numbers that Follow a Normal Distribution'''

print('''

Generate two distributions with random numbers separatly for men and women.
1000 observations for each group.
Men's height has mean of 175.5 cm and standard deviation of 7.4 cm
Women's height has mean of 161.8 cm and standard deviation of 6.9 cm.

Exercise:
1. Show both distributions
2. Identify the minimum height of 2.2% of tallest people in both groups.



REZULT:
''')

import random
import numpy

mu_m, sigma_m = 175.5, 7.4
mu_f, sigma_f = 161.8, 6.9
j = 1000 - 0.02 * 1000

women = []
for i in range(1000):
    women.append(random.gauss(mu_f, sigma_f))
print('1000 observations for women: ', [str('{0:.5g}'.format(i)) + ' cm' for i in women])
print('Minium height of 2.2% tallest women is: ', '{0:.5g}'.format(sorted(women)[980]), 'cm.')

men = []
for i in range(1000):
    men.append(random.gauss(mu_m, sigma_m))
print('1000 observations for men: ', [str('{0:.5g}'.format(i)) + ' cm' for i in men])
print('Minium height of 2.2% tallest men is:', '{0:.5g}'.format(sorted(men)[980]), 'cm.')