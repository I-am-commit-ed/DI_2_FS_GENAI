# Tic Tac Toe (2 players, command line)
# Covers: 2D lists, while loops, conditionals, functions, input validation

def create_board():
    # 3x3 board filled with spaces
    return [[" " for _ in range(3)] for _ in range(3)]


def display_board(board):
    # Nicely formatted 3x3 grid
    print("\n   1   2   3")
    for r in range(3):
        row_display = " | ".join(board[r])
        print(f"{r+1}  {row_display}")
        if r < 2:
            print("  ---+---+---")
    print()


def player_input(board, player_symbol):
    """
    Ask for row and column (1-3).
    Validate:
      - must be two numbers
      - must be in range
      - chosen cell must be empty
    Returns: (row_index, col_index) as 0-based indices
    """
    while True:
        raw = input(f"Player {player_symbol}, enter row and column (e.g. 2 3): ").strip()

        parts = raw.split()
        if len(parts) != 2:
            print("Invalid input. Please enter TWO numbers: row col (example: 2 3).")
            continue

        if not (parts[0].isdigit() and parts[1].isdigit()):
            print("Invalid input. Row and column must be numbers (1 to 3).")
            continue

        row = int(parts[0])
        col = int(parts[1])

        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Out of range. Row and column must be between 1 and 3.")
            continue

        r_idx = row - 1
        c_idx = col - 1

        if board[r_idx][c_idx] != " ":
            print("That cell is already taken. Choose another one.")
            continue

        return r_idx, c_idx


def check_win(board, player_symbol):
    # Check rows
    for r in range(3):
        if all(board[r][c] == player_symbol for c in range(3)):
            return True

    # Check columns
    for c in range(3):
        if all(board[r][c] == player_symbol for r in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player_symbol for i in range(3)):
        return True
    if all(board[i][2 - i] == player_symbol for i in range(3)):
        return True

    return False


def check_tie(board):
    # Tie if no empty spaces left
    return all(board[r][c] != " " for r in range(3) for c in range(3))


def switch_player(current_symbol):
    return "O" if current_symbol == "X" else "X"


def play():
    board = create_board()
    current_player = "X"  # X starts

    print("Welcome to Tic Tac Toe!")
    print("Players take turns placing X and O.")
    print("Enter your move as: row col (example: 1 3)\n")

    while True:
        display_board(board)

        r, c = player_input(board, current_player)
        board[r][c] = current_player

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        current_player = switch_player(current_player)


if __name__ == "__main__":
    play()
