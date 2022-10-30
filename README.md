# matrix_digitizer

## Structure

- `colorbar.py`: defines the colorbar class

- `picker.py`: matplotlib-based script to get the value of a point in an image by just clicking on it

## TODO

- [x] Functions to handle colorbars

- [ ] Samples (image files along with the expected output; we will need these to test the functions we write)

- [ ] Think about the most graceful way to handle masked values. Is it alright to expect the user to manually input them? Or do we not need to worry about masked values at all?

- [x] Graphical way for the user to choose pixels corresponding to the correlation matrix and colorbar?
	
	- <https://stackoverflow.com/questions/28758079/python-how-to-get-coordinates-on-mouse-click-using-matplotlib-canvas>
	
	- <https://stackoverflow.com/questions/5501192/how-to-display-picture-and-get-mouse-click-coordinate-on-it>

- [ ] Is it possible to autodetect the number of entries in the correlation matrix? Or can we just ask the user to input that too?

- [ ] Choose a distance metric for colours. Section 3 of <https://www.researchgate.net/publication/221205971_Distance_measures_in_RGB_and_HSV_color_spaces> lists some commonly used metrics.

- [ ] Decouple colorbar range from colorbar scale
	
	- Currently, one has to input exact values at the top/bottom of the colorbar (or truncate the colour range to between the first and last ticks). This is a problem, since there need not be ticks exactly at the endpoints of the colorbar (see `samples/1.png`). May be better to ask the user to first mark the range of the colorbar with two clicks, and then separately click any two of the ticks (manually inputting the values thereof). A problem is that one may then have to assume something about the orientation of the colorbar. We could of course work around it with a more complicated way of specifying the colorbar position (a draggable line on which ticks can be placed).
