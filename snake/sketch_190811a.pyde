class snake:
    def __init__(self, x, y, xspeed, yspeed):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
    
    def update(self):
        self.x += self.xspeed
        self.y += self.yspeed
        
    def accelarate(x, y):
        self.xspeed = x
        self.yspeed = y
        
    def show(self):
        fill(255)
        rect(self.x, self.y, 50, 50)

s = snake(1, 1, 1, 0)

def setup():
    size(200, 200)
    background(51)
    s = snake(1, 1, 1, 0)
    
    
def draw():
    s.update()
    s.show()
    
