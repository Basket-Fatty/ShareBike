from tkinter import *
import math, numpy
import matplotlib.pyplot as plt


def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb


def operator_page():
    lbl = Label(text="Manager Reports", font=('Arial', '20'))
    lbl.place(x=140, y=200)
    lbl["bg"] = bg_colour
    lbl["fg"] = "white"
    lbl = Label(text="Select your preferred Option", font=('Arial', '15'))
    lbl.place(x=120, y=235)
    lbl["bg"] = bg_colour
    lbl["fg"] = "black"
    btn = Button(text="Generate Daily Earning Report", command=daily_earnings_report)
    btn.place(x=210, y=270)
    btn["bg"] = "blue"
    btn = Button(text="Location Wise Drop Report", command=location_wise_report)
    btn.place(x=210, y=300)
    btn["bg"] = "blue"


def daily_earnings_report():
    last_five_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    earnings = [1000, 1500, 800, 888, 650, 2000, 2500]
    plt.plot(last_five_days, earnings)
    plt.show()


def location_wise_report():
    locations = ["Location1", "Location 2", "Location 3"]
    visits = [50, 80, 90]
    color = ["blue", "green", "yellow"]
    plt.title("Location wise visits")
    plt.pie(visits, labels=locations, colors=color, shadow=True, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()


bg_colour = _from_rgb((226, 97, 233))
window = Tk()
window.title("E-Vehicle Share System")
window.geometry("500x700")
window.configure(background=bg_colour)

logo = PhotoImage(file="bike_logo.png")
logoimg = Label(bg=bg_colour, image=logo)
logoimg.place(x=150, y=20, width=200, height=150)

operator_page()
window.mainloop()
