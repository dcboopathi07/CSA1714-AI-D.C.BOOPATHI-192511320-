
# Tic Tac Toe Game

board = [' '] * 9

def display():
    print()
    for i in range(0, 9, 3):
        print('|'.join(board[i:i+3]))
        if i < 6:
            print('-----')

def check_winner(player):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in wins
    )

player = 'X'

while True:
    display()
    try:
        pos = int(input(f"Player {player}, enter position (1-9): ")) - 1

        if pos not in range(9) or board[pos] != ' ':
            print("Invalid position! Try again.")
            continue

        board[pos] = player

        if check_winner(player):
            display()
            print(f"Player {player} wins!")
            break

        if ' ' not in board:
            display()
            print("It's a draw!")
            break

        player = 'O' if player == 'X' else 'X'

    except ValueError:
        print("Enter a valid number!")
