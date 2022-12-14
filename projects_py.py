# -*- coding: utf-8 -*-
"""projects.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o7NIYFmjAnzuGaeS4R79XkrNJrZlw-qh
"""

!pip install nltk
!pip install sklearn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
import nltk
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LogisticRegression
from lightgbm import LGBMRegressor
from xgboost.sklearn import XGBRegressor
!pip install catboost
from catboost import CatBoostRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import BayesianRidge
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR

df = pd.read_csv('auto_costs (1).csv')
data = pd.DataFrame(df)
data.isnull().sum()

data.head(30)

data['name'] = data['name'].apply(lambda x: x.split(' ')[0])
print(data)

data['name'].value_counts()

data['name'].unique()

# models = {'maxda': 'mazda', 'Nissan': 'nissan','porcshce': 'porsche','toyouta': 'toyota','vokswagen': 'volkswagen', 'vw': 'volkswagen'}
# def clean_name(name):
#   for i in name:
#     if i in models.keys():
#       return models[i]
#     else:
#       return i
# clean_name(data['name'])



data['doornumbers'] = data['doornumbers'].map({'two': 2, 'four': 4})
data

count = data['name'].value_counts()

plt.figure(figsize = (20,6))

plt.subplot(1,3,1)
plt1 = count.plot(kind='bar')
plt.title('Companies')
plt1.set(xlabel = 'Car Company', ylabel='Frequency of Car Company')

plt.subplot(1,3,2)
plt1 = data.carbody.value_counts().plot(kind='bar')
plt.title('Car Type')
plt1.set(xlabel = 'Car Type', ylabel='Frequency of Car type')

plt.subplot(1,3,3)
plt1 = data.fueltypes.value_counts().plot(kind='bar')
plt.title('Fuel Type')
plt1.set(xlabel = 'Fuel Type', ylabel='Frequency of fuel type')

encode_data = pd.DataFrame() 
label = preprocessing.LabelEncoder()
list_encode_name = pd.DataFrame()
for x in  data.columns:
    if( data[x].dtype == 'object'):
        list_encode_name[x] =  data[x]
        encode_data[x] = label.fit_transform( data[x] )
    else:
        encode_data[x] = data[x]
encode_data

# Finding all the numerical columns in the dataset. 
numCols = data.select_dtypes(include=['int64','float'])

# Sorting the columns
numCols = numCols[sorted(numCols.columns)]

# Printing the columns
print(numCols.columns)

#columns_1 = numCols.drop('ID', 'symboling', 'name', 'fueltypes', 'aspiration', 'doornumbers', 'enginetype', 'fuelsystem', 'compressionratio', 'peakrpm', )

plt.figure(figsize=(20,60))

# Dropping the price column from the plot since we dont need to plot a scatter plot for price
numCols = data.drop('price',axis=1)

# running a for-loop to print the scatter plots for all numerical columns
for i in range(len(numCols.columns)):
    # Creating a sub plot
    plt.subplot(len(numCols.columns),2,i+1)
    # Creating a scatter plot
    plt.scatter(data[numCols.columns[i]],data['price'])
    # Assigning a title to the plot
    plt.title(numCols.columns[i]+' vs Price')
    # Setting the y label
    plt.ylabel('Price')
    # setting the x label
    plt.xlabel(numCols.columns[i])


# printing all the plots
plt.tight_layout()

# data['cylindernumber'] = data['cylindernumber'].map({'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'eight': 8})
# data['cylindernumber']

#corr_1 = data[['cylindernumber','price','wheelbase', 'carlength', 'carheight', 'carwidth', 'curbweight', 'enginesize','doornumbers', 'carlength' ,'compressionratio','horsepower', 'boreratio','peakrpm','citympg']]#.corr()
corr_2 = encode_data.corr()
corr_2

plt.figure(figsize =(20,15))
ax = sns.heatmap(corr_2, annot=True,)

from sklearn import linear_model 
from sklearn.metrics import r2_score 
from sklearn.linear_model import LinearRegression
 

x = encode_data.drop('price', axis=1)
y = encode_data.price
x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.3, random_state=16)
x

madel_1 = LinearRegression().fit(x_train, y_train) # practice the model
madel_1

madel_2 = LGBMRegressor().fit(x_train, y_train)
madel_2

madel_3 = XGBRegressor().fit(x_train, y_train)
madel_3

madel_4 = CatBoostRegressor().fit(x_train, y_train)

madel_5 = KernelRidge().fit(x_train, y_train)

madel_6 = ElasticNet().fit(x_train, y_train)

madel_7 = BayesianRidge().fit(x_train, y_train)

madel_8 = GradientBoostingRegressor().fit(x_train, y_train)

list_madels = [madel_1, madel_2, madel_3, madel_4, madel_5, madel_6, madel_7, madel_8]  # add the model to the list
rmse_test =[] # empty list for rmse
r2_test =[]   # empty list for r2

 # check each model and add the result to the empty lists
for madel in list_madels:
  predict = madel.predict(x_test)
  rmse_test.append( round( np.sqrt( mean_squared_error(y_test, predict) ), 4 ) )
  r2_test.append( round(r2_score(y_test, predict) , 4 ) )

 # passing the result to a dataframe
madel_name = "LinearRegression LGBMRegressor XGBRegressor CatBoostRegressor KernelRidge ElasticNet BayesianRidge GradientBoostingRegressor".split()
result = pd.DataFrame({'RMSE':rmse_test,'R2_Test':r2_test}, index = madel_name)
result







import pandas
from sklearn import linear_model

df = pandas.read_csv("auto_costs (1).csv")

X = df[['carlength','carheight', 'curbweight', 'enginesize', 'stroke', 'compressionratio','horsepower', 'peakrpm', ]]
y = df['price']

regr = linear_model.LinearRegression()
regr.fit(X, y)

#predict the CO2 emission of a car where the weight is 2300kg, and the volume is 1300cm3:
predictedCO2 = regr.predict([[168.8,  48.8, 2548, 130, 2.68, 9, 111, 5000,]])
print()
print(predictedCO2)



