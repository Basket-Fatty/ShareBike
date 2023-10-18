from tkinter import*
from PIL import Image,ImageTk
import tkinter.font as tkFont

window = Tk()
window.title("Customer Login")
window.geometry('800x1000')
window.configure(bg='#BFEFFF')

#functions
def signup():
    pass

def clear():
    pass

def viewselected():
    pass

frame = Frame(bg='#BFEFFF')

#heading and logo
main_logo = ImageTk.PhotoImage(file="ss.jpg")
label = Label(frame, image = main_logo)
label.grid(row=0,columnspan=3)


login_lbl = Label(frame, text="Sign Up", bg='#BFEFFF', fg="black", font=("Arial", 30))
login_lbl.grid(row=1, column=0, columnspan=3, pady=20)

#details
lbl1=Label(frame,text="Sign Up for", bg='#BFEFFF', fg="black", font=("Arial", 16))
lbl1.grid(row=2,column=0,columnspan=3)
#radio button
r1_v = IntVar()

r1 = Radiobutton(frame, text='Customer', variable=r1_v, value='Customer',bg='#BFEFFF', fg="black", font=("Arial", 13))
r1.grid(row=3,column=0,padx=30,pady=30)

r2 = Radiobutton(frame, text='Operator', variable=r1_v,value='Operator',bg='#BFEFFF', fg="black", font=("Arial", 13))
r2.grid(row=3,column=1)

r3 = Radiobutton(frame, text='Manager', variable=r1_v,value='Manager',bg='#BFEFFF', fg="black", font=("Arial", 13))
r3.grid(row=3,column=2)

name = Label(frame, text="Name : ", bg='#BFEFFF', fg="black", font=("Arial", 16))
name.grid(row=4, column=0)

name_e = Entry(frame, font=("Arial", 13))
name_e.grid(row=4, column=1, pady=20)

email = Label(frame, text="Email : ", bg='#BFEFFF', fg="black", font=("Arial", 16))
email.grid(row=5, column=0)

email_e = Entry(frame, font=("Arial", 13))
email_e.grid(row=5, column=1, pady=20)

phone = Label(frame, text="Contact No. : ", bg='#BFEFFF', fg="black", font=("Arial", 16))
phone.grid(row=6, column=0)

phone_e = Entry(frame, font=("Arial", 13))
phone_e.grid(row=6, column=1, pady=20)

#dropdown
gender = Label(frame, text="Gender : ", bg='#BFEFFF', fg="black", font=("Arial", 16))
gender.grid(row=7, column=0,pady=20)
my_list = ["Male","Female","Other"]
options = StringVar(frame)
options.set("Select")
om1 =OptionMenu(frame, options, *my_list)
om1.config(width=15,font=("Arial",12))
om1.grid(row=7,column=1)
menu=frame.nametowidget(om1.menuname)
menu.config(font=("Arial",12))

password_lbl = Label(frame, text="Password : ", bg='#BFEFFF', fg="black", font=("Arial", 16))
password_lbl.grid(row=8, column=0)

password_e = Entry(frame, font=("Arial", 13))
password_e.grid(row=8, column=1, pady=20)

#buttons
signup_btn = Button(frame, text="Sign Up", bg="#96CDCD", fg="black", font=("Arial", 16), command=signup)
signup_btn.grid(row=9, column=0 ,pady=30)

clear_btn = Button(frame, text="Clear", bg="#96CDCD", fg="black", font=("Arial", 16), command=clear)
clear_btn.grid(row=9,column=2,pady=30)

#link to redirect
lbl2= Label(frame, text= "Existing User!", cursor= "hand2",bg='#BFEFFF', fg= "black", font= ('Aerial 18'))
lbl2.grid(row=10,columnspan=3,pady=20)


frame.pack()

window.mainloop()