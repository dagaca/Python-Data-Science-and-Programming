# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 01:02:33 2022

@author: Damla
"""

from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

# %% load data
iris = load_iris()

x = iris.data
y = iris.target

# %% normalization data
x = (x-np.min(x)) / (np.max(x) - np.min(x))

# %% train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

# %% knn model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 3)

# %% K-fold CV K = 10
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = knn, X = x_train, y = y_train, cv = 10)
print("average accuracy: ", np.mean(accuracies))
print("average std: ", np.std(accuracies))

# %% test
knn.fit(x_train, y_train)
print("test accuracy: ", knn.score(x_test,y_test))

# %% grid search cross validation with knn
from sklearn.model_selection import GridSearchCV

grid = {"n_neighbors": np.arange(1,50)}
knn = KNeighborsClassifier()

knn_cv = GridSearchCV(knn, grid, cv = 10) # GridSearchCV
knn_cv.fit(x,y)

# %% print hyperparameter K value in KNN algorithm 
print("hyperparameter K: ", knn_cv.best_params_)
print("best accuracy: ", knn_cv.best_score_)

# %% grid search cross validation with logistic regression
x = x[:100,:]
y = y[:100]

# normalization data
x = (x-np.min(x)) / (np.max(x) - np.min(x))

# train test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)

from sklearn.linear_model import LogisticRegression

grid = {"C":np.logspace(-3,3,7), "penalty":["none","l2"]} # l1 = lasso ve l2 = ridge

logreg = LogisticRegression()
logreg_cv = GridSearchCV(logreg, grid, cv = 10)
logreg_cv.fit(x_train,y_train)

print("hyperparameters: ", logreg_cv.best_params_)
print("best accuracy: ", logreg_cv.best_score_)

# %% test
logreg = LogisticRegression(C=1, penalty = "none")
logreg.fit(x_train, y_train)
print("test accuracy: ", logreg.score(x_test,y_test))
