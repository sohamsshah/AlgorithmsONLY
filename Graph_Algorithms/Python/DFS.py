# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:00:55 2020

@author: Soham Shah
"""

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        print(self.graph)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def DFSUtil(self,v,visited):
        visited[v] = True
        print(v,end=' ')
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)
    def DFS(self,v):
        visited = [False]*(max(self.graph)+1)
        self.DFSUtil(v,visited)
        self.DFS_iterative(v,visited)
    def DFS_iterative(self,v, visited):
        stack = [v]
        while stack:
            v = stack[-1]  
            stack.pop() 
            if (not visited[v]):  
                print(v,end=' ')
                visited[v] = True
            for node in self.graph[v]:  
                if (not visited[node]):  
                    stack.append(node)  
                    
            
        
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
  
print("Following is DFS from (starting from vertex 2)") 
g.DFS(2)
g.DFS_iterative(2)
    
