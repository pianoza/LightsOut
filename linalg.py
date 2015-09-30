# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:08:01 2015

@author: cnx
"""

import numpy as np

A = np.arange(25 * 25).reshape(25, 25)
A.fill(0)
I = np.identity(5, dtype=np.int)
B = np.identity(5)

B = np.array([[1, 1, 0, 0, 0],
     [1, 1, 1, 0, 0],
     [0, 1, 1, 1, 0],
     [0, 0, 1, 1, 1],
     [0, 0, 0, 1, 1]])

N1 = np.array([0, 1, 1, 1, 0,
               1, 0, 1, 0, 1,
               1, 1, 0, 1, 1,
               1, 0, 1, 0, 1,
               0, 1, 1, 1, 0])
N2 = np.array([1, 0, 1, 0, 1,
               1, 0, 1, 0, 1,
               0, 0, 0, 0, 0,
               1, 0, 1, 0, 1,
               1, 0, 1, 0, 1])
N1 = N1.reshape(25, 1)
N2 = N2.reshape(25, 1)
#Building A matrix
for t in range(5):
    for i in range(5):
        for j in range(5):
            A[t*5+i][t*5+j] = B[i][j]
            if t > 0:
                A[t*5+i][(t-1)*5+j] = I[i][j]
                A[(t-1)*5+i][t*5+j] = I[i][j]

#Test cases
b = np.array([1, 0, 1, 0, 0,
              1, 0, 0, 1, 1,
              0, 1, 1, 1, 0,
              0, 1, 1, 0, 0,
              0, 0, 1, 1, 0])              

#b = b.reshape(25, 1)


print A
print b
#Elimination
for i in range(24):
    for j in range(i+1, 25):
        if A[i][i] == 0:
            ok = False
            non_zero = i
            for t in range(j, 25):
                if A[j][i] != 0:
                    non_zero = j
                    ok = True
                    break
            if ok == True:
                A[i], A[non_zero] = A[non_zero], A[i]
                b[i], b[non_zero] = b[non_zero], b[i]

        if A[i][i] != 0 and A[j][i] != 0:
            for t in range(i, 25):
                A[j][t] = (A[j][t] + A[i][t]) % 2
                b[j] = (b[j]+b[i]) % 2
print A
print b