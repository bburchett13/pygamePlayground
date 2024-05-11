# Import the pygame library and initialise the game engine
import pygame
import math
pygame.init()

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

# Open a new window
Width = 700
Height = 500
size = (Width, Height)
rectLocationX = 1
rectLocationY = 75

tickRate = 30

targetWidth = math.floor(10000/tickRate)
targetHeight = 100

rectWidth = 100
rectHeight = 100
fallRectX = 0
fallRectY = rectLocationY + rectHeight
fallRectVelocity = tickRate/2

velocity = tickRate/4
draw = False
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

game = False

# Menu

# -------- Main Program Loop -----------
while carryOn:
    while game == False:
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, [(Width-rectWidth)/2, (Height-rectHeight)/2, rectWidth, rectHeight],0)
        pygame.display.flip()
        
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
             game = True
        for event in pygame.event.get():
            # if event.type == pygame.MOUSEBUTTONUP:
            #     pos = pygame.mouse.get_pos()
            #     if pos[0] > (Width-rectWidth)/2 and pos[0] < (Width-rectWidth)/2 + rectWidth and pos[1] < (Height-rectHeight)/2 and pos[1] > (Height-rectHeight)/2 + rectHeight:
            #         game = True
            if event.type == pygame.QUIT: # If user clicked close
                game = True
                carryOn = False # Flag that we are done so we can exit the while loop
            
            clock.tick(tickRate)

    targetWidth = math.floor(10000/tickRate)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and draw == False:
         draw = True
         fallRectX = rectLocationX + rectWidth/2
         pygame.draw.rect(screen, GREEN, [fallRectX, fallRectY, rectWidth/5, rectHeight/5],0)
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we can exit the while loop
                 
     # --- Game logic should go here
     # --- Drawing code should go here
     # First, clear the screen to white. 
    screen.fill(WHITE)
     #The you can draw different shapes and lines or add text to your background stage.
    pygame.draw.rect(screen, RED, [rectLocationX, rectLocationY, rectWidth, rectHeight],0)
    pygame.draw.rect(screen, BLACK, [(Width-targetWidth)/2, (Height-targetHeight), targetWidth, targetHeight],0)
    if draw:
        fallRectY += fallRectVelocity
        pygame.draw.rect(screen, GREEN, [fallRectX, fallRectY, rectWidth/5, rectHeight/5],0)
        if fallRectY > 500:
             draw = False
             fallRectY = rectLocationY + rectHeight
             tickRate = 30
             game = False
        elif fallRectY > (Height-targetHeight) and fallRectX > (Width-targetWidth)/2 and (fallRectX+rectWidth/5) < (Width-targetWidth)/2 + targetWidth:
             tickRate+=5
             fallRectY = rectLocationY + rectHeight
             draw = False
        
        

     # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    if rectLocationX < 0 or rectLocationX + 100 > 700: velocity = velocity * (-1)
    rectLocationX += velocity
     
     # --- Limit to 60 frames per second
    clock.tick(tickRate)
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()