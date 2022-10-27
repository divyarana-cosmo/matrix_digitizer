# matrix_digitizer

## TODO
- [x] Functions to handle colorbars

- [ ] Samples (image files along with the expected output; we will need these to test the functions we write)

- [ ] Think about the most graceful way to handle masked values. Is it alright to expect the user to manually input them? Or do we not need to worry about masked values at all?

- [ ] Graphical way for the user to choose pixels corresponding to the correlation matrix and colorbar?
	
	- <https://stackoverflow.com/questions/28758079/python-how-to-get-coordinates-on-mouse-click-using-matplotlib-canvas>
	
	- <https://stackoverflow.com/questions/5501192/how-to-display-picture-and-get-mouse-click-coordinate-on-it>

- [ ] Is it possible to autodetect the number of entries in the correlation matrix? Or can we just ask the user to input that too?

- [ ] Choose a distance metric for colours. Section 3 of <https://www.researchgate.net/publication/221205971_Distance_measures_in_RGB_and_HSV_color_spaces> lists some commonly used metrics.
