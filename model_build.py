# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 20:11:57 2022

@author: Navi
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("D:\ken_jee_project\eda_data.csv")
df
#selecting the required columns
df.columns

df_model = df[['average_salary','Rating', 'Size', 'Type of ownership', 'Industry', 'Sector', 'Revenue',
             'num_comp', 'Per Hour', 'Employer Provided','True_hq','State',
             'Company_age',
             'python', 'rstudio', 'spark', 'aws', 'excel', 'seniority',
             'job_position', 'description_length']]
#Creating dummy variables
df_dum = pd.get_dummies(df_model)
#train test split

from sklearn.model_selection import train_test_split
X = df_dum.drop('average_salary', axis = 1)
y = df_dum['average_salary'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Multiple linear regression
#Using statsmodels
import statsmodels.api as sma
X_sma = X = sma.add_constant(X)
model = sma.OLS(y,X_sma)
model.fit().summary()

#Using sklearn
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

smodel = LinearRegression()
smodel.fit(X_train, y_train)

np.mean(cross_val_score(smodel, X_train, y_train, scoring = 'neg_mean_absolute_error', cv= 3))
#Lasso Regression
lm_l = Lasso()
np.mean(cross_val_score(lm_l, X_train, y_train, scoring = 'neg_mean_absolute_error', cv= 3))

alpha = []
error = []

for i in range(1, 100):
    alpha.append(i/100)
    lm_la = Lasso(alpha = (i/100))
    error.append(np.mean(cross_val_score(lm_la, X_train, y_train, scoring = 'neg_mean_absolute_error', cv= 3)))
    
plt.plot(alpha, error)
 
err = tuple(zip(alpha, error))
df_err = pd.DataFrame(err, columns = ['alpha', 'error'])
df_err[df_err['error'] == df_err['error'].max()]
lm_l = Lasso(alpha = 0.16)
lm_l.fit(X_train, y_train)

#Random Tree
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(criterion='mse', max_features='log2', n_estimators=170)
rf.fit(X_train, y_train)
np.mean(cross_val_score(rf, X_train, y_train, scoring = 'neg_mean_absolute_error', cv= 3))

#Tune models using GridsearchCV algorithm
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10), 'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}

gs = GridSearchCV(rf, parameters, scoring = 'neg_mean_absolute_error', cv = 3)
gs.fit(X_train, y_train)

gs.best_score_
best_estimator1 = gs.best_estimator_

# test ensembles 
tpred_smodel = smodel.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = best_estimator1.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,tpred_smodel)
mean_absolute_error(y_test,tpred_lml)
mean_absolute_error(y_test,tpred_rf)

mean_absolute_error(y_test,(tpred_smodel+tpred_rf)/2)

best_estimator1
#RandomForestRegressor(criterion='mse', max_features='log2', n_estimators=170)

import pickle
pickl = {'model': rf}
pickle.dump( pickl, open( 'model_file' + ".p", "wb" ) )

file_name = "model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']
      
model.predict(X_test.iloc[1, :].values.reshape(1,-1))

list(X_test.iloc[1, :])

