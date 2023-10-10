from tkinter import *
import random
from tkinter import messagebox


def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def gen_random():
    global rnd1, rnd2
    rnd1 = random.randrange(10,50)
    rnd2 = random.randrange(10,50)
    strn = "Enter the sum of " + str(rnd1) + " and " + str(rnd2)
    return strn


def operator_page():
    lbl = Label(text="Operator Controls", font=('Arial','20'))
    lbl.place(x=140, y=200)
    lbl["bg"] = bg_colour
    lbl["fg"] = "white"
    lbl = Label(text="Select your preferred Option", font=('Arial', '15'))
    lbl.place(x=120, y=235)
    lbl["bg"] = bg_colour
    lbl["fg"] = "black"
    btn = Button(text="Track Vehicle", command=track_vehicle)
    btn.place(x=210, y=270)
    btn["bg"] = "blue"
    btn = Button(text="Charge Vehicle", command=charge_vehicle)
    btn.place(x=210, y=300)
    btn["bg"] = "blue"
    btn = Button(text="Repair Defective Vehicle", command=repair_vehicle)
    btn.place(x=210, y=330)
    btn["bg"] = "blue"
    btn = Button(text="Move a Vehicle", command=repair_vehicle)
    btn.place(x=210, y=360)
    btn["bg"] = "blue"


def track_vehicle():
    track_vehicle_window = Tk()
    track_vehicle_window.title("Track Vehicle")
    track_vehicle_window.geometry("500x400")
    track_vehicle_window.configure(background=bg_colour)
    lbl = Label(track_vehicle_window, text="Vehicle Details", font=('Arial', '15'))
    lbl.place(x=10,y=30)
    lbl["bg"] = bg_colour
    lbl["fg"] = "white"
    lbl = Label(track_vehicle_window, text="Vehicle Number --- Current Location", font=('Arial', '10'))
    lbl.place(x=10, y=60)
    lbl["bg"] = bg_colour
    lbl["fg"] = "black"
    name_box = Listbox(track_vehicle_window)
    name_box.place(x=10, y=90, width=250, height=80)
    populate_vehicle_status(name_box)
    track_vehicle_window.mainloop()


def charge_vehicle():
    charge_vehicle_window = Tk()
    charge_vehicle_window.title("Charge Vehicle")
    charge_vehicle_window.geometry("500x400")
    charge_vehicle_window.configure(background=bg_colour)
    lbl = Label(charge_vehicle_window, text="Please select a Vehicle to Charge", font=('Arial', '15'))
    lbl.place(x=10,y=30)
    lbl["bg"] = bg_colour
    lbl["fg"] = "white"
    lbl = Label(charge_vehicle_window, text="Vehicle Number -- Current Charge", font=('Arial', '10'))
    lbl.place(x=10, y=60)
    lbl["bg"] = bg_colour
    lbl["fg"] = "black"
    name_box = Listbox(charge_vehicle_window)
    name_box.place(x=10, y=90, width=250, height=80)
    populate_discharged_vehicle(name_box)
    btn = Button(charge_vehicle_window, text="Charge Selected Vehicle", command=lambda : charge_button(name_box))
    btn.place(x=10, y=220)
    btn["bg"] = "blue"
    charge_vehicle_window.mainloop()


def repair_vehicle():
    repair_vehicle_window = Tk()
    repair_vehicle_window.title("Charge Vehicle")
    repair_vehicle_window.geometry("500x400")
    repair_vehicle_window.configure(background=bg_colour)
    lbl = Label(repair_vehicle_window, text="Please select a Vehicle to Repair", font=('Arial', '15'))
    lbl.place(x=10,y=30)
    lbl["bg"] = bg_colour
    lbl["fg"] = "white"
    lbl = Label(repair_vehicle_window, text="Vehicle Number Broken down", font=('Arial', '10'))
    lbl.place(x=10, y=60)
    lbl["bg"] = bg_colour
    lbl["fg"] = "black"
    name_box = Listbox(repair_vehicle_window)
    name_box.place(x=10, y=90, width=250, height=80)
    populate_damaged_vehicle(name_box)
    btn = Button(repair_vehicle_window, text="Repair Selected Vehicle", command=lambda : repair_button(name_box))
    btn.place(x=10, y=220)
    btn["bg"] = "blue"
    repair_vehicle_window.mainloop()


def populate_vehicle_status(name_box):
    vehicle_dtl = ["VH123","TR333","TY4444"]
    location = ["Street1","Street2","Street3"]
    for i,j in zip(vehicle_dtl, location):
        str = i + "---" + j + '\n'
        name_box.insert(END,str)


def populate_discharged_vehicle(name_box):
    vehicle_dtl = ["VH123","TR333","TY4444"]
    for i in vehicle_dtl:
        str = i + '\n'
        name_box.insert(END,str)


def populate_damaged_vehicle(name_box):
    vehicle_dtl = ["VH123","TR333","TY4444"]
    for i in vehicle_dtl:
        str = i + '\n'
        name_box.insert(END,str)


def charge_button(name_box):
    selection = name_box.curselection()
    messagebox.showinfo("Vehicle Charged", name_box.get(selection[0]) + " has been charged")


def repair_button(name_box):
    selection = name_box.curselection()
    messagebox.showinfo("Vehicle Repaired", name_box.get(selection[0]) + " has been repaired")



bg_colour = _from_rgb((226, 97, 233))
window = Tk()
window.title("E-Vehicle Share System")
window.geometry("500x700")
window.configure(background=bg_colour)

logo = PhotoImage(file="bike_logo.png")
logoimg = Label(bg=bg_colour, image = logo)
logoimg.place(x = 150, y = 20, width = 200, height = 150)


operator_page()

window.mainloop()