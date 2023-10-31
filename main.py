import tkinter as tk

import sharebike_customer_login

root = tk.Tk()

root.withdraw()
login_window = tk.Toplevel()
login_window.withdraw()
sharebike_customer_login.config(login_window)
login_window.deiconify()

root.mainloop()
