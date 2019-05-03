# Simple Rock Paper Scissors
from collections import OrderedDict
from game import game
from graphs import plot


# Init all the needed dictionaries and variables
draw = "Game is a DRAW"
p1_win = "P1 WINS"
com_win = "COM WINS"

game_statistics = {draw: 0,
                   p1_win: 0,
                   com_win: 0}

p1_move_statistics = OrderedDict({"R": 0,
                                  "P": 0,
                                  "S": 0})

p1_win_statistics = OrderedDict({"R": 0,
                                 "P": 0,
                                 "S": 0})

if __name__ == '__main__':

    game(game_statistics, p1_move_statistics, p1_win_statistics)

    plot(list(p1_move_statistics.values()), list(p1_win_statistics.values()))

    print(p1_win_statistics)
    print(p1_move_statistics)
    print(game_statistics)
