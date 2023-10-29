import tkinter as tk

import sharebike_login

root = tk.Tk()

login_window = tk.Toplevel()
login_window.withdraw()
sharebike_login.config(login_window)
login_window.deiconify()

root.mainloop()
