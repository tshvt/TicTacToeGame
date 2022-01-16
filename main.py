from ai_opponent import AI

moves_rules = [n for n in range(1, 10)]

start_field = f''' 
 {moves_rules[0]} | {moves_rules[1]} | {moves_rules[2]}
----------
 {moves_rules[3]} | {moves_rules[4]} | {moves_rules[5]}
----------
 {moves_rules[6]} | {moves_rules[7]} | {moves_rules[8]}
'''


def make_move_x(number):
    moves[number - 1] = "X"
    field = f''' 
    {moves[0]} | {moves[1]} | {moves[2]}
    ----------
    {moves[3]} | {moves[4]} | {moves[5]}
    ----------
    {moves[6]} | {moves[7]} | {moves[8]}
    '''
    return field


def make_move_o(number):
    moves[number - 1] = "O"
    field = f''' 
    {moves[0]} | {moves[1]} | {moves[2]}
    ----------
    {moves[3]} | {moves[4]} | {moves[5]}
    ----------
    {moves[6]} | {moves[7]} | {moves[8]}
    '''
    return field


def is_empty(number):
    if moves[number - 1] == " ":
        return True


def check_for_win():
    for symbol in ["X", "O"]:
        if moves[0] == symbol and moves[1] == symbol and moves[2] == symbol:
            return f"Player {symbol} wins!"
        elif moves[0] == symbol and moves[3] == symbol and moves[6] == symbol:
            return f"Player {symbol} wins!"
        elif moves[0] == symbol and moves[4] == symbol and moves[8] == symbol:
            return f"Player {symbol} wins!"
        elif moves[1] == symbol and moves[4] == symbol and moves[7] == symbol:
            return f"Player {symbol} wins!"
        elif moves[2] == symbol and moves[5] == symbol and moves[8] == symbol:
            return f"Player {symbol} wins!"
        elif moves[3] == symbol and moves[4] == symbol and moves[5] == symbol:
            return f"Player {symbol} wins!"
        elif moves[6] == symbol and moves[7] == symbol and moves[8] == symbol:
            return f"Player {symbol} wins!"
        elif moves[2] == symbol and moves[4] == symbol and moves[6] == symbol:
            return f"Player {symbol} wins!"
        else:
            if " " not in moves:
                return "Seems like it's a draw! Good game."


print(f"Welcome to the Tic Tac Toe Game!{start_field}"
      f"The rules are simple: \n1)First player plays 'X'. Another person - 'O'."
      f"\n2)The first player to get 3 of their marks in a row"
      f" (up, down, across, or diagonally) is the winner."
      f"\n3)When all 9 squares are full, the game is over."
      f"\n4)To choose a spot on the field write the number."
      f"\nLet's go!\n")

type_of_game = input("Do you want to play with your friend or versus a very smart computer? "
                     "\nType 'C' to choose a bot opponent: ")


game_on = True
moves = [" " for n in range(1, 10)]
while game_on:

    player_x = int(input("Player X, it's your turn: "))
    while not is_empty(player_x):
        player_x = int(input("This place is already taken! Try again: "))
    print(make_move_x(player_x))
    if check_for_win():
        print(check_for_win())
        break

    if type_of_game.upper() != "C":
        player_o = int(input("Player O, it's your turn: "))
        while not is_empty(player_o):
            player_o = int(input("This place is already taken! Try again: "))
    else:
        ai_opponent = AI(moves)
        player_o = ai_opponent.check_for_spot()
    print(make_move_o(player_o))
    if check_for_win():
        print(check_for_win())
        break
