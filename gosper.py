import turtle

def initialize_turtle(size):
	"""Initialize the turtle to draw the curve"""
	turtle.speed("fastest")
	turtle.width(size//4)
	
	turtle.up()
	turtle.left(90)
	turtle.forward(size*size//2)
	turtle.right(90)
	turtle.down()

def get_rainbow_color_list():
	"""Use HSV to RGB color conversion to get a list of 
	RGB tuples that define a rainbow gradient"""
	
	import numpy as np
	import cv2
	hsv = np.ones((1,180,3), dtype=np.uint8)*255
	hsv[0,:,0] = np.arange(0,180)

	rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
	
	color_list = []
	for r,g,b in rgb[0,:,:]:
		color_list.append((r/256, g/256, b/256))
	
	return color_list

def gosper_curve(order: int, size: int, is_A: bool = True) -> None:
	"""Draw the Gosper curve."""
	global iters, maxiters, color_list
	
	if order == 0:
		turtle.pencolor(color_list[len(color_list)*iters//maxiters])
		turtle.forward(size)
		iters += 1
		return
	for op in "A-B--B+A++AA+B-" if is_A else "+A-BB--B-A++A+B":
		gosper_op_map[op](order - 1, size)

gosper_op_map = {
	"A": lambda o, size: gosper_curve(o, size, True),
	"B": lambda o, size: gosper_curve(o, size, False),
	"-": lambda o, size: turtle.right(60),
	"+": lambda o, size: turtle.left(60),
}
size = 20
order = 3

iters = 0
maxiters = 7**order
color_list = get_rainbow_color_list()

initialize_turtle(size)
gosper_curve(order, size)
turtle.mainloop()