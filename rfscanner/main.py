
import sys
import menu
# import importlib
import tkinter as tk
from tkinter import ttk
# args = sys.argv


root = tk.Tk()
# root.geometry( str( width ) + 'x' + str( height ))
# root.configure( background = '#525252' )


app = menu.Application( master = root )

app.createLoginPage()
# app.after( 10000, root.reloadit )
app.mainloop()