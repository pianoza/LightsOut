# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:08:01 2015

@author: cnx
"""

import numpy as np
from mod2solver import mod2solver
from mod2result import mod2result

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

b = np.array([0, 1, 1, 1, 0,
              0, 0, 0, 1, 1,
              1, 1, 1, 1, 0,
              1, 0, 0, 0, 1,
              0, 1, 1, 1, 1])

u, bc = mod2solver(A, b, 25)
result = mod2result(u,bc)
print u
print bc
print result

x = np.zeros(25)
#take x25 and x24 = 0
for i in range(0, 25):
    u[i][23] = 0
    u[i][24] = 0
for i in range(22, -1, -1):
    if u[i][i] == 0:
        x[i] = 0
    else:
        k = 0
        for j in range(24, i, -1):
            k += u[i][j]
        x[i] = (bc[i] + k) % 2
    for j in range(i, -1, -1):
        u[j][i] *= x[i]

print x.reshape(5, 5)