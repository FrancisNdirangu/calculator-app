#will be using tkinter to build a calculator app

from tkinter import *
from tkinter import ttk


def displaybutton(buttonpressed):
    number_clicked.set(buttonpressed)
# tkinter._test()

def addition(buttonpressed):
    #what i need is to get the button pressed and add it to an array
    #i should do this for every button pressed
    #the addition will then be done after the equals button is pressed
    addition_array = []
    addition_array = addition_array.append(buttonpressed)
    #the algorithm would be this
    #you press a button. that button gets saved in an array
    #you then press the plus button
    #you then press the second button
    #then you press the equals sign
    #the summation is then done

root = Tk()
root.title('Calculator App')

content = ttk.Frame(root)
content.grid(column=0,row=0)
calculator = ttk.Label(content,text='Calculator',padding=(10,10,10,10))
calculator.grid(column=3,row=0)

oneButton = ttk.Button(content,text='1',command=lambda buttonpressed = '1': displaybutton(buttonpressed))
oneButton.grid(column =2, row=2)
twoButton = ttk.Button(content,text='2',command=lambda buttonpressed= '2':displaybutton(buttonpressed))
twoButton.grid(column=3,row=2)
threeButton = ttk.Button(content,text='3',command=lambda buttonpressed='3': displaybutton(buttonpressed))
threeButton.grid(column=4,row=2)

number_clicked = StringVar()
ttk.Label(content,textvariable=number_clicked).grid(row=1,column=3)


#the next thing we can do is to create an addition button and an equals button
#what can happen is numbers keep getting added into an array then when we press the equals button
#the numbers get added up.
#find a way of programming pemdas into code.

#i will now add the addition button
addbutton = ttk.Button(content, text='+',command = lambda buttonpressed = '+':displaybutton(buttonpressed))
addbutton.grid(column=5,row=2)

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