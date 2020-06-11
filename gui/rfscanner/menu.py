
import tkinter as tk
from tkinter import ttk

class Application( tk.Frame ):

    def __init__( self, master = None ):
        super().__init__( master )
        self.master = master

    def createLoginPage( self ):

        container = ttk.Frame( self.master )
        container.grid()
        font = ('Consolas', 13)
        text_height = 1
        text_width = 20

        login_text = tk.Text( container, 
            font = font, 
            height = text_height, 
            width = 10,
            relief = tk.FLAT
        )
        login_text.insert( tk.END, 'Login: ' )
        login_text.state = tk.DISABLED
        login_text.grid( column = 0, row = 0 )

        self.login_box = tk.Text( container, font = font, height = text_height, width = text_width )
        self.login_box.grid( column = 1, row = 0 )

        password_text = tk.Text( 
            container, 
            font = font, 
            height = text_height, 
            width = 10,
            relief = tk.FLAT
        )
        password_text.insert( tk.END, 'Password: ' )
        password_text.state = tk.DISABLED
        password_text.grid( column = 0, row = 1 )

        self.password = tk.Text( container, font = font, height = text_height, width = text_width )
        self.password.grid( column = 1, row = 1 )


        button = ttk.Button( container, text = 'Enter', command = self.login )
        button.grid( column = 2, row = 0 )

    def login( self ):
        print( self.login_box.get( 1.0, tk.END ))
        print( self.password.get( 1.0, tk.END ))
