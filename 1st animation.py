import pygame
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Animation")

done = False

clock = pygame.time.Clock()
rect_x = 50
rect_y = 50
change_x = 5
change_y = 5


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    if rect_x > 650 or rect_x <0:
        change_x = change_x * -1
    if rect_y > 450 or rect_y < 0:
        change_y = change_y * -1
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    rect_x += change_x
    rect_y += change_y


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
    
