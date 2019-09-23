import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing
import pickle
import requests
import json

# Importing the dataset
train=pd.read_csv('training.csv')

X=train[['LIMIT_BAL', 'PAY_1', 'AGE', 'EDUCATION', 'SEX']]  # Features
y=train['TARGET'] #Target

# Split dataset into training set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


# ### 1. RANDOM FOREST
# ##### IMPORT LIBRARY
from sklearn.ensemble import RandomForestClassifier

clf=RandomForestClassifier(random_state=20) #pick random sample
clf.fit(X_train,y_train)


# ##### GET THE RESULT
y_pred=clf.predict(X_test)


# ##### CONFUSION MATRIX

# untuk ngitung true positive, false positive
#conf=confusion_matrix(y_test, y_pred)
#print('True positive\t: ', conf[0,0])
#print('False positive\t: ', conf[0,1])
#print('True negative\t: ', conf[1,0])
#print('False negative\t: ', conf[1,1])


# ##### ACCURACY
# Model Accuracy, how often is the classifier correct?
#print("Accuracy: %.2f" % metrics.accuracy_score(y_test, y_pred))
#print("Precission: %.2f" % metrics.precision_score(y_test, y_pred)) #precision : true positive
#print("Recall: %.2f" % metrics.recall_score(y_test, y_pred)) #recall : false positive
#print("AUC: %.2f" % metrics.roc_auc_score(y_test, y_pred))


# Saving model to disk
pickle.dump(clf, open('random_forest.pkl','wb'))

# Loading model to compare the results
model = pickle.load( open('random_forest.pkl','rb'))
print(model.predict([[30000,0,22,2,1]]))