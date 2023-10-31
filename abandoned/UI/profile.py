from tkinter import*
from PIL import Image,ImageTk
import tkinter.font as tkFont

window = Tk()
window.title("Profile")
window.geometry('800x1000')
window.configure(bg='#BFEFFF')

#functions
#instead of entry block create a function to display the corresponding data value from the database for the required field
def back():
    pass

frame = Frame(bg='#BFEFFF')

#heading and logo
main_logo = ImageTk.PhotoImage(file="ss.jpg")
label = Label(frame, image = main_logo)
label.grid(row=0,columnspan=3)

login_lbl = Label(frame, text="Profile", bg='#BFEFFF', fg="black", font=("Arial", 30))
login_lbl.grid(row=1, column=0, columnspan=3, pady=20)

#details
fname = Label(frame, text="First Name : ", bg='#BFEFFF', fg="black", font=("Arial", 16))
fname.grid(row=2, column=0)

lname = Label(frame, text="Last Name : ", bg='#BFEFFF', fg="black", font=("Arial", 16))
lname.grid(row=3, column=0)

email = Label(frame, text="Email : ", bg='#BFEFFF', fg="black", font=("Arial", 16))
email.grid(row=4, column=0)

phone = Label(frame, text="Contact No. : ", bg='#BFEFFF', fg="black", font=("Arial", 16))
phone.grid(row=5, column=0)

cust_id = Label(frame, text="Customer ID : ", bg='#BFEFFF', fg="black", font=("Arial", 16))
cust_id.grid(row=6, column=0)

account = Label(frame, text="Account No. : ", bg='#BFEFFF', fg="black", font=("Arial", 16))
account.grid(row=7, column=0)

balance = Label(frame, text="Balance : ", bg='#BFEFFF', fg="black", font=("Arial", 16))
balance.grid(row=8, column=0)

password_lbl = Label(frame, text="Password : ", bg='#BFEFFF', fg="black", font=("Arial", 16))
password_lbl.grid(row=9, column=0)

#entrybox
fname_e = Entry(frame, font=("Arial", 13))
fname_e.grid(row=2, column=1, pady=20)

lname_e = Entry(frame, font=("Arial", 13))
lname_e.grid(row=3, column=1, pady=20)

email_e = Entry(frame, font=("Arial", 13))
email_e.grid(row=4, column=1, pady=20)

phone_e = Entry(frame, font=("Arial", 13))
phone_e.grid(row=5, column=1, pady=20)

cust_id_e = Entry(frame, font=("Arial", 13))
cust_id_e.grid(row=6, column=1, pady=20)

account_e = Entry(frame, font=("Arial", 13))
account_e.grid(row=7, column=1, pady=20)

balance_e = Entry(frame, font=("Arial", 13))
balance_e.grid(row=8, column=1, pady=20)

password_e = Entry(frame, font=("Arial", 13))
password_e.grid(row=9, column=1, pady=20)

#buttons
back_btn = Button(frame, text="Back", bg="#96CDCD", fg="black",width=11, font=("Arial", 16), command=back)
back_btn.grid(row=10,columnspan=2,pady=30)

frame.pack()

window.mainloop()