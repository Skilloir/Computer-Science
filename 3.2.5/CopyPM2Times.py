import random

strategy_name = "Copy Previous move 2 times and rock if the opponent does scissors more than once"

def beat_move(move):
    if (move=="r"):
        return "p"
    if (move == "p"):
        return "s"
    if (move=="s"):
        return "r"

def move(my_history, their_history):
    """This player always starts with rock
    """
    if (len(their_history) > 1):
        return "r"
    if (their_history[-1] == their_history[-2]):
        return beat_move(their_history[-1])
    return random.choice(["p", "s"])