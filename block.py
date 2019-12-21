import pygame
from pygame.sprite import Sprite


class Block(Sprite):
    def __init__(self, settings, screen, block_type):
        super(Block, self).__init__()
        self.block_type = block_type
        if block_type == -1:
            self.image = pygame.image.load('Images/block_used.png')
        elif block_type == 0:
            self.image = pygame.image.load('Images/block_grey.png')
        elif block_type == 1:
            self.image = pygame.image.load('Images/lava.png')
        else:
            self.image = pygame.image.load('Images/oboo.png')
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.settings = settings
        self.screen = screen

    def move_left(self):
        self.rect.x -= 1

    def restart(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass


class Enemy(Block):
    def __init__(self, settings, screen, block_type, blocks):
        super(Enemy, self).__init__(settings, screen, block_type)
        self.vertSpeed = settings.enemy_speed
        self.timer = 0
        self.phase = 1
        self.image = pygame.image.load('Images/oboo.png')
        self.die = False
        self.blocks = blocks

    def update(self):
        if not self.die:
            if self.phase == 1:  # jump
                self.rect.y -= self.vertSpeed
                self.image = pygame.image.load('Images/oboo.png')
            if self.phase == 2:  # fall
                self.rect.y += self.vertSpeed
                self.image = pygame.image.load('Images/oboo_2.png')
            if self.phase == 3:  # wait
                pass
            self.timer += 1
            if self.timer == 130:
                self.timer = 0
                if self.phase == 3:
                    self.phase = 0
                self.phase += 1
        else:
            self.remove(self.blocks)

    def restart(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.timer = 0
        self.phase = 0
        self.die = False


class Breakable(Block):
    def __init__(self, settings, screen, block_type, blocks):
        super(Breakable, self).__init__(settings, screen, block_type)
        self.image = pygame.image.load('Images/block_brown.png')
        self.hit = False
        self.blocks = blocks

    def update(self):
        if self.hit:
            self.remove(self.blocks)

    def restart(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.hit = False


class Question(Block):
    def __init__(self, settings, screen, block_type, blocks, item_type, x, y):
        super(Question, self).__init__(settings, screen, block_type)
        self.phase = 1
        self.image = pygame.image.load('Images/block_brown.png')
        self.hit = False
        self.spent = False
        self.blocks = blocks
        self.item_type = item_type
        self.x = x
        self.y = y

    def update(self):
        if not self.spent and self.hit:
            self.spent = True
            self.image = pygame.image.load('Images/block_used.png')
            new_item = Item(self.settings, self.screen, self.item_type, self.rect.x, self.y - (self.rect.height + 23), self.blocks)
            self.blocks.add(new_item)

    def restart(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.hit = False
        self.spent = False
        self.image = pygame.image.load('Images/block_brown.png')


class Item(Block):
    def __init__(self, settings, screen, block_type, x, y, blocks):
        super(Item, self).__init__(settings, screen, block_type)
        self.block_type = block_type
        if block_type == 4:
            self.image = pygame.image.load('Images/item_mushroom.png')
            self.flees = True
            self.horizSpeed = settings.item_speed
            self.static = False
        elif block_type == 5:
            self.image = pygame.image.load('Images/item_star.png')
            self.flees = True
            self.horizSpeed = settings.item_speed
            self.static = False
        elif block_type == 6:
            self.image = pygame.image.load('Images/item_flower.png')
            self.flees = False
            self.horizSpeed = 0
            self.static = False
        elif block_type == 7:
            self.image = pygame.image.load('Images/fireball.png')
            self.rect = self.image.get_rect()
            self.flees = True
            self.horizSpeed = settings.item_speed * 3
            self.static = False
        else:
            self.image = pygame.image.load('Images/item_coin.png')
            self.rect = self.image.get_rect()
            self.flees = False
            self.horizSpeed = 0
            self.static = False
        self.rect.x = x
        self.rect.y = y
        self.blocks = blocks
        self.vertSpeed = 0
        self.die = False

    def update(self):
        if not self.die:
            self.rect.x += self.horizSpeed
            collidable_list = pygame.sprite.spritecollide(self, self.blocks, False)
            for collided_object in collidable_list:
                if collided_object is not self:
                    if collided_object.block_type == 2 and self.block_type == 7:
                        self.die = True
                        collided_object.die = True
                    if self.horizSpeed > 0:
                        self.rect.right = collided_object.rect.left
                        # self.horizSpeed *= -1
                    elif self.horizSpeed < 0:
                        self.rect.left = collided_object.rect.right
                        # self.horizSpeed *= -1
            if not self.static:
                self.rect.y += self.vertSpeed
                landed = False
                collidable_list2 = pygame.sprite.spritecollide(self, self.blocks, False)
                for collided_object in collidable_list2:
                    if collided_object is not self:
                        if self.vertSpeed > 0:
                            self.rect.bottom = collided_object.rect.top
                            if collided_object.block_type == 1:
                                self.die = True
                            landed = True
                        elif self.vertSpeed < 0:
                            self.rect.top = collided_object.rect.bottom
                if landed:
                    self.vertSpeed = 0
                else:
                    self.vertSpeed = 2
        else:
            self.remove(self.blocks)

    def restart(self):
        self.die = True
        self.remove(self.blocks)
