# ╔════════╗ ┌────────┐
# ║        ║ │        │
# ║  2048  ║ │        │
# ║        ║ │        │
# ╚════════╝ └────────┘
# ┌────────┐ ╔════════╗
# │        │ ║        ║
# │        │ ║   32   ║
# │        │ ║        ║
# └────────┘ ╚════════╝

from sys import stdout


def show_field(play_field):
    for y in range(4):
        for x in range(4):
            print(play_field[x][y], end='')
        print('')


def show_graphic_field(play_field):
    
    buff = ''
    for y in range(4):
        for x in range(4):
            buff += ' ╔════════╗' if play_field[x][y] else ' ┌────────┐'
        buff += '\n'
        for x in range(4):
            buff += ' ║        ║' if play_field[x][y] else ' │        │'
        buff += '\n'
        for x in range(4):
            buff += ' ║  ' if play_field[x][y] else ' │  '
            buff += f'{play_field[x][y]:^4}' if play_field[x][y] else '    '
            buff += '  ║' if play_field[x][y] else '  │'
        buff += '\n'
        for x in range(4):
            buff += ' ║        ║' if play_field[x][y] else ' │        │'
        buff += '\n'
        for x in range(4):
            buff += ' ╚════════╝' if play_field[x][y] else ' └────────┘'
        buff += '\n'
    clear_screen()
    stdout.write(buff)
    stdout.flush()


def clear_screen():
    stdout.write('\033c')
    stdout.flush()
