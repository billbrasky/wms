
import sys
import gui.stations.qa as gui
# import importlib
import tkinter as tk
from tkinter import ttk

import util.load as util

options = util.getYAML( 'data/options' )

# args = sys.argv


root = tk.Tk()
# root.geometry( str( width ) + 'x' + str( height ))
# root.configure( background = '#525252' )


app = gui.Application( master = root, options = options )

app.loginPage()
# app.after( 10000, root.reloadit )
app.mainloop()