import pygame, math
from constants import ZONE_BOMB_WIDTH, ZONE_BOMB_HEIGHT, BOMB_WIDTH, BOMB_HEIGHT, BOMB_SPEED, BOMB_IMAGE_PATH, BOMB_SOUND_PATH

pygame.mixer.init()

zone_bomb_image = pygame.image.load(BOMB_IMAGE_PATH)
sound_bomb = pygame.mixer.Sound(BOMB_SOUND_PATH)


class Bomb(pygame.sprite.Sprite):

    def __init__(self, player_pos_x: int, player_pos_y: int, surface: pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.width = BOMB_WIDTH
        self.height = BOMB_HEIGHT
        self.angle = 0
        self.direction_deter = False
        self.activated = False
        self.surface = surface

        self.mouse_pos_x = 0
        self.mouse_pos_y = 0

        self.dx = 0
        self.dy = 0

        self.image = pygame.transform.scale(surface, (self.width, self.height))
        self.rect = self.image.get_rect(center=(player_pos_x, player_pos_y))
        self.speed = BOMB_SPEED


    def update(self, mouse_pos_x: int, mouse_pos_y: int) -> None:
        if not(self.direction_deter):
            self.mouse_pos_x = mouse_pos_x
            self.mouse_pos_y = mouse_pos_y
            self.direction_deter = True

        self.dx = self.mouse_pos_x - self.rect.centerx
        self.dy = self.mouse_pos_y - self.rect.centery

        distance = math.sqrt(self.dx**2 + self.dy**2)

        if distance <= 5:
            self.rect.x += self.dx
            self.rect.y += self.dy

            self.width = ZONE_BOMB_WIDTH
            self.height = ZONE_BOMB_HEIGHT

            self.image = pygame.transform.scale(zone_bomb_image, (self.width, self.height))
            self.rect.x -= ZONE_BOMB_WIDTH // 2
            self.rect.y -= ZONE_BOMB_HEIGHT // 2

            sound_bomb.play()
            self.activated = True

        else:
            if not(self.activated):
                self.dx = self.dx / distance * self.speed
                self.dy = self.dy / distance * self.speed

                self.rect.x += self.dx
                self.rect.y += self.dy