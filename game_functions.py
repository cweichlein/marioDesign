import sys
import pygame
import block as bl

 
def check_events(settings, stats, screen, score_board, blocks, mario, fire_balls, mobs):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, blocks, mario, fire_balls)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, settings, mario)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            '''check_play_button(settings, screen, stats, scoreboard, mouse_x, mouse_y, play_button, blocks, mario, 
            fire_balls, mobs)
            check_mode_button(settings, stats, mouse_x, mouse_y, mode_button)'''


def check_keydown_events(event, settings, screen, blocks, mario, fire_balls):
    if event.key == pygame.K_SPACE:
        mario.k_space = True
        mario.k_space_held = True
    if event.key == pygame.K_RIGHT:
        mario.k_right = True
        mario.change_speed(1, 0)
        mario.direction = 1
        # mario.animate('walk_right')
    elif event.key == pygame.K_LEFT:  # can use elif as each event is only connected to only one key
        mario.change_speed(-1, 0)
        mario.direction = -1
        # mario.animate('walk_left')
    if event.key == pygame.K_s:  # throw
        mario.throw()
    elif event.key == pygame.K_q:
        sys.exit()
    '''if mario.rect.x > int(settings.screen_width/2):
        for b in blocks:
            b.move_left()'''


def check_keyup_events(event, settings, mario):
    if event.key == pygame.K_RIGHT:
        mario.k_right = False
        mario.change_speed(-1, 0)
        # mario.animate('stand_right')
        mario.direction = 1
    elif event.key == pygame.K_SPACE:
        mario.k_space_held = False
        mario.k_space = False
    elif event.key == pygame.K_LEFT:  # can use elif as each event is only connected to one key
        mario.change_speed(1, 0)
        # mario.animate('stand_left')
        mario.direction = -1


def create_block(type_set, settings, screen, x, y, blocks, item_type):
    if type_set <= 1:
        new_block = bl.Block(settings, screen, type_set)
    elif type_set == 2:
        new_block = bl.Enemy(settings, screen, type_set, blocks)
    elif type_set == 3:
        new_block = bl.Question(settings, screen, type_set, blocks, item_type, x, y)
    else:
        new_block = bl.Breakable(settings, screen, type_set, blocks)
    new_block.x = x
    new_block.rect.x = new_block.x
    new_block.y = y
    new_block.rect.y = new_block.y
    blocks.add(new_block)


def create_block_row(type_set, item_type, settings, screen, blocks, x_start, row, blocks_long):
    leny = settings.screen_height - (row*settings.block_height)
    lenx = x_start * settings.block_width
    length = blocks_long * settings.block_width + lenx
    while lenx <= length:
        create_block(type_set, settings, screen, lenx, leny, blocks, item_type)
        lenx += 32


def create_level(level, settings, screen, blocks, mario, enemies):
    if level == 1:
        type_set = 3  # spawn item_coin blocks
        item_type = 9
        row = 8
        create_block_row(type_set, item_type, settings, screen, blocks, 16, row, 0)
        create_block_row(type_set, item_type, settings, screen, blocks, 24, row, 1)
        create_block_row(type_set, item_type, settings, screen, blocks, 27, row, 1)
        create_block_row(type_set, item_type, settings, screen, blocks, 31, row, 2)
        type_set = 8  # spawn breakable blocks
        item_type = 0
        row = 8
        create_block_row(type_set, item_type, settings, screen, blocks, 13, row, 3)
        type_set = 3  # spawn item_mushroom block
        item_type = 4
        row = 8
        create_block_row(type_set, item_type, settings, screen, blocks, 12, row, 0)
        type_set = 3  # spawn item_star block
        item_type = 5
        row = 8
        create_block_row(type_set, item_type, settings, screen, blocks, 11, row, 0)
        type_set = 3  # spawn item_flower block
        item_type = 6
        row = 8
        create_block_row(type_set, item_type, settings, screen, blocks, 10, row, 0)
        type_set = 2  # spawn fire-things
        row = 2
        create_block_row(type_set, item_type, settings, screen, blocks, 17, row, 0)
        create_block_row(type_set, item_type, settings, screen, blocks, 31, row, 0)
        create_block_row(type_set, item_type, settings, screen, blocks, 38, row, 0)
        type_set = 0
        row = 1
        while row <= 2:
            create_block_row(type_set, item_type, settings, screen, blocks, 84, row, 16)
            create_block_row(type_set, item_type, settings, screen, blocks, 106, row, 3)
            row += 1
        row = 1
        while row <= 5:
            create_block_row(type_set, item_type, settings, screen, blocks, 0, row, 16)  # entry
            create_block_row(type_set, item_type, settings, screen, blocks, 19, row, 10)  # chub
            create_block_row(type_set, item_type, settings, screen, blocks, 33, row, 3)  # tinyGuy
            create_block_row(type_set, item_type, settings, screen, blocks, 40, row, 43)  # Main
            create_block_row(type_set, item_type, settings, screen, blocks, 101, row, 4)  # stalagmite
            create_block_row(type_set, item_type, settings, screen, blocks, 110, row, 5)  # threshold
            row += 1
        lenx = 8
        while row <= 8:
            create_block_row(type_set, item_type, settings, screen, blocks, 0, row, lenx)
            lenx -= 1
            row += 1
        row = 6
        create_block_row(type_set, item_type, settings, screen, blocks, 40, row, 23)
        row = 13
        create_block_row(type_set, item_type, settings, screen, blocks, 0, row, 115)
        while row >= 11:
            create_block_row(type_set, item_type, settings, screen, blocks, 0, row, 26)
            row -= 1
        create_block_row(type_set, item_type, settings, screen, blocks, 26, row, 0)
        row = 12
        while row >= 10:
            create_block_row(type_set, item_type, settings, screen, blocks, 43, row, 20)
            row -= 1
        row = 12
        create_block_row(type_set, item_type, settings, screen, blocks, 69, row, 0)
        create_block_row(type_set, item_type, settings, screen, blocks, 75, row, 0)
        while row >= 11:
            create_block_row(type_set, item_type, settings, screen, blocks, 78, row, 4)
            row -= 1
        type_set = -1  # now spawn block_used
        row = 9
        create_block_row(type_set, item_type, settings, screen, blocks, 26, row, 0)
        create_block_row(type_set, item_type, settings, screen, blocks, 43, row, 0)
        create_block_row(type_set, item_type, settings, screen, blocks, 52, row, 0)
        create_block_row(type_set, item_type, settings, screen, blocks, 60, row, 0)
        create_block_row(type_set, item_type, settings, screen, blocks, 63, row, 0)
        create_block_row(type_set, item_type, settings, screen, blocks, 35, 5, 0)
        type_set = 1  # now spawn LAVA
        row = 0
        while row <= 2:
            create_block_row(type_set, item_type, settings, screen, blocks, 17, row, 1)
            create_block_row(type_set, item_type, settings, screen, blocks, 30, row, 2)
            create_block_row(type_set, item_type, settings, screen, blocks, 37, row, 2)
            create_block_row(type_set, item_type, settings, screen, blocks, 116, row, 15)
            row += 1

        mario.rect.centery = settings.screen_height/2
        mario.rect.centerx = settings.screen_width/2
        mario.start_x = mario.rect.centerx
        mario.start_y = mario.rect.centery


def fire_ball(settings, screen, mario):
    pass


def throw_fire_ball(settings, screen, mario, fire_balls):
    '''if len(fire_balls) < settings.fire_balls_allowed:
        new_fire_ball = Fire_ball(settings, screen, mario)  # Fire_ball() is from file fire_ball.py
        fire_balls.add(new_fire_ball)'''
    pass


def update_blocks(blocks):
    for block in blocks:
        block.update()


def update_enemies(settings, stats, screen, mario, enemies):
    '''mobs.update()
    # look for mob-mario collisions
    if pygame.sprite.spritecollideany(mario, mobs):
        mario_hit(stats, mario)
    # check_mobs_bottom(stats, screen, mario, mobs)  # if a mob falls off screen'''
    pass


def update_fire_balls(settings, stats, screen, score_board, blocks, mario, fire_balls, mobs):
    '''fire_balls.update()  # move bullets
    for ball in fire_balls.copy():  # remove bullets as they fly off screen
        if ball.rect.bottom <= 0:
            fire_balls.remove(fire_ball)
    # check_bullet_mob_collisions(settings, stats, screen, scoreboard, blocks, mario, fire_balls, mobs)'''
    pass


def update_screen(settings, stats, screen, score_board, blocks, mario, fire_balls, mobs):
    # redraw screen with color each loop pass
    if mario.respawn:
        mario.respawn = False
        # mario.animate('stand_right')
        mario.direction = 1
        # reset(ai_settings, stats, screen, sb, ship, bullets, aliens, alien_bullets, bunkers, bonus, explosions)
    screen.fill(settings.bg_color)
    '''for ball in fire_balls.sprites():
        ball.draw_fire_ball()'''
    mario.blitme()
    # mobs.draw(screen)
    blocks.draw(screen)
    score_board.show_score()

    # NOTE to team-members of RPY:  THE SECTION BELOW IS FOR WHEN WE IMPLEMENT PLAY BUTTONS.
    # we will pass play button objects as parameters for this function, and will analyze them.
    # SAVE THIS FOR FUTURE. In the mean time, most its content will be commented out.
    # Draw the play button if the game is inactive.
    '''if not stats.game_active:
        score_board.display_main_menu()
        play_button.draw_button()
        mode_button.draw_button()
        if settings.mode == 1:  # display black rect with words that give scores
            score_board.display_high_scores()
        if stats.broke_high_score:
            save_high_score(stats, sb)
            stats.broke_high_score = False'''
    pygame.display.flip()  # Make recent screen visible, by flipping it over the old one
