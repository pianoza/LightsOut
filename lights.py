# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 22:27:33 2015

@author: Kaisar
"""

import Tkinter as tk

class Application(tk.Frame):
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid()
        
        
    def createWidgets(self):
        self.quitButton = tk.Button(master, text = "Quit", command = self.quit)
        self.quitButton.grid()
        
        

if __name__ == '__main__':
    app = Application()
    app.mainloop()