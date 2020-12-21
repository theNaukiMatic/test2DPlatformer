import pygame

#variables
SCREEN_SIZE = (800,600)
BACKROUND_COLOR = (121, 217, 215)
GROUND_COLOR = (30, 135, 47)

#init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Working Title")


#player
player_image = pygame.image.load('assets/skeleton_idle/skeleton_idle_00.png')

#platforms
platforms = [
    pygame.Rect(50,500, 700, 50),
]

isGameRunning = True
#gameloop
while(isGameRunning):
    #input
    for event in pygame.event.get():

        #quit button 
        if(event.type == pygame.QUIT):
            isGameRunning = False

    #updating

    #drawing#######################################################################################

    #Background
    screen.fill(BACKROUND_COLOR)

    #Platforms
    for p in platforms:
        pygame.draw.rect(screen,GROUND_COLOR,p)

    #Player
    screen.blit(player_image,(0,0))

    #Screen
    pygame.display.flip()
    ###############################################################################################


#quit
pygame.quit()