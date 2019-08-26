def random_pattern(m_size):
    matrix = []
    for h in range(m_size):
        column = []
        for i in range(m_size):
            row = []
            for j in range(m_size):
                row.append(int(random(0,2)) == 0)
            column.append(row)
        matrix.append(column)
    return matrix

def up_down(m_size, spin):
    matrix = []
    for h in range(m_size):
        column = []
        for i in range(m_size):
            row = []
            for j in range(m_size):
                row.append(spin == j)
            column.append(row)
        matrix.append(column)
    return matrix

def default_matrix(m_size):
    matrix = []
    for x in range(m_size):
        column = []
        for y in range(m_size):
            row = []
            for z in range(m_size):
                row.append(False)
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

def bullets_pattern(m_size, bullets):
    bullet = generate_bullet(m_size)
    bullets.append(bullet)
    if 1 < random(0, 4):
        bullet = generate_bullet(m_size)
        bullets.append(bullet)
    matrix = default_matrix(m_size)
    for b in bullets:
        matrix[b[0]][b[1]][b[2]] = True
        b[0] = b[0] + 1
        if b[0] == m_size:
            bullets.remove(b)
    return matrix

def generate_bullet(m_size):
    x = int(random(0, m_size))
    z = int(random(0, m_size))
    return [0, y, z]

def lift_pattern(m_size, lift_up, lift_down, moving):
    if len(moving) == 0:
        lu, lift_up = pick_lift(lift_up)
        ld, lift_down = pick_lift(lift_down)
        #lu.print_lift()
        #ld.print_lift()
        moving.append(lu)
        moving.append(ld)
    matrix = default_matrix(m_size)
    for l in lift_up:
        matrix[l.x][l.y][l.z] = True
    for l in lift_down:
        matrix[l.x][l.y][l.z] = True
    for l in moving:
        matrix[l.x][l.y][l.z] = True
        l.y += l.d
        #print('l.y: ' + str(l.y))
        if l.y == m_size -1:
            moving.remove(l)
            lift_down.append(l)
            l.d = -1
        elif l.y == 0:
            moving.remove(l)
            lift_up.append(l)
            l.d = 1
    #print('pre len moving: ' + str(len(moving)))
    return matrix, lift_up, lift_down, moving
    
def pick_lift(lift_list):
    n = int(random(len(lift_list)))
    l = lift_list[n]
    lift_list.remove(l)
    return l, lift_list
