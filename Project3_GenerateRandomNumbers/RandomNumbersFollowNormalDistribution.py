'''Generating Random Numbers that Follow a Normal Distribution'''

print('''

Generate two distributions with random numbers separatly for men and women.
1000 observations for each group.
Men's height has mean of 175.5 cm and standard deviation of 7.4 cm
Women's height has mean of 161.8 cm and standard deviation of 6.9 cm.

Exercise:
1. Show both distributions
2. Identify the minimum height of 2.2% of tallest people in both groups.



RESULT:
''')

import numpy

mu_m, sigma_m = 175.5, 7.4
mu_f, sigma_f = 161.8, 6.9
j = 1000 - 0.02 * 1000

female = numpy.random.normal(mu_f, sigma_f, 1000)
print('1000 observations for women: ', [str('{0:.5g}'.format(i)) + ' cm' for i in female])
print('Minium height of 2.2% tallest women is: ', '{0:.5g}'.format(sorted(female)[980]), 'cm.')

male = numpy.random.normal(mu_m, sigma_m, 1000)
print('1000 observations for men: ', [str('{0:.5g}'.format(i)) + ' cm' for i in male])
print('Minium height of 2.2% tallest men is:', '{0:.5g}'.format(sorted(male)[980]), 'cm.')