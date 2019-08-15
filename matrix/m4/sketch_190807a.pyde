m = []
m_size = 4

def setup():
    size(400, 400)
    reset()
    
def draw():
    
    draw_matrix()

def keyPressed():
    if key == CODED:
        if keyCode == UP:
            merge_up()
        elif keyCode == DOWN:
            merge_down()
        elif keyCode == RIGHT:
            merge_right()
        elif keyCode == LEFT:
            merge_left()
        elif keyCode == ENTER:
            reset()
    insert_two()
            
def insert_two():
    is_empty = False
    x = int(random(m_size))
    y = int(random(m_size))
    while not is_empty:
        x = int(random(m_size))
        y = int(random(m_size))
        is_empty = is_rect_empty(x, y)
    m[x][y] = 2

def is_rect_empty(x, y):
    return m[x][y] == 0

def merge_up():
    for i in range(m_size):
        for j in range(m_size):
            if m[i][j] != 0:
                movable = True
                x = j
                while movable and x > 0:
                    if x - 1 == 0:
                        movable = False
                    if m[i][x - 1] == m[i][x]:
                        m[i][x - 1] *= 2
                        m[i][x] = 0
                        movable = False
                    elif m[i][x - 1] == 0:
                        m[i][x - 1] = m[i][x]
                        m[i][x] = 0
                    else:
                        movable = False
                    x -= 1

def merge_down():
   for i in range(m_size):
        for j in range(m_size - 1, -1, -1):
            if m[i][j] != 0:
                movable = True
                x = j
                while movable and x < m_size -1:
                    if x+1 == 0:
                        movable = False
                    if m[i][x+1] == m[i][x]:
                        m[i][x+1] *= 2
                        m[i][x] = 0
                        movable = False
                    elif m[i][x+1] == 0:
                        m[i][x+1] = m[i][x]
                        m[i][x] = 0
                    else:
                        movable = False
                    x += 1
 

def merge_left():
    for j in range(m_size):
        for i in range(m_size):
            if m[i][j] != 0:
                movible = True
                x = i
                while movible and x > 0:
                    if x-1 == m_size -1:
                        movable = False
                    if m[x - 1][j] == m[x][j]:
                        m[x - 1][j] *= 2
                        m[x][j] = 0
                        movable = False
                    elif m[x - 1][j] == 0:
                        m[x - 1][j] = m[x][j]
                        m[x][j] = 0
                    else:
                        movable = False
                    x -= 1


def merge_right():
    for j in range(m_size):
        for i in range(m_size - 1, -1, -1):
            if m[i][j] != 0:
                movible = True
                x = i
                while movable and x < m_size - 1:
                    if x + 1 == m_size - 1:
                        movable = False
                    if m[x + 1][j] == m[x][j]:
                        m[x + 1][j] *= 2
                        m[x][j] = 0
                        movable = False
                    elif m[x + 1][j] == 0:
                        m[x + 1][j] = m[x][j]
                        m[x][j] = 0
                    else:
                        movable = False
                    x += 1
    
def draw_matrix():
    for j in range(m_size):
        for i in range(m_size):
            x = i * height / m_size
            y = j * width / m_size
            fill(define_colour(m[i][j]))
            rect(x, y, height/m_size - 5, width/m_size - 5)
            textAlign(CENTER)
            fill(255)
            textSize(26)
            text(str(m[i][j]), x + 50, y + 50)

def define_colour(number):
    if number == 0:
        return color(153)
    if number == 2:
        return color(238, 228, 218)
    elif number == 4:
        return color(236, 224, 200)
    elif number == 8:
        return color(255, 196, 92)
    elif number == 16:
        return color(245, 149, 99)
    elif number == 32:
        return color(245, 124, 95)
    elif number == 64:
        return color(246, 93, 59)
    elif number == 128:
        return color(237, 206, 113)
    elif number == 256:
        return color(237, 204, 97)
    elif number == 512:
        return color(237, 205, 80)
    elif number == 1024:
        return color(237, 208, 59)
    elif number == 2048:
        return color(238, 194, 46)
    else:
        return color(255, 255, 255)
    
def reset():

    for j in range(m_size):
        row = []
        for i in range(m_size):
            row.append(0)
        m.append(row)
            
    x = int(random(4))
    y = int(random(4))
    m[x][y] = 2
