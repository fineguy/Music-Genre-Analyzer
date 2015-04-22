# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:12:31 2015

@author: timasemenov
"""

from __future__ import division
import scipy.io as sio
from sklearn import cross_validation
from sklearn.qda import QDA

# loads data
data = sio.loadmat('data.mat')
X = data['X']
contents_y = data['y']

y = []

# convert y from cell array to int array
for i in range(len(contents_y[0])):
    y.append(contents_y[0][i])

# divide data into train, cross validation and train sets
X_train, X, y_train, y = cross_validation.train_test_split(X, y, test_size=0.4, random_state=1)
X_cross, X_test, y_cross, y_test = cross_validation.train_test_split(X, y, test_size=0.5, random_state=3)

# classifier regularization parameter
p_best = 0
count_best = 0

# begin training model
print 'Training model in progress...'

for j in range(200):
    p = 0.02*j
    clf = QDA(reg_param=p)
    clf.fit(X_train, y_train)
    count = 0
    
    # fit in the test set
    for i in range(len(y_cross)):
        a = clf.predict(X_cross[i])
        b = y_cross[i]
        if (a == b):
            count += 1
            
    # update the regularization parameter
    if count > count_best:
        count_best = count
        p_best = p
        
    print "Progress at %.1f%%" %(j/2)

print 'Training model completed' 

# test the model
clf = QDA(reg_param=p_best)
clf.fit(X_train, y_train)
count = 0
size = len(y_test)

# fit in the test set
for i in range(size):
    a = clf.predict(X_test[i])
    b = y_test[i]
    #print("Predicted value: " + str(a[0]) + ", actual value: " + str(b))
    if (a == b):
        count += 1

print "%d examples used to train the model" %(len(y_train))
print "%d examples used to tune the model" %(len(y_cross))
print "Correctly predicted : %d, total examples: %d, success rate: %.2f%%" %(count, size, count*100.0/size)