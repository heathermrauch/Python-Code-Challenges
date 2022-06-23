'''
Tic Tac Toe blocker

In this Python challenge, write a function that’ll accept two numbers. These
numbers will represent a position on a tic-tac-toe board. They can be 0 through
8, where 0 is the top-left spot, and 8 is the bottom-right spot.

These parameters are two marks on the tic-tac-toe board. The function should
return the number of the spot that can block these two spots from winning the
game.

Original Challenge found here:
https://www.codecademy.com/resources/blog/advanced-python-code-challenges/
'''


def blocker(one:int, two:int):
    wins = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8]]
    for row in wins:
        if one in row and two in row:
            row.remove(one)
            row.remove(two)
            return row.pop()


if __name__ == '__main__':

    first_move = 2
    second_move = 5
    print(blocker(first_move, second_move))
