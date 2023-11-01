from logic import get_new_board, check_winner


def print_board(board):
    for row in board:
        row = [' ' if x is None else x for x in row]
        print(row)


if __name__ == "__main__":
    board = get_new_board()
    current_player = 'O'
    winner = None
    print("we have a new board")
    while winner is None:
        print_board(board)
        player_input = input(f"player {current_player} > ")
        try:
            row, col = [int(x.strip()) for x in player_input.split(',')]
        except ValueError as e:
            print("Please enter valid play move\n")
            continue

        if board[row][col]:
            print(
                f"{board[row][col]} already marked {row},{col}, please select another place\n")
            continue

        board[row][col] = current_player
        winner = check_winner(board)
        current_player = 'O' if current_player == 'X' else 'X'
        print('\n')

    print_board(board)
    print(f"winner is {winner}")
