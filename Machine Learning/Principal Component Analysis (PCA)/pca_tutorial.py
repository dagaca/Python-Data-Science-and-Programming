# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 21:55:56 2022

@author: Damla
"""

from sklearn.datasets import load_iris
import pandas as pd

# %%
iris = load_iris()

data = iris.data
feature_names = iris.feature_names
y = iris.target

df = pd.DataFrame(data,columns = feature_names)
df["sinif"] = y

x = data

# %%
from sklearn.decomposition import PCA
pca = PCA(n_components = 2, whiten = True) # whiten = normalize
pca.fit(x)

x_pca = pca.transform(x)

print("variance ratio: ", pca.explained_variance_ratio_)

print("sum: ", sum(pca.explained_variance_ratio_))