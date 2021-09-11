class Scene:
	def __init__(self, camera):
		self.camera = camera
		self.objects = []
		self.lights = []
		
	def add_object(self, obj):
		self.objects.append(obj)
		
	def add_light(self, light):
		self.lights.append(light)
		
	def create_image(self):
		self.camera.create_rays()