
from tkinter import *

window= Tk()
window.title('prima interfaccia tkinter')

def km_to_miles():
    print(e1_value.get())
    miles = float(e1_value.get()) * 1.6
    t1.insert(END, miles)


b1= Button(window, text= 'Execute', command= km_to_miles) # il primo paramentro deve essere la variabile WINDOW
b1.grid(column=0, row=0, pady=2, padx=2) # metodo per posizionare il bottone


e1_value=StringVar()
e1= Entry(window, textvariable= e1_value)
e1.grid(column=1, row=0)

t1= Text(window, height=1, width=20)
t1.grid(column=3, row=0)

window.mainloop() # to let the program open - always necessary, otherwise the program closes immmediately
