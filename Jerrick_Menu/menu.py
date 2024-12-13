# imports
import tkinter as tk
from tkinter import ttk, messagebox
import YuMin_TicTacToe.tic_tac_toe as tic_tac_toe
import Nat_Leaderboard.highscore as hs
import Chris_Questions.question_v2 as qv2


class Menu(tk.Frame):
    def __init__(self, parent, controller, difficulty_var, username_var):
        tk.Frame.__init__(self, parent, width=800, height=700,
                          bg="#ced6e0", cursor="sailboat")
        self.grid_propagate(False)
        controller.resizable(False, False)

        # name of window
        controller.title("Tic Tac Toe")

        # define a grid
        self.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        self.rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=0)

        # widgets
        title_label = tk.Label(
            self, text="Tic Tac Toe", font=('Comic Sans MS', 24), background="#ced6e0")
        title_label.grid(row=0, column=3, pady="40", padx="10")

        username_text = tk.Label(
            self, text="Enter Username:", font=('Comic Sans MS', 10), background="#ced6e0")
        username_text.grid(row=2, column=2, pady="20")

        self.username_var = username_var
        username_entry = tk.Entry(self, font=(
            'Arial', 10), textvariable=self.username_var, width="40")
        username_entry.grid(row=2, column=3, columnspan=2)

        # difficulty button widgets
        self.diff_var = difficulty_var
        self.diff_popup = tk.StringVar(value="")

        start_btn = tk.Button(self, text="Start", font=("Comic Sans MS", 10), padx=25,
                              command=self.start_on_click(controller), bg="#9980FA", activebackground="#a4b0be")
        start_btn.grid(row=10, column=4)

        self.diff_text = tk.Label(self, text="Difficulty:", font=(
            'Arial', 12), background="#ced6e0")
        self.diff_text.grid(row=3, column=3, pady="10")

        self.cpu_btn = tk.Button(self, text="2P", font=('Comic Sans MS', 10), padx=20,
                                 bg="#70a1ff", command=self.diff_msg("2P"),  activebackground="#a4b0be")
        self.cpu_btn.grid(row=4, column=3, pady="5")

        self.easy_btn = tk.Button(self, text="EASY", font=(
            'Comic Sans MS', 10), padx=20, bg='#7bed9f', command=self.diff_msg("EASY"), activebackground="#a4b0be")
        self.easy_btn.grid(row=5, column=2, pady="5")

        self.medium_btn = tk.Button(self, text="NORMAL", font=(
            'Comic Sans MS', 10), padx=20, bg='#ff8d63', command=self.diff_msg("NORMAL"), activebackground="#a4b0be")
        self.medium_btn.grid(row=5, column=3, pady="5")

        self.hard_btn = tk.Button(self, text="HARD", font=(
            'Comic Sans MS', 10), padx=20, bg='#ff6b81', command=self.diff_msg("HARD"), activebackground="#a4b0be")
        self.hard_btn.grid(row=5, column=4, pady="5")

        self.update_btn = tk.Button(self, text="Update Question", font=(
            'Comic Sans MS', 10), padx=20, bg='#1e90ff', command=self.update_question, activebackground="#a4b0be")
        self.update_btn.grid(row=10, column=2, pady="5")

        # leaderboard widgets
        leaderboard_title = tk.Label(self, text="Leaderboards: ", font=(
            'Comic Sans MS', 8), background="#ced6e0")
        leaderboard_title.grid(row=7, column=2, pady="15")

        # Set Treeview
        self.tree = ttk.Treeview(self)
        self.tree.grid(row=8, column=3, padx="20", rowspan=3)
        ttk.Style().configure("Treeview", background="#74b9ff")

        scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=8, column=4)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.update_btn = tk.Button(self, text="Update Leaderboard!", font=(
            'Comic Sans MS', 10), bg="#a4b0be", command=self.update_leaderboard())
        self.update_btn.grid(row=9, column=4)

        leaderboard_data = hs.get_scores(self.diff_var.get())
        self.load_csv_to_treeview(self.tree, leaderboard_data)

    # update leaderboard onclick;
    def update_leaderboard(self):
        def inner_func():
            leaderboard_data = hs.get_scores(self.diff_var.get())
            self.load_csv_to_treeview(self.tree, leaderboard_data)
        return inner_func

    # def checker

    def diff_msg(self, diff_click):
        def inner_func():
            self.diff_var.set(diff_click)
            self.diff_text.config(text=f"Difficulty is: {self.diff_var.get()}")
            # changing background of colour to show selection
            if (self.diff_var.get() == "EASY"):
                self.easy_btn.config(bg="#58B19F")
                self.medium_btn.config(bg='#ff8d63')
                self.hard_btn.config(bg='#ff6b81')
                self.cpu_btn.config(bg="#70a1ff")
            elif (self.diff_var.get() == "NORMAL"):
                self.easy_btn.config(bg='#7bed9f')
                self.medium_btn.config(bg="#58B19F")
                self.hard_btn.config(bg='#ff6b81')
                self.cpu_btn.config(bg="#70a1ff")
            elif (self.diff_var.get() == "HARD"):
                self.easy_btn.config(bg='#7bed9f')
                self.medium_btn.config(bg='#ff8d63')
                self.hard_btn.config(bg="#58B19F")
                self.cpu_btn.config(bg="#70a1ff")
            elif (self.diff_var.get() == "2P"):
                self.easy_btn.config(bg='#7bed9f')
                self.medium_btn.config(bg='#ff8d63')
                self.hard_btn.config(bg='#ff6b81')
                self.cpu_btn.config(bg="#58B19F")

            # Load Values into Treeview
            leaderboard_data = hs.get_scores(self.diff_var.get())
            self.load_csv_to_treeview(self.tree, leaderboard_data)
        return inner_func

    def update_question(self):
        self.popup = qv2.QuestionUpdate()
        self.wait_window(self.popup)

    # def start confirmation

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

    # def treeview configuration
    def load_csv_to_treeview(self, tree, data):
        for row in tree.get_children():
            tree.delete(row)

        # Filter only the selected columns
        selected_columns = ["name", "score"]
        tree["columns"] = selected_columns
        tree["show"] = "headings"  # Hide default empty column
        for col in selected_columns:
            tree.heading(col, text=col.capitalize())
            tree.column(col, width=100, anchor="center")

        # Insert rows with selected columns into Treeview
        for row in data:
            filtered_row = [row[col]
                            for col in selected_columns if col in row]
            tree.insert("", "end", values=filtered_row)
