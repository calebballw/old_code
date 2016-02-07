import pygame
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (62, 201, 247)
BROWN = (130, 86, 86)

def draw_circle(screen, x, y):
    #body
    pygame.draw.circle(screen, WHITE, [100 + x, 300 + y], 75)
    pygame.draw.circle(screen, WHITE, [100 + x, 210 + y], 50)
    pygame.draw.circle(screen, WHITE, [100 + x, 140 + y], 25)
    #arms
    pygame.draw.line(screen, BROWN, [100 + x, 210 + y], [175 + x, 220 + y], 5)
    pygame.draw.line(screen, BROWN, [100 + x, 210 + y], [25 + x, 220 + y], 5)
    #facial features
    pygame.draw.circle(screen, BLACK, [90 + x, 130 + y], 5)
    pygame.draw.circle(screen, BLACK, [110 + x, 130 + y], 5)
    pygame.draw.circle(screen, BLACK, [85 + x, 145 + y], 3)
    pygame.draw.circle(screen, BLACK, [115 + x, 145 + y], 3)
    pygame.draw.circle(screen, BLACK, [92 + x, 148 + y], 3)
    pygame.draw.circle(screen, BLACK, [108 + x, 148 + y], 3)
def draw_tree(screen, x, y):
    #the green part
    pygame.draw.polygon(screen, GREEN, [[300 + x, 275 + y], [275 + x, 325 + y], [325 + x, 325 + y]], 0)
    pygame.draw.polygon(screen, GREEN, [[300 + x, 300 + y], [250 + x, 350 + y], [350 + x, 350 + y]], 0)
    pygame.draw.polygon(screen, GREEN, [[300 + x, 325 + y], [225 + x, 375 + y], [375 + x, 375 + y]], 0)
    pygame.draw.polygon(screen, GREEN, [[300 + x, 350 + y], [200 + x, 400 + y], [400 + x, 400 + y]], 0)
    #the stump
    pygame.draw.rect(screen, BROWN, [290 + x, 400 + y, 20 , 50], 0)

    

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Picture")

x_speed = 0
y_speed = 0

x_coord = 10
y_coord = 10

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    x_coord += x_speed
    y_coord += y_speed

    if x_coord >= 600:
        x_coord = 600
    elif x_coord <= -100:
        x_coord = -100
    elif y_coord >= 350:
        y_coord = 350
    elif y_coord <= -200:
        y_coord = -200

    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]
    
    screen.fill(RED)
    draw_circle(screen, x_coord, y_coord)
    draw_tree(screen, x - 300, y - 300)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

