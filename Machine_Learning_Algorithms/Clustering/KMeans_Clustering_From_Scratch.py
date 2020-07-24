# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 23:59:35 2019

@author: Soham Shah
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import random as rd

dataset=pd.read_csv('Mall_Customers.csv')
dataset.describe()


X = dataset.iloc[:, [3, 4]].values

m=X.shape[0] #number of training examples
n=X.shape[1] #number of features. Here n=2
n_iter=100

K=5 # number of clusters


Centroids=np.array([]).reshape(n,0)


for i in range(K):
    rand=rd.randint(0,m-1)
    
    Centroids=np.c_[Centroids,X[rand]]
    
    
Output={}

EuclidianDistance=np.array([]).reshape(m,0)

Y={}


for i in range(n_iter):
     #step 2.a
      EuclidianDistance=np.array([]).reshape(m,0)
      for k in range(K):
          tempDist=np.sum((X-Centroids[:,k])**2,axis=1)
          EuclidianDistance=np.c_[EuclidianDistance,tempDist]
      C=np.argmin(EuclidianDistance,axis=1)+1
     #step 2.b
      Y={}
      for k in range(K):
          Y[k+1]=np.array([]).reshape(2,0)
      for i in range(m):
          Y[C[i]]=np.c_[Y[C[i]],X[i]]
     
      for k in range(K):
          Y[k+1]=Y[k+1].T
    
      for k in range(K):
          Centroids[:,k]=np.mean(Y[k+1],axis=0)
      Output=Y
      
      
plt.scatter(X[:,0],X[:,1],c='black',label='unclustered data')
plt.xlabel('Income')
plt.ylabel('Number of transactions')
plt.legend()
plt.title('Plot of data points')
plt.show()


color=['red','blue','green','cyan','magenta']
labels=['cluster1','cluster2','cluster3','cluster4','cluster5']
for k in range(K):
    plt.scatter(Output[k+1][:,0],Output[k+1][:,1],c=color[k],label=labels[k])
plt.scatter(Centroids[0,:],Centroids[1,:],s=300,c='yellow',label='Centroids')
plt.xlabel('Income')
plt.ylabel('Number of transactions')
plt.legend()
plt.show()