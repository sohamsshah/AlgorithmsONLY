# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 10:36:36 2019

@author: Soham Shah
"""

import matplotlib.pyplot as plt
from sklearn.datasets.samples_generator import make_blobs

from sklearn.cluster import KMeans

X,y_true = make_blobs(n_samples = 300, centers = 4, cluster_std = 0.6,random_state = 0)

plt.scatter(X[:,0], X[:,1],s=50)

kmeans= KMeans(n_clusters = 1)
kmeans.fit(X)

y = kmeans.predict(X)

plt.scatter(X[:,0],X[:,1], c = y, s=50,cmap = 'viridis')

centers = kmeans.cluster_centers_

plt.scatter(centers[:,0],centers[:,1],c = [1],s=200,alpha = 0.5)