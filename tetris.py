import pygame
import sys

pygame.init()
pygame.display.set_mode((500,500))
screen = pygame.display.get_surface()
clock = pygame.time.Clock()

#This is a coordinate list
coordinate_list = [[(155+10*x,10*y+5)for x in range(20)] for y in range(1,26)]

def game_gui():
    pygame.draw.rect(screen,(255,255,255),game_rect,1)

def filled_list():
    coord_bool = []
    """Returns a list of a list with two elements, the first element is the coordinate, the second element is  """
    #Create a 2D List that has two different values, one of them is a tuple 
    #Does this make sense to belong to an object? Edit: No 
    for count,coords in enumerate(coordinate_list,1):
        for coord in coords:
            coord_bool.append([count,screen.get_at(coord)!=(0,0,0)])
        
    return coord_bool




class Piece:
    
    def __init__(self):
        self.rect = pygame.Rect(250,10,10,10)
        self.gravity = 1

    def draw(self):
        pygame.draw.rect(screen,(0,255,0),self.rect)
    
    def apply_gravity(self):
        self.rect.y += self.gravity
    
    def hit_border(self): #Return a boolean
        if self.rect.y >= game_rect.bottom-10:
            self.gravity = 0
            return True
        else:
            return False
    
    def move_right(self):
        if not self.rect.x >= game_rect.right-10:
            self.rect.x += 10
    
    def move_left(self):
        if not self.rect.x <= game_rect.left:
            self.rect.x -= 10
    
    def is_collide(self):
        """The actualized purpose of this will be to see if the next position is a valid positio, returns a Boolean value as the return value"""
        #This function takes from the current rectangle and determines if it is in the current list
        if (self.rect.centerx,self.rect.centery+10) in bg.rects_center: #This only calculates the last position below the rectangle and determine
            return True
        elif (self.rect.centerx-10,self.rect.centery) and (self.rect.centerx,self.rect.centery+10) in bg.rects_center:
            return True
        elif (self.rect.centerx+10,self.rect.centery) and (self.rect.centerx,self.rect.centery+10) in bg.rects_center:
            return True
        #If it is untrue it returns none, and that value is inherentely false.
            
    def compile(self):
        self.apply_gravity()
        self.draw()

class BackGround:

    def __init__(self):
        #Write a function to determine collision
        self.rect_list = []
        self.rects_center = []
        #self.
    
    def consume(self,piece):
        """Appends the rectangle object to the background class and passes the data as it sees fit."""
        self.rect_list.append(piece.rect)
        self.rects_center.append(piece.rect.center)
    
    def draw_bg(self):
        """This will draw the background from the reference list, taken from BackGround.consume() method"""
        for rect in self.rect_list:
            pygame.draw.rect(screen,(255,0,0),rect)
        
    def return_rect_center(self):
        """A Dev function to determine if the coords line up"""
        print(self.rects_center)
    
    def check_filled(self): #I want to see if this can return an index of what row to delete
        """The purpose of this function will be to determine if the rows are filled"""
        #For the row elements, this will only check to see if the rows are filled, I have yet to find a logical fallacy
        #Loop through the entire array and see if a "True" value exsists, once it does, pull its position, if it exsists already count it
        #Other wise add it to another set of numbers, I am begging to dislike how much mmr this takes up :/
        #Once it is "full" delete the row completely, I need to run more evaluation checks, to determine
        count_dict = {x:None for x in range(1,26)}
        
        for key in count_dict: #This is the outer level that stores the keys
            del_list = [] #Instantiate a list every time this outer loop is called
            for element in filled_list():
                if key == element[0]:
                    del_list.append(element[1])
                    if all(del_list):
                        return key



    
    #Get the rectangle at when it collides with a piece
piece = Piece()
bg = BackGround()
game_rect = pygame.Rect(150,10,200,250)

#Create a 2d loop that goes from 155 to 345 

 

while True:
    screen.fill((0,0,0))
    #pygame.time.wait(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                piece.move_right()
            elif event.key == pygame.K_LEFT:
                piece.move_left()    

    

    piece.compile()
    bg.draw_bg()
    game_gui()




    
    if piece.is_collide():
        piece.gravity = 0
        print(bg.check_filled())
        bg.consume(piece)



            

        piece = Piece() #Create new piece object in mmr
        #The object needs to be created last, this is because we are looking at the current piece and not the new one and do not want to make any false evaluations

  
    
  
    if piece.hit_border():
        bg.consume(piece)        
        print(bg.check_filled())
        piece = Piece()
        


    #rect_list[col_index][row_index]
 



  


    pygame.display.update()
    clock.tick(60)

 
