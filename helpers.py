import random, pygame
from tkinter import messagebox

from settings import WINDOW_WIDTH, WINDOW_HEIGHT, ZOMBIE_SPEED_MAX

from zombie import Zombie

list_pos = ['TOP', "LEFT", 'RIGHT', 'DOWN']


def spawn_zombie(zombies):

    list_pos_index = random.randint(0, len(list_pos) - 1)

    width, height = 0, 0

    if  list_pos[list_pos_index] == 'TOP':

        width = random.randint(30, WINDOW_WIDTH)
        height = 1

    elif list_pos[list_pos_index] == 'LEFT':

        width = 1
        height = random.randint(1, WINDOW_HEIGHT)

    elif list_pos[list_pos_index] == 'RIGHT':

        width = WINDOW_WIDTH
        height = random.randint(1, WINDOW_HEIGHT)

    elif list_pos[list_pos_index] == 'DOWN':

        width = random.randint(1, WINDOW_WIDTH)
        height = WINDOW_HEIGHT


    speed = random.randint(1, ZOMBIE_SPEED_MAX)

    zombies.add(Zombie(width, height, pygame.image.load('./assets/textures/persons/zombie.png'), speed))




def quit_game(show_message: bool = False, message_title: str = None, message_text: str = None) -> None:

    if show_message:
        messagebox.showinfo(message_title, message_text)

    pygame.quit()

