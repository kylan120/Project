import pygame
from Settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('Resources/textures/GC_SKYTN.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.bloody_screen = self.get_texture('resources/textures/RedScreen.png', RES)
        self.game_over_image = self.get_texture('resources/textures/deathIMG.png', RES)

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    def player_damage(self):
        self.screen.blit(self.bloody_screen, (0, 0))

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.0 * (self.game.player.rel + 0.1)) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        pygame.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('Resources/textures/ForestTrees.png'),
            2: self.get_texture('Resources/textures/WALL515.png'),
            3: self.get_texture('Resources/textures/WALL517.png')
        }
