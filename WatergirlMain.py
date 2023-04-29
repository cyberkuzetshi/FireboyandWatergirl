import pygame

pygame.init()

player_width = 50
player_height = 80

watergirl_image = pygame.image.load("Watergirl.png").convert_alpha()
watergirl_image = pygame.transform.scale(watergirl_image, (player_width, player_height))

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
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
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
