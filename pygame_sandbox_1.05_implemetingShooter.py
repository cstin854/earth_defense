import sys, pygame
from Shooter import Shooter

#Initializes pygame
pygame.init()

#Sets global variables
size = width, height = 800, 600
speed = [4, 4]
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
refresh_time = 20
keydown_delay = 250
overheat_accumulation = 10
overheat_decumulation = 0.1
number_of_shooters = 2

#Set the size of the screen and the keydown delay
screen = pygame.display.set_mode(size)
pygame.key.set_repeat(keydown_delay,keydown_delay)

#Sets the size of the tracker rectangles
#This can likely be deleted later!
rect_height = 20
rect_width = 100

#Initialize list of shooters
w = []

#Initialize one shooter
w.append(Shooter('intro_ball.gif',100,100))

#Sets the game to 'running'.
running = True

while running == True:
    pygame.time.delay(refresh_time)
    
    for event in pygame.event.get():
        pressed = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
            break
        #Print a message when the 'w' key is pressed.
        elif event.type == pygame.KEYDOWN and pressed[pygame.K_w]:
            print('w was pressed')
            w[0].add_heat()
            print('Increase heat!',w[0].get_heat())
        else:
            pass

    w[0].rectangle = w[0].rectangle.move(speed)
    if w[0].rectangle.left < 0 or w[0].rectangle.right > width:
        speed[0] = -speed[0]
    if w[0].rectangle.top < 0 or w[0].rectangle.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(w[0].image, w[0].rectangle)

    pygame.draw.rect(screen, white, (0, 0, w[0].max_heat, 25))
    red_rect_width = int(w[0].get_heat())
    pygame.draw.rect(screen, red, (0, 0, red_rect_width, 25))
    
    pygame.display.flip()
    w[0].update()

pygame.quit()
sys.exit()
