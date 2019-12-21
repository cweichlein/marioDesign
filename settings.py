import pygame


class Settings:
    def __init__(self):
        self.mode = -1
        self.points = 0

        self.enemy_direction = -1
        self.enemy_gravity = 4
        self.enemy_speed = 2

        self.item_speed = 1

        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        self.block_height = 32
        self.block_width = 32

        self.mario_speed_factor = 0.5
        self.mario_gravity = 0.5
        self.mario_limit = 3
        self.mario_jump_force = 75
        self.mario_lives = 2

        self.fire_ball_speed_factor = 1.5
        self.fire_ball_width = 5
        self.fire_ball_height = 5
        self.fire_balls_allowed = 2
        self.fire_ball_color = 10, 10, 200

        self.mob_speed_factor = 0.1
        self.mob_points = 100

        self.font = pygame.font.Font(None, 24)

        self.character_frames = {
            'mario': {
                'base': self.get_frame_list(path='image/mario/mario/stand_right', count=1),
                'stand_right': self.get_frame_list(path='image/mario/mario/stand_right', count=1),
                'stand_left': self.get_frame_list(path='image/mario/mario/stand_left', count=1),
                'walk_right': self.get_frame_list(path='image/mario/mario/walk_right', count=3),
                'walk_left': self.get_frame_list(path='image/mario/mario/walk_left', count=3),
                'jump_right': self.get_frame_list(path='image/mario/mario/jump_right', count=1),
                'jump_left': self.get_frame_list(path='image/mario/mario/jump_left', count=1)
            },
            'super_mario': {
                'base': self.get_frame_list(path='image/mario/super_mario/stand_right', count=1),
                'stand_right': self.get_frame_list(path='image/mario/super_mario/stand_right', count=1),
                'stand_left': self.get_frame_list(path='image/mario/super_mario/stand_left', count=1),
                'walk_right': self.get_frame_list(path='image/mario/super_mario/walk_right', count=3),
                'walk_left': self.get_frame_list(path='image/mario/super_mario/walk_left', count=3),
                'jump_right': self.get_frame_list(path='image/mario/super_mario/jump_right', count=1),
                'jump_left': self.get_frame_list(path='image/mario/super_mario/jump_left', count=1),
                'crouch_left': self.get_frame_list(path='image/mario/super_mario/crouch_left', count=1),
                'crouch_right': self.get_frame_list(path='image/mario/super_mario/crouch_right', count=1)
            },
            'fire_mario': {
                'base': self.get_frame_list(path='image/mario/fire_mario/stand_right', count=1),
                'stand_right': self.get_frame_list(path='image/mario/fire_mario/stand_right', count=1),
                'stand_left': self.get_frame_list(path='image/mario/fire_mario/stand_left', count=1),
                'walk_right': self.get_frame_list(path='image/mario/fire_mario/walk_right', count=3),
                'walk_left': self.get_frame_list(path='image/mario/fire_mario/walk_left', count=3),
                'jump_right': self.get_frame_list(path='image/mario/fire_mario/jump_right', count=1),
                'jump_left': self.get_frame_list(path='image/mario/fire_mario/jump_left', count=1),
                'crouch_left': self.get_frame_list(path='image/mario/fire_mario/crouch_left', count=1),
                'crouch_right': self.get_frame_list(path='image/mario/fire_mario/crouch_right', count=1)
            },
            'invin_mario': {
                'base': self.get_frame_list(path='image/mario/invin_mario/stand_right', count=4),
                'stand_right': self.get_frame_list(path='image/mario/invin_mario/stand_right', count=4),
                'stand_left': self.get_frame_list(path='image/mario/invin_mario/stand_left', count=4),
                'walk_right': self.get_frame_list(path='image/mario/invin_mario/walk_right', count=4),
                'walk_left': self.get_frame_list(path='image/mario/invin_mario/walk_left', count=4),
                'jump_right': self.get_frame_list(path='image/mario/invin_mario/jump_right', count=4),
                'jump_left': self.get_frame_list(path='image/mario/invin_mario/jump_left', count=4),
                'crouch_left': self.get_frame_list(path='image/mario/invin_mario/crouch_left', count=4),
                'crouch_right': self.get_frame_list(path='image/mario/invin_mario/crouch_right', count=4)
            },
            'goomba': {
                'base': self.get_frame_list(path='image/enemies/goomba/base', count=1),
                'walk': self.get_frame_list(path='image/enemies/goomba/walk', count=2),
                'upside_down': self.get_frame_list(path='image/enemies/goomba/upside_down', count=1),
                'crushed': self.get_frame_list(path='image/enemies/goomba/crushed', count=1)
            },
            'blue_goomba': {
                'base': self.get_frame_list(path='image/enemies/goomba/blue_goomba/base', count=1),
                'walk': self.get_frame_list(path='image/enemies/goomba/blue_goomba/walk', count=2),
                'upside_down': self.get_frame_list(path='image/enemies/goomba/blue_goomba/upside_down', count=1),
                'crushed': self.get_frame_list(path='image/enemies/goomba/blue_goomba/crushed', count=1)
            },
            'gray_goomba': {
                'base': self.get_frame_list(path='image/enemies/goomba/gray_goomba/base', count=1),
                'walk': self.get_frame_list(path='image/enemies/goomba/gray_goomba/walk', count=2),
                'upside_down': self.get_frame_list(path='image/enemies/goomba/gray_goomba/upside_down', count=1),
                'crushed': self.get_frame_list(path='image/enemies/goomba/gray_goomba/crushed', count=1)
            },
            'green_koopa_troopa': {
                'base': self.get_frame_list(path='image/enemies/koopa_troopa/green/base', count=1),
                'walk_right': self.get_frame_list(path='image/enemies/koopa_troopa/green/walk_right', count=2),
                'walk_left': self.get_frame_list(path='image/enemies/koopa_troopa/green/walk_left', count=2),
                'upside_down': self.get_frame_list(path='image/enemies/koopa_troopa/green/upside_down', count=1),
                'in_shell': self.get_frame_list(path='image/enemies/koopa_troopa/green/in_shell', count=1),
            },
            'red_koopa_troopa': {
                'base': self.get_frame_list(path='image/enemies/koopa_troopa/red/base', count=1),
                'walk_right': self.get_frame_list(path='image/enemies/koopa_troopa/red/walk_right', count=2),
                'walk_left': self.get_frame_list(path='image/enemies/koopa_troopa/red/walk_left', count=2),
                'upside_down': self.get_frame_list(path='image/enemies/koopa_troopa/red/upside_down', count=1),
                'in_shell': self.get_frame_list(path='image/enemies/koopa_troopa/red/in_shell', count=1),

            }
        }
        self.initialize_dynamic_settings()

    def get_frame_list(self, path, count=1):
        """Returns a list of image files."""
        return [pygame.transform.scale2x(pygame.image.load(path + '/{}.png'.format(i))) for i in range(0, count)]

    def initialize_dynamic_settings(self):
        self.mario_speed_factor = 0.2
        self.fire_ball_speed_factor = 1.5
        self.mob_speed_factor = 0.1
        self.mode = -1
        self.fire_ball_color = 10, 10, 200
