import pygame, math
from typing import Tuple


from arrow import Arrow
from helpers import quit_game
from settings import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_DAMAGE, PLAYER_SPEED, PLAYER_HP, PLAYER_DAMAGE_IMAGE_PATH, PLAYER_SOUND_TAKING_DAMAGE_PATH, ARROW_IMAGE_PATH, ARROW_SOUND_PATH, BOMB_COUNT_MAX


pygame.mixer.init()

arrow_image = pygame.image.load(ARROW_IMAGE_PATH)

player_damage_image = pygame.image.load(PLAYER_DAMAGE_IMAGE_PATH)

sound_player_bow = pygame.mixer.Sound(ARROW_SOUND_PATH)
sound_player_taking_damage = pygame.mixer.Sound(PLAYER_SOUND_TAKING_DAMAGE_PATH)



class Player(pygame.sprite.Sprite):

    def __init__(self, pos_x: int, pos_y: int, area: Tuple[int], surface: pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.rotate(pygame.transform.scale(surface, (PLAYER_WIDTH, PLAYER_HEIGHT)), 0)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.angle = 0
        self.area = area

        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.surface = surface

        self.hp = PLAYER_HP
        self.damage = PLAYER_DAMAGE
        self.speed = PLAYER_SPEED
        self.bomb = 0



    def update(self, mouse_pos_x: int, mouse_pos_y: int) -> None:

        if self.hp < 1:
            quit_game(False)

        self.moving()
        self.rotate(mouse_pos_x, mouse_pos_y)



    def fire(self, group: pygame.sprite.Group):

        arrow = Arrow(self.rect.centerx, self.rect.centery, arrow_image)
        sound_player_bow.play()
        group.add(arrow)



    def rotate(self, mouse_pos_x: int, mouse_pos_y: int) -> None:

        dx = mouse_pos_x - self.rect.centerx
        dy = mouse_pos_y - self.rect.centery

        self.angle = math.atan2(-dy, dx) * 180 / math.pi

        self.image = pygame.transform.rotate(pygame.transform.scale(self.surface, (self.width, self.height)), self.angle)



    def moving(self) -> None:

        keys = pygame.key.get_pressed()


        if keys[pygame.K_a]:
            if self.rect.x > 0:
                self.rect.x -= self.speed


        if keys[pygame.K_d]:
            if self.rect.x + self.width < self.area[0]:
                self.rect.x += self.speed


        if keys[pygame.K_w]:
            if self.rect.y > 30:
                self.rect.y -= self.speed


        if keys[pygame.K_s]:
            if self.rect.y + self.height < self.area[1]:
                self.rect.y += self.speed



    def taking_damage(self, tuzemec_damage: int):

        self.image = pygame.transform.rotate(pygame.transform.scale(player_damage_image, (self.width, self.height)), self.angle)
        self.hp -= tuzemec_damage


        sound_player_taking_damage.play()

        if self.hp <= 0:
            self.kill()
            quit_game(True, 'Игра окончена', 'Ты проиграл')



    def pickup_loot(self, type_loot: str) -> None:

        if type_loot == 'MEDICINE':

            if self.hp < PLAYER_HP:
                self.hp += 1

        elif type_loot == 'DAMAGE':
            self.damage += 0.5

        elif type_loot == "SPEED":
            self.speed += 0.5

        elif type_loot == 'BOMB':

            if self.bomb < BOMB_COUNT_MAX:
                self.bomb += 1