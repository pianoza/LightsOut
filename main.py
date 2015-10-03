# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 13:54:28 2015

@author: daudt
"""

from Tkinter import *

#==============================================================================
# def paintWhite(event):
#     wideLabel.configure(background='white')
# 
# def paintBlack(event):
#     wideLabel.configure(background='black')
#==============================================================================


root = Tk()

wideLabel = Label(root, text="Lights Out Game")
wideLabel.grid(columnspan=5, row=0)

#==============================================================================
# wideLabel.bind("<Button-1>",paintWhite)
# wideLabel.bind("<Button-3>",paintBlack)
#==============================================================================

rowID = []
columnID = []

for i in range(5):
    rowID.append(Label(root, text=str(i+1)))
    rowID[i].grid(row=i+2, column=0)
    columnID.append(Label(root, text=str(i+1)))
    columnID[i].grid(row=1, column=i+1)
    

lightGrid = []
for numRow in range(5):
    for numColumn in range(5):
        lightGrid.append(Checkbutton(root))
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




root.mainloop()