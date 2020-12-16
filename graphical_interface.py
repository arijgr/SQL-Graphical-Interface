from tkinter import *


#pip install cx-Oracle
import cx_Oracle

#create connection

connection = cx_Oracle.connect('username/password@IP:Port/DatabaseName')
cur = connection.cursor()

#for result in cur:
#    print(result)
#cur.close()
#connection.close()    

#create one first window
window = Tk()

#customization
window.title("Theatre Database Application")
window.geometry("720x480")
window.minsize(480,360)
window.iconbitmap("theatre.ico")
window.config(background='#41B77F')

#frame
frame =Frame(window,bg='#41B77F')
frame.pack(pady=50)

# text1
title = Label(frame,text='Bienvenue sur "Theatre Database Application"' ,font=("Courrier",20),bg='#41B77F',fg='white')
title.pack()

# text1
title = Label(frame,text="Veuillez entrer l'instruction à exécuter.." ,font=("Courrier",10),bg='#41B77F',fg='white')
title.pack()


#TextBox
textBox = Text(frame, height=2, width=40)
textBox.pack(pady=25)

def listener():
    #read input data
    instruction = textBox.get("1.0",END)
    #print(instruction)
    #cur.execute(str(instruction))
    

#Button
button = Button(frame,text="Rechercher",font=("Courrier",20),bg='white',fg='#41B77F',command=listener)
button.pack()






#display app
window.mainloop()
