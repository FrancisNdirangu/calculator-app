#will be using tkinter to build a calculator app

from tkinter import *
from tkinter import ttk


def display():
    pass
# tkinter._test()
root = Tk()
root.title('Calculator App')

content = ttk.Frame(root)
content.grid(column=0,row=0)
calculator = ttk.Label(content,text='Calculator',padding=(10,10,10,10))
calculator.grid(column=3,row=0)

oneButton = ttk.Button(content,text='1',command=display)
oneButton.grid(column =2, row=2)
twoButton = ttk.Button(content,text='2')
twoButton.grid(column=3,row=2)
threeButton = ttk.Button(content,text='3')
threeButton.grid(column=4,row=2)

number_clicked = StringVar()
ttk.Label(content,textvariable=number_clicked)





root.mainloop()
#the frame widget will be for holding the contents on the user interface

#lets break down what we need for a calculator app
#we need to open a window
#the window should have the title 'Calculator App'
#in the window should be ten buttons. each button showing the number it represents.
#when a button is pressed it should appear on the screen
#then we should have buttons for add and subtract
#there should also be an = button for running the computation
#when we press a number then click on add then press another then the = button
#the operation between those two numbers should take place

#the = button will have the default setting on so that it can be invoked when the user presses enter