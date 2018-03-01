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
    id[0][0] = math.cos(theta)
    id[0][1] = -1 * math.sin(theta)
    id[1][0] = math.sin(theta)
    id[1][1] = math.cos(theta)
    return id

def make_rotY( theta ):
    id = new_matrix()
    ident(id)
    id[1][0] = math.cos(theta)
    id[1][1] = -1 * math.sin(theta)
    id[2][0] = math.sin(theta)
    id[2][1] = math.cos(theta)
    return id

def make_rotZ( theta ):
    id = new_matrix()
    ident(id)
    id[2][0] = math.cos(theta)
    id[2][1] = -1 * math.sin(theta)
    id[3][0] = math.sin(theta)
    id[3][1] = math.cos(theta)
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

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for r in range( rows ):
        m.append( [] )
        for c in range( cols ):
            m[r].append( 0 )
    return m
