# http://www.pythonchallenge.com/pc/hex/ambiguity.html
# butter/fly

class Runner:
	n, e, s, w = 0, 1, 2, 3
	dir_name = ("north", "east", "south", "west")
	border = (255,255,255,255)

	def __init__(self, maze, position):
		self.position = position
		self.maze = maze
		self.direction = self.s

	def has_wall_to_front(self):
		if self.direction == self.s: return(self.maze.getpixel( (self.position[0], self.position[1]+1) ) == self.border)
		elif self.direction == self.n: return(self.maze.getpixel( (self.position[0], self.position[1]-1) ) == self.border)
		elif self.direction == self.e: return(self.maze.getpixel( (self.position[0]+1, self.position[1]) ) == self.border)
		elif self.direction == self.w: return(self.maze.getpixel( (self.position[0]-1, self.position[1]) ) == self.border)
		else: raise ValueError, "direction"

	def has_wall_to_left(self):
		self.spin_left()
		val = self.has_wall_to_front()
		self.spin_right()
		return val

	def step_forward(self):
		if self.direction == self.s: self.position = (self.position[0], self.position[1]+1)
		elif self.direction == self.n: self.position = (self.position[0], self.position[1]-1)
		elif self.direction == self.e: self.position = (self.position[0]+1, self.position[1])
		elif self.direction == self.w: self.position = (self.position[0]-1, self.position[1])
		else: raise ValueError, "direction"

	def spin_right(self):
		self.direction = (self.direction + 1 ) % 4

	def spin_left(self):
		self.direction = (self.direction + 4 - 1 ) % 4
		
	def __repr__(self):
		return "<%s instance at %d,%d facing %s on color %r>" % (__name__, self.position[0], self.position[1], self.dir_name[self.direction], self.maze.getpixel((self.position[0], self.position[1]) ))
	
	def get_position(self):
		return(self.position)
		
	def get_color(self):
		return(self.maze.getpixel( (self.position[0], self.position[1]) ))

import Image

source = Image.open("data/maze.png")
dest = Image.new(source.mode, source.size)

bottom = source.size[1]-1

reds = []
runner = Runner(source, (source.size[0]-2, 0))
while runner.get_position()[1] != bottom:
	if runner.has_wall_to_left():
		while runner.has_wall_to_front():
			runner.spin_right()
	else:
		runner.spin_left()

	pos = runner.get_position()
	if dest.getpixel(pos) != (1,2,3,4):
		reds.append(runner.get_color()[0])
		dest.putpixel(pos, (1,2,3,4))
	else:
		del reds[-1]
	runner.step_forward()

file("data/24.zip", "w").write("".join( [chr(i) for i in reds][1::2] ))
