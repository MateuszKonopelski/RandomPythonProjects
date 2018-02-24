'''
You are consultant engaged by a factory which manufactures spoons.

The factory exectuves recently spent $10,000,000 upgrading equipment and
processes in order to combat excessively high defects in manufacturing (23%) which
where leading to high order return rates from clients.

You have been asked to prove (with confidence level of 95%) that new equipment
has improved situation and that the number of defective spoons has decreased
to under 18%. You have been supplied with random sample of 150 spoons and
found that 23 spoons have defects.
'''

import math
from scipy import stats as st
import matplotlib.pyplot as plt
import numpy as np

# Function:
def draw_z_score(x, cond, mu, sigma, p_hat, title):
    '''This function draws a chart with normal distribution with mean, sd
    and based on z score rejection region. Additionally in green is line of
    p_hat so sample mean based on which we reject or not reject h0.'''
    y = st.norm.pdf(x, mu, sigma)
    z = x[cond]
    plt.plot(x, y, color='black')
    plt.fill_between(z, 0 ,st.norm.pdf(z, mu, sigma), facecolor='red')
    plt.plot([p_hat, p_hat], [0, st.norm.pdf(p_hat, mu, sigma)], color='green', lw=2)
    plt.title(title)
    plt.show()

# Variables:
p = 0.18
n = 150
conf_lvl = 0.95

p_hat = 23 / n
sd = math.sqrt((p * (1 - p)))/math.sqrt(n)
z = st.norm.ppf(conf_lvl)
x_critical = p - z*sd

if p_hat < x_critical:
    message = 'There is enough evidence to reject h0.'
else:
    message = 'There is NOT enough evidence to reject h0.'

# Draw Result
x = np.arange(0.08, 0.28, 0.0001)

draw_z_score(x, x < x_critical, p, sd, p_hat, message)
