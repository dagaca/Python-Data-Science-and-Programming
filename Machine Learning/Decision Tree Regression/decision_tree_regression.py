# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 18:21:27 2022

@author: Damla
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("decision_tree_regression_dataset.csv", sep = ";", header = None)

x = df.iloc[:,0].values.reshape(-1,1)
y = df.iloc[:,1].values.reshape(-1,1)

#%% decision tree regression
from sklearn.tree import DecisionTreeRegressor
tree_reg = DecisionTreeRegressor()
tree_reg.fit(x,y)

#tree_reg.predict([[5.5]])
x_ = np.arange(min(x),max(x),0.01).reshape(-1,1)
y_head = tree_reg.predict(x_)

#%% visualization
plt.scatter(x, y, color="red") # verinin(df) x ve y eksenindeki gösterimi
plt.plot(x_,y_head,color="green") # 1-10 arasında 0.01 artan bir array'ın tahmin grafiği
plt.xlabel("Tribün Seviyesi")
plt.ylabel("Ücret")
plt.show()