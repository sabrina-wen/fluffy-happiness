from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = new_matrix()
transform = new_matrix()

#print_matrix(transform)
parse_file( 'script', edges, transform, screen, color )
#print_matrix(transform)
