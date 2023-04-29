import sys
import pygame

pygame.init()

from FireboyMain import Fireboy
from WatergirlMain import Watergirl


screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fireboy and Watergirl")

player_width = 50
player_height = 80

background_image = pygame.image.load("background.png").convert()
picture = pygame.transform.scale(background_image, (screen_width, screen_height))

fireboy = Fireboy()
watergirl = Watergirl()

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

platforms = pygame.sprite.Group()
platforms.add(Platform(0, screen_height - 50, screen_width, 50))
platforms.add(Platform(100, 500, 200, 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    fireboy.update()
    platform_collisions = pygame.sprite.spritecollide(fireboy, platforms, False)
    for platform in platform_collisions:
        if fireboy.rect.bottom > platform.rect.top and fireboy.rect.bottom < platform.rect.bottom:
            fireboy.rect.bottom = platform.rect.top
            fireboy.gravity = 0

    watergirl.update()
    platform_collisions = pygame.sprite.spritecollide(watergirl, platforms, False)
    for platform in platform_collisions:
        if watergirl.rect.bottom > platform.rect.top and watergirl.rect.bottom < platform.rect.bottom:
            watergirl.rect.bottom = platform.rect.top
            watergirl.gravity = 0

    screen.blit(picture, (0, 0))
    platforms.draw(screen)
    screen.blit(fireboy.image, fireboy.rect)
    screen.blit(watergirl.image, watergirl.rect)
    pygame.display.update()

