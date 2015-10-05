# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 13:54:28 2015

@author: daudt
"""

from Tkinter import *
from mod2solver import mod2solver
from mod2result import mod2result
from init import *
import numpy as np

rowID = []
columnID = []
lightGrid = []
lightVar = []
config = np.random.randint(2, size=25)

A = init()
U, nconf = mod2solver(A, config)
result = mod2result(U, nconf)

def click(event):
    position = lightVar.index(event.widget.var)
    if(position%5-1>-1):
        lightVar[position-1].set((lightVar[position-1].get() + 1) % 2)
    if(position%5+1<5):
        lightVar[position+1].set((lightVar[position+1].get() + 1) % 2)
    if(position-5>-1):
        lightVar[position-5].set((lightVar[position-5].get() + 1) % 2)
    if(position+5<25):
        lightVar[position+5].set((lightVar[position+5].get() + 1) % 2)
    
    
root = Tk()

wideLabel = Label(root, text="Lights Out Game")
wideLabel.grid(columnspan=5, row=0)

for i in range(5):
    rowID.append(Label(root, text=str(i+1)))
    rowID[i].grid(row=i+2, column=0)
    columnID.append(Label(root, text=str(i+1)))
    columnID[i].grid(row=1, column=i+1)

for numRow in range(5):
    for numColumn in range(5):
        lightVar.append(IntVar())
        lightGrid.append(Checkbutton(root,
                                     variable=lightVar[numRow*5+numColumn])
                                     )
        lightGrid[numRow*5+numColumn].var = lightVar[numRow*5+numColumn]
        lightGrid[numRow*5+numColumn].var.set(config[numRow*5+numColumn])
        lightGrid[numRow*5+numColumn].bind("<Button-1>", click)
        lightGrid[numRow*5+numColumn].grid(row=numRow+2, column=numColumn+1)

optionsLabel = Label(root, text="Actions:")
optionsLabel.grid(columnspan=5, row=7)

# Change to button
newConfigurationButton = Label(root, text="New Configuration Button")
newConfigurationButton.grid(columnspan=5, row=8)

# Change to button
manualConfigurationButton = Label(root, text="Manual Configuration Button")
manualConfigurationButton.grid(columnspan=5, row=9)

# Change to button
solveButton = Label(root, text="Solve Button")
solveButton.grid(columnspan=5, row=10)



print result.reshape(5, 5)
root.mainloop()
