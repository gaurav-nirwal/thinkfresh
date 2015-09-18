from scipy import stats
import collections
#import matplotlib.pyplot as plt

# Reduced version of Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

#plt.hist(x=freq.keys(), weights=freq.values())
chi, p= stats.chisquare(freq.values())
print chi #2408.43314652
print p #0.0
