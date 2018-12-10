#This will work for all pygame projects
import pygame
import random
import os

WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
	# sprite for the Player
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
		self.image.set_colorkey(BLACK)
		self.rect = self.image.get_rect()
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
		self.y_speed = 5

	def update(self):
		self.rect.x += 5
		self.rect.y += self.y_speed
		if self.rect.bottom > HEIGHT - 100:
			self.y_speed = -5
		if self.rect.top < 100:
			self.y_speed = 5
		if self.rect.left > WIDTH:
			self.rect.right = 0
		
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True
while running:
	# keep loop running at the right speed
	clock.tick(FPS)
	#process input (event)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	#update
	all_sprites.update()

	#draw
	screen.fill(GREEN)
	all_sprites.draw(screen)
	#after drawing everything, flip the display
	pygame.display.flip()

pygame.quit()
