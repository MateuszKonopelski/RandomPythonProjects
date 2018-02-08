print('''
The team of traders under your supervision earns profits which can be approximated with Laplace distribution.
Profits (of any trade) have a mean of $95.70 and a std. dev. of $1,247.
Your team makes about 100 trades every week.

Questions:
A. What is the probability of my team making a loss in any given week?
B. What is the probability of my team making over $20,000 in any given week?
''')

print('\nSOLUTION\n')

'''
Any distribution (inc Laplace) can be approximated
to Normal Distribution using Central Limit Theorem.
'''

# set up
import math
import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np

# Data
mu = 95.7                           # mean
sigma = 1247                        # standard deviation
n = 100                             # sampling size (trades here)
xcritical1 = 0                      # making a loss
xcritical2 = 20000 / n              # Earning $20k a weak by 100 trades

mu_1 = mu                           # Based on Central Limit Theorem
sigma_1 = sigma / (math.sqrt(n))    # Based on CLT

# Calc
def Z(xcritical, mu, sigma):
    return (xcritical - mu) / sigma     # Standard Score (z-value)

Z1 = Z(xcritical1, mu_1, sigma_1)
Z2 = Z(xcritical2, mu_1, sigma_1)

P1 = st.norm.cdf(Z1)                    # Cumulative Distribution Function for ND
P2 = 1 - st.norm.cdf(Z2)

# Plots
def draw_z_score(x, cond, mu, sigma, title):
    y = st.norm.pdf(x, mu, sigma)                #Probability Density function for ND
    z = x[cond]
    plt.plot(x, y)
    plt.fill_between(z, 0, st.norm.pdf(z, mu, sigma))
    plt.title(title)
    plt.text(-300, 0.0020, r'$\mu=' + str(mu_1) + ',\ \sigma=' + str(sigma_1) + '$')
    plt.show()

x = np.arange(-400, 500, 1)                     # Fixed interval by experimenting
title1 = 'Probability of making loss: ' + '{0:.4g}'.format(P1*100) + '%'
title2 = 'Probability of earning more than $20k: ' + '{0:.4g}'.format(P2*100) + '%'

draw_z_score(x, x < xcritical1, mu_1, sigma_1, title1)
draw_z_score(x, x > xcritical2, mu_1, sigma_1, title2)
