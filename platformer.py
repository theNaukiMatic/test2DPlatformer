import pygame

#variables
SCREEN_SIZE = (800,600)
BACKROUND_COLOR = (121, 217, 215)

#init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Working Title")


isGameRunning = True
#gameloop
while(isGameRunning):
    #input
    for event in pygame.event.get():

        #quit button 
        if(event.type == pygame.QUIT):
            isGameRunning = False

    #updating

    #drawing
    screen.fill(BACKROUND_COLOR)
    pygame.display.flip()

#quit
pygame.quit()