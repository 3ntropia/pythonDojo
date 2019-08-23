from pattern import random_pattern, up_down

resolution = 800
m_size = 8
scl = resolution / m_size - 30
spin = 0
option = 0

def setup():
    size(resolution, resolution, P3D)
    #lights()>
    frameRate(2)
    background(0)
            
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
    if option == 0:
        m = random_pattern(m_size)
    elif option == 1:
        m = up_down(m_size, spin)
    elif option == 2:
        m = pattern3(m_size, spin)
    #m = guess(m_size)
    draw_matrix(m)
    spin += 1
    if spin == 9:
        spin = 0
        option += 1
    if option == 3:
        option = 0
    

def pattern3(m_size, spin):
    matrix = []
    for i in range(m_size):
        column = []
        for j in range(m_size):
            row = []
            for h in range(m_size):
                row.append(i - spin == j)
            column.append(row)
        matrix.append(column)
    return matrix

def guess(m_size):
    matrix = []
    for i in range(m_size):
        column = []
        for j in range(m_size):
            row = []
            for h in range(m_size):
                row.append(False)
            column.append(row)
        matrix.append(column)
    matrix[0][0][0] = True
    matrix[0][0][7] = True
    return matrix
