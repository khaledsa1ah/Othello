class Othello:
    def __init__(self):
        self.board = [[' ' for _ in range(8)] for _ in range(8)]
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
            while 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == self.opponent():
                r += dr
                c += dc
            if 0 <= r < 8 and 0 <= c < 8 and self.board[r][c] == self.current_player:
                return True
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
        return not any(self.is_valid_move(row, col) for row in range(8) for col in range(8))

    def determine_winner(self):
        black_count, white_count = self.count_discs()
        if black_count > white_count:
            return 'Black'
        elif white_count > black_count:
            return 'White'
        else:
            return 'Tie'


# Example usage:
game = Othello()
game.print_board()

while not game.is_game_over():
    print(f"Current player: {game.current_player}")
    move = input("Enter your move (e.g., A3): ")
    col = ord(move[0].upper()) - ord('A')
    row = int(move[1]) - 1
    if game.make_move(row, col):
        game.print_board()
    else:
        print("Invalid move. Try again.")

winner = game.determine_winner()
print(f"Game over! {winner} wins.")
