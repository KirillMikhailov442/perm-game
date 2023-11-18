import pygame, time
from tkinter import messagebox

from settings import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, FPS, WINDOW_BACKGROUND_COLOR, BACKGROUND_SOUND_PATH, BACKGROUND_SOUND_VICTORY_PATH, PLAYER_IMAGE_PATH, BOSS_IMAGE_PATH, MOUSE_IMAGE_PATH, MOUSE_WIDTH, MOUSE_HEIGHT, BOMB_IMAGE_PATH, ZONE_BOMB_WIDTH, ZONE_BOMB_HEIGHT, ZONE_BOMB_IMAGE_PATH, BOSS_SPAWN_TIME_SECONDS, BOSS_SOUND_PATH, WINDOW_FONT_PATH, WINDOW_ICON_PATH, WINDOW_BACKGROUND_IMAGE_PATH
from player import Player
from bomb import Bomb
from boss import Boss
from helpers import spawn_tuzemec, quit_game


def start_game():

    messagebox.showinfo('Небольшое обучение', 'A - Влево \n W - Вверх \n S - Вниз \n D - Вправо \n ЛКМ - Стрелять \n ПКМ - Кидать гранату')

    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.fill(WINDOW_BACKGROUND_COLOR)
    pygame.display.set_caption(WINDOW_TITLE)
    pygame.display.set_icon(pygame.image.load(WINDOW_ICON_PATH))
    pygame.mouse.set_visible(False)

    clock = pygame.time.Clock()

    pygame.mixer.music.load(BACKGROUND_SOUND_PATH)
    pygame.mixer.music.play(-1)



    # шрифт
    font = pygame.font.Font(WINDOW_FONT_PATH, 20)


    # верхнее меню
    pygame.transform.scale(pygame.image.load('./assets/textures/bombs/bomb-0.png'), (40, 30))
    indicator_bomb_rect = pygame.Rect(50, 0, 40, 30)

    pygame.transform.scale(pygame.image.load('./assets/textures/hp/hp-5.png'), (30, 30))
    indicator_hp_rect = pygame.Rect(10, 0, 30, 30)

    start_time = time.time()
    game_time = start_time

    game_time_text = font.render('Время: 0', True, 'BLACK')
    game_time_text.get_rect(topright=(WINDOW_WIDTH, 0))

    indicator_boss_hp = font.render('Здоровье вождя: 100', True, 'RED')
    indicator_boss_hp.get_rect(center=(WINDOW_WIDTH // 2, 0))

    # текстура заднего фона
    background_image = pygame.transform.scale(pygame.image.load(WINDOW_BACKGROUND_IMAGE_PATH), (WINDOW_WIDTH, WINDOW_HEIGHT))
    background_image.get_rect(topleft=(0, 0))



    player = Player(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.image.load(PLAYER_IMAGE_PATH))
    boss = Boss(WINDOW_WIDTH // 2, 10, pygame.image.load(BOSS_IMAGE_PATH))


    tuzemecs = pygame.sprite.Group()

    TIMER_EVENT = pygame.USEREVENT + 1

    pygame.time.set_timer(TIMER_EVENT, 1000) 



    # группа лута
    loots = pygame.sprite.Group()
    # группа стрел
    arrows = pygame.sprite.Group()
    # группа бомб
    bombs = pygame.sprite.Group()



    mouse = pygame.image.load(MOUSE_IMAGE_PATH)
    mouse_pos_x = 100
    mouse_pos_y = 100

    cursor = pygame.transform.scale(mouse, (MOUSE_WIDTH, MOUSE_HEIGHT))
    cursor.get_rect(center=(mouse_pos_x, mouse_pos_y))
    cursor_rect = pygame.Rect(mouse_pos_x - MOUSE_WIDTH // 2, mouse_pos_y - MOUSE_HEIGHT // 2, MOUSE_WIDTH, MOUSE_HEIGHT)

    mode_bomb, mode_boss = False, False

    window_rect = screen.get_rect()

    while True:


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit_game(True, 'Выйти из игры', 'Вы решили выйти из игры, игра окончена')



            if event.type == pygame.MOUSEBUTTONUP:
                
                if event.button == 3:

                    player_pos_x, player_pos_y = player.rect.center
                    zone_bomb = pygame.image.load(BOMB_IMAGE_PATH)

                    cursor_rect = pygame.Rect(mouse_pos_x - MOUSE_WIDTH // 2, mouse_pos_y - MOUSE_HEIGHT // 2, MOUSE_WIDTH, MOUSE_HEIGHT)

                    if player.bomb > 0:
                        bombs.add(Bomb(player_pos_x, player_pos_y, zone_bomb))
                        player.bomb -= 1

                    mode_bomb = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if event.button == 1:
                    player.fire(arrows)

                if event.button == 3:

                    cursor_rect = pygame.Rect(mouse_pos_x - ZONE_BOMB_WIDTH // 2, mouse_pos_y - ZONE_BOMB_HEIGHT // 2, cursor_rect.centerx, cursor_rect.centery)

                    mode_bomb = True

            
            if event.type == TIMER_EVENT:
                spawn_tuzemec(tuzemecs)



            # режим бомб
            if mode_bomb:

                mouse = pygame.image.load(ZONE_BOMB_IMAGE_PATH)
                cursor = pygame.transform.scale(mouse, (ZONE_BOMB_WIDTH, ZONE_BOMB_HEIGHT))

            if not(mode_bomb):

                mouse = pygame.image.load(MOUSE_IMAGE_PATH)
                cursor = pygame.transform.scale(mouse, (MOUSE_WIDTH, MOUSE_HEIGHT))


            if window_rect.collidepoint(mouse_pos_x, mouse_pos_y):

                if event.type == pygame.MOUSEMOTION:

                    mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()

                    if mode_bomb:
                        cursor_rect = pygame.Rect(mouse_pos_x - ZONE_BOMB_WIDTH // 2, mouse_pos_y - ZONE_BOMB_HEIGHT // 2, ZONE_BOMB_WIDTH, ZONE_BOMB_HEIGHT)
                    
                    else:
                        cursor_rect = pygame.Rect(mouse_pos_x - MOUSE_WIDTH // 2, mouse_pos_y - MOUSE_HEIGHT // 2, MOUSE_WIDTH, MOUSE_HEIGHT)


        screen.blit(background_image, background_image.get_rect(topleft=(0, 0)))



        # верхнее меню
        screen.blit(pygame.transform.scale(pygame.image.load(f'./assets/textures/bombs/bomb-{player.bomb}.png'), (40, 30)), (indicator_bomb_rect.x, indicator_bomb_rect.y))

        screen.blit(pygame.transform.scale(pygame.image.load(f'./assets/textures/hp/hp-{player.hp}.png'), (30, 30)), (indicator_hp_rect.x, indicator_bomb_rect.y))

        game_time = time.time() - start_time

        game_time_minutes = int(game_time // 60)
        game_time_seconds =int(game_time % 60)

        game_time_text = font.render(f'Время: {game_time_minutes}:{game_time_seconds}', True, 'BLACK')

        screen.blit(game_time_text, game_time_text.get_rect(topright=(WINDOW_WIDTH - 10, 0)))




        player_pos_x, player_pos_y = player.rect.center

        # отрисовать все объекты
        loots.draw(screen)

        tuzemecs.draw(screen)
        tuzemecs.update(player_pos_x, player_pos_y)

        arrows.draw(screen)
        arrows.update(mouse_pos_x, mouse_pos_y, (WINDOW_WIDTH, WINDOW_HEIGHT))

        bombs.draw(screen)
        bombs.update(mouse_pos_x, mouse_pos_y)


        # попадание пуль в туземцов
        for arrow in arrows:

            for tuzemec in tuzemecs:

                if arrow.rect.colliderect(tuzemec.rect):
                    tuzemec.taking_damage(player.damage, loots, True)
                    arrow.kill()

        # попадание пуль в босса
        if mode_boss:
            for arrow in arrows:

                if arrow.rect.colliderect(boss.rect):
                    boss.taking_damage(player.damage)
                    arrow.kill()


        # соприкосновение туземцов с игроком
        for tuzemec in tuzemecs:

            if player.rect.colliderect(tuzemec.rect):
                player.taking_damage(tuzemec.damage)
                tuzemec.taking_damage(tuzemec.hp, loots, False)


        # сбор предметов
        for loot in loots:

            if player.rect.colliderect(loot.rect):

                type_loot = loot.pickup()

                if type_loot == 'MEGA_BOMB':
                    tuzemecs.empty()

                else:
                    player.pickup_loot(type_loot)



        # время босса
        if time.time() - start_time > BOSS_SPAWN_TIME_SECONDS:

            if not(mode_boss):
                pygame.mixer.music.load(BOSS_SOUND_PATH)
                pygame.mixer.music.play(-1)
                mode_boss = True
            
            screen.blit(boss.image, boss.rect)
            boss.update(player_pos_x, player_pos_y)

            indicator_boss_hp = font.render(f'Здоровье вождя: {int(boss.hp)}', True, 'RED')
            screen.blit(indicator_boss_hp, indicator_boss_hp.get_rect(topright=(WINDOW_WIDTH // 2, 0)))


        if mode_boss:

            if player.rect.colliderect(boss.rect):
                player.taking_damage(player.hp)
                quit_game(True, 'Игрв окончена', "Тебя убил босс")

            if boss.hp <= 0:
                pygame.mixer.music.load(BACKGROUND_SOUND_VICTORY_PATH)
                pygame.mixer.music.play(1)
                quit_game(True, 'Победа', 'Ты победил')


        # взрыв бомб по туземцам
        for bomb in bombs:

            for tuzemec in tuzemecs:

                if bomb.activated:


                    is_in_zone_x, is_in_zone_y = False, False


                    if ((tuzemec.rect.x + tuzemec.width < bomb.rect.x + bomb.width) and (tuzemec.rect.x > bomb.rect.x)):
                        is_in_zone_x = True

                    if ((tuzemec.rect.y + tuzemec.height < bomb.rect.x + bomb.height) and (tuzemec.rect.y > bomb.rect.y)):
                        is_in_zone_y = True

                    
                    if (is_in_zone_x and is_in_zone_y):
                        tuzemec.taking_damage(tuzemec.hp, loots, True)

            if bomb.activated:
                bomb.kill()


                    
        screen.blit(player.image, player.rect)
        player.update(mouse_pos_x, mouse_pos_y)


        screen.blit(cursor, cursor_rect)

        pygame.display.update()
        clock.tick(FPS)
