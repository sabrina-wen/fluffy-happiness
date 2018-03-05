from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix -
	 scale: create a scale matrix,
	    then multiply the transform matrix by the scale matrix -
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix,
	    then multiply the transform matrix by the translation matrix -
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname, "r")
    lines = file.readlines()
    num = 0
    while (num < len(lines)):
        lines[num] = lines[num].strip('\n')
        #print lines[num]
        if (lines[num] == "line"):
            num = num + 1
            new_pts = lines[num].split(' ')
            add_edge(points, float(new_pts[0]), float(new_pts[1]), float(new_pts[2]), float(new_pts[3]), float(new_pts[4]), float(new_pts[5]))
            #print_matrix(points)
        elif (lines[num] == "ident"):
            ident(transform)
            #print_matrix(transform)
        elif (lines[num] == "scale"):
            num = num + 1
            new_pts = lines[num].split(' ')
            scalar_matrix = make_scale(float(new_pts[0]), float(new_pts[1]), float(new_pts[2]))
            matrix_mult(scalar_matrix, transform)
            #print_matrix(transform)
        elif (lines[num] == "move"):
            num = num + 1
            new_pts = lines[num].split(' ')
            translation_matrix = make_translate(float(new_pts[0]), float(new_pts[1]), float(new_pts[2]))
            matrix_mult(translation_matrix, transform)
            #print_matrix(transform)
        elif (lines[num] == "rotate"):
            num = num + 1
            new_pts = lines[num].split(' ')
            if (new_pts[0] == "x"):
                rotate_matrix = make_rotX(math.radians(float(new_pts[1])))
            elif (new_pts[0] == "y"):
                rotate_matrix = make_rotY(math.radians(float(new_pts[1])))
            elif (new_pts[0] == "z"):
                rotate_matrix = make_rotZ(math.radians(float(new_pts[1])))
            matrix_mult(rotate_matrix, transform)
            #print_matrix(transform)
        elif (lines[num] == "apply"):
            matrix_mult(transform, points)
            #print_matrix(points)
        elif (lines[num] == "display"):
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif (lines[num] == "save"):
            num = num + 1
            draw_lines(points, screen, color)
            save_extension(screen, lines[num])
        elif (lines[num] == "quit"):
            return
        num = num + 1
