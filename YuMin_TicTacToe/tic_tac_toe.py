import tkinter as tk
from tkinter import font
from typing import NamedTuple
import Jerrick_Menu.menu as menu
from ZQ_Algo.easy import easy as ai_easy
from ZQ_Algo.medium import medium as ai_medium
from ZQ_Algo.hard import hard as ai_hard
from Lukas_Forfeits_Questions.TicTacToe_Question_Generator import QuestionGenerator
from Lukas_Forfeits_Questions.TicTacToe_Forfeit_Generator import ForfeitGenerator
import Nat_Leaderboard.highscore as hs
from Chris_Questions.question_v2 import QuestionPopup


class Player(NamedTuple):
    label: str
    color: str


class Move(NamedTuple):
    row: int
    col: int
    label: str = ""


BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label="X", color="blue"),
    Player(label="O", color="green"),
)


class Game():
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self._players = players
        self.board_size = board_size
        self.current_player = self._players[0]
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_combos = []
        self._setup_board()

    def _setup_board(self):
        self._current_moves = [
            [Move(row, col) for col in range(self.board_size)]
            for row in range(self.board_size)
        ]
        self._winning_combos = self._get_winning_combos()

    def _get_winning_combos(self):
        rows = [
            [(move.row, move.col) for move in row]
            for row in self._current_moves
        ]
        columns = [list(col) for col in zip(*rows)]
        first_diagonal = [row[i] for i, row in enumerate(rows)]
        second_diagonal = [col[j] for j, col in enumerate(reversed(columns))]
        return rows + columns + [first_diagonal, second_diagonal]

    def is_valid_move(self, move):
        # Return True if move is valid, and False otherwise.
        row, col = move.row, move.col
        move_was_not_played = self._current_moves[row][col].label == ""
        no_winner = not self._has_winner
        return no_winner and move_was_not_played

    def process_move(self, move):
        # Process the current move and check if it's a win.
        row, col = move.row, move.col
        self._current_moves[row][col] = move
        for combo in self._winning_combos:
            results = set(
                self._current_moves[n][m].label
                for n, m in combo
            )
            is_win = (len(results) == 1) and ("" not in results)
            if is_win:
                self._has_winner = True
                self.winner_combo = combo
                break

    def has_winner(self):
        # Return True if the game has a winner, and False otherwise.
        return self._has_winner

    def is_tied(self):
        # Return True if the game is tied, and False otherwise.
        no_winner = not self._has_winner
        played_moves = (
            move.label for row in self._current_moves for move in row
        )
        return no_winner and all(played_moves)

    def toggle_player(self):
        # Return a toggled player.
        self.current_player = self._players[0] if self.current_player == self._players[1] else self._players[1]

    def reset_game(self):
        # Reset the game state to play again.
        for row, row_content in enumerate(self._current_moves):
            for col, _ in enumerate(row_content):
                row_content[col] = Move(row, col)
        self._has_winner = False
        self.winner_combo = []


class Board(tk.Frame):
    def __init__(self, game, parent, controller, difficulty_var, username_var):
        tk.Frame.__init__(self, parent)
        self._cells = {}
        self._game = game
        self.diff = difficulty_var
        self.username = username_var
        self.controller = controller
        self.question_generator = QuestionGenerator()
        self._create_board_display()
        self._create_board_grid()

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold")
        )
        self.display.pack()

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        self.buttons = []
        for row in range(self._game.board_size):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(self._game.board_size):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight="bold"),
                    fg="black",
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)
                button.configure(command=lambda b=button: self.play(b))
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky="nsew"
                )
                self.buttons.append(button)

    def play(self, clicked_btn):
        # Handle a player's move.
        row, col = self._cells[clicked_btn]
        move = Move(row, col, self._game.current_player.label)
        question = self.question_generator.get_question(self.diff.get())

        if self._game.is_valid_move(move):

            # TODO: Change to use Chris's Frame
            is_answer_correct = tk.BooleanVar()
            self.popup = QuestionPopup(
                question, self.diff.get(), is_answer_correct)
            self.wait_window(self.popup)

            if is_answer_correct.get():

                self._update_button(clicked_btn)
                self._game.process_move(move)

                if self._game.is_tied():
                    self._update_display(msg="Tied game!", color="red")
                    self.update()
                    tk.messagebox.showinfo(message="Game was tied!")
                    self._update_button(clicked_btn)
                    self.reset_board()
                    self.question_generator.reset_questions()
                    self.controller.show_frame(menu.Menu)

                elif self._game.has_winner():
                    self._highlight_cells()
                    msg = f'Player "{self._game.current_player.label}" won!'
                    color = self._game.current_player.color
                    self._update_display(msg, color)
                    self.update()
                    if not self.diff.get() == "2P":
                        hs.update_score(self.username.get(), self.diff.get())
                    tk.messagebox.showinfo(
                        message=f"{self._game.current_player.label} won!")
                    self._update_button(clicked_btn)
                    self.reset_board()
                    self.question_generator.reset_questions()
                    self.controller.show_frame(menu.Menu)

            if self.diff.get() == "2P":
                self._game.toggle_player()
                msg = f"{self._game.current_player.label}'s turn"
                self._update_display(msg)

            else:  # AI plays
                self.update()
                self.after(1000)
                # check difficulty
                diff = self.diff.get()
                # Use AI to calculate move
                board_state = []
                for row in self._game._current_moves:
                    for move in row:
                        board_state.append(move.label)
                ai_move = self._get_ai_move(
                    diff, board_state, self._game.current_player.label)
                # Toggle turn and play the AI’s move and update current moves
                self._game.toggle_player()
                self._update_button(self.buttons[ai_move])
                ai_row = (ai_move) // 3
                ai_col = (ai_move) % 3
                move = Move(ai_row, ai_col, self._game.current_player.label)
                self._game.process_move(move)
                if self._game.is_tied():
                    self._update_display(msg="Tied game!", color="red")
                    self.update()
                    tk.messagebox.showinfo(message="Game was tied!")
                    self._update_button(clicked_btn)
                    self.reset_board()
                    self.question_generator.reset_questions()
                    self.controller.show_frame(menu.Menu)

                elif self._game.has_winner():
                    self._highlight_cells()
                    msg = f'Player "{self._game.current_player.label}" won!'
                    color = self._game.current_player.color
                    self._update_display(msg, color)
                    self.update()
                    # TODO: Show Forfeit
                    tk.messagebox.showinfo(
                        message=f"{self._game.current_player.label} won!")
                    tk.messagebox.showinfo(
                        title="Do your forfeit!",
                        message=f"{ForfeitGenerator().get_forfeit(self.diff.get())}")
                    self._update_button(clicked_btn)
                    self.reset_board()
                    self.question_generator.reset_questions()
                    self.controller.show_frame(menu.Menu)

                # Toggle move back
                self._game.toggle_player()

    # returns a number from 0-8 that corresponds to a
    # square on the tictactoe board

    def _get_ai_move(self, difficulty: str, board_state, player):
        if difficulty == "EASY":
            return ai_easy(board_state)
        elif difficulty == "MEDIUM":
            return ai_medium(player, board_state)
        else:
            return ai_hard(player, board_state)

    def _update_button(self, clicked_btn):
        clicked_btn.config(text=self._game.current_player.label)
        clicked_btn.config(fg=self._game.current_player.color)

    def _update_display(self, msg, color="black"):
        self.display["text"] = msg
        self.display["fg"] = color

    def _highlight_cells(self):
        for button, coordinates in self._cells.items():
            if coordinates in self._game.winner_combo:
                button.config(highlightbackground="red")

    def reset_board(self):
        # Reset the game's board to play again.
        self._game.reset_game()
        self._update_display(msg="Ready?")
        for button in self._cells.keys():
            button.config(highlightbackground="lightblue")
            button.config(text="")
            button.config(fg="black")
