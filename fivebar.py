# Five Bar Parallel SCARA plotter kinematics
# Bill Ola Rasmussen
# version 0.5
import math

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		else:
			return False
	def __str__(self):
		return "point(" + str(self.x) + "," + str(self.y) + ")"
	def towards(self,p2,amt):
		'weighted middle algorithm, amt = 0.5 for middle'
		x = self.x + (p2.x - self.x) * amt
		y = self.y + (p2.y - self.y) * amt
		return Point(x,y)

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

# FiveBar notes:
#	arm singularity: 180 deg angle on arm joint (A or B)
#	tip singularity: 180 deg angle on center joint (C)
class FiveBar:
	'Five bar mechanism, see drawing for variable names'
	def __init__(self,O1,O2,L1,L2,L3,L4b,L4a):
		self.O1,self.O2,self.L1,self.L2,self.L3,self.L4b,self.L4a = O1,O2,L1,L2,L3,L4b,L4a
	def solve(self,D):
		'find O1,O2 angles given point x,y, return empty tuple if impossble'
		# right arm
		Dc = Circle(D,self.L4a + self.L4b)
		O2c = Circle(self.O2,self.L2)
		Bt = O2c.intersect(Dc)
		if(len(Bt) < 2): return () # impossible or (todo) arm singularity
		B = Bt[0] # note: we are selecting the 'turn right' bend, todo: select using parameter
		# left arm
		C = D.towards(B,self.L4a / (self.L4a + self.L4b))
		Cc = Circle(C,self.L3)
		O1c = Circle(self.O1,self.L1)
		At = O1c.intersect(Cc)
		if(len(At) < 2): return () # impossible or (todo) arm singularity
		A = At[0] # note: we are selecting the 'turn right' bend, todo: select using parameter
		return math.atan2(A.y - self.O1.y,A.x - self.O1.x), math.atan2(B.y - self.O2.y,B.x - self.O2.x)

def main():
	print('Five Bar Kinematics')

	# hardcoded setup for test
	O1 = Point(15,0)
	O2 = Point(35,0)
	fb = FiveBar(O1 = O1, O2 = O2, L1 = 10, L2 = 10, L3 = 10, L4b = 10, L4a = 0)

	for y in range(22,-22,-1):
		print()
		for x in range(40):
			if Point(x,y) == O1:
				print('1', end = ' ')
				continue
			if Point(x,y) == O2:
				print('2', end = ' ')
				continue
			res = fb.solve(Point(x,y))
			if(len(res) == 0):
				print('.', end = ' ')
			else:
				print('*', end = ' ')

	print('done.')

if __name__ == "__main__":
	main()
