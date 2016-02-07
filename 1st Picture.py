import pygame
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (62, 201, 247)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Picture")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(BLUE)
    pygame.draw.rect(screen, GREEN, [0, 400, 700, 100], 5)
    offset = 400
    while offset <= 500:
        pygame.draw.line(screen, GREEN, [0, offset], [700, offset], 5)
        offset += 1
    pygame.draw.line(screen, BLACK, [350, 350], [350, 200], 5)
    pygame.draw.line(screen, BLACK, [350, 350], [400, 400], 5)
    pygame.draw.line(screen, BLACK, [350, 350], [300, 400], 5)
    pygame.draw.line(screen, BLACK, [350, 275], [300, 300], 5)
    pygame.draw.line(screen, BLACK, [350, 275], [400, 300], 5)
    pygame.draw.ellipse(screen, BLACK, [100, 50, 500, 150], 0)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Giant Head Man!", True, BLACK)
    screen.blit(text, [270, 125])
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

