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

def circle_intersect(x1,y1,r1,x2,y2,r2):
	'Intersection of two cricles, return empty tuple if no or infinite solutions'
	# see: https://stackoverflow.com/a/3349134

	dx = x2 - x1	# distance between circle centers on the x axis
	dy = y2 - y1	# distance between circle centers on the y axis
	dc = math.sqrt(dx ** 2 + dy ** 2)	# distance between circle centers

	if dc > r1 + r2: return () # no solution, circles do not overlap
	if dc < abs(r1 - r2): return () # no solution, one circle contains the other circle
	if dc == 0 and r1 == r2: return () # infinite solutions, circles are coincident

	a = (r1 ** 2 - r2 ** 2 + dc ** 2) / (2 * dc)
	h = math.sqrt(r1 ** 2 - a ** 2)
	xm = x1 + a * dx / dc # middle of the intersection
	ym = y1 + a * dy / dc
	xi1 = xm + h * dy / dc # first intersection point
	yi1 = ym - h * dx / dc
	if h == 0:
		return xi1,yi1 # circles overlap at only one point
	xi2 = xm - h * dy / dc # second intersection point
	yi2 = ym + h * dx / dc
	return xi1,yi1,xi2,yi2

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