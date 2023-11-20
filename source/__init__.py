import pygame
# import sys          # sys.exit()

import common.GlobalDefine as DEFINE
import GlobalConfig as config

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
config.prepareResourcePath()

# Set up the drawing window
screen = pygame.display.set_mode(DEFINE.SCREEN_SIZE)

ball = pygame.image.load(config.getResource("intro_ball.gif"))      #  Make sure the gif file of the bouncing ball is in the same folder as the code block
ballrect = ball.get_rect()

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill( DEFINE.RGBCode_white )

    # Draw a solid blue circle in the center
    pygame.draw.circle( screen, DEFINE.RGBCode_blue, (250, 250), 75 )

    ballrect = ballrect.move(DEFINE.speed)
    if ballrect.left < 0 or ballrect.right > DEFINE.SCREEN_WIDTH:
        DEFINE.speed[0] = -DEFINE.speed[0]
    if ballrect.top < 0 or ballrect.bottom > DEFINE.SCREEN_HEIGHT:
        DEFINE.speed[1] = -DEFINE.speed[1]

    screen.fill(DEFINE.RGBCode_black)      #  erase the screen by filling it with a black RGB color
    # Note: If we did not take the time to erase the ball from the screen, 
    # we would actually see a "trail" of the ball as we continuously draw the ball in its new positions.

    # copying pixel colors from one image to another
    screen.blit( ball,          # a source Surface to copy from
                 ballrect       # a position to place the source onto the destination.
               )

    # Flip the display
    pygame.display.flip()
    # Pygame manages the display with a double buffer. This (flip method) makes everything we have drawn on the screen Surface become visible. This buffering makes sure we only see completely drawn frames on the screen. Without it, the user would see the half completed parts of the screen as they are being created.

# Done! Time to quit.
pygame.quit()
# sys.exit()
