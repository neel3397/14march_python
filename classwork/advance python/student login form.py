import tkinter

#create screen

screen=tkinter.Tk()

screen.title("student login")

screen.geometry("500x500")

#tkinter variable
email_var=tkinter.StringVar()
password_var=tkinter.StringVar()
msg_var=tkinter.StringVar()

#python function

def myfun():
    msg_var.set(email_var.get())

lbl=tkinter.Label(screen,text="login form",font=("arial",26,"bold"))
lbl.pack()

#id display
e1_lbl=tkinter.Label(screen,text="enter id",font=("arial",12,"bold"))
e1_lbl.place(x=50,y=60)
e1=tkinter.Entry(screen)
e1.place(x=180,y=60)



#email display
e2_lbl=tkinter.Label(screen,text="enter email",font=("arial",12,"bold"))
e2_lbl.place(x=50,y=80)
e2=tkinter.Entry(screen,textvariable=email_var)
e2.place(x=180,y=80)


#password display
e3_lbl=tkinter.Label(screen,text="enter password",font=("arial",12,"bold"))
e3_lbl.place(x=50,y=100)

e3=tkinter.Entry(screen,textvariable=password_var)
e3.place(x=180,y=100)

#message display
msg_lbl=tkinter.Label(screen,text="message",textvariable=msg_var)
msg_lbl.place(x=18,y=160)



#button display
button=tkinter.Button(screen,text="student login",font=("arial",12,"bold"),bg="black",fg="white",command=myfun)
button.place(x=180,y=130)












screen.mainloop()
