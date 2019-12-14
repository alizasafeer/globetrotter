import os
path=os.getcwd()

w = 400
h = 600
   
class Bird:
    def __init__(self):
        self.x= 64
        self.y = h/2
       
        self.gravity = 0.6
        self.lift = -15
        self.velocity = 0
       
    def show(self):
        fill (255)
        ellipse (self.x,self.y, 32, 32)
       
       
    def update(self):
        self.velocity += self.gravity
        self.velocity *= 0.9
        self.y += self.velocity
       
        if (self.y > h):
            self.y = h
            self.velocity = 0
           
        if (self.y < 0):
            self.y = 0
            self.velocity = 0
   
    def up (self):
        self.velocity += self.lift
   
       
       

bird = Bird()


def setup ():
    size(w,h)
def draw():
    background (0)
    bird.update()
    bird.show()
   
   
   
def keyPressed():
    if keyCode == UP :   #!!!
        bird.up()
    
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
        
class Game:
     def __init__(self,w,h,g,bg_img):
        self.w=w
        self.h=h
        self.g=g
        self.x=0
                
        #adding the general background of the game
        self.bg_img=loadImage(path+"/images/background.png")
        
        #generating obstacles
        self.obstacles=[]
        for i in range(10):
            self.obstacle.append(Obstacle(300+(75*i),500,200,300)
    
    def display_images(self):#displaying the background images
        image(bg_img,0,0,self.w-x+1,self.h,x-1,0,self.w,self.h)
        
        for a in self.obstacles:
            a.display_images()
        

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
    

        
