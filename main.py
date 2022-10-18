# Conway's Game Of Life
# The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells,
# each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively).
# Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or
# diagonally adjacent. At each step in time, the following transitions occur:

# 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
# 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
import os
import random
from time import sleep
import sys
import getopt


def _roll_for_value():
    roll = random.randint(0, 100)
    v = 0
    if roll > 50:
        v = 1
    return v


def _generate_board(n):
    """
    :param n: The number of cells in the board. Returns a board with n*n cells.
    :return: a 2D array with a random cell setup
    """

    return [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]


def _print_board(board):
    for row in board:
        for col in row:
            p_value = "□" if col == 1 else ""
            print("{}".format(p_value), end=" ")
        print("")


def _clear_terminal():
    os.system('clear')


def _print_meta_info(opts, i, generations, seed):
    if len(opts) > 1:
        print(f"Running with seed: {seed}")
    print(f"Generations {i + 1}/{generations}")


def _count_live_neighbours(cell_pos, board):
    x, y = cell_pos
    board_size = len(board)
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            if 0 <= x+i < board_size-1 and 0 <= y + j < board_size - 1:
                count += board[x+i][y+j]

    return count


def _decide_cell_fate(cell_pos, board, new_board, neighbouring_live_cell_count):
    x, y = cell_pos

    if board[x][y] == 1:
        if neighbouring_live_cell_count < 2:
            new_board[x][y] = 0
        elif neighbouring_live_cell_count == 2:
            new_board[x][y] = 1
        elif neighbouring_live_cell_count > 3:
            new_board[x][y] = 0

    elif board[x][y] == 0:
        if neighbouring_live_cell_count == 3:
            new_board[x][y] = 1


def _traverse_board(board):
    n = len(board)
    new_board = [[0 for _ in range(n)] for _ in range(n)]
    for i in enumerate(board):
        for j in enumerate(board[1]):
            cell_pos = (i[0], j[0])
            neighbouring_live_cells_count = _count_live_neighbours(cell_pos, board)
            _decide_cell_fate(cell_pos, board, new_board, neighbouring_live_cells_count)
    return new_board


def _generate_blinker():
    return [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]


def _generate_toad():
    return [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]


if __name__ == '__main__':
    opts, arg = getopt.getopt(sys.argv[1:], 'g:s:')
    seed = "random"

    if len(opts) > 1:
        seed = opts[1][1]
        random.seed(seed)

    generations = int(opts[0][1])
    board = _generate_board(25)
    _print_board(board)
    for i in range(generations):
        _print_meta_info(opts, i, generations, seed)
        new_board = _traverse_board(board)
        board = new_board
        _print_board(board)
        sleep(0.25)
        if i < generations - 1:
            _clear_terminal()
