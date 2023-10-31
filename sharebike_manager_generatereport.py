import tkinter as tk
# using Pillow library for importing images from the system
from PIL import ImageTk
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *

import manager
import employee

# storing not so easy string to remember in a variable so that it can be reusable
bg_color = '#363636'
"""
#function for clearing the widgets
def clear_widgets(frame):
    #selecting all widgets within the frame
    for widget in frame.winfo_children():
        widget.destroy()
"""


# initialization
def config(window):
    window.title('ShareBike | Generate Report - Manager')
    # window.eval("tk::PlaceWindow . center")
    # taking the half of whatever screen this code would be running on
    width = window.winfo_screenwidth() // 2
    # would leave a 10% of gap from the top and bottom of the screen
    height = int(window.winfo_screenheight() * 0.1)
    # Setting the actual geometry now
    window.geometry('400x600+' + str(width) + '+' + str(height))

    main_frame = tk.Frame(window, width=400, height=600, bg=bg_color)
    view_report_frame = tk.Frame(window, bg=bg_color)

    for frame in (main_frame, view_report_frame):
        frame.grid(row=0, column=0)

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
        ).place(x=160, y=400)

        tk.Button(
            main_frame,
            text='Generate Vehicle Graph',
            font=("TkHeadingFont", 10),
            bg='#191919',
            fg='white',
            activebackground='#000000',
            activeforeground='white',
            command=generate_vacancy_graph
        ).place(x=135, y=450)

    def generate_vacancy_graph():
        data = {'VACANT': 20, 'RENTED': 15, 'DAMAGED': 30,
                'LOPOWER': 35}

        vehicles_status = {}
        vehicle_dtls = employee.track_vehicle()
        for vehicle_id, vehicle_more_infos in vehicle_dtls.items():
            cnt = 0
            stat = vehicle_more_infos[2]
            if stat in vehicles_status:
                cnt = vehicles_status[stat]
            cnt = cnt + 1
            print(stat + "___" + str(cnt))
            vehicles_status.update({stat: cnt})

        # vehicles_status = {'VACANT': 20, 'RENTED': 15, 'DAMAGED': 30,
        #                   'LOWPOWER': 35}

        courses = list(vehicles_status.keys())
        values = list(vehicles_status.values())

        fig = plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(courses, values, color='maroon',
                width=0.4)

        plt.xlabel("Vehicle Current state")
        plt.ylabel("Number of Vehicles")
        plt.title("Status of various Vehicles")
        plt.show()

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

    load_main_frame()
