import pandas as pd
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

#remove % symbol from interest rate and convert to float
loansData['Interest.Rate'] = [float(interest[0:-1])/100 for interest in loansData['Interest.Rate']]
intrate = loansData['Interest.Rate']

#remove "month" at the end of loan length and convert to integer
loansData['Loan.Length'] = [int(length[0:-7]) for length in loansData['Loan.Length']]
loanamount = loansData['Amount.Requested']

#create a new column called Fico Score with lower limit value
loansData['FICO.Score'] = [int(val.split('-')[0]) for val in loansData['FICO.Range']]
fico = loansData['FICO.Score']

# dependent variable
y = np.matrix(intrate).transpose()

#independent variables
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamount).transpose()

x = np.column_stack([x1,x2])
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

f.summary() #output the model
