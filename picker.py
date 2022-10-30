"""
Script that allows the user to click and pick a value in an image, and then returns the data value corresponding to that point.

"""

from colorbar import get_cbar_hsv, colorbar
import numpy as np
import matplotlib.pyplot as plt
import PIL

class picker():
	def __init__(self, filename):
		self.filename = filename
		self.point = None
		
		self.fig, self.ax = plt.subplots()
		with PIL.Image.open(filename) as img:
			self.im = plt.imshow(img)
	
	def onclick(self, click):
		x = int(np.round(click.xdata))
		y = int(np.round(click.ydata))
		self.point = (x,y)
		plt.show(block=False)
	
	def pick(self):
		cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
		plt.show(block=False)
		return cid
	
	def show(self):
		plt.show(block=False)
	
	def prompt(self, message):
		self.ax.set_title(message)
		plt.show(block=False)
		plt.pause(0.1)
	
	def get_point(self):
		self.point = None
		cid = self.pick()
		while self.point is None:
			plt.pause(0.1)
		self.fig.canvas.mpl_disconnect(cid)
		return self.point

if __name__ == "__main__":
	p = picker("samples/1.png")
	
	p.prompt("click one end of the colorbar")
	cbar_lim_1 = np.array(p.get_point())
	
	p.prompt("click the other end of the colorbar")
	cbar_lim_2 = np.array(p.get_point())
	
	p.prompt("Go to the terminal now") #TODO: This is not actually displayed.
	p.show()
	
	cbar_val_1 = float(input("Input the data value for the first point you clicked: "))
	cbar_val_2 = float(input("Input the data value for the second point you clicked: "))
	
	n = int(np.round(np.sqrt(np.sum((cbar_lim_1 - cbar_lim_2)**2)))) #Number of points to use to represent to colorbar. TODO: Better way to set this?
	cbar_pixels_x = np.linspace(cbar_lim_1[0], cbar_lim_2[0], n,  dtype=int)
	cbar_pixels_y = np.linspace(cbar_lim_1[1], cbar_lim_2[1], n,  dtype=int)
	cbar_pixels = [(cbar_pixels_x[i], cbar_pixels_y[i]) for i in range(n)]
	
	vals = np.linspace(cbar_val_1, cbar_val_2, n)
	cbar_hsv = get_cbar_hsv(p.filename, cbar_pixels)
	cbar = colorbar(vals, cbar_hsv)
	
	print("Go back to the figure window")
	p.prompt("Pick the point whose value you want")
	point = p.get_point()
	
	print("The value corresponding to the point you clicked is between ", cbar.match_range(get_cbar_hsv(p.filename, [point])[0]))
