import tkinter as tk
from tkinter import messagebox
import Lukas_Forfeits_Questions.TicTacToe_Question_Generator as qnG


class QuestionPopup (tk.Toplevel):
    # initialize
    def __init__(self, question, difficulty, is_answer_correct):
        tk.Toplevel.__init__(self, width="1000", height="200", bg="#ced6e0")
        # define grid system
        self.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=0)
        self.grid_propagate(False)

        self.title("Answer this question!")
        self.difficulty = difficulty
        self.question = question
        self.is_answer_correct = is_answer_correct
        self.question_frame()

    # question format
    def question_frame(self):
        tk.Label(self, text=self.question,
                 font=('Comic Sans MS', 14), bg="#ced6e0").grid(row=1, column=1, columnspan=3)
        tk.Label(self, text=self.difficulty,
                 font=('Comic Sans MS', 10), width=8, bg="#747d8c").grid(row=0, column=4)

        tk.Button(self, text="Correct",
                  bg='#7bed9f', fg='white', font=('Comic Sans MS', 24),
                  command=self.on_click_correct).grid(row=3, column=1)
        tk.Button(self, text="Wrong",
                  bg='#ff6b81', fg='white', font=('Comic Sans MS', 24),
                  command=self.on_click_wrong).grid(row=3, column=3)

    def on_click_correct(self):
        self.answer_check("CORRECT")

    def on_click_wrong(self):
        self.answer_check("WRONG")

    # check for answer
    def answer_check(self, input):
        if (input.upper() == "CORRECT"):
            # messagebox for correct answer
            messagebox.showinfo(
                title="Result",
                message="Correct answer! Good job!")
            self.is_answer_correct.set(True)
        else:
            # messagebox for wrong answer
            messagebox.showinfo(
                title="Result",
                message="Wrong answer! Good luck next time!")
            self.is_answer_correct.set(False)
        self.destroy()


# add questions
class QuestionUpdate(tk.Toplevel):
    question_list = qnG.questions_dict

    def __init__(self):
        tk.Toplevel.__init__(self)
        self.diff = 'EASY'
        self.question_view()
        self.question_addon()

    # main format
    def question_addon(self):
        tk.Label(self, text="Input the Question below",
                 font=('Comic Sans MS', 35)).grid(row=0, column=0)

        self.txtbox_qn = tk.Entry(self, font=('Comic Sans MS', 20), width=50)
        self.txtbox_qn.grid(row=1, column=0)
        self.lbox_qn = tk.Listbox(self, listvariable=tk.StringVar(value=self.list_qn),
                                  width=130, height=20)
        self.lbox_qn.grid(row=2, column=0, rowspan=3)

        self.btn_diff = tk.Button(self, text=self.diff.upper(),
                                  bg='#7bed9f', fg='black', font=('Comic Sans MS', 24), width=10, command=self.on_click_diff)
        self.btn_diff.grid(row=0, column=1, rowspan=2)
        tk.Button(self, text="Add",
                  bg='#a4b0be', fg='#1e90ff', font=('Comic Sans MS', 24), width=10,
                  command=self.on_click_add).grid(row=2, column=1)
        tk.Button(self, text="Remove",
                  bg='#a4b0be', fg='#ff4757', font=('Comic Sans MS', 24), width=10,
                  command=self.on_click_remove).grid(row=3, column=1)
        tk.Button(self, text="Exit",
                  bg='black', fg='#ff4757', font=('Comic Sans MS', 24), width=10, height=1, command=self.on_click_exit).grid(row=4, column=1)

    def on_click_add(self):
        # prompt for empty text box
        if (self.txtbox_qn.get() == ''):
            messagebox.showinfo(
                title="Question?",
                message="Please input the question!")
        else:
            self.question_update("ADD")
            messagebox.showinfo(
                title="List Updated",
                message=str(self.diff) + " List updated!"
            )

    def on_click_remove(self):
        # prompt for empty text box
        if (self.txtbox_qn.get() == ''):
            messagebox.showinfo(
                title="Question?",
                message="Please input a valid question! (case-sensitive)")
        else:
            self.question_update("REMOVE")

    def on_click_exit(self):
        tk.Frame.destroy(self)
    # on toggle difficulty

    def on_click_diff(self):
        if (self.diff.upper() == 'EASY'):
            self.diff = 'NORMAL'
            bg_color = '#ff8d63'
        elif (self.diff.upper() == 'NORMAL'):
            self.diff = 'HARD'
            bg_color = '#ff6b81'
        elif (self.diff.upper() == 'HARD'):
            self.diff = 'EASY'
            bg_color = '#7bed9f'
        else:
            messagebox.showwarning(message="ERROR")
            return
    # update list and button
        self.btn_diff.config(text=self.diff, bg=bg_color)
        self.update_list()
    # access text file and view questions

    def question_view(self):
        self.list_qn = self.question_list[self.diff.upper()]
    # access text file and add question

    def question_update(self, input):
        self.txt_update = str(self.txtbox_qn.get())
        if (input.upper() == "ADD"):
            self.question_list[self.diff.upper()].append(self.txt_update)
            self.update_list()
    # on click remove
        elif (input.upper() == "REMOVE"):
            if (self.txt_update in self.list_qn):
                self.question_list[self.diff.upper()].remove(self.txt_update)
                self.update_list()
                messagebox.showinfo(
                    title="List Updated",
                    message=str(self.diff) + " List updated!"
                )
            else:
                messagebox.showinfo(
                    title="Question?",
                    message="Please input a valid question! (case-sensitive)")
                return
        else:
            messagebox.showwarning(message="ERROR")
            return

    # update list
    def update_list(self):
        self.question_view()
        self.lbox_qn.config(listvariable=tk.StringVar(value=self.list_qn))
