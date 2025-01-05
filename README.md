# Data-Preprocessing-for-COVID-19-Dataset
# Description:
# This script is designed to preprocess a COVID-19 dataset in preparation for further analysis or modeling. The script performs the following key tasks:

# Library Imports: It imports essential libraries for data manipulation, numerical computations, and visualization (numpy, matplotlib.pyplot, pandas).

# Dataset Import: It reads the dataset from an Excel file (Covid_Data_new.xlsx) using pandas. The independent variables (features) and dependent variable (target) are separated into X and Y respectively.

# Handling Missing Data: It uses the SimpleImputer class from sklearn.impute to handle missing data by replacing NaN values with the mean of the corresponding columns. This step is crucial for maintaining the # # integrity of the dataset and ensuring that machine learning models can be trained without errors due to missing values.

# The script includes print statements to display the intermediate results of X and Y after loading the dataset and after handling missing values in specified columns.

import numpy as np
import matplotlib.pyplot as pit
import pandas as pd
data_set=pd.read_excel('Covid_Data_new.xlsx')
X=data_set.iloc[:, :-1].values
Y=data_set.iloc[:,  -1].values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')

imputer.fit(X[:, 0:1])
X[: , 0:1] = imputer.transform(X[:, 0:1])
imputer.fit(X[:, 4:5])
X[: , 4:5] = imputer.transform(X[:, 4:5])
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(), [1])], remainder= 'passthrough')
X=np.array(ct.fit_transform(X))
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
Y=le.fit_transform(Y)
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size = 0.2,random_state=42)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train[:, 6:]=sc.fit_transform(X_train[:, 6:])
X_test[:, 6:]=sc.fit_transform(X_test[:, 6:])
print(X_train)
print(X_test)
print(Y_train)
print(Y_test)
