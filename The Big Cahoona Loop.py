import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("The Big Cahoona Loop Lab")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    
    startix = 5
    startiy = 5
    for x in range(50):
        for n in range(140):
            pygame.draw.rect(screen, GREEN, [startix, startiy, 5, 5], 0)
            startix += 10
        startiy += 10
        startix = 5

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
    
    
