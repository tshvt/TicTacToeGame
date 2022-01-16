from random import randint


class AI:
    def __init__(self, players_moves):
        self.moves = players_moves

    def check_for_spot(self):
        if self.moves[0] == "X" and self.moves[1] == "X" and self.moves[2] == " ":
            return 3
        elif self.moves[1] == "X" and self.moves[2] == "X" and self.moves[0] == " ":
            return 1
        elif self.moves[0] == "X" and self.moves[2] == "X" and self.moves[1] == " ":
            return 2
        elif self.moves[0] == "X" and self.moves[3] == "X" and self.moves[6] == " ":
            return 7
        elif self.moves[0] == "X" and self.moves[6] == "X" and self.moves[3] == " ":
            return 4
        elif self.moves[3] == "X" and self.moves[6] == "X" and self.moves[0] == " ":
            return 1
        elif self.moves[0] == "X" and self.moves[4] == "X" and self.moves[8] == " ":
            return 9
        elif self.moves[0] == "X" and self.moves[8] == "X" and self.moves[4] == " ":
            return 5
        elif self.moves[8] == "X" and self.moves[4] == "X" and self.moves[0] == " ":
            return 1
        elif self.moves[1] == "X" and self.moves[4] == "X" and self.moves[7] == " ":
            return 8
        elif self.moves[1] == "X" and self.moves[7] == "X" and self.moves[4] == " ":
            return 5
        elif self.moves[4] == "X" and self.moves[7] == "X" and self.moves[1] == " ":
            return 2
        elif self.moves[2] == "X" and self.moves[5] == "X" and self.moves[8] == " ":
            return 9
        elif self.moves[2] == "X" and self.moves[8] == "X" and self.moves[5] == " ":
            return 6
        elif self.moves[5] == "X" and self.moves[8] == "X" and self.moves[2] == " ":
            return 3
        elif self.moves[3] == "X" and self.moves[4] == "X" and self.moves[5] == " ":
            return 6
        elif self.moves[6] == "X" and self.moves[7] == "X" and self.moves[8] == " ":
            return 9
        elif self.moves[7] == "X" and self.moves[8] == "X" and self.moves[6] == " ":
            return 7
        elif self.moves[6] == "X" and self.moves[8] == "X" and self.moves[7] == " ":
            return 8
        elif self.moves[2] == "X" and self.moves[4] == "X" and self.moves[6] == " ":
            return 7
        elif self.moves[2] == "X" and self.moves[6] == "X" and self.moves[4] == " ":
            return 5
        elif self.moves[4] == "X" and self.moves[6] == "X" and self.moves[2] == " ":
            return 3
        else:
            if self.moves[4] == " ":
                return 5
            else:
                next_move = randint(0, 8)
                while not self.is_empty(next_move):
                    next_move = randint(0, 8)
                return next_move+1

    def is_empty(self, number):
        if self.moves[number] == " ":
            return True
