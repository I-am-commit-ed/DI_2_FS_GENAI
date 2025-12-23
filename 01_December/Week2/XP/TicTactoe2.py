# Tic Tac Toe (2 players) - uses ONLY the 4 main functions from the hint:
# display_board(), player_input(player), check_win(), play()

# Global board so the functions match the exact signatures from the assignment
board = [[" " for _ in range(3)] for _ in range(3)]


def display_board():
    """
    Displays the 3x3 board.
    Empty cells show their position number (1-9) to make input easy.
    """
    print("\nTic Tac Toe\n")

    pos = 1
    for r in range(3):
        row_cells = []
        for c in range(3):
            cell = board[r][c]
            row_cells.append(str(pos) if cell == " " else cell)
            pos += 1

        print(" " + " | ".join(row_cells))
        if r < 2:
            print("---+---+---")
    print()


def player_input(player):
    """
    Asks the current player for a position (1-9).
    Validates:
      - input is a number
      - input is in range 1-9
      - chosen spot is empty
    Returns: (row, col) as 0-based indices
    """
    while True:
        choice = input(f"Player {player}, choose a position (1-9): ").strip()

        if not choice.isdigit():
            print("Invalid input. Please type a number from 1 to 9.")
            continue

        pos = int(choice)
        if pos < 1 or pos > 9:
            print("Out of range. Choose a number from 1 to 9.")
            continue

        # Convert position (1-9) to row/col
        pos_index = pos - 1
        row = pos_index // 3
        col = pos_index % 3

        if board[row][col] != " ":
            print("That spot is taken. Choose another.")
            continue

        return row, col


def check_win():
    """
    Checks if there is a winner.
    Returns:
      'X' or 'O' if someone won,
      None otherwise.
    """
    # Rows
    for r in range(3):
        if board[r][0] != " " and board[r][0] == board[r][1] == board[r][2]:
            return board[r][0]

    # Columns
    for c in range(3):
        if board[0][c] != " " and board[0][c] == board[1][c] == board[2][c]:
            return board[0][c]

    # Diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None


def play():
    """
    Main game loop:
      - show board
      - get move
      - place mark
      - check win / tie
      - switch player
    """
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]  # reset board each new game

    current_player = "X"  # X starts

    while True:
        display_board()

        row, col = player_input(current_player)
        board[row][col] = current_player

        winner = check_win()
        if winner:
            display_board()
            print(f"Player {winner} wins!")
            break

        # Tie check: no empty spaces left
        is_tie = True
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    is_tie = False
                    break
            if not is_tie:
                break

        if is_tie:
            display_board()
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


# Run the game
play()
