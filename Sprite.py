from __future__ import print_function
import pygame
from PIL import Image

class Sprite():
    ''' Creates a pygame sprite '''
    def __init__(self, filename, x_pos=0, y_pos=0, x_vector=0, y_vector=0):
        self.image = pygame.image.load(filename)
        self.filename = filename
        self.rectangle = self.image.get_rect()
        a,b,c,d = self.rectangle
        self.size = (c,d)
        self.x_vector = x_vector
        self.y_vector = y_vector
        self.rectangle = self.rectangle.move(x_pos,y_pos)
        self.contour_map = self.set_contour_map()
        self.set_contour()

    def get_sprite_filename(self):
        #print('My sprites filename is ',self.filename)
        return self.filename

    def get_left(self):
        return self.rectangle.left

    def get_right(self):
        return self.rectangle.right

    def get_top(self):
        return self.rectangle.top

    def get_bottom(self):
        return self.rectangle.bottom

    def move(self):
        #print(self.rectangle)
        speed = (self.x_vector,self.y_vector)
        self.rectangle = self.rectangle.move(speed)
        #print(self.rectangle)
        ''' Need to implement something where this changes the contour:
        Right now, the contour is just 0's and 1's based on an initial position
        of (0,0) '''
        self.set_contour()
    
    def set_vector(self,x_vec, y_vec):
        self.x_vector = x_vec
        self.y_vector = y_vec
        return
    
    def get_vector(self):
        return (self.x_vector,self.y_vector)

    def set_contour_map(self):
        ''' Sets the contour map '''
        #To be implemeted!
        image = Image.open(self.filename)
        (cols,rows) = self.size
        #print(cols)
        #print(rows)
        list_representation = []
        max_color = 0
        for row in range(0,rows):
            temp = []
            for column in range(0,cols):
                temp.append(image.getpixel((column,row)))
                #print('Row = ',row,' Column = ',str(column))
                #print(image.getpixel((column,row)))
                max_color = max(max_color,image.getpixel((column,row)))
            list_representation.append(temp)
                
        zero_one_rep = []
        
        for row in range(0,rows):
            temp = []
            for column in range(0,cols):
                temp.append(not (list_representation[row][column] >= max_color))
                #if list_representation[row][column] >= max_color:
                #    temp.append(0)
                #else:
                #    temp.append(1)
            zero_one_rep.append(temp)
        #print(zero_one_rep)
        
        return zero_one_rep
    
    def get_contour_map(self):
        return self.contour_map
    
    def set_contour(self):
        x,y = self.size
        temp = []
        for j in range(0,y):
            for i in range(0,x):
                #print(self.contour_map[j][i])
                if self.contour_map[j][i]:
                    temp.append((self.get_left()+j,self.get_top()+i))
        self.contour = temp
        return
    
    def get_contour(self):
        return self.contour

pygame.init()

#Temp test suite for Windows
path = 'D:/Users/stingley/Documents/GitHub/earth_defense/'
file_name = 'test_sprite.gif'
file_path = path+file_name
w = Sprite(file_path)
#get_contour(file_path)
#print(w.get_vector())
#print(w.get_contour_map())
#w.get_contour()