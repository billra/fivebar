# Five Bar Parallel SCARA plotter kinematics
# Bill Ola Rasmussen
# version 0.1

class Point:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):
		return "point("+str(self.x)+","+str(self.y)+")"

def main():
	print('Five Bar Kinematics')

	p = Point(3,9)
	print(p)

	print('done.')

if __name__ == "__main__":
	main()

# todo:
# doctest with testfiles
