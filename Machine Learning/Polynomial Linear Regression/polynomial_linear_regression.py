# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 12:27:28 2022

@author: Damla
"""
# import library
import pandas as pd 
import matplotlib.pyplot as plt

# import data
df = pd.read_csv("polynomial_regression.csv", sep = ";")

x = df.araba_fiyat.values.reshape(-1,1)
y = df.araba_max_hiz.values.reshape(-1,1)

# data visualization
plt.scatter(x,y)
plt.ylabel("Araba Max Hızı")
plt.xlabel("Araba Fiyatı")
plt.show()

# linear regression =  y = b0 + b1*x
# multiple linear regression   y = b0 + b1*x1 + b2*x2

#%% linear regression
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x,y)

#%% linear regression predict
y_head = lr.predict(x)
plt.plot(x,y_head,color="red",label="Linear Regression")
plt.show()

print("10 milyon TL değerinde arabanın hız tahmini: ", lr.predict(10000)) # 3 sıfır eksik yazıldı bilerek.

#%% polynomial regression
# polynomial regression =  y = b0 + b1*x +b2*x^2 + b3*x^3 + ... + bn*x^n
from sklearn.preprocessing import PolynomialFeatures
polynomial_regression = PolynomialFeatures(degree = 2)

# transform
x_polynomial = polynomial_regression.fit_transform(x)

# fit
linear_regression2 = LinearRegression()
linear_regression2.fit(x_polynomial,y)

#%% polynomial regression predict
y_head2 = linear_regression2.predict(x_polynomial)
plt.plot(x,y_head2,color="green",label="Polynomial Regression")
plt.legend()
plt.show()