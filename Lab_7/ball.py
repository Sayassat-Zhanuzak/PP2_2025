import pygame 

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)
BLACK = ()
RED = (219, 7, 1)
FPS = 60
clock = pygame.time.Clock()

MOVEMENT_SPEED = 20
CIRCLE_RAD = 40

running = True
INITIAL_X_POS = 100
INITIAL_Y_POS = 100

x = INITIAL_X_POS
y = INITIAL_Y_POS

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
            
            
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_UP]:
        
        y = max(CIRCLE_RAD,y - MOVEMENT_SPEED)
        
    if pressed[pygame.K_DOWN]:
        
        y = min(SCREEN_HEIGHT - CIRCLE_RAD, y + MOVEMENT_SPEED)
        
    if pressed[pygame.K_LEFT]:
        
        x = max(CIRCLE_RAD, x - MOVEMENT_SPEED)  
    
    if pressed[pygame.K_RIGHT]:
        
        x = min(SCREEN_WIDTH - CIRCLE_RAD, x + MOVEMENT_SPEED)
                      
    screen.fill(WHITE)
    
    
    
    pygame.draw.circle(screen, RED, (x, y), CIRCLE_RAD)

    pygame.display.flip()
    clock.tick(FPS)
