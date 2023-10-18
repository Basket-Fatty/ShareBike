import tkinter as tk
# using Pillow library for importing images from the system
from PIL import ImageTk
from tkinter import *

import manager

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
        text="Generate Report!",
        bg=bg_color,
        fg="white",  # text color
        font=('TkMenuFont', 14)
    ).pack(pady=20)  # pady is used to create a padding along the y axis

    tk.Label(
        main_frame,
        text="Start Time",
        bg=bg_color,
        fg="white",
    ).place(x=120, y=320)

    start_time_box = tk.Entry(
        main_frame,
        bg='#191919',
        fg='white',
    )
    start_time_box.place(x=200, y=320)

    tk.Label(
        main_frame,
        text="End Time",
        bg=bg_color,
        fg="white",
    ).place(x=120, y=350)

    end_time_box = tk.Entry(
        main_frame,
        bg='#191919',
        fg='white',
    )
    end_time_box.place(x=200, y=350)

    # Pay Button
    tk.Button(
        main_frame,
        text='Generate Report',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        activebackground='#000000',
        activeforeground='white',
        command=lambda: view_report_button(start_time_box, end_time_box)
    ).place(x=180, y=400)


# view_report_function
def view_report_button(start_time_box, end_time_box):
    # widget protection so they don't get modified due to the other frames
    view_report_frame.pack_propagate(False)
    # clearing the widgets of main_frame
    # clear_widgets(load_main_frame)
    # raising the view_profile_frame on the top
    view_report_frame.tkraise()

    main_logo = ImageTk.PhotoImage(file="ShareBike.png")
    logo_widget = tk.Label(view_report_frame, image=main_logo, bg=bg_color, height=250, width=250)
    logo_widget.image = main_logo
    logo_widget.pack()

    # Back Button
    tk.Button(
        view_report_frame,
        text='BACK',
        font=("TkHeadingFont", 10),
        bg='#191919',
        fg='white',
        activebackground='#000000',
        activeforeground='white',
        command=lambda: load_main_frame()
    ).pack()

    print('View report button clicked!!!')

    # integrate with the back end
    start_time = start_time_box.get()
    end_time = end_time_box.get()
    data = manager.report_period(int(start_time), int(end_time))
    print(data)

    # display the data


# initialization
root = tk.Tk()
root.title('ShareBike | Generate Report - Manager')
# root.eval("tk::PlaceWindow . center")
# taking the half of whatever screen this code would be running on
width = root.winfo_screenwidth() // 2
# would leave a 10% of gap from the top and bottom of the screen
height = int(root.winfo_screenheight() * 0.1)
# Setting the actual geometry now
root.geometry('400x600+' + str(width) + '+' + str(height))

main_frame = tk.Frame(root, width=400, height=600, bg=bg_color)
view_report_frame = tk.Frame(root, bg=bg_color)

for frame in (main_frame, view_report_frame):
    frame.grid(row=0, column=0)

load_main_frame()

# running the application
root.mainloop()