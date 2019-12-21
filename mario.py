import pygame
from pygame.sprite import Sprite
import math
# from animation import Animation
from timer import Timer
import block


class Mario(Sprite):  # , Animation):
    def __init__(self, settings, stats, screen, score_board, blocks):
        super(Mario, self).__init__()  # initialize superclass object
        self.settings = settings  # save passed objects for local access
        self.screen = screen
        self.stats = stats
        self.score_board = score_board
        self.blocks = blocks

        self.screen_rect = screen.get_rect()  # gets the passed screen object's rectangle
        # self.animate_set_character(character='mario', settings=settings)  #
        self.image = pygame.image.load('Images/mario.png')
        self.rect = self.image.get_rect()  # gets the image's rectangle
        self.mario_gravity = settings.mario_gravity
        self.horizSpeed = float(0)
        self.vertSpeed = float(0)
        self.die = False
        self.respawn = False
        self.k_space = False
        self.k_space_held = False
        self.jump_force = settings.mario_jump_force
        self.jump_speed = 3
        self.jump_potential_energy = 0
        self.jump_kinetic_energy = 0
        self.k_right = False
        self.start_x = 0
        self.start_y = 0
        self.direction = 1  #
        self.health = 1
        self.invincibility_time = 0
        self.prevImage = self.image
        self.fire_mario = False
        self.coin = 0
        self.life = settings.mario_lives
        self.coinMult = 1

    def change_speed(self, h, v):
        self.horizSpeed += float(h)
        self.vertSpeed += float(v)

    def invincibility(self, time):
        self.invincibility_time += time

    def healthi(self, direction):
        self.health += direction
        if self.health < 1:
            self.die = True
        if direction < 0:
            self.invincibility(100)
            self.fire_mario = False
            self.score_board.update(self.life, self.coin, self.fire_mario)
        if self.health > 1:
            if not self.fire_mario:
                self.image = pygame.image.load('Images/mario_super.png')
            x = self.rect.x
            bottom = self.rect.bottom
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.bottom = bottom
        else:
            self.image = pygame.image.load('Images/mario.png')
            x = self.rect.x
            bottom = self.rect.bottom
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.bottom = bottom

    def throw(self):
        if self.fire_mario:
            new_fireball = block.Item(self.settings, self.screen, 7, self.rect.x + 32, self.rect.y + 32, self.blocks)
            self.blocks.add(new_fireball)

    def update(self):
        # self.update_animation()
        if self.fire_mario:
            self.image = pygame.image.load('Images/mario_fire.png')
        if self.invincibility_time > 0:
            self.invincibility_time -= 1
            if self.invincibility_time % 2 != 0:
                self.prevImage = self.image
                self.image = pygame.image.load('Images/mario_invisible.png')
            else:
                self.image = self.prevImage
        if not self.die:
            if self.rect.x < int(self.settings.screen_width/2):
                self.rect.x += self.horizSpeed
            else:
                if self.horizSpeed < 0:
                    self.rect.x += self.horizSpeed
                if self.k_right:
                    for b in self.blocks:
                        b.move_left()
            collidable_list = pygame.sprite.spritecollide(self, self.blocks, False)
            for collided_object in collidable_list:
                if collided_object.block_type == 2 and self.invincibility_time < 1:
                    self.healthi(-1)
                if collided_object.block_type == 4:  # grabbed a mushroom
                    collided_object.die = True
                    self.prevImage = self.image  # without this line, he cannot become super properly while invincible
                    self.healthi(1)
                if collided_object.block_type == 5:  # grabbed a star
                    collided_object.die = True
                    self.invincibility(1500)
                if collided_object.block_type == 6:  # grabbed a flower
                    if not self.health > 1:
                        self.healthi(1)
                    collided_object.die = True
                    self.fire_mario = True
                    self.score_board.update(self.life, self.coin, self.fire_mario)
                if collided_object.block_type == 9:  # grabbed a coin
                    collided_object.die = True
                    self.coin += 1
                    if self.coin >= self.coinMult * 2:
                        self.life += 1
                        self.coinMult += 1
                    self.score_board.update(self.life, self.coin, self.fire_mario)
                if self.horizSpeed > 0:
                    self.rect.right = collided_object.rect.left
                elif self.horizSpeed < 0:
                    self.rect.left = collided_object.rect.right
            self.rect.y += self.vertSpeed
            landed = False
            collidable_list2 = pygame.sprite.spritecollide(self, self.blocks, False)
            for collided_object in collidable_list2:
                if collided_object.block_type == 2 and self.invincibility_time < 1:
                    pygame.mixer.music.load('music/Wilhelm.mp3')
                    pygame.mixer.music.play(1)
                    self.healthi(-1)
                if collided_object.block_type == 4:  # grabbed a mushroom
                    collided_object.die = True
                    self.prevImage = self.image  # without this line, he cannot become super properly while invincible
                    self.healthi(1)
                if collided_object.block_type == 5:  # grabbed a star
                    collided_object.die = True
                    self.invincibility(1500)
                if collided_object.block_type == 6:  # grabbed a flower
                    if not self.health > 1:
                        self.healthi(1)
                    collided_object.die = True
                    self.fire_mario = True
                    self.score_board.update(self.life, self.coin, self.fire_mario)
                if collided_object.block_type == 9:  # grabbed a coin
                    collided_object.die = True
                    self.coin += 1
                    if self.coin >= self.coinMult * 2:
                        self.life += 1
                        self.coinMult += 1
                    self.score_board.update(self.life, self.coin, self.fire_mario)
                if self.vertSpeed > 0:
                    self.rect.bottom = collided_object.rect.top
                    if collided_object.block_type == 1:
                        pygame.mixer.music.load('music/Wilhelm.mp3')
                        pygame.mixer.music.play(1)
                        self.healthi(-self.health)
                    landed = True
                elif self.vertSpeed < 0:
                    self.rect.top = collided_object.rect.bottom
                    if collided_object.block_type == 3:
                        collided_object.hit = True  # hit a question block from below
                    if collided_object.block_type == 8 and self.health > 1:
                        collided_object.hit = True  # hit a breakable block from below
            if landed:
                self.vertSpeed = 0
                self.jump_potential_energy = self.jump_force
            else:
                self.vertSpeed = 2
            if self.k_space and self.jump_potential_energy > 0:
                self.jump_potential_energy -= 1
                self.vertSpeed = -self.jump_speed
                if self.direction == 1:
                    # self.animate(name_of_animation='jump_right')
                    pass
                elif self.direction == -1:
                    # self.animate(name_of_animation='jump_left')
                    pass
            if self.vertSpeed < 0 and not self.k_space_held:
                self.vertSpeed = max(self.vertSpeed, 0)
        else:
            self.restart()
        # self.blitme()

    # draws mario image at the current position of self.rect
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def restart(self):
        self.life -= 1
        if self.life < 1:
            self.coinMult = 1
            self.coin = 0
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        for b in self.blocks:
            b.restart()
        self.die = False
        self.respawn = True
        self.health = 1
        self.invincibility_time = 0
        self.image = pygame.image.load('Images/mario.png')
        self.prevImage = self.image
        self.score_board.update(self.life, self.coin, self.fire_mario)
