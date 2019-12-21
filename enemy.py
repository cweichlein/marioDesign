import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, screen, settings, image, x, y, player, floor, block, goombas, koopas):
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.image = image
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.rect.left, self.rect.top = self.x, self.y
        self.player = player
        self.floor = floor
        self.block = block
        self.goombas = goombas
        self.koopas = koopas
        self.death_animation_frame = 0
        self.last_frame = 0

        """CHANGE TO -1 TO START LEFT"""
        self.enemy_direction = settings.enemy_direction
        self.enemy_speed = settings.enemy_speed
        self.enemy_gravity = settings.enemy_gravity

        # Collision flags
        self.enemy_player_collide_flag = False
        self.enemy_block_collide_flag = False
        self.enemy_goomba_collide_flag = False
        self.enemy_koopa_collide_flag = False
        self.player_enemy_kill = False
        self.block_enemy_kill = False
        self.shell_mode = False
        self.shell_movement = False
        self.shell_enemy_kill = False

        self.start_movement = True
        self.dead = False
        self.stop = False

    def check_player_collision(self):
        """Checks collisions with Mario"""
        if self.rect.colliderect(self.player.rect):
            # pts = [self.rect.topleft, self.rect.midtop, self.rect.topright]
            pts = []
            x, y = self.rect.topleft
            limitx, limity = self.rect.topright
            for point in range(x, limitx):
                pts.append((x, y))
            for pt in pts:
                if self.rect.collidepoint(pt) and self.rect.left < self.player.rect.centerx < self.rect.right:
                    self.set_killed()
            self.enemy_player_collide_flag = True
            return True

    def set_killed(self):
        """Set the enemy's status to killed by the player"""
        self.player_enemy_kill = True
        self.last_frame = pygame.time.get_ticks()
        self.shell_mode = True
        self.dead = True

    def check_block_collision(self):
        # Check if colliding with map (i.e pipe) or dying from block
        if pygame.sprite.spritecollideany(self, self.block):
            self.enemy_block_collide_flag = True
            self.enemy_direction *= -1
            return True
        """NEED TO CHECK FOR IF MARIO HITS BLOCK KILLING ENEMY"""
        for block_rect in self.block:
            if self.rect.contains(block_rect.rect):
                self.enemy_direction = abs(self.enemy_direction) * -1
                self.enemy_block_collide_flag = True
                self.block_enemy_kill = True
                self.dead = True
                return True

    def check_friendly_collision(self):
        """FIX ENEMY COLLIDING WITH SELF"""
        # Check for collisions with friendly or koopa shell
        for goomba_rect in self.goombas:
            if goomba_rect is not self and self.rect.colliderect(goomba_rect.rect) and not goomba_rect.dead:
                self.enemy_goomba_collide_flag = True
                self.enemy_direction *= -1
                return True
        for koopa_rect in self.koopas:
            if koopa_rect is not self and self.rect.colliderect(koopa_rect.rect):
                if koopa_rect.shell_movement:
                    self.shell_enemy_kill = True
                self.enemy_koopa_collide_flag = True
                self.enemy_direction *= -1
                return True

    def check_floor(self):
        # Returns true if at enemy on floor
        for floor_rect in self.floor:
            if self.rect.colliderect(floor_rect):
                return True
        for block in self.block:
            pts = [block.rect.topleft, block.rect.midtop, block.rect.topright]
            for pt in pts:
                if self.rect.collidepoint(pt):
                    self.x += self.enemy_direction * self.enemy_speed
                    return True

    def check_boundary(self):
        if self.rect.x >= (self.player.rect.x + (self.screen.get_width()/2)):
            self.start_movement = False
        else:
            self.start_movement = True
        if self.rect.x <= (self.player.rect.x - (self.screen.get_width()/2)) or \
                self.rect.y - (self.rect.height * 2) >= self.screen.get_height():
            self.start_movement = False
            self.dead = True
            self.kill()

    def check_collisions(self):
        # If flag is set already, no need to check collisions again
        # Also might stops from getting multiple flags set off
        self.check_player_collision()
        self.check_block_collision()
        self.check_friendly_collision()
        if self.enemy_player_collide_flag is True or self.enemy_block_collide_flag is True\
                or self.enemy_goomba_collide_flag is True or self.enemy_koopa_collide_flag is True:
            return True

    def reset_parameters(self):
        self.enemy_player_collide_flag = False
        self.enemy_block_collide_flag = False
        self.enemy_goomba_collide_flag = False
        self.enemy_koopa_collide_flag = False
        self.player_enemy_kill = False
        self.block_enemy_kill = False
        self.shell_mode = True
        self.shell_enemy_kill = False
        self.dead = False
        self.stop = False
        self.enemy_direction = self.settings.enemy_direction
        self.enemy_speed = self.settings.enemy_speed
        self.enemy_gravity = self.settings.enemy_gravity
        self.rect.left, self.rect.top = self.x, self.y

    def blit(self):
        self.screen.blit(self.image, self.rect)
