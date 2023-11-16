import pygame, math
import random

from loot import Loot
from settings import ZOMBIE_DAMAGE, ZOMBIE_HP, ZOMBIE_DAMAGE_IMAGE_PATH, ZOMBIE_DAMAGE_SOUND_PATH, LIST_LOOTS, LOOT_SPAWN_CHANSE, ZOMBIE_WIDTH, ZOMBIE_HEIGHT

pygame.mixer.init()

zombie_damage_image = pygame.image.load(ZOMBIE_DAMAGE_IMAGE_PATH)

sound_zombie_taking_damage = pygame.mixer.Sound(ZOMBIE_DAMAGE_SOUND_PATH)



class Zombie(pygame.sprite.Sprite):

    def __init__(self, pos_x: int, pos_y: int, surface: pygame.Surface, speed: int) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.rotate(pygame.transform.scale(surface, (ZOMBIE_WIDTH, ZOMBIE_HEIGHT)), 0)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.angle = 0

        self.width = ZOMBIE_WIDTH
        self.height = ZOMBIE_HEIGHT
        self.surface = surface

        self.hp = ZOMBIE_HP
        self.damage = ZOMBIE_DAMAGE
        self.speed = speed



    def update(self, player_pos_x: int, player_pos_y: int) -> None:
        
        dx = player_pos_x - self.rect.centerx
        dy = player_pos_y - self.rect.centery

        distance = math.sqrt(dx**2 + dy**2)

        dx = dx / distance * self.speed
        dy = dy / distance * self.speed

        self.rect.x += dx
        self.rect.y += dy


        self.rotate(player_pos_x, player_pos_y)



    def rotate(self, player_pos_x: int, player_pos_y: int) -> None:
        
        dx = player_pos_x - self.rect.centerx
        dy = player_pos_y - self.rect.centery

        self.angle = math.atan2(-dy, dx) * 180 / math.pi

        self.image = pygame.transform.rotate(pygame.transform.scale(self.surface, (self.width, self.height)), self.angle)



    def taking_damage(self, player_damage: int, group: pygame.sprite.Group, is_spawn: bool) -> None:

        self.image = pygame.transform.rotate(pygame.transform.scale(zombie_damage_image, (self.width, self.height)), self.angle)
        self.hp -= player_damage


        if self.hp <= 0:
            self.kill()
            sound_zombie_taking_damage.play()

            if is_spawn: self.spawn_loot(self.rect.centerx, self.rect.centery, group)



    def spawn_loot(self, zombie_pos_x: int, zombie_pos_y: int, group: pygame.sprite.Group) -> None:

        prob_spawn_loot = random.randint(1, LOOT_SPAWN_CHANSE)

        if prob_spawn_loot == 1:

            index_loot = random.randint(0, len(LIST_LOOTS) - 1)

            loot = Loot(zombie_pos_x, zombie_pos_y, LIST_LOOTS[index_loot])
            group.add(loot)