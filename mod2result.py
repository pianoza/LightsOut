# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 22:34:35 2015

@author: daudt
"""

import numpy as np

def mod2result(U,bc):
    x = np.zeros(25)
    
    for i in range(22, -1, -1):
        temp = bc[i]
        for j in range(25):
            temp += x[j]*U[i][j]
        x[i] = np.mod(temp,2)
        
    return x.reshape(5, 5)

