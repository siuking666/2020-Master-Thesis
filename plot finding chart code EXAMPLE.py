# Code that generates a finding chart from a FITS file and mark/label stars

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
from matplotlib import gridspec
from matplotlib.colors import LogNorm
from matplotlib.patches import ConnectionPatch
from mpl_toolkits.axes_grid1 import ImageGrid
from PIL import Image
import copy

fig = plt.figure(figsize=(12, 12))

########################

image_2010_03_29 = fits.getdata('2010_03_29_mosaic.fits')
image_2010_03_29t = np.sqrt((image_2010_03_29/3e+5)**2) + 1e-20
plt.imshow(image_2010_03_29t, cmap='gray', norm=LogNorm(vmin=0.00005, vmax=.003), origin='lower', interpolation='none')
plt.axis('off')

plt.title('2010.238', fontsize = 25)
plt.plot(162.96-1, 152.43-1, '*', markeredgewidth=1, color='blue', markersize=20)
plt.xlim(112.96000000000001-1, 212.96-1)
plt.ylim(102.43-1, 202.43-1)

plt.scatter(193.14-1, 137.9-1, s=1500, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
plt.annotate('116', xy=(193.14-1, 137.9-1), xytext=(193.14-1+2.5, 137.9-1+-1.5), color='lime', fontsize=15, fontstyle='normal')
plt.scatter(141.1-1, 154.53-1, s=1500, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
plt.annotate('301', xy=(141.1-1, 154.53-1), xytext=(141.1-1+2.5, 154.53-1+-1.5), color='lime', fontsize=15, fontstyle='normal')
plt.scatter(145.74-1, 133.93-1, s=1500, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
plt.annotate('304', xy=(145.74-1, 133.93-1), xytext=(145.74-1+2.5, 133.93-1+-1.5), color='lime', fontsize=15, fontstyle='normal')

plt.annotate('S25', xy=(171.0-1, 121.0-1), xytext=(171.0-1+-1.0, 121.0-1+-0.5), color='red', fontsize=15, fontstyle='normal')
plt.annotate('S7', xy=(125.5-1, 148.0-1), xytext=(125.5-1+-1.0, 148.0-1+-0.5), color='red', fontsize=15, fontstyle='normal')

########################

plt.tight_layout()
plt.subplots_adjust(wspace=-.6, hspace =.2)#,vspace= -.1)
plt.savefig('2010.238 finding chart.png', dpi=500)#, bbox_inches='tight')
plt.show()
plt.close()
