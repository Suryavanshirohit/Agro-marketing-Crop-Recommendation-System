import pandas as pd
import numpy as np
import itertools
import statsmodels.api as sm
import warnings 

warnings.filterwarnings("ignore", category=DeprecationWarning)
mydateparser = lambda dates: pd.datetime.strptime(dates,'%Y/%d/%m')  #lambda x: pd.datetime.strptime(x,'%d/%m/%Y')
y = pd.read_csv(r'E:\crop_prediction\PRICE_DATA\COTTON.csv')#,  parse_dates=[0], index_col=0, squeeze=True, date_parser=mydateparser)
        
        
# Define the p, d and q parameters to take any value between 0 and 2
p = d = q = range(0, 2)

# Generate all different combinations of p, q and q triplets
pdq = list(itertools.product(p, d, q))

# Generate all different combinations of seasonal p, q and q triplets
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]


warnings.filterwarnings("ignore") # specify to ignore warning messages

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)

            results = mod.fit()
            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
            minAIC[round(results.aic,2)]=(param, param_seasonal)

        except:
            continue
        
        
        
Fparam=((1,0,0),(0,0,0,12))
print(Fparam)
y = y.dropna()
ny = np.array(y['PRICE'])
mod = sm.tsa.statespace.SARIMAX(ny,
                                order=Fparam[0],
                                seasonal_order=Fparam[1],
                                enforce_stationarity=False,
                                enforce_invertibility=False)

results = mod.fit()

print(results.summary().tables[1])


# Get forecast 5 steps ahead in future
pred_uc = results.get_forecast(steps=3)
# Get confidence intervals of forecasts
pred_ci = pred_uc.conf_int()
print(pred_ci[0])
c = pd.DataFrame(pred_ci)

a,b = c[0] , c[1] 
a,b = pd.DataFrame(a) , pd.DataFrame(b)
a = list(a[0])
b = list(b[1])
a.extend(b)

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from pylab import rcParams
rcParams['figure.figsize'] = 10, 6

plt.figure(figsize=(10,6))
plt.grid(True)
plt.xlabel('DATE')
plt.ylabel('Close Price')
plt.plot(a)
#plt.plot(b)
#plt.plot(data['Close'])
plt.title('')
plt.show('TATA Closing Price')


