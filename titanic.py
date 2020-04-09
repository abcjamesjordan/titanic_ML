# Titanic Machine Learning program for Kaggle @ https://www.kaggle.com/c/titanic/
# Author: James Jordan
# Start Date: April 9, 2020

#imports see requirements.txt for virtual environment
import numpy as np
import pandas as pd

test = pd.read_csv('data/test.csv', sep=',')
train = pd.read_csv('data/train.csv', sep=',', index_col = 0, header = 0)

train_basic = train.iloc[:, ['survived', 'pclass', 'sex', 'age', 'fare']]

print(train_basic.head())
