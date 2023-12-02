import random, pygame
from tkinter import messagebox
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, TUZEMEC_SPEED_MAX, LIST_POS_SPAWN_TUZEMEC
from tuzemec import Tuzemec


def spawn_tuzemec(tuzemecs):
    """appearance of natives on craft cards"""
    list_pos_index = random.randint(0, len(LIST_POS_SPAWN_TUZEMEC) - 1)
    width, height = 0, 0

    if  LIST_POS_SPAWN_TUZEMEC[list_pos_index] == 'TOP':
        width = random.randint(30, WINDOW_WIDTH)
        height = 1

    elif LIST_POS_SPAWN_TUZEMEC[list_pos_index] == 'LEFT':
        width = 1
        height = random.randint(1, WINDOW_HEIGHT)

    elif LIST_POS_SPAWN_TUZEMEC[list_pos_index] == 'RIGHT':
        width = WINDOW_WIDTH
        height = random.randint(1, WINDOW_HEIGHT)

    elif LIST_POS_SPAWN_TUZEMEC[list_pos_index] == 'DOWN':
        width = random.randint(1, WINDOW_WIDTH)
        height = WINDOW_HEIGHT

    speed = random.randint(1, TUZEMEC_SPEED_MAX)
    tuzemecs.add(Tuzemec(width, height, pygame.image.load('./assets/textures/persons/tuzemec.png'), speed))


def quit_game(show_message: bool = False, message_title: str = None, message_text: str = None) -> None:
    """quit the game"""
    if show_message: messagebox.showinfo(message_title, message_text)
    pygame.quit()