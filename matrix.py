import math

def make_translate( x, y, z ):
    id = new_matrix()
    ident(id)
    id[0][3] = x
    id[1][3] = y
    id[2][3] = z
    return id

def make_scale( x, y, z ):
    id = new_matrix()
    ident(id)
    id[0][0] = x
    id[1][1] = y
    id[2][2] = z
    return id

def make_rotX( theta ):
    id = new_matrix()
    ident(id)
    id[1][1] = math.cos(theta)
    id[1][2] = -1 * math.sin(theta)
    id[2][1] = math.sin(theta)
    id[2][2] = math.cos(theta)
    return id

def make_rotY( theta ):
    id = new_matrix()
    ident(id)
    id[0][0] = math.cos(theta)
    id[0][2] = math.sin(theta)
    id[2][0] = -1 * math.sin(theta)
    id[2][2] = math.cos(theta)
    return id

def make_rotZ( theta ):
    id = new_matrix()
    ident(id)
    id[0][0] = math.cos(theta)
    id[0][1] = -1 * math.sin(theta)
    id[1][0] = math.sin(theta)
    id[1][1] = math.cos(theta)
    return id

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix ) ):
        for c in range( len(matrix[0]) ):
            s+= str(matrix[r][c]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix ) ):
        for c in range( len(matrix[0]) ):
            if r == c:
                matrix[r][c] = 1
            else:
                matrix[r][c] = 0

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    # init variables
    curr_col = 0
    curr_row = 0
    # convert each col in m2 into a 1d array, dot product w/ each row in m1
    while (curr_col < len(m2[0]) and curr_row < len(m2)):
        #print "current coordinate is: (" + str(curr_row) + ", " + str(curr_col) + ")"
        sum = 0
        for r in range(len(m2)):
            sum += m2[r][curr_col] * m1[curr_row][r]
        m2[curr_row][curr_col] = sum
        if (curr_col != len(m2[0]) - 1):
            curr_col = curr_col + 1
        else:
            curr_col = 0
            curr_row = curr_row + 1
    return m2

def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m
