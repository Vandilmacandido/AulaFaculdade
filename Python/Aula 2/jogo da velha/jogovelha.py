import tkinter as tk
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        # Create the game board
        self.buttons = []
        for i in range(9):
            button = tk.Button(master, text="", width=5, height=2, command=lambda x=i: self.player_move(x))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        self.player_symbol = "X"
        self.computer_symbol = "O"
        self.current_player = self.player_symbol

        self.status_label = tk.Label(master, text=f"{self.current_player}'s turn")
        self.status_label.grid(row=3, column=0, columnspan=3)

        self.reset_button = tk.Button(master, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=4, column=0, columnspan=3)

    def player_move(self, position):
        if self.buttons[position]["text"] == "":
            self.buttons[position]["text"] = self.player_symbol
            self.check_winner(self.player_symbol)
            self.current_player = self.computer_symbol
            self.computer_move()
            self.check_winner(self.computer_symbol)
            self.status_label.config(text=f"{self.current_player}'s turn")

    def computer_move(self):
        available_positions = [i for i in range(9) if self.buttons[i]["text"] == ""]
        position = random.choice(available_positions)
        self.buttons[position]["text"] = self.computer_symbol

    def check_winner(self, symbol):
        # Check rows
        for i in range(0, 9, 3):
            if self.buttons[i]["text"] == self.buttons[i+1]["text"] == self.buttons[i+2]["text"] == symbol:
                self.display_winner(symbol)
                return
        # Check columns
        for i in range(3):
            if self.buttons[i]["text"] == self.buttons[i+3]["text"] == self.buttons[i+6]["text"] == symbol:
                self.display_winner(symbol)
                return
        # Check diagonals
        if self.buttons[0]["text"] == self.buttons[4]["text"] == self.buttons[8]["text"] == symbol:
            self.display_winner(symbol)
            return
        if self.buttons[2]["text"] == self.buttons[4]["text"] == self.buttons[6]["text"] == symbol:
            self.display_winner(symbol)
            return
        # Check if the game is a tie
        if all(button["text"] != "" for button in self.buttons):
            self.display_winner("tie")

    def display_winner(self, winner):
        if winner == "tie":
            self.status_label.config(text="It's a tie!")
        else:
            self.status_label.config(text=f"{winner} wins!")

    def reset_game(self):
        for button in self.buttons:
            button["text"] = ""
        self.current_player = self.player_symbol
        self.status_label.config(text=f"{self.current_player}'s turn")

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()