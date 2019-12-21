import pygame
from mario import Mario
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    pygame.mixer.music.load('music/basement.mp3')
    pygame.mixer.music.play(-1)
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    stats = 0
    score_board = Scoreboard(settings, stats, screen)
    blocks = Group()
    mario = Mario(settings, stats, screen, score_board, blocks)
    fire_balls = 0
    level = 1
    enemies = Group()

    gf.create_level(level, settings, screen, blocks, mario, enemies)

    while True:
        # Listen for user activity, and input all data. gf is a # file alias
        # tic.increment_tic()
        gf.check_events(settings, stats, screen, score_board, blocks, mario, fire_balls, enemies)
        if True:  # stats.game_active
            mario.update()
            gf.update_fire_balls(settings, stats, screen, score_board, blocks, mario, fire_balls, enemies)
            gf.update_enemies(settings, stats, screen, mario, enemies)
            gf.update_blocks(blocks)
        gf.update_screen(settings, stats, screen, score_board, blocks, mario, fire_balls, enemies)


run_game()
