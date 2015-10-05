# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 13:54:28 2015

@author: daudt
"""

from Tkinter import *

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
            
def onPlayButton():
    global isPlaying
    isPlaying = True
    stateLabel.configure(text="Current state: Playing")

def onManConfigButton():
    global isPlaying
    isPlaying = False
    stateLabel.configure(text="Current state: Manual Configuration")

# Variable that stores state -> 0 means manual input and 1 means playing game
isPlaying = False

root = Tk()

wideLabel = Label(root, text="Lights Out Game")
wideLabel.grid(columnspan=6, row=0)

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
        i=numRow*5+numColumn
        lightGrid.append(Checkbutton(root, command=lambda i=i: onPressedButton(i)))
        lightGrid[numRow*5+numColumn].grid(row=numRow+2, column=numColumn+1)

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

stateLabel = Label(root, text="Current state: Manual Configuration")
stateLabel.grid(columnspan=7, row=12)

root.mainloop()