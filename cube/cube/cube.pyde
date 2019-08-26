from pattern import random_pattern, up_down, default_matrix, bullets_pattern, lift_pattern
from lift import lift

resolution = 800
m_size = 8
scl = resolution / m_size - 30
spin = 0
option = 3
bullets = []
lift_up = []
lift_down = []
moving = []


def setup():
    size(resolution, resolution, P3D)
    #lights()>
    frameRate(2)
    background(0)
    for x in range(m_size):
        for z in range(m_size):
            if random(0, 1) > .5:
                lift_up.append(lift(x, 0, z, -1))
            else:
                lift_down.append(lift(x, m_size, z, 1))
            
def draw_matrix(matrix):
    for x in range(m_size):
        for y in range(m_size):
            for z in range(m_size):
                bx = x * scl
                by = y * scl
                bz = z * scl
                pushMatrix()
                translate(bx, by, bz)
                stroke(255)
                noFill()
                if matrix[x][y][z]:
                    fill(255, 0, 0)
                else:
                    fill(0)
                box(10)
                popMatrix()
                
def draw():
    translate(20, 0, -200)
    rotateX(-PI/5)
    rotateY(0.9)
    #p = int(random(0,2))
    global option
    global spin
    global lift_up
    global lift_up
    global moving
    if option == 0:
        m = random_pattern(m_size)
    elif option == 1:
        m = up_down(m_size, spin)
        global bullets
        bullets = []
    elif option == 2:
        m = bullets_pattern(m_size, bullets)
    elif option == 3:
        m = lift_pattern(m_size, lift_up, lift_up, moving)
    #m = guess(m_size)
    draw_matrix(m)
    spin += 1
    if spin == 9 and option != 2:
        spin = 0
        option += 1
    elif spin == 20:
        spin = 0
        option += 1
    if option == 4:
        option = 0
    
