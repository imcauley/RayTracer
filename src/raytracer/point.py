import numpy as np

class Point:
	def __init__(self, vector):
		self.vector = vector
		
		self.normalized = vector / np.linalg.norm(vector)

	def copy(self):
		return Point(np.array(self.vector))

	def __repr__(self) -> str:
		return '(' + str(self.vector[0]) + ', ' + str(self.vector[1]) + ', ' + str(self.vector[2]) + ')'
		
	def unit_vector(self):
		return self.normalized
	
	def translate(self, point):
		self.vector = self.vector - point.vector
		
	def x_rotation(self, theta):
		R = np.array([[1,0,0],[0,np.cos(theta),-np.sin(theta)],[0, np.sin(theta), np.cos(theta)]])
		self.vector = np.dot(R,self.vector)

	def z_rotation(self, theta):
		R = np.array([[np.cos(theta),0,np.sin(theta)],[0,1,0],[-np.sin(theta), 0, np.cos(theta)]])
		self.vector = np.dot(R,self.vector)
	
	def y_rotation(self, theta):
		R = np.array([[np.cos(theta), -np.sin(theta),0],[np.sin(theta), np.cos(theta),0],[0,0,1]])
		self.vector = np.dot(R,self.vector)

	