# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 23:20:28 2015

@author: cnx
"""

import numpy as np

def init():
    A = np.arange(25 * 25).reshape(25, 25)
    A.fill(0)
    I = np.identity(5, dtype=np.int)
    B = np.identity(5)
    
    B = np.array([[1, 1, 0, 0, 0],
         [1, 1, 1, 0, 0],
         [0, 1, 1, 1, 0],
         [0, 0, 1, 1, 1],
         [0, 0, 0, 1, 1]])
    #Building A matrix
    for t in range(5):
        for i in range(5):
            for j in range(5):
                A[t*5+i][t*5+j] = B[i][j]
                if t > 0:
                    A[t*5+i][(t-1)*5+j] = I[i][j]
                    A[(t-1)*5+i][t*5+j] = I[i][j]
    return A