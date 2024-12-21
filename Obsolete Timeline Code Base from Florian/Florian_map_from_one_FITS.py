# Code that generates a progressive timeline map from FITS files and given positions

## Check the dirty code from the original code for more options

# Wish List:
# Brightness of every subplots
# Still need Sgr A* in the image
# Date needs displayed
# Name label of the object?
# Orbit trajectury?

########################

# Copied from 2 other reference code from Florian; might not need all.
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cm as cm
import matplotlib.image as mpimg
import matplotlib.patches as patches
from matplotlib.colors import LogNorm
from matplotlib.patches import ConnectionPatch
from astropy.utils.data import download_file
from astropy.io import fits
from pylab import *
from optparse import OptionParser
from mpl_toolkits.axes_grid1 import ImageGrid
from PIL import Image
import copy


########################
#copy paste for every additional FITS images

# import the FITS file
image_data_1 = fits.getdata('2016_03_23.fits')

print(type(image_data_1))
# class numpy.ndarray

print(image_data_1.shape)
# pixel size of image

########################
########################
########################
# Functional stuff from singular plot code

# matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs
# Create a new figure.
# This should create the blank master file
fig = plt.figure()


# matplotlib.pyplot.subplot(*args, **kwargs)
# Add a subplot to the current figure.
# *args: Either a 3-digit integer or three separate integers describing the position of the subplot. (row column index)
# increasing the numbers made the subplot much smaller
# this sets the position of the subplot on the master image
ax0 = fig.add_subplot(111) 

# set title for subplot
ax0.set_title('L\' continuum, NACO')

# This math operation sets the brightness/contrast of FITS image and save it to another variable
image_data_1a = image_data_1/np.max(image_data_1)

# Axes.scatter(self, x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, *, plotnonfinite=False, data=None, **kwargs)
# A scatter plot of y vs x with varying marker size and/or color.
# This sets the white circle pointer, and x, y, shape...etc
ax0.scatter(864., 810, s=2500, facecolors='none', color='white', linewidth=1, linestyle='dashed')

# matplotlib.pyplot.imshow(X, cmap=None, norm=None, aspect=None, interpolation=None, alpha=None, vmin=None, vmax=None, origin=None, extent=None, shape=<deprecated parameter>, filternorm=1, filterrad=4.0, imlim=<deprecated parameter>, resample=None, url=None, *, data=None, **kwargs)
# Display an image, i.e. data on a 2D regular raster.
# This sets the properties of the subplot, cmap=colormap, vmin/vmax=scalar (range that colormap covers), extent=filled size
ax0.imshow(image_data_1a, cmap='afmhot', vmin=.0, vmax=.015, origin='lower', interpolation='none', extent=[0,1167,0,1170]) 

# Axes.tick_params(self, axis='both', **kwargs)
# Change the appearance of ticks, tick labels, and gridlines.
ax0.tick_params(
    axis='both',          # Which axis to apply the parameters to.
    which='both',      # apply arguments to which ticks.
    bottom= False ,      # ticks along the bottom edge are off
    top= False ,         # ticks along the top edge are off
    labelbottom= False, # labels along the bottom edge are off
right= False, left= False, labelleft= False)


# class matplotlib.spines.Spine(axes, spine_type, path, **kwargs)[source]
# An axis spine -- the line noting the data area boundaries.
ax0.spines['top'].set_visible(False)
ax0.spines['right'].set_visible(False)
ax0.spines['bottom'].set_visible(False)
ax0.spines['left'].set_visible(False)


# Axes.set_xlim(self, left=None, right=None, emit=True, auto=False, *, xmin=None, xmax=None)
# Set the x/y-axis view limits.
# The white circle does not auto-scale with this!!
ax0.set_xlim(788, 900)
ax0.set_ylim(765, 856)

########################

# No need to change these

# This module provides routines to adjust subplot params so that subplots are nicely fit in the figure. In doing so, only axis labels, tick labels, axes titles and offsetboxes that are anchored to axes are currently considered.
plt.tight_layout()
# Save the current figure.
plt.savefig('X7_2016_NACO.png', dpi=600, bbox_inches='tight')
# Display it
plt.show()
# Close it
plt.close()

