import tkinter as tk
from tkinter import messagebox
import random


class Othello:
    def __init__(self):
        self.board = []
        for _ in range(8):
            row = []
            for _ in range(8):
                row.append(' ')
            self.board.append(row)
        self.board[3][3] = 'W'
        self.board[4][4] = 'W'
        self.board[3][4] = 'B'
        self.board[4][3] = 'B'
        self.current_player = 'B'

    def print_board(self):
        print("   A B C D E F G H")
        for i in range(8):
            print(i + 1, end=' ')
            for j in range(8):
                print('|' + self.board[i][j], end=' ')
            print('|')

    def is_valid_move(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        if self.board[row][col] != ' ':
            return False
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            found_opponent = False
            while 0 <= r < 8 and 0 <= c < 8:
                if self.board[r][c] == ' ':
                    break
                elif self.board[r][c] == self.current_player:
                    if found_opponent:
                        return True
                    else:
                        break
                else:
                    found_opponent = True
                    r += dr
                    c += dc
        return False

    def make_move(self, row, col):
        if not self.is_valid_move(row, col):
            return False
        self.board[row][col] = self.current_player
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            to_flip = []
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == self.opponent():
                to_flip.append((r, c))
                r += dr
                c += dc
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == self.current_player:
                for flip_r, flip_c in to_flip:
                    self.board[flip_r][flip_c] = self.current_player
        self.current_player = self.opponent()
        return True

    def opponent(self):
        return 'B' if self.current_player == 'W' else 'W'

    def count_discs(self):
        black_count = sum(row.count('B') for row in self.board)
        white_count = sum(row.count('W') for row in self.board)
        return black_count, white_count

    def is_game_over(self):
        for row in range(8):
            for col in range(8):
                if self.is_valid_move(row, col) :
                    return False
        return True

    def determine_winner(self):
        black_count, white_count = self.count_discs()
        if black_count > white_count:
            return 'Black'
        elif white_count > black_count:
            return 'White'
        else:
            return 'Tie'

    def get_valid_moves(self):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                if self.is_valid_move(row, col):
                    valid_moves.append((row, col))
        return valid_moves

    def play_alphabeta(self, depth, alpha=float('-inf'), beta=float('inf'), maximizing_player=True):
        valid_moves = self.get_valid_moves()
        if depth == 0 or not valid_moves:
            black_count, white_count = self.count_discs()
            return black_count - white_count if maximizing_player else white_count - black_count, None

        if maximizing_player:
            max_value = float('-inf')
            best_move = None
            for move in valid_moves:
                new_board = Othello()
                new_board.board = [row[:] for row in self.board]
                new_board.current_player = self.current_player
                new_board.make_move(move[0], move[1])
                value, _ = new_board.play_alphabeta(depth - 1, alpha, beta, False)
                if value > max_value:
                    max_value = value
                    best_move = move
                alpha = max(alpha, max_value)
                if alpha >= beta:
                    break
            return max_value, best_move
        else:
            min_value = float('inf')
            best_move = None
            for move in valid_moves:
                new_board = Othello()
                new_board.board = [row[:] for row in self.board]
                new_board.current_player = self.current_player
                new_board.make_move(move[0], move[1])
                value, _ = new_board.play_alphabeta(depth - 1, alpha, beta, True)
                if value < min_value:
                    min_value = value
                    best_move = move
                beta = min(beta, min_value)
                if alpha >= beta:
                    break
            return min_value, best_move


class OthelloGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Othello")
        self.game = Othello()
        self.buttons = [[None for _ in range(8)] for _ in range(8)]
        self.difficulty_level = tk.StringVar(value='medium')
        self.create_board()
        self.create_info_labels()
        self.create_menu()

    def create_board(self):
        for row in range(8):
            for col in range(8):
                button = tk.Button(self.master, width=5, height=2, command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
                self.update_button(row, col)

    def create_info_labels(self):
        self.black_count_label = tk.Label(self.master, text="Black: 2", font=("Arial", 12, "bold"), fg="black")
        self.black_count_label.grid(row=8, column=0, columnspan=4)
        self.white_count_label = tk.Label(self.master, text="White: 2", font=("Arial", 12, "bold"), fg="black", bg="gray")
        self.white_count_label.grid(row=8, column=4, columnspan=4)

    def create_menu(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)
        difficulty_menu = tk.Menu(menu_bar, tearoff=0)
        difficulty_menu.add_radiobutton(label="Easy", variable=self.difficulty_level, value='easy')
        difficulty_menu.add_radiobutton(label="Medium", variable=self.difficulty_level, value='medium')
        difficulty_menu.add_radiobutton(label="Hard", variable=self.difficulty_level, value='hard')
        menu_bar.add_cascade(label="Difficulty", menu=difficulty_menu)
        menu_bar.add_command(label="Play Again", command=self.play_again)
        menu_bar.add_command(label="Exit", command=self.master.destroy)

    def update_button(self, row, col):
        color = self.game.board[row][col]
        if color == 'B':
            bg_color = 'black'
        elif color == 'W':
            bg_color = 'white'
        elif (row, col) in self.game.get_valid_moves():
            bg_color = 'light green'
        else:
            bg_color = 'dark green'
        self.buttons[row][col].config(bg=bg_color)

    def make_move(self, row, col):
        if self.game.current_player == 'B':  # Only allow human player to move when it's their turn
            if self.game.make_move(row, col):
                self.update_board()
                self.update_counts()
                if self.game.is_game_over():
                    self.show_winner()
                else:
                    self.master.after(1000, self.ai_move)  # Wait for 1 second before AI move

    def update_board(self):
        for row in range(8):
            for col in range(8):
                self.update_button(row, col)

    def update_counts(self):
        black_count, white_count = self.game.count_discs()
        self.black_count_label.config(text=f"Black: {black_count}")
        self.white_count_label.config(text=f"White: {white_count}")

    def ai_move(self):
        if self.difficulty_level.get() == 'easy':
            depth = 1
        elif self.difficulty_level.get() == 'medium':
            depth = 3
        else:
            depth = 5
        _, best_move = self.game.play_alphabeta(depth)
        self.game.make_move(best_move[0], best_move[1])
        self.update_board()
        self.update_counts()
        if self.game.is_game_over():
            self.show_winner()

    def show_winner(self):
        winner = self.game.determine_winner()
        messagebox.showinfo("Game Over", f"{winner} wins!")
        self.play_again()

    def play_again(self):
        self.game = Othello()
        self.update_board()
        self.update_counts()


if __name__ == "__main__":
    root = tk.Tk()
    app = OthelloGUI(root)
    root.mainloop()
