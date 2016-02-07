#Mario Program
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mario Template")

clock = pygame.time.Clock()

background_position = [0, 0]
background_mario = pygame.image.load("bowser.jpg").convert()

done = False

while not done:
    for event in pygame.event.get():
        screen.blit(background_mario, background_position)
        
        if event.type == pygame.QUIT:
            done = True
        

    
    


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
        
