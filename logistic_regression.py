import pandas as pd
import statsmodels.api as sm
import math as m

ld = pd.read_csv('D:\Thinkful\Files\loansData_clean.csv')

ld['IR_TF'] = [1 if x<12 else 0 for x in ld['Interest.Rate']*100]

ld['Intercept'] = 1.0
ind_vars = ['Amount.Requested', 'FICO.Score', 'Intercept']
ld['IR_TF'].head()

logit = sm.Logit(ld['IR_TF'], ld[ind_vars])
result = logit.fit()
coeff = result.params

def logistic_function(coeff, FICOScore, LoanAmount):
    p = 1/(1 + m.exp(-coeff['Intercept']-coeff['FICO.Score']*FICOScore-coeff['Amount.Requested']*LoanAmount))
    return p

# probablity of getting a loan of $10,000 with a FICO score of 720
prob = logistic_function(coeff, 720, 10000) 
print prob
#0.7459