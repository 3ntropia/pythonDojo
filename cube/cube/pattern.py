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
