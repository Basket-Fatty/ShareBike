from tkinter import *
from tkinter import ttk
import sqlite3

#functions
def create_database():
    with sqlite3.connect("database_name.db") as conn:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS table1(trip_id INTEGER, vehicle_id INTEGER, 
                    start_time TIMESTAMP, end_time TIMESTAMP, charge DECIMAL, start_station_name TEXT, 
                    start_postcode TEXT, end_station_name TEXT, end_postcode TEXT)""")

def view_data():
    with sqlite3.connect("database_name.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM table1")
        rows = cur.fetchall()
        for row in rows:
            tree.insert("", END, values=row)

def clear():
    pass

window = Tk()
window.title("Travel History")
window.geometry('1100x600')
window.configure(bg='#BFEFFF')

#heading
heading_label = Label(window, text="Travel History", font=('Arial', 20, 'bold'), bg='#BFEFFF')
heading_label.pack(pady=20)  

#table
frame = Frame(window, bg='#BFEFFF')
frame.pack(fill=BOTH, expand=YES, padx=10, pady=10) 

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial', 10,'bold')) 

create_database()
my_conn = sqlite3.connect('database_name.db')
r_set = my_conn.execute('''SELECT * from table1''')

tree = ttk.Treeview(frame, columns=("Trip ID", "Vehicle ID", "Start Time", "End Time", "Charge",
                                    "Start Station", "Start Postcode", "End Station", "End Postcode"),
                    yscrollcommand=Scrollbar.set, xscrollcommand=Scrollbar.set)

tree.grid(column=0, row=0, sticky='nsew')
tree['show'] = 'headings'

scrollbar = Scrollbar(frame, orient="vertical", command=tree.yview)
scrollbar_x = Scrollbar(frame, orient="horizontal", command=tree.xview)
tree.configure(yscrollcommand=scrollbar.set, xscrollcommand=scrollbar_x.set)
tree.grid(column=0, row=0, sticky='nsew')

scrollbar.grid(row=0, column=1, sticky='ns')
scrollbar_x.grid(row=1, column=0, sticky='ew')

tree.heading("#1", text="Trip ID",anchor='center')
tree.heading("#2", text="Vehicle ID",anchor='center')
tree.heading("#3", text="Start Time",anchor='center')
tree.heading("#4", text="End Time",anchor='center')
tree.heading("#5", text="Charge",anchor='center')
tree.heading("#6", text="Origin",anchor='center')
tree.heading("#7", text="Start Postcode",anchor='center')
tree.heading("#8", text="Destination",anchor='center')
tree.heading("#9", text="End Postcode",anchor='center')

tree.column("#0", width=60, anchor='center')  
tree.column("#1", width=60, anchor='center') 
tree.column("#2", width=120, anchor='center')  
tree.column("#3", width=120, anchor='center')  
tree.column("#4", width=60, anchor='center')  
tree.column("#5", width=100, anchor='center')  
tree.column("#6", width=100, anchor='center')  
tree.column("#7", width=100, anchor='center')  
tree.column("#8", width=100, anchor='center')  
tree.column("#9", width=100, anchor='center')

s = ttk.Style()
s.configure('Treeview.Heading', background='black', foreground='dark blue')

for student in r_set:
    tree.insert("", END, values=student)

tree.grid(row=0, column=0, sticky='nsew')  
scrollbar.grid(row=0, column=1, sticky='ns')
scrollbar_x.grid(row=1, column=0, sticky='ew')

frame.grid_rowconfigure(0, weight=1)  
frame.grid_columnconfigure(0, weight=1) 

#button
button1 = Button(window, text="Back",width=11, bg="#96CDCD", fg="black", font=("Arial", 16), command=clear)
button1.pack(side=BOTTOM, padx=10, pady=10)  

window.mainloop()