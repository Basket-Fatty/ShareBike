import tkinter as tk
# using Pillow library for importing images from the system
from PIL import ImageTk
from tkinter import *
import data_manipulation as dm

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


def track_vehicle():
    track_vehicle_window = Tk()
    track_vehicle_window.title("Track Vehicle")
    track_vehicle_window.geometry("500x400")
    track_vehicle_window.configure(background=bg_color)
    lbl = Label(track_vehicle_window, text="Vehicle Details", font=('Arial', '15'))
    lbl.place(x=10,y=30)
    lbl["bg"] = bg_color
    lbl["fg"] = "white"
    lbl = Label(track_vehicle_window, text="Vehicle Number --- Current Location", font=('Arial', '10'))
    lbl.place(x=10, y=60)
    lbl["bg"] = bg_color
    lbl["fg"] = "yellow"
    name_box = Listbox(track_vehicle_window)
    name_box.place(x=10, y=90, width=250, height=80)
    populate_vehicle_status(name_box)
    track_vehicle_window.mainloop()


def populate_vehicle_status(name_box):
    vehicle_dtls = dm.track_vehicle()
    for vehicle_id, vehicle_dtls in vehicle_dtls.items():
        total_info = str(vehicle_id) + "---" + vehicle_dtls[3]
        name_box.insert(END, total_info)

track_vehicle()