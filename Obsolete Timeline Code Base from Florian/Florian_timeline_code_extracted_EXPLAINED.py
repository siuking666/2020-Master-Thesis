# Code that generates a progressive timeline map from FITS files and given positions

## Check the dirty code from the original code for more options (ie: Arrow/Cross/Circle/Square)

# Wish List:
# Need Sgr A* marked and aligned in the images (center the crop at Sag A's coordinates)
# Standardizing the displayed region of every subplots (Use a formula, dummy variables to take the radius from Sag A)
# Tuning the Brightness/Contrast of every subplots (refer to QFitsView screenshots)
# Date needs displayed
# Name label of the object? (Optional, captions might work)
# Orbit trajectury? (Optional, good to have)

########################

# Copied from 2 other reference code from Florian; might not need all.
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cm as cm
import matplotlib.image as mpimg
import matplotlib.patches as patches
from astropy.utils.data import download_file
from astropy.io import fits
from pylab import *
from optparse import OptionParser
from matplotlib.colors import LogNorm
from matplotlib.patches import ConnectionPatch
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


#copy paste these 3 lines for every FITS images

image_data_2 = fits.getdata('2005_naco_gggg.fits')
print(type(image_data_2))
print(image_data_2.shape)

image_data_3 = fits.getdata('2006_a.fits')
print(type(image_data_3))
print(image_data_3.shape)


# matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs
# Create a new figure.
# This should create the blank master file
fig = plt.figure()

########################
########################
########################

# WTF IS THIS?! dummy-variables that are referred to below...
a = [0,301,0,301]
b = 14
c = 'white'

# Dummy variables used below of Coordinates on the image 
aaa1 = 145 # delta x = 33 = 2*16.5
aaa2 = 178
bbb1 = 160 # delta y = 28 = 2*14
bbb2 = 188

########################

# matplotlib.pyplot.subplot(*args, **kwargs)
# Add a subplot to the current figure.
# *args: Either a 3-digit integer or three separate integers describing the position of the subplot. (row column index)
# increasing the numbers made the subplot much smaller
# this sets the position of the subplot on the master image
ax1 = fig.add_subplot(431)

# set title for subplot
ax0.set_title('L\' continuum, NACO')

# Add the date
ax1.text(147.0+6.43, 162.0, '2004', color='white', size=14)

# This math operation sets the brightness/contrast of FITS image and save it to another variable
image_data_10t = np.sqrt((image_data_1/1.997e+5)**2)
image_data_10 = image_data_10t + image_data_10t[145:146,176:177]

# Add the Sgr A cross & circle markers 
# Axes.scatter(self, x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, *, plotnonfinite=False, data=None, **kwargs)
# A scatter plot of y vs x with varying marker size and/or color.
# This sets the white circle pointer, and x, y, shape...etc
ax1.plot(165+2.48, 183-9, "wx", markeredgewidth=2, color='white',markersize= b) 
ax1.scatter(172.5, 178, s=350, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax1.scatter(161.75, 176.75, s=350, facecolors='none', color= c, linewidth=1, linestyle='dashed') # naco_gg

# matplotlib.pyplot.imshow(X, cmap=None, norm=None, aspect=None, interpolation=None, alpha=None, vmin=None, vmax=None, origin=None, extent=None, shape=<deprecated parameter>, filternorm=1, filterrad=4.0, imlim=<deprecated parameter>, resample=None, url=None, *, data=None, **kwargs)
# Display an image, i.e. data on a 2D regular raster.
# This sets the properties of the subplot, cmap=colormap, vmin/vmax=scalar (range that colormap covers), extent=filled size
ax1.imshow(image_data_10, cmap='hot', norm=LogNorm(vmin=0.00025, vmax=.35), origin='lower', interpolation='none', extent=a)
## OR ax0.imshow(image_data_1a, cmap='afmhot', vmin=.0, vmax=.015, origin='lower', interpolation='none', extent=[0,1167,0,1170]) 
ax1.axis('off')

## COPIED OVER. Not sure if we need this
# Axes.tick_params(self, axis='both', **kwargs)
# Change the appearance of ticks, tick labels, and gridlines.
ax0.tick_params(
    axis='both',          # Which axis to apply the parameters to.
    which='both',      # apply arguments to which ticks.
    bottom= False ,      # ticks along the bottom edge are off
    top= False ,         # ticks along the top edge are off
    labelbottom= False, # labels along the bottom edge are off
right= False, left= False, labelleft= False)

## COPIED OVER. Not sure if we need this
# class matplotlib.spines.Spine(axes, spine_type, path, **kwargs)[source]
# An axis spine -- the line noting the data area boundaries.
ax0.spines['top'].set_visible(False)
ax0.spines['right'].set_visible(False)
ax0.spines['bottom'].set_visible(False)
ax0.spines['left'].set_visible(False)

# Axes.set_xlim(self, left=None, right=None, emit=True, auto=False, *, xmin=None, xmax=None)
# Set the x/y-axis view limits.
# The white circle does not auto-scale with this!!
plt.xlim(aaa1+6.43,aaa2+6.43)  #center 161.5
plt.ylim(bbb1,bbb2)  #center 174

########################

ax2 = fig.add_subplot(432)
ax2.text(147.0+5.45, 162.0-1.37, '2005', color='white', size=14)
ax2.plot(165+1.95, 183-10.37, "wx", markeredgewidth=2, color='white',markersize= b)
ax2.scatter(171., 177.5, s=350, facecolors='none', color='lime', linewidth=1, linestyle='dashed') # naco_gg
ax2.scatter(161.75, 176.75, s=350, facecolors='none', color=c, linewidth=1, linestyle='dashed') # naco_gg

image_data_20 = image_data_2/9.77356     # naco_gggg

ax2.imshow(image_data_20, cmap='hot', vmin=0.065, vmax=.3 , origin='lower', interpolation='none', extent=a)
ax2.axis('off')

plt.xlim(aaa1+5.45,aaa2+5.45)  #center 161.5
plt.ylim(bbb1-1.37,bbb2-1.37)  #center 174

# repeat this section for as many more sources 

########################

# No need to change these

# This module provides routines to adjust subplot params so that subplots are nicely fit in the figure. In doing so, only axis labels, tick labels, axes titles and offsetboxes that are anchored to axes are currently considered.
plt.tight_layout()

#Tune the subplot layout.
plt.subplots_adjust(wspace=-.6, hspace =.1)#,vspace= -.1)

# Save the current figure.
plt.savefig('overview_s4711_all.png', dpi=600)#, bbox_inches='tight')

# Display it
plt.show()

# Close it
plt.close()

