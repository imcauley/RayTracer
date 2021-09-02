class Ray:
	def __init__(self, origin, direction, time_to_live=20):
		self.origin = origin
		self.direction = direction
		self.time_to_live = time_to_live
	
	def intercepting_point(self, objects):
		closest_point = None
		
		for obj in objects:
			if(point := obj.intersect(self)):
				if(closest_point and point.distance > closest_point.distance):
					closest_point = point
					
		return closest_point