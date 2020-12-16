from tkinter import *
#import tkinter as tk

window = Tk()
listbox_widget = Listbox(window)

#for entry in listbox_entries:
#    listbox_widget.insert(END, entry)

#TextBox
textBox = Text(window, height=2, width=40)
textBox.pack(pady=25)

def listener():
    #read input data
    listbox_widget.delete(0,END)
    instruction = textBox.get("1.0",END)
    listbox_widget.insert(END, instruction)
    #print(instruction)
    #cur.execute(str(instruction))
    

#Button
button = Button(window,text="Rechercher",font=("Courrier",20),bg='white',fg='#41B77F',command=listener)
button.pack()

listbox_widget.pack()
window.mainloop()
