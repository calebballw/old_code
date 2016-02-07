#test

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Wassup")

clock = pygame.time.Clock()

click_sound = pygame.mixer.Sound("playerLaser.wav")

background_position = [0, 0]
background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("ship.png").convert()
player_image.set_colorkey(BLACK)

done = False

while not done:
    for event in pygame.event.get():
        screen.blit(background_image, background_position)
        player_position = pygame.mouse.get_pos()
        x = player_position[0]
        y = player_position[1]
        screen.blit(player_image, [x + -50, y + -50])
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
            pygame.draw.line(screen, WHITE, [x, y], [x, y + 100], 5)

    
    


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
        
