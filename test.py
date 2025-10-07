# -*- coding: utf-8 -*-

from sklearn.datasets import fetch_california_housing

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

df=fetch_california_housing()

df

dataset=pd.DataFrame(df.data)
print(dataset)

dataset.columns=df.feature_names
dataset.head()

df.target.shape

dataset['Price']=df.target
dataset.head()

X=dataset.iloc[:,:-1] #independent feature
y=dataset.iloc[:,-1] # dependent feature

"""**Linear Regression**"""

from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
mse=cross_val_score(lin_reg,X,y,scoring='neg_mean_squared_error',cv=5)
mean_mse=np.mean(mse)
print(mean_mse)

"""**Ridge Regression**"""

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
ridge=Ridge()
paramters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}
ridge_regressor=GridSearchCV(ridge,paramters,scoring='neg_mean_squared_error',cv=5)
ridge_regressor.fit(X,y)

print(ridge_regressor.best_params_) #which lambda was suitable
print(ridge_regressor.best_score_)

"""**Lasso Regression**"""

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso
lasso=Lasso()
paramters={'alpha':[1e-15,1e-10,1e-8,1e-3,1e-2,1,5,10,20,30,35,40,45,50,55,100]}
lasso_regressor=GridSearchCV(lasso,paramters,scoring='neg_mean_squared_error',cv=5)
lasso_regressor.fit(X,y)
print(lasso_regressor.best_params_)
print(lasso_regressor.best_score_)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)

prediction_lasso=lasso_regressor.predict(X_test)
prediction_ridge=ridge_regressor.predict(X_test)

import seaborn as sns
sns.displot(y_test-prediction_lasso,kde=True)

import seaborn as sns
sns.displot(y_test-prediction_ridge,kde=True)