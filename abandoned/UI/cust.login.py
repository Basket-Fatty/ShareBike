from tkinter import *
from PIL import Image,ImageTk

window = Tk()
window.title("Customer Login")
window.geometry('600x750')
window.configure(bg='#BFEFFF')

#functions
def login():
    pass
def clear():
    pass

frame = Frame(bg='#BFEFFF')

#heading and logo
main_logo = ImageTk.PhotoImage(file="ss.jpg")
label = Label(frame, image = main_logo)
label.grid(row=0,column=0,columnspan=2)

login_lbl = Label(frame, text="Log In", bg='#BFEFFF', fg="black", font=("Arial", 30))
login_lbl.grid(row=1, column=0, columnspan=2, pady=40)

#details 
email_lbl = Label(frame, text="Email", bg='#BFEFFF', fg="black", font=("Arial", 16))
email_lbl.grid(row=2, column=0)

email_e = Entry(frame, font=("Arial", 13))
email_e.grid(row=2, column=1, pady=20)

password_lbl = Label(frame, text="Password ", bg='#BFEFFF', fg="black", font=("Arial", 16))
password_lbl.grid(row=3, column=0)

password_e = Entry(frame, font=("Arial", 13))
password_e.grid(row=3, column=1, pady=20)

#buttons
login_btn = Button(frame, text="Log In", bg="#96CDCD", fg="black", font=("Arial", 16), command=login)
login_btn.grid(row=4, column=0, pady=30)

clear_btn = Button(frame, text="Clear", bg="#96CDCD", fg="black", font=("Arial", 16), command=clear)
clear_btn.grid(row=4,column=1,pady=30)

#links to redirect
lbl1= Label(frame, text= "Forgot Password?", cursor= "hand2",bg='#BFEFFF', fg= "black", font= ('Aerial 18'))
lbl1.grid(row=5,columnspan=2,pady=20)

lbl2= Label(frame, text= "Create New Account !", cursor= "hand2",bg='#BFEFFF', fg= "black", font= ('Aerial 18'))
lbl2.grid(row=6,columnspan=2)

frame.pack()

window.mainloop()