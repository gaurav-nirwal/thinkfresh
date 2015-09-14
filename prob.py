import matplotlib.pyplot as plt
from collections import Counter
from numpy import arange
import scipy.stats as stats

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
c = Counter(x)
sum_value = sum(c.values())
l = c.keys()

for k,v in c.iteritems():
    print "The Frequency of {0} is {1}".format(k,float(v)/sum_value) #calculate frequency

#boxplot
plt.figure(1)
plt.boxplot(x)
plt.savefig("boxplot_of_number_list.png")

#histogram
plt.figure(2)
bins = arange(11)-.5 # bins: -0.5  0.5  1.5  2.5  3.5  4.5  5.5  6.5  7.5  8.5  9.5
plt.hist(x, bins=bins,histtype='bar', color='green') 
plt.xticks(range(10)) # ticks on x-axis:1-9
plt.xlim([0, 10]) #x-axis
plt.xlabel('Values')
plt.ylabel('Absolute Frequencies')
plt.savefig("histogram_of_number_list.png")

#QQ Plot
plt.figure(3)
qqplot = stats.probplot(x, dist='norm', plot=plt)
plt.savefig("QQPlot_of_number_list.png")