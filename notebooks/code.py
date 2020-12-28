import numpy as np
import pandas as pd
from scipy import stats
from sklearn.preprocessing import StandardScaler
import scipy.io
from scipy.io import loadmat

def calc_sri(X, time_scale, distribution, start_date=None, end_date=None):
    month_cols = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    distr_dict = {'gamma': stats.gengamma, 
                  'gev': stats.genextreme,
                  'expo': stats.expon,
                  'lognorm' : stats.lognorm,
                  'weibull' : stats.dweibull}
    if start_date!=None and end_date != None:
        X_scale = X.loc[start_date:end_date,'Discharge'].rolling(time_scale).sum()
    elif start_date!=None and end_date == None:
        X_scale = X.loc[start_date:,'Discharge'].rolling(time_scale).sum()
    elif start_date==None and end_date != None:
        X_scale = X.loc[:end_date,'Discharge'].rolling(time_scale).sum()
    else:
        X_scale = X['Discharge'].rolling(time_scale).sum()
    X_scale.fillna(0, inplace=True)
    X_np = X_scale.to_numpy()
    df_shape = X_scale.shape
    res = 12 - df_shape[0]%12
    X_np = np.append(X_np,res*[0])
    X_np[X_np==np.nan] = np.finfo(float).eps
    X_np[X_np<=0] = np.finfo(float).eps
    X_np = np.reshape(X_np,(-1,12))
    
    sri = []
    loglikelihood = []
    for i in range(12):
        if distribution=='gamma':
            a,c,loc,scale = distr_dict[distribution].fit(X_np[:,i])
            cdf_fitted = distr_dict[distribution].cdf(X_np[:,i], a, c)
            loglikelihood.append(distr_dict[distribution].logpdf(X_np[:,i], a, c).sum())
        elif distribution=='gev':
            a,loc,scale = distr_dict[distribution].fit(X_np[:,i])
            cdf_fitted = distr_dict[distribution].cdf(X_np[:,i], a)
            loglikelihood.append(distr_dict[distribution].logpdf(X_np[:,i], a).sum())
        elif distribution=='expo':
            loc,scale = distr_dict[distribution].fit(X_np[:,i])
            cdf_fitted = distr_dict[distribution].cdf(X_np[:,i], 1/scale)
            loglikelihood.append(distr_dict[distribution].logpdf(X_np[:,i], 1/scale).sum())
        elif distribution=='lognorm':
            s,loc,scale = distr_dict[distribution].fit(X_np[:,i])
            cdf_fitted = distr_dict[distribution].cdf(X_np[:,i], s)
            loglikelihood.append(distr_dict[distribution].logpdf(X_np[:,i], s).sum())
        elif distribution=='weibull':
            c,loc,scale = distr_dict[distribution].fit(X_np[:,i])
            cdf_fitted = distr_dict[distribution].cdf(X_np[:,i], c)
            loglikelihood.append(distr_dict[distribution].logpdf(X_np[:,i], c).sum())

        cdf_fitted[cdf_fitted<=0.0] = np.finfo(float).eps
        sri.append(stats.norm.ppf(cdf_fitted))
    return np.transpose(sri), np.array(loglikelihood)

############################################################################################################
def calculate_aic(n, loglike, num_params):
    aic = -loglike + 2 * num_params
    return aic
    
#############################################################################################################   
data_dict = loadmat('./Vijayawada_runoff.mat')
data_dict.items
data_array =list(data_dict.values())
data=np.array(data_array[3:])
data=data.flatten()
df=pd.DataFrame(data)
df1=pd.DataFrame(pd.date_range(start='1965-01', periods=600, freq='M'))
frames=[df1,df]
daily_discharge=pd.concat(frames,axis=1)
daily_discharge.head()
daily_discharge.columns = ['Date', 'Discharge']
daily_discharge = daily_discharge.set_index('Date')
discharge_monthly_sum = daily_discharge[['Discharge']].resample('M').sum()
sri_np, logl = calc_sri(discharge_monthly_sum, time_scale=1, distribution='lognorm')
df_sri = pd.DataFrame(np.ravel(sri_np)[0:discharge_monthly_sum.shape[0]], columns=['SRI'])
df_sri = df_sri.set_index(daily_discharge.index)
df_sri.head()
daily_discharge['SRI'] = df_sri['SRI']
daily_discharge.to_csv('sri.csv',index=False)
