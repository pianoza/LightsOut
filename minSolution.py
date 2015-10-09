# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:07:14 2015

@author: daudt, kaisar
"""
import numpy as np
from operator import add

def minSolution(x):
    n1 = [0, 1, 1, 1, 0,
          1, 0, 1, 0, 1,
          1, 1, 0, 1, 1,
          1, 0, 1, 0, 1,
          0, 1, 1, 1, 0]
    
    n2 = [1, 0, 1, 0, 1,
          1, 0, 1, 0, 1,
          0, 0, 0, 0, 0,
          1, 0, 1, 0, 1,
          1, 0, 1, 0, 1,]
           
    n3 = np.mod(map(add, n1, n2),2)
    
    solutions = []
    
    solutions.append(x)
    solutions.append(np.mod(map(add, x, n1),2))
    solutions.append(np.mod(map(add, x, n2),2))
    solutions.append(np.mod(map(add, x, n3),2))
        
    minPresses = 25
    minIndex = 0
    for i in range(4):
        if countOnes(solutions[i])<minPresses:
            minPresses = countOnes(solutions[i])
            minIndex = i
            print i
    print minPresses
    return solutions[minIndex].copy()
    
def countOnes(x):
    counter = 0    
    for i in range(25):
        if x[i]==1:
            counter = counter+1
            
    return counter