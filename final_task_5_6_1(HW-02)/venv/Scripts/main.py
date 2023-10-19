tabel = [
    [' ', '1', '2', '3'],
    ['1', '-', '-', '-'],
    ['2', '-', '-', '-'],
    ['3', '-', '-', '-']
]

def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end= ' ')
        print()


def check_win(board, player):
    for row in board:
        if row.count(player)  == 3:
            return True

    for i in range(3):
        if board[1][i] == player and board[2][i] == player and board[3][i] == player:
            return True
        if board[i][1] == player and board[i][2] == player and board[i][3] == player:
            return True

    if board[1][1] == player and board[2][2] == player and board[3][3] == player:
        return True

    if board[1][3] == player and board[2][2] == player and board[3][1] == player:
        return True

current_player = 'X'

while True:
    print_board(tabel)
    print('Ход игрока', current_player)


    row = int(input('Введите номер строки: '))
    if row < 1 or row > 3:
        print('Некоректное значение!')
        continue

    col = int(input('Введите номер столбца: '))
    if col < 1 or col > 3:
        print('Некоректное значение!')
        continue

    if tabel[row][col] != '-':
        print('Выберите свободную ячейку!')
        continue

    tabel[row][col] = current_player

    if check_win(tabel, current_player):
        print_board(tabel)
        print(f'Игрок,  {current_player}, выиграл!')
        break

    if all([cell != '-' for row in tabel for cell in row]):
        print_board(tabel)
        print('Ничья!')
        break

    current_player = '0' if current_player == 'X' else "X"


