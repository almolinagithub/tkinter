
from tkinter import *

window = Tk()
window.title('weights converter, enter  weight in kg:')

def converter_fun():
    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274
    t1.insert(END, grams)
    t2.insert(END, pounds)
    t3.insert(END, ounces)


e1_value=StringVar()
e1= Entry(window, textvariable = e1_value)
e1.grid(row=0, column=2)

b1= Button(window, text= 'convert', command = converter_fun)
b1.grid(row=2, column=2 , padx=2, pady=1 , rowspan= 3)



t1= Text(window, height=1, width= 10)
t1.grid(row=5, column = 2)
t2= Text(window, height=1, width= 10)
t2.grid(row=6, column = 2)
t3= Text(window, height=1, width= 10)
t3.grid(row=7, column = 2)

window.mainloop()
