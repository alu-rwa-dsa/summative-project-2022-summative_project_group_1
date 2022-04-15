"""
DSA Summative: Test for cognitive recognition using a tower of hanoi puzzle game
----------------------

"""

import pygame, sys, time, tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

pygame.init()
pygame.display.set_caption("DSA Summative Group 1")
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

game_done = False
framerate = 60

# game vars:
steps = 0
n_disks = 1
disks = []
towers_midx = [120, 320, 520]
pointing_at = 0
floating = False
floater = 0

# colors:
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
blue = (78, 162, 196)
grey = (170, 170, 170)
green = (77, 206, 145)
ghost_white = (248, 248, 255)
white_smoke = (245, 245, 245)


def blit_text(screen, text, midtop, aa=True, font=None, font_name=None, size=None, color=(255, 0, 0)):
    """
    
    :param screen: Screen intended for gameplay and interactivity with the user
    :type screen:blit (block transfer)
    :param text:
    :type text: Any
    :param midtop:
    :type midtop: Any
    :param aa:
    :type aa: bool = True
    :param font: Font of the game if any
    :type font: Optional[{render}] = None
    :param font_name: Font name or family of the game if any
    :type font_name: Any = None
    :param size:
    :type size: Any = None
    :param color:
    :type color: Tuple[int, int, int] = (255, 0, 0)) -> None


    """

    if font is None:  # font option is provided to save memory if font is
        font = pygame.font.SysFont(font_name, size)  # already loaded and needs to be reused many times
        font_surface = font.render(text, aa, color)
        font_rect = font_surface.get_rect()
        font_rect.midtop = midtop
        screen.blit(font_surface, font_rect)


def menu_screen():
    """

    Method to be called before starting actual game loop
    This is the initial menu of the screen

    """
    global screen, n_disks, game_done
    menu_done = False
    while not menu_done:  # every screen/scene/level has its own loop
        screen.fill(ghost_white)
        blit_text(screen, 'Tower of Hanoi Implementation', (320, 70), font_name='Montserrat', size=55, color=blue)
        blit_text(screen, 'Use arrow keys to select difficulty:', (320, 150), font_name='Montserrat', size=40,
                  color=grey)
        if n_disks <= 2:
            blit_text(screen, str(n_disks), (320, 222), font_name='Montserrat', size=53, color=green)
        elif 2 < n_disks <= 4:
            blit_text(screen, str(n_disks), (320, 222), font_name='Montserrat', size=53, color=orange)
        elif n_disks > 4:
            blit_text(screen, str(n_disks), (320, 222), font_name='Montserrat', size=53, color=red)
        blit_text(screen, 'Press Enter to Start', (320, 300), font_name='Montserrat', size=60, color=blue)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    menu_done = True
                    game_done = True
                if event.key == pygame.K_RETURN:
                    menu_done = True
                if event.key in [pygame.K_RIGHT, pygame.K_UP]:
                    n_disks += 1
                    if n_disks > 7:
                        n_disks = 7
                if event.key in [pygame.K_LEFT, pygame.K_DOWN]:
                    n_disks -= 1
                    if n_disks < 1:
                        n_disks = 1
            if event.type == pygame.QUIT:
                menu_done = True
                game_done = True
        pygame.display.flip()
        clock.tick(60)


def game_over():
    """

    Method to end the game after the game shows
    cognitive ability of the user with the corresponding results

    """
    global screen, steps
    screen.fill(white_smoke)
    min_steps = 2 ** n_disks - 1
    blit_text(screen, 'Congratulations, You Win', (320, 70), font_name='Montserrat', size=72, color=blue)
    blit_text(screen, 'Congratulations, You Win', (322, 70), font_name='Montserrat', size=72, color=blue)
    blit_text(screen, 'Steps Taken to complete: ' + str(steps), (320, 200), font_name='Montserrat', size=55, color=grey)
    blit_text(screen, 'Minimum Steps: ' + str(min_steps), (320, 160), font_name='Montserrat', size=55, color=grey)
    if steps - min_steps == 0:
        blit_text(screen, 'You finished in minumum steps!', (320, 300), font_name='Montserrat', size=35, color=green)
        blit_text(screen, 'This shows impeccable cognitive function!', (320, 320), font_name='Montserrat', size=35,
                  color=green)
    elif steps <= min_steps+(min_steps*0.20):
        blit_text(screen, 'You did okay', (320, 300), font_name='Montserrat', size=35, color=green)
        blit_text(screen, 'Make sure to be careful and more observing, No need to approach a specialist', (320, 325),
                  font_name='Montserrat', size=26, color=green)
    elif min_steps+(min_steps*0.20) < steps <= min_steps+(min_steps*0.50):
        blit_text(screen, 'This is not good', (320, 300), font_name='Montserrat', size=30, color=orange)
        blit_text(screen, 'Consider reaching out to a specialist for any underlying cognitive difficulties', (320, 325),
                  font_name='Montserrat', size=24, color=orange)
    elif steps > min_steps+(min_steps*0.50):
        blit_text(screen, 'You did poorly', (320, 300), font_name='Montserrat', size=30, color=red)
        blit_text(screen, 'There seems to be signs of severe congitive failure, seek help ASAP', (320, 325),
                  font_name='Montserrat', size=27, color=red)
    pygame.display.flip()
    time.sleep(10)  # wait for 2 secs
    pygame.quit()  # pygame exit
    sys.exit()  # console exit


def draw_towers():
    """

    Method to draw the towers or rods used for the game

    """
    global screen
    for xpos in range(40, 460 + 1, 200):
        pygame.draw.rect(screen, green, pygame.Rect(xpos, 400, 160, 20))
        pygame.draw.rect(screen, grey, pygame.Rect(xpos + 75, 200, 10, 200))
    blit_text(screen, 'Start', (towers_midx[0], 403), font_name='mono', size=14, color=white)
    blit_text(screen, 'Finish', (towers_midx[2], 403), font_name='mono', size=14, color=white)


def make_disks():
    """

    Method to create the disks

    """
    global n_disks, disks
    disks = []
    height = 20
    ypos = 397 - height
    width = n_disks * 23
    for i in range(n_disks):
        disk = {}
        disk['rect'] = pygame.Rect(0, 0, width, height)
        disk['rect'].midtop = (120, ypos)
        disk['val'] = n_disks - i
        disk['tower'] = 0
        disks.append(disk)
        ypos -= height + 3
        width -= 23


def draw_disks():
    """

    Method to draw the disks
    :return: Display the drawn disks on the screen
    :rtype: none

    """
    global screen, disks
    for disk in disks:
        pygame.draw.rect(screen, blue, disk['rect'])
    return


def draw_ptr():
    """

    Method to show interactivity of the discs to the user
    :return: Shows the cursor which is used to move the disks
    :rtype: none

    """
    ptr_points = [(towers_midx[pointing_at] - 7, 440), (towers_midx[pointing_at] + 7, 440),
                  (towers_midx[pointing_at], 433)]
    pygame.draw.polygon(screen, red, ptr_points)
    return


def check_won():
    """

    Method to check if the user has won the game

    """
    global disks
    over = True
    for disk in disks:
        if disk['tower'] != 2:
            over = False
    if over:
        time.sleep(0.2)
        game_over()


def reset():
    """

    Method to reset the game

    """
    global steps, pointing_at, floating, floater
    steps = 0
    pointing_at = 0
    floating = False
    floater = 0
    menu_screen()
    make_disks()

    """
    
    Call of the menu_screen and make_disks methods to start the game

    """


menu_screen()
make_disks()

"""

    A loop is used to control the interactivity with the user and in the case of an error,
    a message is printed
    
"""

# main game loop:
while not game_done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                reset()
            if event.key == pygame.K_q:
                game_done = True
            if event.key == pygame.K_RIGHT:
                pointing_at = (pointing_at + 1) % 3
                if floating:
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 100)
                    disks[floater]['tower'] = pointing_at
            if event.key == pygame.K_LEFT:
                pointing_at = (pointing_at - 1) % 3
                if floating:
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 100)
                    disks[floater]['tower'] = pointing_at
            if event.key == pygame.K_UP and not floating:
                for disk in disks[::-1]:
                    if disk['tower'] == pointing_at:
                        floating = True
                        floater = disks.index(disk)
                        disk['rect'].midtop = (towers_midx[pointing_at], 100)
                        break
            if event.key == pygame.K_DOWN and floating:
                for disk in disks[::-1]:
                    if disk['tower'] == pointing_at and disks.index(disk) != floater:
                        if disk['val'] > disks[floater]['val']:
                            floating = False
                            disks[floater]['rect'].midtop = (towers_midx[pointing_at], disk['rect'].top - 23)
                            steps += 1
                        else:
                            messagebox.showinfo('Error', 'Illegal move. Click the screen with your mouse to resume')
                        break
                else:
                    floating = False
                    disks[floater]['rect'].midtop = (towers_midx[pointing_at], 400 - 23)
                    steps += 1

    screen.fill(black)
    draw_towers()
    draw_disks()
    draw_ptr()
    blit_text(screen, 'Steps: ' + str(steps), (320, 20), font_name='mono', size=30, color=white)
    pygame.display.flip()
    if not floating: check_won()
    clock.tick(framerate)
