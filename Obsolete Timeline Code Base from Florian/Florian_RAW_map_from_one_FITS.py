import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import ConnectionPatch
from astropy.io import fits
from matplotlib.colors import LogNorm
import copy



image_data_1 = fits.getdata('2016_03_23.fits')

print(type(image_data_1))
print(image_data_1.shape)


fig = plt.figure()

ax0 = fig.add_subplot(111) #u'2.1609$\mu$m'

#ax0.set_title(u'Br$\gamma$-line map')
ax0.set_title('L\' continuum, NACO')

#levels0=[0.5]
#levels1=[.525,0.565,0.65,0.75]

#ax0.contour(image_data_1,levels0, colors='skyblue', linewidths=1, origin='lower', extent=[0,101,0,101])
#ax0.contour(image_data_1,levels1, colors='lime', linewidths=1, origin='lower', extent=[0,101,0,101])

image_data_1a = image_data_1/np.max(image_data_1)


#ax0.plot(54, 67, "wx", markeredgewidth=2, color='lightblue',markersize=10)

#x = 'blue'

#y = 'lime'

#ax0.arrow(280, 90, 10, -10, head_width=4, head_length=5, fc= x, ec= x)
#ax0.arrow(260, 100, -10, -10, head_width=4, head_length=5, fc= x, ec= x)
#ax0.arrow(220, 100, -10, -10, head_width=4, head_length=5, fc= x, ec= x)

# Create a Rectangle patch
#rect = patches.Rectangle((75,30),19,15,linewidth=1,edgecolor='lime',facecolor='none')  #94 45

# Add the patch to the Axes
#ax0.add_patch(rect)


ax0.scatter(864., 810, s=2500, facecolors='none', color='white', linewidth=1, linestyle='dashed') # naco_gg
ax0.imshow(image_data_1a, cmap='afmhot', vmin=.0, vmax=.015, origin='lower', interpolation='none', extent=[0,1167,0,1170]) 



#ellipse0 = Ellipse(xy=(62, 69), width=80., height=32., angle=70,edgecolor='white', fc='None', lw=2)

#ax0.add_patch(ellipse0)

#ellipse1 = Ellipse(xy=(105, 61), width=55., height=30., angle=10,edgecolor='white', fc='None', lw=2)

#ax0.add_patch(ellipse1)

#ax0.text(24.0, 14.0, '0".2', color='white', size=14)

#ax0.plot([25, 45], [12.5, 12.5], color='white')

#ax0.text(160.0, 100.0, 'North', color='white', size=15)

#ax0.text(6., 53.0, 'East', color='white', size=15)

ax0.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom= False ,      # ticks along the bottom edge are off
    top= False ,         # ticks along the top edge are off
    labelbottom= False, # labels along the bottom edge are off
right= False, left= False, labelleft= False)

ax0.spines['top'].set_visible(False)
ax0.spines['right'].set_visible(False)
ax0.spines['bottom'].set_visible(False)
ax0.spines['left'].set_visible(False)

ax0.set_xlim(788, 900)
ax0.set_ylim(765, 856)

###################################################################################
plt.tight_layout()
plt.savefig('X7_2016_NACO.png', dpi=600, bbox_inches='tight')
plt.show()
plt.close()
