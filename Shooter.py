import pygame
from PIL import Image

def get_contour(image):
    image = Image.open(image)
    size = image.size
    print(size)
    (x,y) = size
    print(x)
    print(y)

class Shooter():
    ''' Docstring for Shooter class '''

    def __init__(self, filename, x_pos, y_pos):
        print('Sup? Im making a shooter.')
        self.image = pygame.image.load(filename)
        self.overheat_tracker = 0
        self.is_decumulating = True
        self.filename = filename
        self.penalty_time = 0
        self.max_penalty_time = 5000
        self.in_penalty = False
        self.penalty_decrementor = 100
        self.overheat_accumulation = 10
        self.overheat_decumulation = 0.1
        self.max_heat = 100
        self.rectangle = self.image.get_rect()
        self.rectangle = self.rectangle.move(x_pos,y_pos)
        print(self.rectangle)

    def get_sprite_filename(self):
        print('My sprites filename is ',self.filename)
        return self.filename

    def get_heat(self):
        return self.overheat_tracker

    def get_penalty_time(self):
        print('My current penalty time is ',self.penalty_time)
        return self.penalty_time

    def give_penalty(self):
        '''Sets current penalty to max penalty,
        and sets Boolean in_penalty to false.
        Should also change the sprite to show overheating'''
        self.in_penalty = True
        self.penalty_time = self.max_penalty_time

    def reduce_penalty(self):
        '''Reduces penalty time by penalty_decrementor'''
        self.penalty_time = self.penalty_time - self.penalty_decrementor
        if self.penalty_time <= 0:
            self.penalty_time = 0
            self.in_penalty = False
            self.overheat_tracker = 0
        print('Current penalty time = ',self.penalty_time)

    def shoot(self):
        '''To be implemented!
        Should make a sound that depends on how hot the gun is...
        Should provide a shot vector to the game'''
        if self.in_penalty:
            print('Fail! Cant shoot while in penalty')
            '''Make a fail sound here'''
        else:
            print('Go ahead and shoot...')
            self.add_heat()
            '''Here is where I'd make a sound...'''
            '''Here is where I'd pass the vector to the game...'''

    def add_heat(self):
        '''Should add heat to overheat.
        If overheated, should put self in penalty'''
        self.overheat_tracker = self.overheat_tracker + self.overheat_accumulation
        print('Current heat = ',self.overheat_tracker)
        if self.overheat_tracker > self.max_heat:
            self.overheat_tracker = self.max_heat
            self.give_penalty()

    def update(self):
        '''To be implemented! Should do the following...
        1. Decumulate IF NOT IN PENALTY
        2. IF in penalty, reduce penalty'''

        if self.in_penalty:
            self.reduce_penalty()
        else:
            self.cooldown()

    def cooldown(self):
        ''' Cools down overheat tracker '''
        self.overheat_tracker = self.overheat_tracker - self.overheat_decumulation
        if self.overheat_tracker < 0:
            self.overheat_tracker = 0

    def get_left(self):
        return self.rectangle.left

    def get_right(self):
        return self.rectangle.right

    def get_top(self):
        return self.rectangle.top

    def get_bottom(self):
        return self.rectangle.bottom

    def move(self,speed):
        print(self.rectangle)
        self.rectangle = self.rectangle.move(speed)
        print(self.rectangle)

class Bullet():
    def __init__(self,image_name,x_pos,y_pos,x_vector,y_vector):
        image = pygame.image.load(image_name)

get_contour('intro_ball.gif')
