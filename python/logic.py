import random as rm

from .settings import *


def check_game_state(play_field):
    lose_counter = 0
    for y in range(4):
        for x in range(4):
            if play_field[x][y] == 2048:
                return(1)
            if play_field[x][y]:
                lose_counter += 1
    if lose_counter == 16:
        return(-1)
    else:
        return(0)


def create_random_block(play_field):
    while True:
        x, y = rm.randint(0, 3), rm.randint(0, 3)
        if not play_field[x][y]:
            break
    play_field[x][y] = 2 if rm.randint(0, CHANCE_DROP_FOUR - 1) else 4


def swipe_field(play_field, direction: str):
    for y in PATTERN_Y[direction]:
        for x in PATTERN_X[direction]:
            move_ceil(play_field, direction, x, y)


def move_ceil(play_field, direction, x, y):
    play_border = 0, 1, 2, 3
    move_x = MOVE_CEIL_VECTOR[direction]['x']
    move_y = MOVE_CEIL_VECTOR[direction]['y']
    if play_field[x][y]:
        while True:
            if (x + move_x) not in play_border \
                    or (y + move_y) not in play_border:
                break
            elif not play_field[x + move_x][y + move_y]:
                play_field[x + move_x][y + move_y] = play_field[x][y]
            elif play_field[x + move_x][y + move_y] == play_field[x][y]:
                play_field[x + move_x][y + move_y] *= 2
            else:
                break

            play_field[x][y] = 0
            x, y = x + move_x, y + move_y
