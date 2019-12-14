import random

scl = 30 

w = 600
h = 600

food = ''
alt = True

global score
score = 0


#globetrotter 
class Person:
    def __init__(self,x,y,r,g):#,img,w,h,F):
        self.x=x
        self.y=y
        self.r=r #radius
        self.g=g #ground level
        self.vx=0 #movement across x
        self.vy=0 #movement across y
        self.w=w
        self.h=h
        
        ###
        #    self.F=F #number of creature frames!!!
     #   self.f=0
        ###
    #       self.img = loadImage(path+"/images/"+img)
        self.dir = 1
        
        self.keyHandler = {LEFT:False, RIGHT:False, UP:False}
    #     self.jump = audioPlayer.loadFile(path+"/sounds/jump.mp3")  !!!


    def character (self):
        self.face =  loadImage ('head_up.png')
        
    def show(self):
        image(self.face, self.x, self.y)
    
    
        
        
    def gravity(self):
        if self.y + self.r < self.g:
            self.vy += 0.3
            if self.y+self.r+self.vy > self.g:
                self.vy = self.g-(self.y+self.r)
                
    
    def update(self):
        self.gravity()
        
        if self.keyHandler[LEFT] == True:
            self.vx = -5  #go to the left 5 pixels along the x axis 
            self.dir = -1
        elif self.keyHandler[RIGHT] == True:
                self.vx = 5   #go to the right 5 pixels along the x axis 
                self.dir = 1
        else:
            self.vx = 0
            
        if self.keyHandler[UP] == True and self.y+self.r == self.g:
            self.vy = -10   #go up 10 pixels along the y axis 
            self.jump.rewind()
            self.jump.play()
            
            #update the location of mario    
        self.x += self.vx
        self.y += self.vy
        

        #check if mario has reached the middle of the window
        if self.x >= g.w/2:
            g.x += self.vx
    
class Obstacle:
    def__init__(self,x,y,w,h,imglist,location,img,img_cloud):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.imglist= [Agra, Paris, Dubai]
        self.img=loadImage(path+"/images/"+self.location)
        self.img_cloud=loadImage(path+"/images/cloud.png"
        self.location=location
        
    def monument_obstacle(self):
        image(self.img,x,y)
                        
    def cloud_obstacle(self):
        image(self.img_cloud,x,y)
        
        

g = Person(1,2,3,4)

def setup():
    size(g.w,g.h)
    background(0)
   
def draw():
    #if not g.pause: !!!
    background(0)
    g.character()
  #  else:
  #  fill(255,0,0)
    textSize(30)
   # text("Paused",g.w//2,g.h//2)
    

        
