# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 14:25:22 2022

@author: aditi
"""

'''
a gradient measures the change in all weights with regard to the error
higher the gradient, the steeper the slope and faster a model can learn 
g = partial derivative with respect to its inputs
in ML it is a derivative of a func that has more than one input variable-slope
gradient reduces as the top of the hill approaches

derivatives learned in maths classes: power rule
chain rule

'''
#importing the dataset
import pandas as pd
import seaborn as sns
housing = pd.read_csv('data.csv')
housing.head()

#normalising the data
housing = (housing- housing.mean())/housing.std()
housing.head()

#simple linear regression
#Set variable X with size
x = housing['Size']

#Set varibale y with price
y = housing['Price']
sns.pairplot(housing,x_vars='Size',y_vars='Price',size=6,aspect=0.6,kind='scatter')



