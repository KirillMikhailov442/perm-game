import pygame, math
from typing import Tuple

from settings import AMMO_WIDTH, AMMO_HEGHT, AMMO_SPEED




class Ammo(pygame.sprite.Sprite):

    def __init__(self, player_pos_x: int, player_pos_y: int, surface: pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)


        self.width = AMMO_WIDTH
        self.height = AMMO_HEGHT
        self.angle = 0
        self.direction_deter = False
        self.surface = surface

        self.distance = 0
        self.dx = 0
        self.dy = 0

        self.image = pygame.transform.rotate(pygame.transform.scale(surface, (self.width, self.height)), 0)
        self.rect = self.image.get_rect(center=(player_pos_x, player_pos_y))
        self.speed = AMMO_SPEED

        self.rotate(50, 50)



    def update(self, mouse_pos_x: int, mouse_pos_y: int, area: Tuple[int]) -> None:

        self.moving(mouse_pos_x, mouse_pos_y, area)
        self.rotate(mouse_pos_x, mouse_pos_y)



    def moving(self, mouse_pos_x: int, mouse_pos_y: int, area: Tuple[int]) -> None:

        if self.direction_deter:
            distance = self.distance
            dx = self.dx
            dy = self.dy

        else:
            dx = mouse_pos_x - self.rect.centerx
            dy = mouse_pos_y - self.rect.centery

            self.dx = dx
            self.dy = dy

            distance = math.sqrt(dx**2 + dy**2)
            self.distance = distance

            self.direction_deter = True

        dx = dx / distance * self.speed
        dy = dy / distance * self.speed

        self.rect.x += dx
        self.rect.y += dy

        is_kill = False

        if self.rect.x <= 0:
            is_kill = True
        
        elif self.rect.y <= 0:
            is_kill = True

        elif self.rect.x + self.width >= area[0]:
            is_kill = True

        elif self.rect.y + self.height >= area[1]:
            is_kill = True


        if is_kill:
            self.kill()



    def rotate(self, mouse_pos_x: int, mouse_pos_y: int) -> None:

        if self.direction_deter:
            dx = self.dx
            dy = self.dy
        
        else:
            dx = mouse_pos_x - self.rect.centerx
            dy = mouse_pos_y - self.rect.centery

        self.angle = math.atan2(-dy, dx) * 180 / math.pi

        self.image = pygame.transform.rotate(pygame.transform.scale(self.surface, (self.width, self.height)), self.angle)