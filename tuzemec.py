import pygame, math
import random
from loot import Loot
from constants import TUZEMEC_DAMAGE, TUZEMEC_HP, TUZEMEC_DAMAGE_IMAGE_PATH, TUZEMEC_DAMAGE_SOUND_PATH, LIST_LOOTS, LOOT_SPAWN_CHANSE, TUZEMEC_WIDTH, TUZEMEC_HEIGHT

pygame.mixer.init()

tuzemec_damage_image = pygame.image.load(TUZEMEC_DAMAGE_IMAGE_PATH)
sound_tuzemec_taking_damage = pygame.mixer.Sound(TUZEMEC_DAMAGE_SOUND_PATH)

class Tuzemec(pygame.sprite.Sprite):

    def __init__(self, pos_x: int, pos_y: int, surface: pygame.Surface, speed: int) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.rotate(pygame.transform.scale(surface, (TUZEMEC_WIDTH, TUZEMEC_HEIGHT)), 0)
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.angle = 0

        self.width = TUZEMEC_WIDTH
        self.height = TUZEMEC_HEIGHT
        self.surface = surface

        self.hp = TUZEMEC_HP
        self.damage = TUZEMEC_DAMAGE
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
        """tuzemec rotation"""
        dx = player_pos_x - self.rect.centerx
        dy = player_pos_y - self.rect.centery

        self.angle = math.atan2(-dy, dx) * 180 / math.pi
        self.image = pygame.transform.rotate(pygame.transform.scale(self.surface, (self.width, self.height)), self.angle)


    def taking_damage(self, player_damage: int, group: pygame.sprite.Group, is_spawn: bool) -> None:
        """tuzemec taking damage"""
        self.image = pygame.transform.rotate(pygame.transform.scale(tuzemec_damage_image, (self.width, self.height)), self.angle)
        self.hp -= player_damage

        if self.hp <= 0:
            self.kill()
            sound_tuzemec_taking_damage.play()

            if is_spawn: self.spawn_loot(self.rect.centerx, self.rect.centery, group)


    def spawn_loot(self, tuzemec_pos_x: int, tuzemec_pos_y: int, group: pygame.sprite.Group) -> None:
        """appearance of prey after the death of a native"""
        prob_spawn_loot = random.randint(1, LOOT_SPAWN_CHANSE)

        if prob_spawn_loot == 1:
            index_loot = random.randint(0, len(LIST_LOOTS) - 1)
            loot = Loot(tuzemec_pos_x, tuzemec_pos_y, LIST_LOOTS[index_loot])
            group.add(loot)