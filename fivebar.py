# Five Bar Parallel SCARA plotter kinematics
# Bill Ola Rasmussen
# version 0.1

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __str__(self):
		return "point(" + str(self.x) + "," + str(self.y) + ")"

class Circle:
	def __init__(self,center,radius):
		self.center = center
		self.radius = radius
	def __str__(self):
		return "circle(" + str(self.center) + "," + str(self.radius) + ")"

def main():
	print('Five Bar Kinematics')

	p = Point(3,9)
	print(p)

	c = Circle(Point(5,2),8)
	print(c)

	print('done.')

if __name__ == "__main__":
	main()

# todo:

# intersection of two circles: https://stackoverflow.com/a/3349134