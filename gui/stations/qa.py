
import tkinter as tk
from tkinter import ttk


class Application( tk.Frame ):

    def __init__( self, master = None, options: dict = None ):
        super().__init__( master )
        self.master = master
        self.root_container = None
        self.options = options

    def createFrame( self ):

        if self.root_container is not None:
            print( 'A root contiainer already exists!' )
            self.root_container.destroy()

        self.root_container = ttk.Frame( self.master )
        self.root_container.grid()

    def loginPage( self ):

        self.createFrame()

        self.container = ttk.Frame( self.root_container )
        self.container.grid()

        font = ('Consolas', 13)
        text_height = 1
        text_width = 20

        login_text = tk.Text( self.container, 
            font = font, 
            height = text_height, 
            width = 10,
            relief = tk.FLAT
        )
        login_text.insert( tk.END, 'Login: ' )
        login_text.state = tk.DISABLED
        login_text.grid( column = 0, row = 0 )

        self.login_box = tk.Text( self.container, font = font, height = text_height, width = text_width )
        self.login_box.insert( tk.END, 'test' )
        self.login_box.grid( column = 1, row = 0 )

        password_text = tk.Text( 
            self.container, 
            font = font, 
            height = text_height, 
            width = 10,
            relief = tk.FLAT
        )
        password_text.insert( tk.END, 'Password: ' )
        password_text.state = tk.DISABLED
        password_text.grid( column = 0, row = 1 )

        self.password = tk.Text( self.container, font = font, height = text_height, width = text_width )
        self.password.insert( tk.END, 'test' )
        self.password.grid( column = 1, row = 1 )

        button = ttk.Button( self.container, text = 'Enter', command = self.login )
        button.grid( column = 2, row = 0 )

    
        
    def login( self ):
        user = self.login_box.get( 1.0, tk.END ).strip()
        password = self.password.get( 1.0, tk.END ).strip()

        # check against database ( hasn't been setup yet )
        # for now, allow if its not blank
        if len( user ) + len( password ) == 0:
            # create pop up window
            print( f'User, "{user}", does not exist or incorrect password.' )
            return

        else:
            self.createFrame()
            self.genericMenu()

    def genericMenu( self ):

        self.container = ttk.Frame( self.root_container )
        self.container.grid()

        listbox = tk.Listbox( self.container )

        employee_class = 'picker'

        index = 0
        for option in self.options[employee_class]:
            index += 1
            listbox.insert( tk.END, f'{index}) {option}' )


        
        listbox.grid()
        





        
        

