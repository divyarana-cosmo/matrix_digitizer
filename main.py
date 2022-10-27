"""
Playground to test various things
"""

import PIL
import matplotlib

def get_cbar_hsv(filename, pixels):
	"""
	Given an image file containing a colorbar and a list of pixels corresponding to the location of the colorbar in that image, return the HSV values of those pixels. For now, we will assume two colours are close if their HSV values are close.
	
	Arguments:
		filename -> str
		pixels -> list of 2-element tuples
	
	Returns:
		hsv -> a list of 3-element RGB tuples
	"""
	rgbs = []
	with PIL.Image.open(filename) as im:
		for pixel in pixels:
			rgb = im.getpixel(pixel) #each element of the tuple (c) satisfies 0 <= c < 256.
			rgbs.append(tuple([c/256 for c in rgb]))
	
	hsv = matplotlib.colors.rgb_to_hsv(rgbs)
	return hsv

def dist(c1, c2):
	"""
	Distance metric to decide if two colours are close
	"""
	c1 = np.array(c1)
	c2 = np.array(c2)
	return np.sqrt(np.sum((c1 - c2)**2))

class colorbar:
	def __init__(self, vals, hsvs, dist):
		"""
		vals: an array containing the axis values of the colorbar
		hsvs: hsv values for the corresponding element in vals
		dist: a 'distance metric' in colour-space that outputs a float given two three-element tuples.
		"""
		self.range = vals
		self.hsvs = hsvs
		self.dist = dist
	
	def match(self, hsv):
		"""
		Given a 3-element tuple (HSV values), return the element of vals that is the closest to it.
		"""
		dists = [ self.dist(hsv, c) for c in self.hsvs ]
		i = np.argmin(dists)
		return self.vals[i]

if __name__ == "__main__":
	"""
	Just some example usage of the above functions for now
	"""
	vals = np.range(0,1,100) #The axis values on the colorbar
	pixels = [(10,i) for i in range(10,110)] #Pixels of the image on which the colorbar is located
	cbar_hsv = get_cbar_hsv("example_colorbar.png", pixels)
	cbar = colorbar(vals, cbar_hsv, dist)
	
	print( cbar.match((0.3,0.3,0.3)) ) #What value corresponds to the colour (0.3,0.3,0.3)?
