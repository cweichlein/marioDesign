import pygame
import math

from animation import Animation
from enemy import Enemy
from settings import Settings
from timer import Timer


class Goomba(Enemy, Animation):
    def __init__(self, screen, settings, x, y, player, floor, block, goombas, koopas):
        super().__init__(screen, settings, x, y, player, floor, block, goombas, koopas)

        self.animate_set_character(character='goomba', settings=settings)

    def update(self):
        self.animate(name_of_animation='jump_right')
        self.update_animation()
        self.blitme()

    def crushed_death_animation(self):
        time = pygame.time.get_ticks()
        # Animate and keep on screen for half a second before killing sprite
        self.animate(name_of_animation='crushed')
        if abs(time - self.last_frame) > 1000:
            self.player.score += 100
            self.kill()

    def upside_down_death_animation(self):
        time = pygame.time.get_ticks()
        # Animate getting hit (Go up for two seconds)
        if self.death_animation_frame == 0:
            self.rect.y += (abs(self.enemy_direction) * self.enemy_speed)
        else:
            self.rect.y += (abs(self.enemy_direction) * self.enemy_speed * -1)
        # After two seconds fall down while upside down
        if self.death_animation_frame == 0 and abs(self.last_frame - time) > 2000:
            self.animate(name_of_animation='upside_down')
            self.death_animation_frame += 1
        """MIGHT BE REDUNDANT WITH CHECK BOUNDARY"""
        # Kill off after 10 seconds (Enough to be off screen)
        if abs(self.last_frame - time) > 10000:
            self.player.score += 100
            self.kill()

    def update(self):
        if not self.dead:
            self.goomba_physics()
        else:
            if self.player_enemy_kill is True:
                self.animate(name_of_animation='crushed')
            elif self.block_enemy_kill is True:
                self.animate(name_of_animation='upside_down')
            elif self.shell_enemy_kill is True:
                self.animate(name_of_animation='upside_down')
        self.update_animation()

    def goomba_physics(self):
        self.check_boundary()
        # If no blocks are touching enemy -> Fall Down
        if not self.check_floor() and self.start_movement:
            self.rect.y += (abs(self.enemy_direction) * self.enemy_gravity)
            self.rect.x = self.rect.x + (self.enemy_direction * (self.enemy_speed - 1))
        if self.check_floor() and self.start_movement:
            self.rect.x = self.rect.x + (self.enemy_direction * self.enemy_speed)

        if self.check_collisions():
            # Collides with player
            if self.enemy_player_collide_flag:
                # Enemy dead
                if self.player_enemy_kill:
                    self.dead = True
                    self.last_frame = pygame.time.get_ticks()
                    self.animate(name_of_animation='crushed')
                else:
                    self.enemy_player_collide_flag = False
            # Collision with map or block
            elif self.enemy_block_collide_flag:
                # Killed by player hitting block
                if self.block_enemy_kill:
                    self.dead = True
                    self.animate(name_of_animation='upside_down')
                # If colliding with map (i.e. Pipe) change direction
                else:
                    self.rect.x += (self.ENEMY_DIRECTION * self.ENEMY_SPEED)
                    self.enemy_block_collide_flag = False
            # If colliding with goomba change direction
            elif self.enemy_goomba_collide_flag:
                self.rect.x += (self.ENEMY_DIRECTION * self.ENEMY_SPEED)
                self.enemy_goomba_collide_flag = False
            # If colliding with koopa
            elif self.enemy_koopa_collide_flag:
                # Colliding with koopa shell thats moving
                if self.shell_enemy_kill:
                    self.dead = True
                    self.animate(name_of_animation='upside_down')
                # Colliding with koopa enemy or shell
                else:
                    self.rect.x += (self.ENEMY_DIRECTION * self.ENEMY_SPEED)
                    self.enemy_koopa_collide_flag = False