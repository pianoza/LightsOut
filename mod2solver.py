# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 18:26:31 2015

@authors: daudt, kaisar
"""
import numpy as np


def mod2solver(A,b,size=25):
    # Loop over each row
    for row in range(size):
        if A[row][row] == 0:
            #look for non zero pivot
            newPivot = -1
            for findPivot in range(row+1,size):
                if A[findPivot][row] == 1:
                    newPivot = findPivot
                    break
            #swap rows
            if newPivot > -1:
                
                A[row],A[newPivot] = A[newPivot].copy(),A[row].copy() 
                b[row],b[newPivot] = b[newPivot].copy(),b[row].copy()
                #should I worry about final cases here?
        for otherRows in range(row+1, size):
            #clear column under current pivot
            if A[otherRows][row] == 1:
                A[otherRows] = np.mod(A[otherRows]+A[row], 2)
                b[otherRows] = np.mod(b[otherRows]+b[row], 2)
                
    return A,b