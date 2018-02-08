'''Generating Random Numbers that Follow a Normal Distribution'''

print('''

Generate two distributions with random numbers separatly for men and women.
1000 observations for each group.
Men's height has mean of 175.5 cm and standard deviation of 7.4 cm
Women's height has mean of 161.8 cm and standard deviation of 6.9 cm.

Exercise:
1. Show both samples
2. Identify the minimum height of 2.2% of tallest people in both groups.
3. Show the histogram


RESULT:
''')

import numpy
import matplotlib.pyplot as plt

mu_m, sigma_m = 175.5, 7.4
mu_f, sigma_f = 161.8, 6.9

female = numpy.random.normal(mu_f, sigma_f, 1000)
print('1000 observations for women: ', [str('{0:.5g}'.format(i)) + ' cm' for i in female])
# Because top 2.2% of normal distribution falls into mean + 2sd
print('Minimum height of 2.2% tallest women is: ', '{0:.5g}'.format(mu_f + 2 * sigma_f), 'cm.')

male = numpy.random.normal(mu_m, sigma_m, 1000)
print('1000 observations for men: ', [str('{0:.5g}'.format(i)) + ' cm' for i in male])
print('Minimum height of 2.2% tallest men is:', '{0:.5g}'.format(mu_m + 2 * sigma_m), 'cm.')

plt.hist(male, bins='auto', label='Male')
plt.hist(female, bins='auto', label='Female')
plt.title("height histogram")
plt.legend(loc='upper right')
plt.show()

