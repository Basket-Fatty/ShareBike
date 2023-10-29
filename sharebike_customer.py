import tkinter as tk
# using Pillow library for importing images from the system
from PIL import ImageTk
from tkinter import *
import importlib

# storing not so easy string to remember in a variable so that it can be reusable
bg_color = '#363636'
"""
#function for clearing the widgets
def clear_widgets(frame):
    #selecting all widgets within the frame
    for widget in frame.winfo_children():
        widget.destroy()
"""


# initializing the main_frame
def load_main_frame():
    main_frame.pack_propagate(
        False)  # using a function which would prevent the child label element to affect the parent frame element
    # main_frame widgets
    main_logo = ImageTk.PhotoImage(file="ShareBike.png")
    logo_widget = tk.Label(main_frame, image=main_logo, bg=bg_color, height=250, width=250)
    logo_widget.image = main_logo
    logo_widget.pack()

    # adding texts in the main_widget
    tk.Label(
        main_frame,
        text='Ready to bike along the streets?',
        bg=bg_color,
        fg="white",  # text color
        font=('TkMenuFont', 14)
    ).pack(pady=20)  # pady is used to create a padding along the y axis

    # Adding View Profile Button
    tk.Button(
        main_frame,
        text='View Profile',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        activebackground='#000000',
        activeforeground='white',
        command=lambda: view_profile_button()
    ).pack(pady=5)

    # Adding Rent Button
    tk.Button(
        main_frame,
        text='Rent',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        activebackground='#000000',
        activeforeground='white',
        command=lambda: rent_button()
    ).pack(pady=5)

    # Adding Return Button
    tk.Button(
        main_frame,
        text='Return',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        activebackground='#000000',
        activeforeground='white',
        command=lambda: return_button()
    ).pack(pady=5)

    # Adding Report Button
    tk.Button(
        main_frame,
        text='Report',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        activebackground='#000000',
        activeforeground='white',
        command=lambda: report_button()
    ).pack(pady=5)

    # Pay Button
    tk.Button(
        main_frame,
        text='Pay',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        activebackground='#000000',
        activeforeground='white',
        command=lambda: pay_button()
    ).pack(pady=5)

    # Transaction History Button
    tk.Button(
        main_frame,
        text='Transaction History',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        activebackground='#000000',
        activeforeground='white',
        command=lambda: transaction_history_button()
    ).pack(pady=5)


# view profile function
def view_profile_button():
    # widget protection so they don't get modified due to the other frames
    view_profile_frame.pack_propagate(False)
    # clearing the widgets of main_frame
    # clear_widgets(load_main_frame)
    # raising the view_profile_frame on the top
    view_profile_frame.tkraise()

    main_logo = ImageTk.PhotoImage(file="ShareBike.png")
    logo_widget = tk.Label(view_profile_frame, image=main_logo, bg=bg_color, height=250, width=250)
    logo_widget.image = main_logo
    logo_widget.pack()

    # Back Button
    tk.Button(
        view_profile_frame,
        text='BACK',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        activebackground='#000000',
        activeforeground='white',
        command=lambda: load_main_frame()
    ).pack()

    print('View Profile button clicked!!!')


# rent fuction
def rent_button():
    import sharebike_customer_rent
    importlib.reload(sharebike_customer_rent)


# return fuction
def return_button():
    import sharebike_customer_return
    importlib.reload(sharebike_customer_return)


# report fuction
def report_button():
    import sharebike_customer_report
    importlib.reload(sharebike_customer_report)

# pay fuction
def pay_button():
    import sharebike_customer_pay
    importlib.reload(sharebike_customer_pay)

# transaction history function
def transaction_history_button():
    print('transaction history button clicked!!!')


# initialization
root = tk.Toplevel()
root.title('ShareBike | Home - Customer')
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
width = root.winfo_screenwidth() // 2
# would leave a 10% of gap from the top and bottom of the screen
height = int(root.winfo_screenheight() * 0.1)
# Setting the actual geometry now
root.geometry('400x600+' + str(width) + '+' + str(height))

main_frame = tk.Frame(root, width=400, height=600, bg=bg_color)

view_profile_frame = tk.Frame(root, bg=bg_color)

for frame in (main_frame, view_profile_frame):
    frame.grid(row=0, column=0)

load_main_frame()

# running the application
root.mainloop()