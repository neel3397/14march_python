"""tkinter module: it is used to build gui applications-

gui-graphical user interface"""

import tkinter

#create screen

screen=tkinter.Tk()

screen.title("my first application")

screen.geometry("500x500")

def myfun():
    print("this is button click event")

#lbl=tkinter.Label(screen,text="hello and welcome to my application",font=("arial",20,"bold"))
#lbl.place(x=20,y=50)

button1=tkinter.Button(screen,text="call1",bg="black",fg="blue",font=("arial",20,"bold"))
button1.grid(row=0,column=0)
button2=tkinter.Button(screen,text="call1",bg="black",fg="blue",font=("arial",20,"bold"))
button2.grid(row=1,column=1)
button3=tkinter.Button(screen,text="call1",bg="black",fg="blue",font=("arial",20,"bold"))
button3.grid(row=0,column=2)

button=tkinter.Button(screen,text="click here",bg="black",fg="blue",font=("arial",20,"bold"),command=myfun)
button.grid(row=1,column=0)



screen.mainloop()
