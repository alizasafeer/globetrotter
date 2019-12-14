import os
path=os.getcwd()

w = 400
h = 600
   
class Bird:#the class that represents the moving piece
    def __init__(self):
        self.x= 64
        self.y = h/2
       
        self.gravity = 0.6# gravity of the game that anchors movement
        self.lift = -15
        self.velocity = 0
       
        self.g= '' 
       
    def show(self):#function to initialise image of our character
        self.g=loadImage("girl.png") 
        image(self.g,self.x,self.y, 64, 64)
       
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
   

   
   

    
class Obstacle: #class to initialise obstacles, based on the location
    def __init__(self):#,x,y,w,h):#,imglist,location,img,img_cloud):
        self.top = random (h/2)
        self.bottom = random(h/2)
        self.x=w
        self.y=50
        self.w=w
        self.h=h
        self.speed = 5
        self.imglist= ["Agra", "Paris", "Dubai"]
        self.img = ''
        self.img_cloud= ''

        
# self.location=location
    
    def display (self):
        self.img=loadImage("Dubai.png") 
        image(self.img, self.x, 0)#, self.w, self.top)

        self.img_cloud=loadImage("cloud.png")#loading image of the cloud obstacle
        image(self.img_cloud, self.x,h-self.bottom)#,self.w, self.bottom)
    
    def update (self):
        self.x -= self.speed; 



obs = Obstacle()#instance of the Bird class


bird = Bird()

def setup ():
    size(w,h)
def draw():
    background (0)
    bird.update()
    bird.show()
    obs.display()

        
#movement control of the bird    
def keyPressed():
    if keyCode == UP :   #!!!
        bird.up()
    #    obs.display()
