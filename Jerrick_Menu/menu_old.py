# imports
import tkinter as tk
from tkinter import messagebox
import YuMin_TicTacToe.tic_tac_toe as tic_tac_toe
import Nat_Leaderboard.highscore as hs


class Menu(tk.Frame):
    def __init__(self, parent, controller, difficulty_var, username_var):
        tk.Frame.__init__(self, parent, width=600, height=400)

        # define a grid
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)
        self.columnconfigure(5, weight=1)
        self.columnconfigure(6, weight=0)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)

        # widgets
        title_label = tk.Label(
            self, text="Tic Tac Toe", font=('Comic Sans MS', 24))
        title_label.grid(row=0, column=3)

        username_text = tk.Label(
            self, text="Enter Username:", font=('Comic Sans MS', 10))
        username_text.grid(row=2, column=2)

        self.username_var = username_var
        username_entry = tk.Entry(self, font=(
            'Arial', 10), textvariable=self.username_var)
        username_entry.grid(row=2, column=3)

        # difficulty button widgets
        self.diff_var = difficulty_var
        self.diff_popup = tk.StringVar(value="")

        start_btn = tk.Button(self, text="Start", font=(
            "Comic Sans MS", 10), padx=25, command=self.start_on_click(controller))
        start_btn.grid(row=2, column=4)

        hard_btn = tk.Button(self, text="2 Player", font=(
            'Comic Sans MS', 10), padx=20, bg='gray', command=self.diff_msg("2P"))
        hard_btn.grid(row=3, column=2)

        self.diff_text = tk.Label(
            self, text="Difficulty:", font=('Arial', 12))
        self.diff_text.grid(row=3, column=3)

        easy_btn = tk.Button(self, text="EASY", font=(
            'Comic Sans MS', 10), padx=20, bg='#AAFF77', command=self.diff_msg("EASY"))
        easy_btn.grid(row=4, column=2)

        medium_btn = tk.Button(self, text="MEDIUM", font=(
            'Comic Sans MS', 10), padx=20, bg='#FFE25C', command=self.diff_msg("MEDIUM"))
        medium_btn.grid(row=4, column=3)

        hard_btn = tk.Button(self, text="HARD", font=(
            'Comic Sans MS', 10), padx=20, bg='#F56262', command=self.diff_msg("HARD"))
        hard_btn.grid(row=4, column=4)

        # leaderboard widgets
        leaderboard_title = tk.Label(
            self, text="Leaderboards: ", font=('Comic Sans MS', 8))
        leaderboard_title.grid(row=5, column=2)

    # def checker
    def diff_msg(self, diff_click):
        def inner_func():
            self.diff_var.set(diff_click)
            self.diff_text.config(text=f"Difficulty is: {self.diff_var.get()}")
            print(hs.get_scores(self.diff_var.get()))
        return inner_func

    def start_on_click(self, controller):
        def inner_func():
            if (self.username_var.get() == ""):
                messagebox.showinfo(
                    title="Username?",
                    message="Username is blank, please input a username!")

            elif (self.diff_var.get() == ""):
                messagebox.showinfo(
                    title="Difficulty?",
                    message="Difficulty not selected, please select a difficulty!")

            else:
                if messagebox.askyesno(title="Confirmation", message=f"Username is: {self.username_var.get()} \nDifficulty selected: {self.diff_var.get()}"):
                    # launch next portion of game here, open new window using new class.
                    controller.show_frame(tic_tac_toe.Board)
        return inner_func
