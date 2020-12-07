# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:04:49 2019

@author: Soham Shah
"""

from sklearn.linear_model import LinearRegression

x = [[6,2],[8,1],[10,0],[14,2],[18,0]]
y = [[7],[9],[13],[17.5],[18]]

model = LinearRegression()

model.fit(x,y)
X_test = [[8,2],[9,0],[11,2],[16,2],[12,0]]
y_test = [[11],[8.5],[15],[18],[11]]
predictions = model.predict(X_test)
for i,predictions in enumerate(predictions):
    print('Predicted: %s,Target: %s' %(predictions, y_test[i]))
    
print(model.score(X_test,y_test))


