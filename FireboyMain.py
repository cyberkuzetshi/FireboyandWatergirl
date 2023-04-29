import pygame
pygame.init()

player_width = 50
player_height = 80

fireboy_image = pygame.image.load("Fireboy.png").convert_alpha()
fireboy_image = pygame.transform.scale(fireboy_image, (player_width, player_height))

class Fireboy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = fireboy_image
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.speed = 1
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = 0.01
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
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
