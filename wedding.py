# All invites with 2 guests
%matplotlib inline 
from numpy.random import binomial
from numpy import mean, std
import matplotlib.pyplot as plt
from math import sqrt, pow
trial_results = []
invited = 100
guests_per_invite = 2
probability = 0.75
trials = 100000
print "Computed mean:  {0:.2f}".format(invited*guests_per_invite*probability)
print "Computed stdev: {0:.2f}".format(
    sqrt(invited*((1.0-probability)*probability*pow(guests_per_invite, 2))))

for i in range(trials):
    trial_results.append(guests_per_invite * binomial(invited, probability))

print "Monte Carlo mean: {0:.2f}".format(mean(trial_results))

print "Monte Carlo stdev: {0:.2f}".format(std(trial_results))
plt.hist(trial_results, bins=100, range=(100, 200))
plt.show()