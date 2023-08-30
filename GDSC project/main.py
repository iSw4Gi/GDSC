#GDSC Students 
#Data Analysis Project
#Auther : iSw4Gi = Nader ALharbi
# v.1


import matplotlib as pl
import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from matplotlib.figure import Figure
import matplotlib.pyplot as pl
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

#backend switching
pl.switch_backend('TkAgg')
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        #window title
        self.title('GDSC')
        #this for adding image to the window 
        try:
            p1 = PhotoImage(file= r'C:\Users\Admin\Desktop\GDSC\GDSC project\logo.png')
            self.iconphoto(False,p1)
        except FileNotFoundError:
            print("put your logo.png dict in : p1")

        

        
        #this is the level's of the analysis
        levels= [6,12,8,16,15]
        #it's look like converted but bealive me this how it showld look 
        intrested = [0,50,100,150, 200]
        # the GDSC colors
        bar_colors = ['red', 'blue', 'green', 'yellow']
        
        #the figurs implemntation
        fig = Figure(figsize=(6,4) ,dpi=100)
        fig_canvas = FigureCanvasTkAgg(fig, self)
        NavigationToolbar2Tk(fig_canvas,self)
        #the GUI
        axes = fig.add_subplot()
        axes.bar(levels,intrested,color=bar_colors)
        axes.set_title("GDSC Tabuk")
        fig_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



#for running the App
if __name__ == '__main__':
    app = App()
    app.mainloop()