# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:12:31 2015

@author: timasemenov
"""


import scipy.io as sio
from sklearn import cross_validation
from sklearn import svm

# loads data
data = sio.loadmat('data.mat')
X = data['X']
contents_y = data['y']

y = []

# convert y from cell array to int array
for i in range(len(contents_y[0])):
    y.append(contents_y[0][i])

# divide data into train and test sets
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.4, random_state=1)

# create a Support Vector Machine classifier
clf = svm.SVC(kernel='poly', degree=4)
clf.fit(X_train, y_train)
count = 0       # counter for correctly predicted values

for i in range(len(y_test)):
    a = clf.predict(X_test[i])
    b = y_test[i]
    print("Predicted value: " + str(a[0]) + ", actual value: " + str(b))
    if (a == b):
        count += 1

print str(len(y_train)) + " examples used to train the model"
print "Correctly predicted : " + str(count) + ", total examples: " + str(len(y_test)) + ", percentage: " + str(count*100.0/len(y_test))