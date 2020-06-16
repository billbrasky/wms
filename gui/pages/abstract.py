import tkinter as tk
from tkinter import ttk

class Page( tk.Frame ):
    def __init__( self ):
        tk.Frame.__init__( self )

    def show( self ):
        self.lift()