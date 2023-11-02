def get_new_board():
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]


def check_winner(board):
    """
    1. Check each row
    2. Check each column
    3. Check left to right diagonal
    4. Check right to left diagonal
    5. Return draw if board is full
    6. Game is not finished
    """

    board_length = len(board)

    for row in board:
        if len(set(row)) == 1:
            return row[0]

    for col_idx in range(board_length):
        column = [board[row_idx][col_idx] for row_idx in range(board_length)]
        if len(set(column)) == 1:
            return column[0]

    left_to_right_diag = []
    for idx, row in enumerate(board):
        left_to_right_diag.append(row[idx])
    if len(set(left_to_right_diag)) == 1:
        return left_to_right_diag[0]

    right_to_left_diag = []
    for idx, row in enumerate(board):
        board_end_idx = board_length - 1
        right_to_left_diag.append(row[board_end_idx - idx])
    if len(set(right_to_left_diag)) == 1:
        return right_to_left_diag[0]

    all_marks = [mark for row in board for mark in row]
    if not " " in all_marks:
        return "draw"

    return " "
