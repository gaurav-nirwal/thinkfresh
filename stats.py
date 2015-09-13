import pandas as pd
from scipy import stats #for obtaining mode

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

data = data.splitlines() # split the string into seperate lines
data = [i.split(', ') for i in data] # split each line on ', ' and return a list 

column_names = data[0]
rows = data[1:]
df = pd.DataFrame(rows, columns=column_names)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# apply functions for mean. median, mode, range, std deviation and variance
print "The mean for the Alcohol and Tobacco dataset is " + str(mean(df['Alcohol'] + df['Tobacco']))
print "The median for the Alcohol and Tobacco dataset is " + str(median(df['Alcohol'] + df['Tobacco']))
print "The mode for the Alcohol and Tobacco dataset is " + str(stats.mode(df['Alcohol'] + df['Tobacco']))
print "The standard deviation for the Alcohol and Tobacco dataset is " + str((df['Alcohol'] + df['Tobacco']).std())
print "The variance for the Alcohol and Tobacco dataset is " + str((df['Alcohol'] + df['Tobacco']).var())
print "The range for the Alcohol and Tobacco dataset is " + str(max(df['Alcohol'] + df['Tobacco']) - min(df['Alcohol'] + df['Tobacco']))



