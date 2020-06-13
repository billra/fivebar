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

	def intersect(self,c2):
		'Intersection of two circles, return empty tuple if no or infinite solutions'
		# see: https://stackoverflow.com/a/3349134
	
		dx = c2.center.x - self.center.x	# distance between circle centers on the x axis
		dy = c2.center.y - self.center.y	# distance between circle centers on the y axis
		dc = math.sqrt(dx ** 2 + dy ** 2)	# distance between circle centers
	
		if dc > self.radius + c2.radius: return () # no solution, circles do not overlap
		if dc < abs(self.radius - c2.radius): return () # no solution, one circle contains the other circle
		if dc == 0 and self.radius == c2.radius: return () # infinite solutions, circles are coincident
	
		a = (self.radius ** 2 - c2.radius ** 2 + dc ** 2) / (2 * dc)
		h = math.sqrt(self.radius ** 2 - a ** 2)
		xm = self.center.x + a * dx / dc # middle of the intersection
		ym = self.center.y + a * dy / dc
		xi1 = xm + h * dy / dc # first intersection point
		yi1 = ym - h * dx / dc
		if h == 0:
			return Point(xi1,yi1), # circles overlap at only one point (note: single element tuple)
		xi2 = xm - h * dy / dc # second intersection point
		yi2 = ym + h * dx / dc
		return Point(xi1,yi1),Point(xi2,yi2)

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