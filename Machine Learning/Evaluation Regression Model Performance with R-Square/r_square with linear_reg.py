# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 19:57:31 2022

@author: Damla
"""

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

y_head = linear_reg.predict(x)

plt.plot(x,y_head,color="red")

#%% r_square
from sklearn.metrics import r2_score

print("r_square score: ", r2_score(y,y_head))