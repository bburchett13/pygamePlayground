# Import the pygame library and initialise the game engine
import pygame
import math
from random import randrange
from pygame import font
pygame.init()
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)

# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)

# Open a new window
Width = 700
Height = 500
size = (Width, Height)


tickRate = 30
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

# The loop will carry on until the user exits the game (e.g. clicks the close button).
carryOn = True
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

game = False
lives = 4
points = 0
# quit = False

#define menu
def menu(game):

    points = 0
    tickRate = 30
    while game == False:
        screen.fill(WHITE)

        #Create button surface
        button_surface = pygame.Surface((200, 50))
        # Create a pygame.Rect object that represents the button's boundaries
        button_rect = pygame.Rect((Width-200/2)/2, (Height-50)/2, 200, 50)  # Adjust the position as needed

        pygame.draw.rect(screen, GREEN, [(Width-200/2)/2, (Height-50)/2, 200, 50],0)

        # Render text on the button
        text = my_font.render("Click to Start", False, WHITE)
        # text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))
        screen.blit(text, ((Width-200/2)/2,(Height-50)/2))

        scoreDisplay = my_font.render(str(points), False, BLACK)
        scoreRect = scoreDisplay.get_rect(topright=(300,100))
        pygame.draw.rect(scoreDisplay, BLACK, scoreRect,1)
        pygame.display.flip()
        
        key = pygame.key.get_pressed()
        # if key[pygame.K_SPACE]:
        #      game = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If user clicked close
                lives = 0
                points = 0
                carryOn = False # Flag that we are done so we can exit the while loop
                game = False
                
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Call the on_mouse_button_down() function
                if button_rect.collidepoint(event.pos):
                    # pygame.time.delay(1000)
                    lives = 4
                    carryOn = True
                    game = True
            clock.tick(tickRate)

    return [lives, game, carryOn, points]

#define alien game
def alien(tickRate, lives, game, points):
    scoreDisplay = my_font.render(str(points), False, BLACK)
    scoreRect = scoreDisplay.get_rect()
    pygame.draw.rect(scoreDisplay, BLACK, scoreRect,1)
    rectLocationX = 1
    rectLocationY = 75
    rectWidth = 100
    rectHeight = 100
    fallRectX = 0
    fallRectY = rectLocationY + rectHeight
    fallRectVelocity = tickRate/2
    targetWidth = math.floor(10000/tickRate)
    targetHeight = 100
    draw = False
    velocity = tickRate/4
    carryOn = True
    gameEnd = False

    while not gameEnd:
        targetWidth = math.floor(10000/tickRate)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and draw == False:
            draw = True
            fallRectX = rectLocationX + rectWidth/2
            pygame.draw.rect(screen, GREEN, [fallRectX, fallRectY, rectWidth/5, rectHeight/5],0)
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                game = False
                gameEnd = True
                carryOn = False # Flag that we are done so we can exit the while loop
                    
        # --- Game logic should go here
        # --- Drawing code should go here
        # First, clear the screen to white. 
        screen.fill(WHITE)
        for life in range(0,lives):
            pygame.draw.rect(screen, BLACK, [life*rectWidth/2, 0,rectWidth/5, rectHeight/5])
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
                lives -= 1
                gameEnd = True
                if lives < 1:
                    game = False
            elif fallRectY > (Height-targetHeight) and fallRectX > (Width-targetWidth)/2 and (fallRectX+rectWidth/5) < (Width-targetWidth)/2 + targetWidth:
                fallRectY = rectLocationY + rectHeight
                draw = False
                points += 1
                gameEnd = True

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        if rectLocationX < 0 or rectLocationX + 100 > 700: velocity = velocity * (-1)
        rectLocationX += velocity
        
        # --- Limit to 60 frames per second
        clock.tick(tickRate)
    return [game, lives, carryOn, points]


#define jump game
def jump(tickRate, lives, game, points):
    scoreDisplay = my_font.render(str(points), False, BLACK)
    scoreRect = scoreDisplay.get_rect()
    pygame.draw.rect(scoreDisplay, BLACK, scoreRect,1)
    rectLocationX = 100
    rectLocationY = 400
    rectWidth = 100
    rectHeight =  100
    rectVelocity = 0

    dodgeRectWidth = 70
    dodgeRectHeight = 70
    dodgeRectX = 500
    dodgeRectY = 430
    dodgeRectVelocity = tickRate/3
    carryOn = True
    gameEnd = False
    

    while not gameEnd:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                game = False
                gameEnd = True
                carryOn = False # Flag that we are done so we can exit the while loop

        #draw my shapes
        screen.fill(WHITE)
        for life in range(0,lives):
            pygame.draw.rect(screen, BLACK, [life*rectWidth/2, 0,rectWidth/5, rectHeight/5])
        #The you can draw different shapes and lines or add text to your background stage.
        pygame.draw.rect(screen, BLACK, [rectLocationX, rectLocationY, rectWidth, rectHeight],0)
        pygame.draw.rect(screen, RED, [dodgeRectX, dodgeRectY, dodgeRectWidth, dodgeRectHeight],0)

        #update shape position
        pygame.display.flip()
        dodgeRectX -= dodgeRectVelocity
        rectLocationY -= rectVelocity
        rectVelocity -= 5
        if rectLocationY >= 400:
            rectLocationY = 400
            rectVelocity = 0


        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and rectVelocity == 0:
            #jump code
            rectVelocity = tickRate * 1.5
        
        #check for collision
        if dodgeRectX <= rectLocationX+rectWidth and dodgeRectX+dodgeRectWidth >= rectLocationX and rectLocationY+rectHeight >= dodgeRectY:
            lives -= 1
            print(lives)
            gameEnd = True
            if lives < 1:
                game = False

        if dodgeRectX < -200:
            points += 1
            gameEnd = True

        clock.tick(tickRate)
    
    return [game, lives, carryOn, points]

games = [alien, jump]

# -------- Main Program Loop -----------
while carryOn:
    
    [lives, game, carryOn,points] = menu(game)

    while game:
        [game,lives,carryOn,points] = games[randrange(2)](tickRate,lives,game, points)
        tickRate += 1
    clock.tick(tickRate)
    
#Once we're done, we can quit   
pygame.quit()


