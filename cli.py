from logic import get_new_board, check_winner

logo = """
___________.__         ___________               ___________            
\__    ___/|__| ____   \__    ___/____    ____   \__    ___/___   ____  
  |    |   |  |/ ___\    |    |  \__  \ _/ ___\    |    | /  _ \_/ __ \ 
  |    |   |  \  \___    |    |   / __ \\\  \___    |    |(  <_> )  ___/ 
  |____|   |__|\___  >   |____|  (____  /\___  >   |____| \____/ \___  >
                   \/                 \/     \/                      \/ 
                   
How to play:
    player O > row_num, col_num
    player O > 0,0

    ['O', ' ', ' ']
    [' ', ' ', ' ']
    [' ', ' ', ' ']

=========================================================================
"""


def print_board(board):
    print("     0   1   2")
    print("   -------------")
    for i, row in enumerate(board):
        print(f"{i} | {' | '.join(row)} |")
        print("   -------------")


if __name__ == "__main__":
    board = get_new_board()
    current_player = 'O'
    winner = ' '
    print(logo)
    while winner is ' ':
        print_board(board)
        player_input = input(f"player {current_player} > ")
        try:
            row, col = [int(x.strip()) for x in player_input.split(',')]
        except ValueError as e:
            print("Please enter valid play move\n")
            continue

        if row >= len(board[0]) or col >= len(board):
            print("You placed a mark out of bounds! Try again...\n")
            continue

        if not board[row][col] == ' ':
            print(
                f"{board[row][col]} already marked {row},{col}, please select another place\n")
            continue

        board[row][col] = current_player
        winner = check_winner(board)
        current_player = 'O' if current_player == 'X' else 'X'
        print('\n')

    print_board(board)
    print(f"winner is {winner}")
