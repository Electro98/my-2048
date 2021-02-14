import keyboard

from time import sleep
from .cmd_drawer import show_graphic_field, clear_screen
from .logic import create_random_block, swipe_field


def play(play_field, direction):
    create_random_block(play_field)
    show_graphic_field(play_field)
    sleep(0.5)
    swipe_field(play_field, direction)
    show_graphic_field(play_field)


def refresh_screen(play_field):
    clear_screen()
    show_graphic_field(play_field)


def control_game(event: keyboard.KeyboardEvent):
    global play_field
    if event.event_type == 'up':
        direction = event.name
        if direction in ('left', 'right', 'up', 'down'):
            play(play_field, direction)
        elif direction == 'r':
            play_field = [[0 for i in range(4)] for i in range(4)]
            refresh_screen(play_field)
        elif direction == 'e':
            return(0)
        else:
            refresh_screen(play_field)


def main():
    global play_field
    play_field = [[0 for i in range(4)] for i in range(4)]
    refresh_screen(play_field)
    keyboard.hook(control_game)
    keyboard.wait()


if __name__ == '__main__':
    main()
