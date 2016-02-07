import pygame
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (130, 86, 86)
LIGHTBLUE = (22, 214, 240)

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Animation")

snow_list = []
for i in range(150):
    x = random.randrange(0, 700)
    y = random.randrange(0, 400)
    snow_list.append([x, y])
snowc = 1
stick = 220
stickc = 5
door = 0
doorc = 1
snow1 = 326
snow2 = 210
snow3 = 140

clock = pygame.time.Clock()

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BLUE)
    pygame.draw.rect(screen, BROWN, [400, 100, 250, 300], 0)
    pygame.draw.polygon(screen, BROWN, [[525, 50], [350, 100], [700, 100]], 0)
    pygame.draw.rect(screen, BLACK, [500, 300, 50, 100], 0)
    pygame.draw.rect(screen, LIGHTBLUE, [450, 150, 50, 75], 0)
    pygame.draw.rect(screen, LIGHTBLUE, [550, 150, 50, 75], 0)
    pygame.draw.rect(screen, RED, [500, 300, door, 100], 0)
    door += doorc
    if door >= 50:
        doorc *= -1
    if door <= -10:
        doorc *= -1
        
    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        snow_list[i][1] += 1
        if snow_list[i][1] > 400:
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            x = random.randrange(0, 700)
            snow_list[i][0] = x
    pygame.draw.rect(screen, WHITE, [0, 400, 700, 100], 0)
    man = []
    pygame.draw.circle(screen, WHITE, [100, snow1], 75)
    pygame.draw.circle(screen, WHITE, [100, snow2], 50)
    pygame.draw.circle(screen, WHITE, [100, snow3], 25)
    pygame.draw.line(screen, BROWN, [100, 210], [175, stick], 5)
    pygame.draw.line(screen, BROWN, [100, 210], [25, stick], 5)
    stick += stickc
    if stick > 280:
        stickc *= -1
    if stick < 160:
        stickc *= -1
        
    pygame.draw.circle(screen, BLACK, [90, 130], 5)
    pygame.draw.circle(screen, BLACK, [110, 130], 5)
    pygame.draw.circle(screen, BLACK, [85, 145], 3)
    pygame.draw.circle(screen, BLACK, [115, 145], 3)
    pygame.draw.circle(screen, BLACK, [92, 148], 3)
    pygame.draw.circle(screen, BLACK, [108, 148], 3)


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
