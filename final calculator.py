#will be using tkinter to build a calculator app

from tkinter import *
from tkinter import ttk
import numpy

number_array = ['haha']

def displaybutton(buttonpressed):
    number_clicked.set(buttonpressed)
    
    number_array.append(buttonpressed)
    print(number_array)
    # print('the sum of the array would be:', sum(number_array))
# tkinter._test()

def calculate(buttonpressed):
    pass 



def equals():
    # print(number_array)
    pass
    # pass
#currently focusing on fixing the addition before the equals is added

#the main thing i must remember about this calculator is that i will be doing one operation per step
#this means that i must either do the operation then save the final number
#if i was to do this with addition then the algorithm would be such
#add the number to an array
#press the add button, this will add the + sign into the array
#press the second number, which will add it to the array
#then we will press the equals button
#the equals button will take the contents of the array located at the even contents of the array
#turn them into integers
#then compare what the sign is inbetween them
#if the sign is a plus the function will add the two integers and display that answer on the screen

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

equals_sign = ttk.Button(content,text='=',command=equals())
equals_sign.grid(column=5,row=3 )

addbutton = ttk.Button(content, text='+',command = calculate(number_clicked))
addbutton.grid(column=5,row=2)



root.mainloop()
#the frame widget will be for holding the contents on the user interface

#lets break down what we need for a calculator app
#we need to open a window
#the window should have the title 'Calculator App'
#in the window should be ten buttons. each button showing the number it represents.
#I think what we should do is the following
#everytime we click on a number that number should go into an array
#when you click on a sign like addition that sign should also go into the array
#when you click = it should turn the numbers into integers
#it should remove the quotes from the operation sign then it should evaluate the calculation
#the calculation can be evaluated by adding the numbers in a loop
#the previous number should be added to the next
#then the result is saved into an array
#then the next number is selected and added into the next number
