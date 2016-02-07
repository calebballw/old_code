import pygame
import random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

class Rectangle():
    def __init__(self):
        self.x = 0
        self.y = 0

        self.h = 10
        self.w = 10

        self.change_x = 0
        self.change_y = 0

        self.color = [0, 0, 0]
    def move(self):
        self.x += self.change_x
        self.y += self.change_y
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.w, self.h], 0)
class Ellipse(Rectangle):
    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, [self.x, self.y, self.w, self.h], 0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Class Lab")
 
done = False
                         
clock = pygame.time.Clock()

my_list = []
for i in range(1000):
    my_object = Rectangle()
    my_object.x = random.randint(0, 700)
    my_object.y = random.randint(0, 500)
    my_object.h = random.randint(20, 70)
    my_object.w = random.randint(20, 70)
    my_object.change_x = random.randint(-3, 3)
    my_object.change_y = random.randint(-3, 3)
    my_object.color = [random.randint(1, 250), random.randint(1, 250), random.randint(1, 250)]
    my_list.append(my_object)
for f in range(1000):
    my_e = Ellipse()
    my_e.x = random.randint(0, 700)
    my_e.y = random.randint(0, 500)
    my_e.h = random.randint(20, 70)
    my_e.w = random.randint(20, 70)
    my_e.change_x = random.randint(-3, 3)
    my_e.change_y = random.randint(-3, 3)
    my_e.color = [random.randint(1, 250), random.randint(1, 250), random.randint(1, 250)]
    my_list.append(my_e)
    

     
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Drawing code should go here
 
    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
    for c in my_list:
        c.draw(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
