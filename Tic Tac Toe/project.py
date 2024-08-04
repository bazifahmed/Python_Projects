import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("486x513")
        self.player_turn = "X"
        self.buttons = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, command=lambda row=i, column=j: self.click(row, column), height=4, width=8, font=('Helvetica', 24))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def click(self, row, column):
        if self.buttons[row][column]['text'] == "":
            self.buttons[row][column]['text'] = self.player_turn
            if self.check_win():
                self.buttons[row][column]['bg'] = 'green'
                messagebox.showinfo("Game Over", f"Player {self.player_turn} wins!")
                self.window.quit()
            self.player_turn = "O" if self.player_turn == "X" else "X"

    def check_win(self):
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                row[0]['bg'] = row[1]['bg'] = row[2]['bg'] = 'green'
                return True
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                self.buttons[0][column]['bg'] = self.buttons[1][column]['bg'] = self.buttons[2][column]['bg'] = 'green'
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            self.buttons[0][0]['bg'] = self.buttons[1][1]['bg'] = self.buttons[2][2]['bg'] = 'green'
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            self.buttons[0][2]['bg'] = self.buttons[1][1]['bg'] = self.buttons[2][0]['bg'] = 'green'
            return True
        return False

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()