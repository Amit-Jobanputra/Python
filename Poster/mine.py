import random

# Board size
ROWS, COLS = 5, 5
MINES = 5  # Number of mines

# Generate empty board
def create_board():
    board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
    return board

# Place mines randomly
def place_mines(board):
    mine_positions = set()
    while len(mine_positions) < MINES:
        r, c = random.randint(0, ROWS - 1), random.randint(0, COLS - 1)
        if (r, c) not in mine_positions:
            mine_positions.add((r, c))
            board[r][c] = '*'  # Mine symbol
    return mine_positions

# Count mines around a cell
def count_adjacent_mines(board, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    count = 0
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == '*':
            count += 1
    return count

# Fill the board with mine counts
def generate_numbers(board):
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != '*':
                board[r][c] = str(count_adjacent_mines(board, r, c))

# Display board (hidden mode for unrevealed cells)
def display_board(board, revealed):
    print("\n   " + " ".join(str(i) for i in range(COLS)))  # Column indices
    print("  +" + "--" * COLS + "+")
    for r in range(ROWS):
        row_str = f"{r} |"
        for c in range(COLS):
            if revealed[r][c]:
                row_str += f" {board[r][c]}"
            else:
                row_str += " ."
        row_str += " |"
        print(row_str)
    print("  +" + "--" * COLS + "+")

# Reveal empty spaces (flood fill)
def reveal(board, revealed, row, col):
    if not (0 <= row < ROWS and 0 <= col < COLS) or revealed[row][col]:
        return
    revealed[row][col] = True
    if board[row][col] == '0':  # If no mines nearby, reveal neighbors
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr != 0 or dc != 0:
                    reveal(board, revealed, row + dr, col + dc)

# Check for win condition
def check_win(board, revealed):
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != '*' and not revealed[r][c]:
                return False  # Unrevealed safe cell remains
    return True

# Main game loop
def play_minesweeper():
    board = create_board()
    mines = place_mines(board)
    generate_numbers(board)
    revealed = [[False] * COLS for _ in range(ROWS)]  # Track revealed cells

    while True:
        display_board(board, revealed)
        try:
            row, col = map(int, input("\nEnter row and column (e.g., 1 2): ").split())
            if (row, col) in mines:
                print("\n💥 You hit a mine! Game Over.")
                break
            reveal(board, revealed, row, col)  # Reveal the selected cell
            if check_win(board, revealed):
                print("\n🎉 Congratulations! You cleared the board!")
                break
        except (ValueError, IndexError):
            print("Invalid input! Enter row and column numbers correctly.")

    # Show full board after game ends
    print("\nFinal Board:")
    for r in range(ROWS):
        print(" ".join(board[r]))

if __name__ == "__main__":
    play_minesweeper()
