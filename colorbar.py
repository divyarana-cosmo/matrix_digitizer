"""
Functions to handle a colorbar
"""

import numpy as np
import PIL
import matplotlib

def get_cbar_hsv(filename, pixels):
	"""
	Given an image file containing a colorbar and a list of pixels corresponding to the location of the colorbar in that image, return the HSV values of those pixels.
	
	Arguments:
		filename -> str
		pixels -> list of 2-element tuples
	
	Returns:
		hsv -> a list of 3-element RGB tuples
	"""
	hsvs = []
	with PIL.Image.open(filename) as im:
		for pixel in pixels:
			hsvs.append( get_im_hsv(im, pixel) )
	return hsvs

def get_im_hsv(im, pixel):
	"""
	Arguments
		Im: PIL.Image.Image
		pixel: 2-element tuple
	
	Returns
		hsv: 3-element tuple
	"""
	rgb = im.getpixel(pixel) #each element of the tuple (c) satisfies 0 <= c < 256.
	rgb = tuple([c/256 for c in rgb])
	hsv = matplotlib.colors.rgb_to_hsv(rgb)
	return hsv

def dist(c1, c2):
	"""
	Distance metric to decide if two colours are close
	"""
	c1 = np.array(c1)
	c2 = np.array(c2)
	return np.sqrt(np.sum((c1 - c2)**2))

class colorbar:
	def __init__(self, vals, hsvs, dist=dist):
		"""
		vals: an array containing the axis values of the colorbar
		hsvs: hsv values for the corresponding element in vals
		dist: a 'distance metric' in colour-space that outputs a float given two three-element tuples.
		"""
		self.vals = vals
		self.hsvs = hsvs
		self.dist = dist
	
	def match(self, hsv):
		"""
		Given a 3-element tuple (HSV values), return the element of vals that is the closest to it.
		If multiple values are consistent with the same colour (e.g. a colorbar with a small number of levels), the smallest among them will be returned.
		"""
		dists = [ self.dist(hsv, c) for c in self.hsvs ]
		i = np.argmin(dists)
		return self.vals[i]
	
	def match_range(self, hsv):
		"""
		Given a 3-element tuple (HSV values), return the range of vals that is consistent with it (as a tuple).
		"""
		dists = [ self.dist(hsv, c) for c in self.hsvs ]
		min_d = np.min(dists)
		inds = np.nonzero(dists == min_d) #return indices where dist is the same as the minimum distance
		vals = self.vals[inds]
		return (np.min(vals), np.max(vals))

if __name__ == "__main__":
	"""
	Just some example usage of the above functions for now
	"""
	pixels = [(19,i) for i in range(19,441)] #Pixels of the image on which the colorbar is located
	vals = np.linspace(1,-6,len(pixels)) #The axis values on the colorbar
	cbar_hsv = get_cbar_hsv("samples/1.png", pixels)
	cbar = colorbar(vals, cbar_hsv, dist)
	
	print("Colour at pixel 342: ", cbar_hsv[342-19])
	print("Value corresponding to the given colour: ", cbar.match((0.59689922, 0.60992908, 0.55078125)) ) #Should be between -4.2 and -4.4 for this colour
	print("Range of values corresponding to the given colour: ", cbar.match_range((0.59689922, 0.60992908, 0.55078125)) )
