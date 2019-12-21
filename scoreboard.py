import pygame


class Scoreboard:
    def __init__(self, settings, stats, screen):
        self.settings = settings
        self.stats = stats
        self.screen = screen
        self.font = settings.font
        self.lives = settings.mario_lives
        self.coins = 0
        self.txt_lives = self.font.render(("Mario: " + str(self.lives)), True, (0, 128, 0))
        self.txt_coins = self.font.render(("Coins: " + str(self.coins)), True, (0, 128, 0))
        self.txt_instructions = self.font.render("Press s to throw fireball.", True, (0, 128, 0))
        self.fire_power = False

    def update(self, lives, coins, fire_mario):
        self.lives = lives
        self.coins = coins
        self.txt_lives = self.font.render(("Mario: " + str(self.lives)), True, (0, 128, 0))
        self.txt_coins = self.font.render(("Coins: " + str(self.coins)), True, (0, 128, 0))
        self.fire_power = fire_mario

    def show_score(self):
        self.screen.blit(self.txt_lives, (32, 32))
        self.screen.blit(self.txt_coins, (64 + self.txt_lives.get_width(), 32))
        if self.fire_power:
            self.screen.blit(self.txt_instructions, (32, 64))
