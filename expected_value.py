"""
This problem was asked by Two Sigma.

Alice wants to join her school's Probability Student Club. Membership dues are computed via one of two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate the two games and calculate their expected value.
"""
from random import randint

NUM_TRIALS = 1000000


def d6():
    return randint(1, 6)


def game_one():
    prev, curr = None, None
    cost = 0
    while prev != 5 or curr != 6:
        prev = curr
        curr = d6()
        cost += 1
    return cost


def ev_game_one():
    games = []
    for i in range(NUM_TRIALS):
        games.append(game_one())
    return sum(games) / len(games)


def game_two():
    prev, curr = None, None
    cost = 0
    while prev != 5 or curr != 5:
        prev = curr
        curr = d6()
        cost += 1
    return cost


def ev_game_two():
    games = []
    for i in range(NUM_TRIALS):
        games.append(game_two())
    return sum(games) / len(games)


if __name__ == '__main__':
    print('first game', ev_game_one())
    print('second game', ev_game_two())

"""
After running each game for 1000000 trials, we get:

$ 35.989 for game 1

$ 42.008 for game 2

So game 1 is indeed the better one to play.
"""