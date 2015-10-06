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

isPlaying = True

def onManConfigButton():
    global isPlaying
    isPlaying = False
    stateLabel.configure(text="Current state: Manual Configuration")

def onPlayButton():
    global isPlaying
    isPlaying = True
    stateLabel.configure(text="Current state: Playing")

def onPressedButton(i):
    if isPlaying:
        column = i % 5
        row = (i - column)/5
        if (row+1)<5:
            lightGrid[(row+1)*5+column].toggle()
        if (row-1)>-1:
            lightGrid[(row-1)*5+column].toggle()
        if (column+1)<5:
            lightGrid[row*5+column+1].toggle()
        if (column-1)>-1:
            lightGrid[row*5+column-1].toggle()
            

rowID = []
columnID = []
lightGrid = []
lightVar = []
config = np.random.randint(2, size=25)

#==============================================================================
# config = config2
# 
# print config
# print config2
#==============================================================================

A = init()
U, nconf = mod2solver(A, config)
result = mod2result(U, nconf)

#==============================================================================
# def click(event):
#     if isPlaying:
#         position = lightVar.index(event.widget.var)
#         if(position%5-1>-1):
#             lightVar[position-1].set((lightVar[position-1].get() + 1) % 2)
#         if(position%5+1<5):
#             lightVar[position+1].set((lightVar[position+1].get() + 1) % 2)
#         if(position-5>-1):
#             lightVar[position-5].set((lightVar[position-5].get() + 1) % 2)
#         if(position+5<25):
#             lightVar[position+5].set((lightVar[position+5].get() + 1) % 2)
#     
#==============================================================================
    
root = Tk()

wideLabel = Label(root, text="Lights Out Game")
wideLabel.grid(columnspan=6, row=0)


for i in range(5):
    rowID.append(Label(root, text=str(i+1)))
    rowID[i].grid(row=i+2, column=0)
    columnID.append(Label(root, text=str(i+1)))
    columnID[i].grid(row=1, column=i+1)
    
lightGrid = []
for numRow in range(5):
    for numColumn in range(5):
        i=numRow*5+numColumn
        lightGrid.append(Checkbutton(root, command=lambda i=i: onPressedButton(i)))
        lightGrid[numRow*5+numColumn].grid(row=numRow+2, column=numColumn+1)
        if config[numRow*5+numColumn]==1:
            lightGrid[numRow*5+numColumn].select()
        else:
            lightGrid[numRow*5+numColumn].deselect()


#==============================================================================
# for numRow in range(5):
#     for numColumn in range(5):
#         lightVar.append(IntVar())
#         lightGrid.append(Checkbutton(root,
#                                      variable=lightVar[numRow*5+numColumn])
#                                      )
#         lightGrid[numRow*5+numColumn].var = lightVar[numRow*5+numColumn]
#         lightGrid[numRow*5+numColumn].var.set(config[numRow*5+numColumn])
#         lightGrid[numRow*5+numColumn].bind("<Button-1>", click)
#         lightGrid[numRow*5+numColumn].grid(row=numRow+2, column=numColumn+1)
#==============================================================================

optionsLabel = Label(root, text="Actions:")
optionsLabel.grid(columnspan=6, row=7)

newConfigurationButton = Button(root, text="New Configuration")
newConfigurationButton.grid(columnspan=6, row=8)

manualConfigurationButton = Button(root, text="Manual Configuration", command=onManConfigButton)
manualConfigurationButton.grid(columnspan=6, row=9)

playButton = Button(root, text="Play", command=onPlayButton)
playButton.grid(columnspan=6, row=10)

solveButton = Button(root, text="Solve")
solveButton.grid(columnspan=6, row=11)

stateLabel = Label(root, text="Current state: Playing")
stateLabel.grid(columnspan=7, row=12)

#==============================================================================
# print config
# print config2
#==============================================================================

print result.reshape(5, 5)

root.mainloop()

