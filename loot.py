import pygame

from settings import LIST_LOOTS_IMAGES_PATH, LOOT_MEDICINE_SOUND_PATH, LOOT_SPEED_SOUND_PATH, LOOT_MEGA_BOMB_SOUND_PATH, LOOT_MORE_SOUND_PATH, LOOT_WIDTH, LOOT_HEIGHT

list_loots_images = {
    "MEDICINE": pygame.image.load(LIST_LOOTS_IMAGES_PATH['MEDICINE']),
    "DAMAGE": pygame.image.load(LIST_LOOTS_IMAGES_PATH['DAMAGE']),
    'SPEED': pygame.image.load(LIST_LOOTS_IMAGES_PATH['SPEED']),
    'BOMB': pygame.image.load(LIST_LOOTS_IMAGES_PATH['BOMB']),
    'MEGA_BOMB': pygame.image.load(LIST_LOOTS_IMAGES_PATH['MEGA_BOMB'])
}

pygame.mixer.init()

sound_up_hp = pygame.mixer.Sound(LOOT_MEDICINE_SOUND_PATH)
sound_up_speed = pygame.mixer.Sound(LOOT_SPEED_SOUND_PATH)
sound_mega_bomb = pygame.mixer.Sound(LOOT_MEGA_BOMB_SOUND_PATH)
sound_loot_more = pygame.mixer.Sound(LOOT_MORE_SOUND_PATH)



class Loot(pygame.sprite.Sprite):

    def __init__(self, pos_x: int, pos_y: int, type_loot: list_loots_images) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(list_loots_images[type_loot], (LOOT_WIDTH, LOOT_HEIGHT))
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.type_loot = type_loot


    def pickup(self) -> str:

        self.play_music()
        self.kill()

        return self.type_loot
    

    def play_music(self) -> None:

        if self.type_loot == 'MEDICINE':
            sound_up_hp.play()

        elif self.type_loot == 'DAMAGE':
            sound_loot_more.play()
        
        elif self.type_loot == 'SPEED':
            sound_up_speed.play()

        elif self.type_loot == 'BOMB':
            sound_loot_more.play()

        elif self.type_loot == 'MEGA_BOMB':
            sound_mega_bomb.play()