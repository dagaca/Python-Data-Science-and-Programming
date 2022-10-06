# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 01:46:43 2022

@author: Damla
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import data
data = pd.read_csv("data.csv")

data.drop(["id", "Unnamed: 32"], axis = 1, inplace = True)

M = data[data.diagnosis == "M"]
B = data[data.diagnosis == "B"]

data.diagnosis = [1 if each == "M" else 0 for each in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"], axis=1)

# normalization
x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data))

# train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1)

#%% Naive bayes
from sklearn.naive_bayes import GaussianNB

nb = GaussianNB()
nb.fit(x_train,y_train)

#%% test
print("Accuracy of Naive Bayes Algorithm: ", nb.score(x_test,y_test))