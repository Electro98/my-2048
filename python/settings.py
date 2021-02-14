
CHANCE_DROP_FOUR = 10  # 1/n - chance
PATTERN_Y = {
    'up': (1, 2, 3),
    'down': (2, 1, 0),
    'right': (0, 1, 2, 3),
    'left': (0, 1, 2, 3),
}
PATTERN_X = {
    'up': (0, 1, 2, 3),
    'down': (0, 1, 2, 3),
    'right': (2, 1, 0),
    'left': (1, 2, 3),
}
MOVE_CEIL_VECTOR = {
    'up': {'x': 0, 'y': -1},
    'down': {'x': 0, 'y': 1},
    'right': {'x': 1, 'y': 0},
    'left': {'x': -1, 'y': 0},
}
