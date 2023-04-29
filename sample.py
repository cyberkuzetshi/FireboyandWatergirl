import sys
import pygame
from level import Level
from game_data import level_0

pygame.init()

screen_width = 1410
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
level = Level(level_0, screen)
pygame.display.set_caption("My Platform Game")

player_width = 50
player_height = 90

background_image = pygame.image.load("background.png").convert()

fireboy_image = pygame.image.load("Fireboy.png").convert_alpha()
fireboy_image = pygame.transform.scale(fireboy_image, (player_width, player_height))

watergirl_image = pygame.image.load("Watergirl.png").convert_alpha()
watergirl_image = pygame.transform.scale(watergirl_image, (player_width, player_height))
picture = pygame.transform.scale(background_image, (screen_width, screen_height))

class Fireboy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = fireboy_image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.speed = 1
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = 0.1
        self.jump_height = 1.2
        self.is_jumping = False
        self.jump_count = 0
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and not self.is_jumping:
            self.is_jumping = True
            self.jump_count = 0
            self.velocity.y = -self.jump_height
        self.velocity.y += self.gravity
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        # Keep the player within the game screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.is_jumping = False
            self.velocity.y = 0
fireboy = Fireboy()
class Watergirl(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = watergirl_image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.speed = 1
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = 0.01
        self.jump_height = 1.2
        self.is_jumping = False
        self.jump_count = 0
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w] and not self.is_jumping:
            self.is_jumping = True
            self.jump_count = 0
            self.velocity.y = -self.jump_height
        self.velocity.y += self.gravity
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        # Keep the player within the game screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            self.is_jumping = False
            self.velocity.y = 0

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
platforms.add(Platform(0, 400, 200, 20))
platforms.add(Platform(300, 300, 200, 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    level.run()

    fireboy.update()
    platform_collisions = pygame.sprite.spritecollide(fireboy, platforms, False)
    for platform in platform_collisions:
        if fireboy.rect.bottom > platform.rect.top and fireboy.rect.bottom < platform.rect.bottom:
            fireboy.rect.bottom = platform.rect.top
            fireboy.is_jumping = False
            fireboy.velocity.y = 0
            fireboy.gravity = 0
            break
    else:
        fireboy.gravity = 0.01
    for platform in platform_collisions:
        if fireboy.rect.right == platform.rect.left+1:
            fireboy.rect.right = platform.rect.left
        if fireboy.rect.left == platform.rect.right-1:
            fireboy.rect.left = platform.rect.right

    watergirl.update()
    platform_collisions = pygame.sprite.spritecollide(watergirl, platforms, False)
    for platform in platform_collisions:
        if watergirl.rect.bottom > platform.rect.top and watergirl.rect.bottom < platform.rect.bottom:
            watergirl.rect.bottom = platform.rect.top
            watergirl.is_jumping = False
            watergirl.velocity.y = 0
            watergirl.gravity = 0
            break
    else:
        watergirl.gravity = 0.01
    for platform in platform_collisions:
        if watergirl.rect.right == platform.rect.left+1:
            watergirl.rect.right = platform.rect.left
        if watergirl.rect.left == platform.rect.right-1:
            watergirl.rect.left = platform.rect.right

    screen.blit(picture, (0, 0))
    platforms.draw(screen)
    screen.blit(fireboy.image, fireboy.rect)
    screen.blit(watergirl.image, watergirl.rect)
    pygame.display.update()
