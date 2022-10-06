# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 10:44:43 2022

@author: Damla
"""
# import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#%% import data
df = pd.read_csv("linear_regression_dataset.csv", sep = ";")

#%% data visualization
plt.scatter(df.deneyim, df.maas)
plt.xlabel("Deneyim")
plt.ylabel("Maaş")
plt.show()

#%% linear regression
from sklearn.linear_model import LinearRegression

linear_reg = LinearRegression()

x = df.deneyim.values.reshape(-1,1)
y = df.maas.values.reshape(-1,1)

linear_reg.fit(x,y)

#%% prediction
b0 = linear_reg.predict([[0]]) # x=0 iken b0, b0=constant(bias)
print("b0: ", b0)

b0_ = linear_reg.intercept_ # intercept = y eksenini kestiği nokta yani b0
print("b0_: ",b0_)

b1 = linear_reg.coef_ # coeff yani eğim(slope)
print("b1: ", b1)

# y = b0 + b1*x
# maas = 1663 + 1138 * deneyim

maas_yeni = 1663 + 1138*11
print(maas_yeni)

linear_reg_pred = linear_reg.predict([[11]])
print(linear_reg_pred)

#%% visualize line
array = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]).reshape(-1,1)

plt.scatter(x,y)
plt.show()

y_head = linear_reg.predict(array) # maas tahminleri
plt.plot(array, y_head, color="green")
