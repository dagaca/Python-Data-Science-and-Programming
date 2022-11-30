# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 17:21:26 2022

@author: Damla
"""

import pandas as pd

# %% import twitter data 
data = pd.read_csv(r"gender-classifier.csv", encoding = "latin1")
data = pd.concat([data.gender,data.description], axis = 1)
data.dropna(axis = 0, inplace = True)
data.gender = [1 if each == "female" else 0 for each in data.gender]

# %% cleaning data
# regular expression RE
import re

first_description = data.description[4]
description = re.sub("[^a-zA-Z]", " ", first_description) # a dan z ye ve A dan Z ye olanları bulma geri kalanları " " (space) ile değiştir
description = description.lower() # büyük harfleri küçük harflere çevir

# %% stopwords (irrelavent words) -> gereksiz kelimeler

import nltk # natural language tool kit
nltk.download('wordnet') # "wordnet" corpus adında bir klasöre indiriliyor
from nltk.corpus import stopwords

description = description.split()

# split yerine tokenizer kullanabiliriz
# description = nltk.word_tokenize(description)

# split kullanırsak "shouldn't" gibi kelimeler "should" ve "not" olarak iki kelimeye ayrılmaz ama word_tokenize() ile ayrılır.
# %% 
# gereksiz kelimeleri çıkarma işlemi
description = [word for word in description if not word in set(stopwords.words("english"))]

# %%
# lemmatization loved -> love   gitmeyeceğim -> git

import nltk as nlp

lemma = nlp.WordNetLemmatizer()
description = [lemma.lemmatize(word) for word in description]

description = " ".join(description)

# %%
# Yukarıda tek bir veri ile yapılacak işlemler test edildi. Bu aşamada tüm data için aynı işlemler uygulanacak.

description_list = []
for description in data.description:
    description = re.sub("[^a-zA-Z]", " ", description)
    description = description.lower()
    description = description.split()
    # description = [word for word in description if not word in set(stopwords.words("english"))]
    lemma = nlp.WordNetLemmatizer()
    description = [ lemma.lemmatize(word) for word in description]
    description = " ".join(description)
    description_list.append(description)

# %% bag of words

from sklearn.feature_extraction.text import CountVectorizer # bag of words yaratmak için kullanılan metot
max_features = 5000

count_vectorizer = CountVectorizer(max_features = max_features, stop_words = "english")
sparce_matrix = count_vectorizer.fit_transform(description_list).toarray() # x

print("En Sık Kullanılan {} Kelime: {}".format(max_features,count_vectorizer.get_feature_names()))

# %%
y = data.iloc[:,0].values # male or female classes
x = sparce_matrix

# train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 42)

# %% naive bayes
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(x_train,y_train)

# %% prediction
y_pred = nb.predict(x_test)

print("Accuracy: ", nb.score(y_pred.reshape(-1,1), y_test))