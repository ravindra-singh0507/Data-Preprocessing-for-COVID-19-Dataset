# -*- coding: utf-8 -*-
"""Data Preprocessing Template.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LbwUF-RkNSulLoB7Bhiam5ultn7i25FP

# Data Preprocessing

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as pit
import pandas as pd

"""## Importing Dataset"""

data_set=pd.read_excel('Covid_Data_new.xlsx')
X=data_set.iloc[:, :-1].values
Y=data_set.iloc[:,  -1].values

print(X)

print(Y)

"""


## Handling Missing Data"""

from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean')

imputer.fit(X[:, 0:1])
X[: , 0:1] = imputer.transform(X[:, 0:1])

print(X)

imputer.fit(X[:, 4:5])
X[: , 4:5] = imputer.transform(X[:, 4:5])

print(X)

"""## Encoding Categorical Data

### Encoding independent variables
"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(), [1])], remainder= 'passthrough')
X=np.array(ct.fit_transform(X))

print(X)

"""### Encoding dependent variables"""

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
Y=le.fit_transform(Y)

print(Y)

"""## Splitting data into Test set & Training Set

"""

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(X, Y, test_size = 0.2,random_state=42)

print(X_train)

print(X_test)

print(Y_train)

print(Y_test)

"""## Feature Scaling"""

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train[:, 6:]=sc.fit_transform(X_train[:, 6:])
X_test[:, 6:]=sc.fit_transform(X_test[:, 6:])

print(X_train)