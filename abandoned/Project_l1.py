
from tkinter import *
from tkinter import messagebox, StringVar, OptionMenu
from abandoned import data_manipulation as dm


def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


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
    btn = Button(text="Move a Vehicle", command=move_vehicle)
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
    lbl = Label(repair_vehicle_window, text="Vehicle Number Broken down --- location", font=('Arial', '10'))
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


def move_vehicle():
    move_vehicle_window = Tk()
    move_vehicle_window.title("Move Vehicle")
    move_vehicle_window.geometry("500x400")
    move_vehicle_window.configure(background=bg_colour)
    lbl = Label(move_vehicle_window, text="Please select a Vehicle to move", font=('Arial', '15'))
    lbl.place(x=10,y=30)
    lbl["bg"] = bg_colour
    lbl["fg"] = "white"
    lbl = Label(move_vehicle_window, text="Vehicle Number --- Current location", font=('Arial', '10'))
    lbl.place(x=10, y=60)
    lbl["bg"] = bg_colour
    lbl["fg"] = "black"
    name_box = Listbox(move_vehicle_window)
    name_box.place(x=10, y=90, width=250, height=80)
    populate_move_vehicle(name_box)
    selected = populate_dropdown(name_box, move_vehicle_window)
    btn = Button(move_vehicle_window, text="Move Vehicle", command=lambda: move_button(name_box, selected))
    btn.place(x=10, y=240)
    btn["bg"] = "blue"
    move_vehicle_window.mainloop()


def populate_vehicle_status(name_box):
    vehicle_dtls = dm.track_vehicle()
    for vehicle_id, vehicle_dtls in vehicle_dtls.items():
        total_info = str(vehicle_id) + "---" + vehicle_dtls[3]
        name_box.insert(END, total_info)


def populate_discharged_vehicle(name_box):
    vehicle_dtls = dm.track_vehicle()
    for vehicle_id, vehicle_dtls in vehicle_dtls.items():
        if vehicle_dtls[2] == 'LOWPOWER':
            total_info = str(vehicle_id) + "---" + vehicle_dtls[3]
            name_box.insert(END, total_info)


def populate_damaged_vehicle(name_box):
    vehicle_dtls = dm.track_vehicle()
    for vehicle_id, vehicle_dtls in vehicle_dtls.items():
        if vehicle_dtls[2] == 'DAMAGED':
            total_info = str(vehicle_id) + "---" + vehicle_dtls[3]
            name_box.insert(END, total_info)


def populate_move_vehicle(name_box):
    vehicle_dtls = dm.track_vehicle()
    for vehicle_id, vehicle_dtls in vehicle_dtls.items():
        if vehicle_dtls[2] == 'VACANT':
            total_info = str(vehicle_id) + "---" + vehicle_dtls[3]
            name_box.insert(END, total_info)
    name_box.select_set(0)


def populate_dropdown(name_box, move_vehicle_window):
    selection = name_box.curselection()
    print(selection)
    print(name_box.get(selection[0]))
    fetched_string_array = name_box.get(selection[0]).split("---")
    current_location = fetched_string_array[1]
    location_dct = dm.fetch_all_location_info_in_dict()
    filtered_location = []
    for key, value in location_dct.items():
        if value != current_location:
            filtered_location.append(value)
    clicked = StringVar(move_vehicle_window)
    clicked.set("Select Location")
    drop = OptionMenu(move_vehicle_window, clicked, *filtered_location)
    drop.place(x=10, y=200, width="150")
    return clicked


def charge_button(name_box):
    selection = name_box.curselection()
    print(name_box)
    fetched_string_array = name_box.get(selection[0]).split("---")
    vehicle_id = fetched_string_array[0]
    location_dct = dm.fetch_all_location_info_in_dict()
    location = find_location_id(location_dct, fetched_string_array[1])
    time = 100
    dm.update_vehicle_charge(vehicle_id, time, "VACANT", location)
    messagebox.showinfo("Vehicle Charged", vehicle_id + " has been charged")


def repair_button(name_box):
    selection = name_box.curselection()
    fetched_string_array = name_box.get(selection[0]).split("---")
    vehicle_id = fetched_string_array[0]
    location_dct = dm.fetch_all_location_info_in_dict()
    location = find_location_id(location_dct, fetched_string_array[1])
    time = 100
    dm.update_vehicle_charge(vehicle_id, time, "VACANT", location)
    messagebox.showinfo("Vehicle Charged", vehicle_id + " has been repaired")


def move_button(name_box, optionbox_selection):
    selected_location = optionbox_selection.get()
    selection = name_box.curselection()
    fetched_string_array = name_box.get(selection[0]).split("---")
    vehicle_id = fetched_string_array[0]
    location_dct = dm.fetch_all_location_info_in_dict()
    location = find_location_id(location_dct, fetched_string_array[1])
    time = 100
    dm.update_vehicle_charge(vehicle_id, time, "VACANT", selected_location)
    messagebox.showinfo("Vehicle location changed", "Vehicle "+ name_box.get(selection[0]) + " to " + selected_location)


def find_location_id(location_dct, to_match):
    for key, value in location_dct.items():
        if value == to_match:
            return key


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