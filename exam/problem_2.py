from math import floor

number = int(input())
matrix = [[el for el in input().split()] for _ in range(number)]

movements = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1),
}

gold = 0

MOVES = []


def get_me_player_position(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'P':
                return (row, col)


def is_valid(new_row, new_col, number):
    if 0 <= new_row < number and 0 <= new_col < number:
        return True
    return False


def player_move(matrix, move, gold, number):
    has_lost = False
    player_position = get_me_player_position(matrix)
    row, col = player_position
    matrix[row][col] = 0
    r, c = move
    new_row = row + r
    new_col = col + c
    if is_valid(new_row, new_col, number):
        if not matrix[new_row][new_col] == 'X':
            gold += int(matrix[new_row][new_col])
            matrix[new_row][new_col] = 'P'
            has_lost = False
        else:
            gold = floor(gold / 2)
            has_lost = True
            moves = []
    else:
        gold = floor(gold / 2)
        has_lost = True
        moves = []
    return (matrix, gold, has_lost)


while True:
    command = input()
    if command in movements:
        move = movements[command]
        matrix, gold, has_lost, = player_move(matrix, move, gold, number)
        if has_lost:
            print(f"Game over! You've collected {gold} coins.")
            break
        MOVES.append(get_me_player_position(matrix))
    if gold >= 100:
        print(f"You won! You've collected {gold:.0f} coins.")
        break

print("Your path: ")
if MOVES:
    [print(list(el)) for el in MOVES]
