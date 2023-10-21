import tkinter as tk
#using Pillow library for importing images from the system
from PIL import ImageTk
from tkinter import *
import importlib
#storing not so easy string to remember in a variable so that it can be reusable
bg_color = '#363636'
"""
#function for clearing the widgets
def clear_widgets(frame):
    #selecting all widgets within the frame
    for widget in frame.winfo_children():
        widget.destroy()
"""

#initializing the main_frame
def load_main_frame():
    main_frame.pack_propagate(False) #using a function which would prevent the child label element to affect the parent frame element
    #main_frame widgets
    main_logo = ImageTk.PhotoImage(file="ShareBike.png")
    logo_widget = tk.Label(main_frame, image=main_logo, bg=bg_color, height=250, width=250)
    logo_widget.image = main_logo
    logo_widget.pack()

    #adding texts in the main_widget
    tk.Label(
        main_frame, 
        text= "Let's help our customers",
        bg=bg_color,
        fg="white", #text color
        font=('TkMenuFont', 14)
        ).pack(pady=20) #pady is used to create a padding along the y axis

    #Adding Track Button
    tk.Button(
        main_frame,
        text='Track',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        activebackground='#000000',
        activeforeground='white',
        command=lambda:track_button() 
        ).pack(pady=5) 

    #Adding Charge Button
    tk.Button(
        main_frame,
        text='Charge',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        activebackground='#000000',
        activeforeground='white',
        command=lambda:charge_button() 
        ).pack(pady=5)

    #Adding Move Button
    tk.Button(
        main_frame,
        text='Move',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        activebackground='#000000',
        activeforeground='white',
        command=lambda:move_button() 
        ).pack(pady=5)

    #Adding Repair Button
    tk.Button(
        main_frame,
        text='Repair',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        activebackground='#000000',
        activeforeground='white',
        command=lambda:repair_button() 
        ).pack(pady=5)

    


#track_function
# def track_button():
#     #widget protection so they don't get modified due to the other frames
#     view_profile_frame.pack_propagate(False)
#     #clearing the widgets of main_frame
#     #clear_widgets(load_main_frame)
#     #raising the view_profile_frame on the top
#     view_profile_frame.tkraise()
#
#     main_logo = ImageTk.PhotoImage(file="ShareBike.png")
#     logo_widget = tk.Label(view_profile_frame, image=main_logo, bg=bg_color, height=250, width=250)
#     logo_widget.image = main_logo
#     logo_widget.pack()
#
#     #Back Button
#     tk.Button(
#         view_profile_frame,
#         text='BACK',
#         font=("TkHeadingFont", 10),
#         bg='#191919',
#         fg='white',
#         activebackground='#000000',
#         activeforeground='white',
#         command=lambda:load_main_frame()
#         ).pack()
#
#     print('Track button clicked!!!')

def track_button():
    #widget protection so they don't get modified due to the other frames
    charge_window = importlib.import_module("sharebike-operator-track")

#charge fuction
def charge_button():
    charge_window = importlib.import_module("sharebike-operator-charge")

#return fuction
def move_button():
    # print('Move button clicked!!!')
    move_window = importlib.import_module("sharebike-operator-move")

#report fuction
def repair_button():
    move_window = importlib.import_module("sharebike-operator-repair")
    print('repair button clicked')




#initialization
root = tk.Toplevel()
root.title('ShareBike | Home - Operator')
#root.eval("tk::PlaceWindow . center")
#taking the half of whatever screen this code would be running on
width = root.winfo_screenwidth() // 2
#would leave a 10% of gap from the top and bottom of the screen
height = int(root.winfo_screenheight() * 0.1)
#Setting the actual geometry now
root.geometry('400x600+' + str(width) + '+' + str(height))


main_frame = tk.Frame(root, width=400, height=600, bg=bg_color)
view_profile_frame = tk.Frame(root, bg=bg_color)


for frame in (main_frame, view_profile_frame):
    frame.grid(row=0, column=0)

load_main_frame()


#running the application
root.mainloop()