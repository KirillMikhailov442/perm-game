import pygame, math
from constants import BOSS_WIDTH, BOSS_HEIGHT, BOSS_SPEED, BOSS_DAMAGE_IMAGE_PATH, BOSS_HP

boss_image_damage = pygame.image.load(BOSS_DAMAGE_IMAGE_PATH)


class Boss(pygame.sprite.Sprite):

    def __init__(self, pos_x: int, pos_y: int, surface: pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.width = BOSS_WIDTH
        self.height = BOSS_HEIGHT
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.surface = surface
        self.angle = 0

        self.image = pygame.transform.scale(self.surface, (self.width, self.height))
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

        self.speed = BOSS_SPEED
        self.hp = BOSS_HP


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
        """boss rotation"""
        dx = player_pos_x - self.rect.centerx
        dy = player_pos_y - self.rect.centery
        self.angle = math.atan2(-dy, dx) * 180 / math.pi

        self.image = pygame.transform.rotate(pygame.transform.scale(self.surface, (self.width, self.height)), self.angle)


    def taking_damage(self, player_damage: int) -> None:
        """boss taking damage"""
        self.image = pygame.transform.rotate(pygame.transform.scale(boss_image_damage, (self.width, self.height)), self.angle)
        self.hp -= player_damage

        if self.hp <= 0: self.kill()