import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats #for QQ-Plot


loansdata = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansdata.dropna(inplace=True) 

loansdata.boxplot(column='Amount.Requested')
plt.savefig('loansdata_boxplot.png')

minreq = loansdata['Amount.Requested'].min() #1000
maxreq = loansdata['Amount.Requested'].max() #35000

bins = [minreq, 5000, 10000, 15000, 20000, 25000, 30000, maxreq] #specifying the bins for the histogram
loansdata.hist(column='Amount.Requested', bins=bins)
plt.xticks(bins) #show the ticks on the x-axis
plt.xlim(0, 35000) # x-axis start and end
plt.savefig('loansdata_histogram.png')

stats.probplot(loansdata['Amount.Requested'], dist="norm", plot=plt)
plt.savefig('loansdata_qqplot.png')

'''the minimum amount requested is 1000, however, some investors offer very low amounts against the requested amount (in low hundreds). Most amounts requested and 
funded are in the 5000 to 15000 range with the median being 10000. In either case the amounts are not normally distributed'''