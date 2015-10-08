# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 13:54:28 2015

@authors: daudt, kaisar
"""

from Tkinter import *
from mod2solver import mod2solver
from mod2result import mod2result
from init import *
import numpy as np

#declaring variables
rowID = []
columnID = []
lightGrid = []
lightVar = []
config = []
boardState = np.zeros(25)
root = Tk()
solutionScreenVar = StringVar()

def isSolved(state):
    return not np.count_nonzero(state)

def onPressedButton(i):
    #print i
    column = i % 5
    row = (i - column)/5
    global lightGrid
    global boardState
    #print "before:\n{}".format(boardState.reshape(5, 5))
    boardState[row*5+column] = (boardState[row*5+column] + 1) % 2
    if (row+1)<5:
        lightGrid[(row+1)*5+column].toggle()
        boardState[(row+1)*5+column] = (boardState[(row+1)*5+column] + 1) % 2
    if (row-1)>-1:
        lightGrid[(row-1)*5+column].toggle()
        boardState[(row-1)*5+column] = (boardState[(row-1)*5+column] + 1) % 2
    if (column+1)<5:
        lightGrid[row*5+column+1].toggle()
        boardState[row*5+column+1] = (boardState[row*5+column+1] + 1) % 2
    if (column-1)>-1:
        lightGrid[row*5+column-1].toggle()
        boardState[row*5+column-1] = (boardState[row*5+column-1] + 1) % 2
    if isSolved(boardState):
        solutionScreenVar.set("Well Done!")
    #print "after:\n{}".format(boardState.reshape(5, 5))    

def onNewGameButton():
    global config
    global lightGrid
    global boardState
    config = getConfig()
    lightGrid = []
    boardState = config.copy()
    for numRow in range(5):
        for numColumn in range(5):
            i=numRow*5+numColumn
            lightGrid.append(Checkbutton(root, 
                                         command=lambda i=i: onPressedButton(i),
                                         width=10,
                                         height=6,
                                         indicatoron=0
                                        )
                            )
            lightGrid[numRow*5+numColumn].grid(row=numRow+2, column=numColumn+1)
            if config[numRow*5+numColumn]==1:
                lightGrid[numRow*5+numColumn].select()
            else:
                lightGrid[numRow*5+numColumn].deselect()
    solutionScreenVar.set("New Game")

def getSolution(config):
    A = init()
    U, nconf = mod2solver(A.copy(), config.copy())
    #print U
    return mod2result(U.copy(), nconf.copy())
    
def onShowSolutionButton():
    solutionFormatted = getSolution(boardState.copy())
    solutionFormatted = solutionFormatted.reshape(5, 5)
    solutionScreenVar.set(solutionFormatted)

wideLabel = Label(root, text="Lights Out Game")
wideLabel.grid(columnspan=6, row=0)

#start new game
onNewGameButton()

optionsLabel = Label(root, text="Actions:")
optionsLabel.grid(columnspan=6, row=7)

newGameButton = Button(root, text="New game", command=onNewGameButton)
newGameButton.grid(columnspan=6, row=8)

showSolutionButton = Button(root, text="Show solution", command=onShowSolutionButton)
showSolutionButton.grid(columnspan=6, row=9)

solutionScreen = Label(root, textvariable=solutionScreenVar)
solutionScreen.grid(columnspan=6, row = 10)


root.mainloop()

