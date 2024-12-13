import tkinter as tk
import YuMin_TicTacToe.tic_tac_toe as tic_tac_toe
import Jerrick_Menu.menu as menu


LARGEFONT = ("Verdana", 35)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}
        self.username_var = tk.StringVar()
        self.diff_var = tk.StringVar()

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (menu.Menu, tic_tac_toe.Board):
            if F == tic_tac_toe.Board:
                frame = F(tic_tac_toe.Game(), container,
                          self, self.diff_var, self.username_var)
            else:  # if menu
                frame = F(container, self, self.diff_var, self.username_var)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(menu.Menu)

    # to display the current frame passed as
    # parameter
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


# Driver Code
app = tkinterApp()
app.mainloop()
