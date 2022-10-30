"""
Script that allows the user to click and pick a value in an image, and then returns the data value corresponding to that point.
"""

from colorbar import get_cbar_hsv, get_im_hsv, colorbar
import numpy as np
import matplotlib.pyplot as plt
import PIL

class picker():
	def __init__(self, filename):
		self.filename = filename
		self.im = PIL.Image.open(filename)
		
		self.point = None
		self._dt = 0.1 #How long to wait for event loop to run etc.
		
		self.fig, self.ax = plt.subplots()
		self.imshow = plt.imshow(self.im)
		self.ax.set_xticks([])
		self.ax.set_yticks([])
	
	def onclick(self, click):
		x = int(np.round(click.xdata))
		y = int(np.round(click.ydata))
		self.point = (x,y)
		self.show()
	
	def pick(self):
		cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
		self.show()
		return cid
	
	def show(self):
		plt.show(block=False)
	
	def prompt(self, message):
		self.ax.set_title(message)
		self.show()
		plt.pause(self._dt)
	
	def get_point(self, message=None):
		if message is not None:
			self.prompt(message)
		self.point = None
		cid = self.pick()
		while self.point is None:
			plt.pause(self._dt)
		self.fig.canvas.mpl_disconnect(cid)
		return self.point

if __name__ == "__main__":
	try:
		filename = input("Enter the path to the image. Ctrl+D for default (samples/1.png): ")
	except EOFError:
		filename = "samples/1.png"
		print("\nUsing default.\n")
	
	p = picker(filename)
	
	cbar_lim_1 = np.array(p.get_point("Click one end of the colorbar"))
	
	cbar_lim_2 = np.array(p.get_point("Click the other end of the colorbar"))
	
	p.prompt("Go to the terminal now")
	
	cbar_val_1 = float(input("Input the data value for the first point you clicked: "))
	cbar_val_2 = float(input("Input the data value for the second point you clicked: "))
	
	n = int(np.round(np.sqrt(np.sum((cbar_lim_1 - cbar_lim_2)**2)))) #Number of points to use to represent to colorbar.
	cbar_pixels_x = np.linspace(cbar_lim_1[0], cbar_lim_2[0], n,  dtype=int)
	cbar_pixels_y = np.linspace(cbar_lim_1[1], cbar_lim_2[1], n,  dtype=int)
	cbar_pixels = [(cbar_pixels_x[i], cbar_pixels_y[i]) for i in range(n)]
	
	vals = np.linspace(cbar_val_1, cbar_val_2, n)
	cbar_hsv = get_cbar_hsv(p.filename, cbar_pixels)
	cbar = colorbar(vals, cbar_hsv)
	
	print("Go back to the figure window")
	point = p.get_point("Pick the point whose value you want")
	
	print("\nThe value corresponding to the point you clicked is between ", cbar.match_range(get_im_hsv(p.im, point)))
