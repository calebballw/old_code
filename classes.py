import pygame
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
BLUE = (62, 201, 247)

pygame.init()

class Ball():
    def __init__(self):
        self.x = 0
        self.y = 0

        self.change_x = 0
        self.change_y = 0

        self.size = 10
        self.color = [255, 255, 255]

    def move(self):
        self.x += self.change_x
        self.y += self.change_y
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Classes")

done = False

clock = pygame.time.Clock()

theBall = Ball()
theBall.x = 100
theBall.y = 100
theBall.change_x = 2
theBall.change_y = 1
theBall.color = [255, 0, 0]

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLUE)
    theBall.move()
    theBall.draw(screen)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
