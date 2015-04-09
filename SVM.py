# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:12:31 2015

@author: timasemenov
"""

import numpy as np
import scipy.io as sio
from sklearn import cross_validation
from sklearn import svm

data = sio.loadmat('data.mat')
contents_X = data['X']
contents_y = data['y']

y = []
X = []

for i in range(len(contents_y[0])):
    a = contents_X[0, i]
    b = []
    
    for j in range(len(a)):
        for k in range(2):
            b.append(a[j][k])
    if (len(b) == 800):
        X.append(b)
        y.append(contents_y[0][i])


X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.6, random_state=1)

lin_clf = svm.LinearSVC()
lin_clf.fit(X_train, y_train)
count = 0
for i in range(len(y_test)):
    a = lin_clf.predict(X_test[i])
    b = y_test[i]
    print("Predicted value: " + str(a) + ", actual value: " + str(b))
    if (a == b):
        count += 1

print len(y_train)
print "Correctly predicted: " + str(count) + ", total examples: " + str(len(y_test))
    