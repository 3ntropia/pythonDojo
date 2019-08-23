max_size = 600
scl = 20

class food:
    def __init__(self):
        self.x = int(random(max_size / scl)) * scl
        self.y = int(random(max_size / scl)) * scl
        
    def show(self):
        fill(255, 0, 0)
        rect(self.x, self.y, scl, scl)
        
    def new(self):
        self.x = int(random(max_size / scl)) * scl
        self.y = int(random(max_size / scl)) * scl

class snake:
    def __init__(self, x, y, xspeed = 0, yspeed = 0):
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        
    def accelarate(self, x, y):
        self.xspeed = x
        self.yspeed = y
        
    def show(self):
        fill(255)
        rect(self.x, self.y, scl, scl)
        for sqr in tail:
            rect(sqr.x, sqr.y, scl, scl)

    def update(self):
        self.x += self.xspeed * scl
        self.y += self.yspeed * scl
        self.x = constrain(self.x, 0, width - scl)
        self.y = constrain(self.y, 0, height - scl)

def eat(x, y, fx, fy):
    return dist(x, y, fx, fy) < scl
    
def keyPressed():    
    if key == CODED:
        if keyCode == UP:
            s.accelarate(0, -1)
        elif keyCode == DOWN:
            s.accelarate(0, 1)
        elif keyCode == RIGHT:
            s.accelarate(1, 0)
        elif keyCode == LEFT:
            s.accelarate(-1, 0)

def mousePressed():
    tail.append(snake(s.x, s.y))

s = snake(0, 0)
f = food()
tail = []

def setup():
    size(max_size, max_size)
    frameRate(5)
    tail = []
    
def update_tail(s):
    for index in range(0, len(tail)):
        if index == len(tail)-1:
            tail[index].x = s.x
            tail[index].y = s.y
        else:
            tail[index].x = tail[index+1].x
            tail[index].y = tail[index+1].y

def check_death(s, tail):
    for sqr in tail:
        if dist(s.x, s.y, sqr.x, sqr.y) < scl:
            return True
    return False
                                                                                                                                                                                                                                                                                                                        
def draw():
    background(0)
    s.update()
    global tail
    if check_death(s, tail):
        tail = []
    s.show()
    update_tail(s)
    if eat(s.x, s.y, f.x, f.y):
        tail.append(snake(s.x, s.y))
        f.new()
    f.show()
    



    
