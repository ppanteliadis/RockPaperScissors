# Simple Rock Paper Scissors
import random


draw = "Game is a DRAW"
p1_win = "P1 WINS"
com_win = "COM WINS"

moves = {"R": 1, "P": 2, "S": 3}

valid_moves = {"R", "P", "S", "E"}

# Make the game kernel. All the possible moves and their outcomes as well as a count for how many times they occurred.
game_kernel = {("R", "P"): com_win,
               ("R", "S"): p1_win,
               ("P", "R"): p1_win,
               ("P", "S"): com_win,
               ("S", "R"): com_win,
               ("S", "P"): p1_win,
               ("R", "R"): draw,
               ("P", "P"): draw,
               ("S", "S"): draw}

# Some dictionaries to hold some interesting game statistics
com_move_statistics = {"R": 0,
                       "P": 0,
                       "S": 0}


# Compare the outcome of the battle
def compare(player_move, com_move):
    return game_kernel[player_move, com_move]


# Print the statistics at the end of the game
def print_game_stats(dict):
    print("P1 Wins: %s | COM Wins: %s | Draws: %s" % (dict["P1 WINS"], dict["COM WINS"], dict["Game is a DRAW"]))


# Resets all the values of a dictionary to 0
def reset_dict(d):
    for v in d:
        d[v] = 0


# A basic animation function for the move.
def animate_move(move, p1=True):
    if move == "R":
        return "O"
    elif move == "P":
        return "__"
    elif move == "S":
        if p1:
            return "8<"
        else:
            return ">8"


def game(game_statistics, p1_move_statistics, p1_win_statistics):
    # Start the game
    while 1:
        print_game_stats(game_statistics)

        # Get the user input and make it uppercase.
        p1_move = input("Exit(E), Rock(R), Paper(P), Scissors(S), SHOOT: ").upper()

        while p1_move not in valid_moves:
            print("Restarting the score")
            reset_dict(game_statistics)
            reset_dict(p1_move_statistics)
            reset_dict(p1_win_statistics)

            # Get the user input and make it uppercase.
            p1_move = input("Exit(E), Rock(R), Paper(P), Scissors(S), SHOOT: ").upper()

        # Analyze the player's move
        if p1_move == 'E':
            break

        # Get the computer's move.
        com_move = random.choice(list(moves.keys()))

        print("P1: %s vs. COM: %s " % (animate_move(p1_move), animate_move(com_move, p1=False)))

        result = compare(p1_move, com_move)
        print(result)

        # Increment the appropriate scores
        game_statistics[result] += 1
        p1_move_statistics[p1_move] += 1

        if result == p1_win:
            p1_win_statistics[p1_move] += 1

