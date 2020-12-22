import pygame
import render

# variables
SCREEN_SIZE = (800, 600)
BACKROUND_COLOR = (121, 217, 215)
GROUND_COLOR = (30, 135, 47)
FPS = 60
PLAYER_SPEED = 8
GRAVITY = 1
JUMP_SPEED = -15

# init
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Working Title")
clock = pygame.time.Clock()

# player
player_height = 128
player_width = 96

player_walking_animation = render.Animation([
    pygame.image.load('assets/skeleton_walk/skeleton_walk_00.png'),
    pygame.image.load('assets/skeleton_walk/skeleton_walk_01.png'),
    pygame.image.load('assets/skeleton_walk/skeleton_walk_02.png'),
    pygame.image.load('assets/skeleton_walk/skeleton_walk_03.png'),
    pygame.image.load('assets/skeleton_walk/skeleton_walk_04.png'),
    pygame.image.load('assets/skeleton_walk/skeleton_walk_05.png'),
    pygame.image.load('assets/skeleton_walk/skeleton_walk_06.png'),
    pygame.image.load('assets/skeleton_walk/skeleton_walk_07.png'),
    pygame.image.load('assets/skeleton_walk/skeleton_walk_08.png'),
    pygame.image.load('assets/skeleton_walk/skeleton_walk_09.png'),
    pygame.image.load('assets/skeleton_walk/skeleton_walk_10.png'),
    pygame.image.load('assets/skeleton_walk/skeleton_walk_11.png'),
    pygame.image.load('assets/skeleton_walk/skeleton_walk_12.png'),
])
player_walking_animation.setAnimationSpeed(4)
player_idle_animation = render.Animation([
    pygame.image.load('assets/skeleton_idle/skeleton_idle_00.png'),
    pygame.image.load('assets/skeleton_idle/skeleton_idle_01.png'),
    pygame.image.load('assets/skeleton_idle/skeleton_idle_02.png'),
    pygame.image.load('assets/skeleton_idle/skeleton_idle_03.png'),
    pygame.image.load('assets/skeleton_idle/skeleton_idle_04.png'),
    pygame.image.load('assets/skeleton_idle/skeleton_idle_05.png'),
    pygame.image.load('assets/skeleton_idle/skeleton_idle_06.png'),
    pygame.image.load('assets/skeleton_idle/skeleton_idle_07.png'),
    pygame.image.load('assets/skeleton_idle/skeleton_idle_08.png'),
    pygame.image.load('assets/skeleton_idle/skeleton_idle_09.png'),
    pygame.image.load('assets/skeleton_idle/skeleton_idle_10.png'),
])
player_x = 300
player_y = 0
player_accelaration_y = GRAVITY
player_speed_y = 0
player_on_ground = False
player_direction = "right"
player_state = "idle"

# platforms
platforms = [
    pygame.Rect(50, 500, 700, 50),
    pygame.Rect(50, 450, 50, 50),
    pygame.Rect(700, 450, 50, 50),
]

isGameRunning = True
# gameloop
while(isGameRunning):

    player_state = "idle"
    # input
    for event in pygame.event.get():
        # quit button
        if(event.type == pygame.QUIT):
            isGameRunning = False

    # player control
    new_player_x = player_x
    new_player_y = player_y
    keys = pygame.key.get_pressed()

    # move left
    if(keys[pygame.K_LEFT]):
        new_player_x -= PLAYER_SPEED
        player_direction = "left"
        player_state = "walking"

    # move right
    if(keys[pygame.K_RIGHT]):
        new_player_x += PLAYER_SPEED
        player_direction = "right"
        player_state = "walking"

    # jump
    if(keys[pygame.K_SPACE]) and player_on_ground:
        player_speed_y = JUMP_SPEED

    # animation updates
    player_idle_animation.update()
    player_walking_animation.update()

    # horizontal movement
    player_hitbox_x = pygame.Rect(
        new_player_x, player_y, player_width, player_height)
    x_collision = False

    # collision detection on all platforms
    for p in platforms:
        if p.colliderect(player_hitbox_x):
            x_collision = True
            break

    # No collision
    if(x_collision == False):
        player_x = new_player_x

    # vertical movement
    player_speed_y += player_accelaration_y
    new_player_y += player_speed_y

    player_hitbox_y = pygame.Rect(player_x, new_player_y, 96, 128)
    y_collision = False
    player_on_ground = False

    # collision detection on all platforms
    for p in platforms:
        if p.colliderect(player_hitbox_y):
            y_collision = True
            player_speed_y = 0
            # if player collide with platform it sticks to the platform
            if(player_y < p[1]):
                player_y = p[1] - player_height
                player_on_ground = True
            break

    # No collision
    if(y_collision == False):
        player_y = new_player_y

    # updating

    #drawing#######################################################################################

    # Background
    screen.fill(BACKROUND_COLOR)

    # Platforms
    for p in platforms:
        pygame.draw.rect(screen, GROUND_COLOR, p)

    # Player
    if(player_state == "idle"):
        if player_direction == "right":
            player_idle_animation.draw(screen, player_x, player_y, False)

        else:
            player_idle_animation.draw(screen, player_x, player_y, True)

    else:
        if player_direction == "right":
            player_walking_animation.draw(screen, player_x, player_y, False)

        else:
            player_walking_animation.draw(screen, player_x, player_y, True)

    # Screen
    pygame.display.flip()
    clock.tick(FPS)
    ###############################################################################################


# quit
pygame.quit()
