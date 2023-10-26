# Import a library of functions called 'pygame'
from turtle import st
import pygame
import numpy as np
import math

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Point3D:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
		
class Line3D():
	
	def __init__(self, start, end):
		self.start = start
		self.end = end

def loadOBJ(filename):
	
	vertices = []
	indices = []
	lines = []
	
	f = open(filename, "r")
	for line in f:
		t = str.split(line)
		if not t:
			continue
		if t[0] == "v":
			vertices.append(Point3D(float(t[1]),float(t[2]),float(t[3])))
			
		if t[0] == "f":
			for i in range(1,len(t) - 1):
				index1 = int(str.split(t[i],"/")[0])
				index2 = int(str.split(t[i+1],"/")[0])
				indices.append((index1,index2))
			
	f.close()
	
	#Add faces as lines
	for index_pair in indices:
		index1 = index_pair[0]
		index2 = index_pair[1]
		lines.append(Line3D(vertices[index1 - 1],vertices[index2 - 1]))
		
	#Find duplicates
	duplicates = []
	for i in range(len(lines)):
		for j in range(i+1, len(lines)):
			line1 = lines[i]
			line2 = lines[j]
			
			# Case 1 -> Starts match
			if line1.start.x == line2.start.x and line1.start.y == line2.start.y and line1.start.z == line2.start.z:
				if line1.end.x == line2.end.x and line1.end.y == line2.end.y and line1.end.z == line2.end.z:
					duplicates.append(j)
			# Case 2 -> Start matches end
			if line1.start.x == line2.end.x and line1.start.y == line2.end.y and line1.start.z == line2.end.z:
				if line1.end.x == line2.start.x and line1.end.y == line2.start.y and line1.end.z == line2.start.z:
					duplicates.append(j)
					
	duplicates = list(set(duplicates))
	duplicates.sort()
	duplicates = duplicates[::-1]
	
	#Remove duplicates
	for j in range(len(duplicates)):
		del lines[duplicates[j]]
	
	return lines

def loadHouse():
    house = []
    #Floor
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(5, 0, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 0, 5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(-5, 0, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 0, -5)))
    #Ceiling
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 5, -5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(5, 5, 5), Point3D(-5, 5, 5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(-5, 5, -5)))
    #Walls
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(-5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 5, 5)))
    #Door
    house.append(Line3D(Point3D(-1, 0, 5), Point3D(-1, 3, 5)))
    house.append(Line3D(Point3D(-1, 3, 5), Point3D(1, 3, 5)))
    house.append(Line3D(Point3D(1, 3, 5), Point3D(1, 0, 5)))
    #Roof
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(0, 8, -5)))
    house.append(Line3D(Point3D(0, 8, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(0, 8, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(0, 8, -5)))
	
    return house

def loadCar():
    car = []
    #Front Side
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-2, 3, 2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(2, 3, 2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(3, 2, 2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 1, 2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(-3, 1, 2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 2, 2)))

    #Back Side
    car.append(Line3D(Point3D(-3, 2, -2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(-2, 3, -2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, -2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 2, -2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(3, 1, -2), Point3D(-3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, -2), Point3D(-3, 2, -2)))
    
    #Connectors
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-3, 2, -2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 1, -2)))

    return car

def loadTire():
    tire = []
    #Front Side
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-.5, 1, .5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(.5, 1, .5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(1, .5, .5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, -.5, .5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(.5, -1, .5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(-.5, -1, .5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-1, -.5, .5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, .5, .5)))

    #Back Side
    tire.append(Line3D(Point3D(-1, .5, -.5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, -.5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, -.5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, .5, -.5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, -.5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(.5, -1, -.5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, -.5), Point3D(-1, -.5, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, -.5), Point3D(-1, .5, -.5)))

    #Connectors
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-1, .5, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, -.5, -.5)))
    
    return tire
rotate180Matrix = np.array([[-1,0,0,0],
							[0,1,0,0],
							[0,0,-1,0],
							[0,0,0,1]])



carLocation = np.array([[[1,0,0,-20],
						[0,1,0,0],
						[0,0,1,15],
						[0,0,0,1]]])
houseLocations = np.array([
	[[1,0,0,0],
  	 [0,1,0,0],
	 [0,0,1,0],
	 [0,0,0,1]],

	[[1,0,0,20],
  	 [0,1,0,0],
	 [0,0,1,0],
	 [0,0,0,1]],

	[[1,0,0,40],
  	 [0,1,0,0],
	 [0,0,1,0],
	 [0,0,0,1]],

	[[1,0,0,-20],
  	 [0,1,0,0],
	 [0,0,1,0],
	 [0,0,0,1]],
	
#rotated 180
	[[-1,0,0,40],
	 [0,1,0,0],
	 [0,0,-1,30],
	 [0,0,0,1]], 

	[[-1,0,0,20],
	 [0,1,0,0],
	 [0,0,-1,30],
	 [0,0,0,1]],

	[[-1,0,0,0],
	 [0,1,0,0],
	 [0,0,-1,30],
	 [0,0,0,1]],

	[[-1,0,0,-20],
	 [0,1,0,0],
	 [0,0,-1,30],
	 [0,0,0,1]]
])


def toHomogeneous(model):
	list = []
	for line in model:
		list.append(Line3D([line.start.x, line.start.y, line.start.z, 1], [line.end.x, line.end.y, line.end.z, 1]))
	return list

def objectToWorld(model, position):
	list = []
	for pos in position:
		for line in model:
			start = np.matmul(pos, line.start)
			end = np.matmul(pos, line.end)
			list.append(Line3D(start, end))
	
	return list

	
def worldToCamera(model):
	list = []
	translate = np.array([[1,0,0,camX],
					      [0,1,0,camY],
						  [0,0,1,camZ],
						  [0,0,0,1]])
	rotate = np.array([[math.cos(math.degrees(angle)),0,-math.sin(math.degrees(angle)),0],
					   [0,1,0,0],
					   [math.sin(math.degrees(angle)),0,math.cos(math.degrees(angle)),0],
					   [0,0,0,1]])
	for line in model:
		start = np.matmul(translate,line.start)
		start = np.matmul(rotate,start)
		end = np.matmul(translate,line.end)
		end = np.matmul(rotate,end)
		list.append(Line3D(start,end))
	return list
	
def clip(model):
	list = []
	fov = 45
	zoom = 1/math.tan(fov/2)
	f = 1000
	n = .0001
	clipMatrix = np.array([[zoom, 0, 0, 0], [0, zoom, 0, 0], [0, 0, ((f+n)/(f-n)), (-2*(n*f)/(f-n))], [0, 0, 1, 0]])
	##CHECK THIS MATH. IS ZOOM THE SAME? IF NOT, HOW TO SOLVE?
	for line in model:
		start = np.matmul(clipMatrix, line.start)
		end = np.matmul(clipMatrix, line.end)
		wStart = start[3]
		wEnd = end[3]
		xStart = start[0]
		yStart = start[1]
		zStart = start[2]
		xEnd = end[0]
		yEnd = end[1]
		zEnd = end[2]

		if not ((xStart < -wStart and xEnd < -wEnd) or (yStart < -wStart and yEnd < -wEnd) or (zStart < -wStart or zEnd < -wEnd)
		  or (xStart > wStart and xEnd > wEnd) or (yStart > wStart and yEnd > wEnd) or (zStart > wStart and zEnd > wEnd)):
			#doing the normalization here
			newStart = start/wStart
			newEnd = end/wEnd
			list.append(Line3D([newStart[0], newStart[1], 1], [newEnd[0], newEnd[1], 1]))
	return list
		


def toScreenSpace(model):
	list = []
	transformationMatrix = np.array([[256, 0, 256], [0, -256, 256], [0, 0, 1]])
	#np.matmul(transformationMatrix, )
	for line in model:
		start = np.matmul(transformationMatrix, line.start)
		end = np.matmul(transformationMatrix, line.end)
		list.append(Line3D([start[0], start[1]], [end[0], end[1]]))
	return list


def drawHouse(model):
	homogeneous = toHomogeneous(model)
	worldSpace = objectToWorld(homogeneous, houseLocations)
	cameraSpace = worldToCamera(worldSpace)
	clipSpace = clip(cameraSpace)
	screenSpace = toScreenSpace(clipSpace)
	


	for line in screenSpace:
		#BOGUS DRAWING PARAMETERS SO YOU CAN SEE THE HOUSE WHEN YOU START UP
		pygame.draw.line(screen, RED, line.start, line.end)
	
def drawTires(model):
	test = 0

def drawCar(model):
	homogeneous = toHomogeneous(model)
	worldSpace = objectToWorld(homogeneous, carLocation)
	cameraSpace = worldToCamera(worldSpace)
	clipSpace = clip(cameraSpace)
	screenSpace = toScreenSpace(clipSpace)
	for line in screenSpace:
		pygame.draw.line(screen, GREEN, line.start, line.end)



# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Set the height and width of the screen
size = [512, 512]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Shape Drawing")
 
#Set needed variables
done = False
clock = pygame.time.Clock()
start = Point(0.0,0.0)
end = Point(0.0,0.0)
linelist = loadHouse()
carLineList = loadCar()
tireLineList = loadTire()
angle = 0
camX = 0
camY = 0
camZ = 30


#Loop until the user clicks the close button.
while not done:
 
	# This limits the while loop to a max of 100 times per second.
	# Leave this out and we will use all CPU we can.
	clock.tick(100)

	# Clear the screen and set the screen background
	screen.fill(BLACK)

	#Controller Code#
	#####################################################################

	for event in pygame.event.get():
		if event.type == pygame.QUIT: # If user clicked close
			done=True
			
	pressed = pygame.key.get_pressed()

	if pressed[pygame.K_a]:
		camX += math.cos(math.degrees(angle))
		camZ -= math.sin(math.degrees(angle))
	elif pressed[pygame.K_d]:
		camX -= math.cos(math.degrees(angle))
		camZ += math.sin(math.degrees(angle))
	elif pressed[pygame.K_w]:
		camX -= math.sin(math.degrees(angle))
		camZ -= math.cos(math.degrees(angle))
	elif pressed[pygame.K_s]:
		camX += math.sin(math.degrees(angle))
		camZ += math.cos(math.degrees(angle))
	elif pressed[pygame.K_q]:
		angle -= .0005

	elif pressed[pygame.K_e]:
		angle += .0005

	elif pressed[pygame.K_r]:
		camY -= 1
	elif pressed[pygame.K_f]:
		camY += 1
	elif pressed[pygame.K_h]:
		linelist = loadHouse()
		carLineList = loadCar()
		tireLineList = loadTire()
		camX = 0
		camY = 0
		camZ = 30
		angle = 0




	#Viewer Code#
	#####################################################################    

	#for s in linelist:
		#BOGUS DRAWING PARAMETERS SO YOU CAN SEE THE HOUSE WHEN YOU START UP
	#	pygame.draw.line(screen, BLUE, (20*s.start.x+200, -20*s.start.y+200), (20*s.end.x+200, -20*s.end.y+200))
	drawHouse(linelist)
	drawCar(carLineList)

	# Go ahead and update the screen with what we've drawn.
	# This MUST happen after all the other drawing commands.
	pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
