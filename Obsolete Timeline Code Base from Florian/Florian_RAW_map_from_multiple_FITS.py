import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cm as cm
import matplotlib.image as mpimg
from PIL import Image
from astropy.utils.data import download_file
from astropy.io import fits
from pylab import *
from optparse import OptionParser
from matplotlib.colors import LogNorm
from mpl_toolkits.axes_grid1 import ImageGrid
from PIL import Image


#data = np.loadtxt("plot_me.dat")
#x,y=np.loadtxt("plot_me.dat",unpack=True) #thanks warren!
#x,y =  zip(*data)
#plot.plot(x, y, linewidth=2.0)

#image_data_1a = fits.getdata('2013_naco.fits')
#image_data_1b = fits.getdata('2002_naco.fits')
#image_data_1b = fits.getdata('2002_naco_gg.fits')
#image_data_1b = fits.getdata('2002_naco_gggg.fits')
#image_data_1c = fits.getdata('2003_naco.fits')


image_data_1 = fits.getdata('2004_naco_f.fits')
#image_data_2 = fits.getdata('2005_naco_b.fits')
image_data_2 = fits.getdata('2005_naco_gggg.fits')
#image_data_3 = fits.getdata('2006_naco.fits') 2006_naco = 2006_d
image_data_3 = fits.getdata('2006_a.fits')
image_data_4 = fits.getdata('2006_b.fits')
image_data_5 = fits.getdata('2006_c.fits')
image_data_6 = fits.getdata('2006_d.fits')
  
image_data_7 = fits.getdata('2007_naco_a.fits')
image_data_8 = fits.getdata('2007_naco_b.fits')
image_data_9 = fits.getdata('2007_naco_c.fits')
image_data_10 = fits.getdata('2007_naco_d.fits')

image_data_11 = fits.getdata('2008_naco.fits')
#image_data_6 = fits.getdata('2009_naco.fits')


image_data_12 = fits.getdata('2010_naco_a.fits')
#image_data_8 = fits.getdata('2011_naco.fits')
#image_data_9 = fits.getdata('2012_naco.fits')


print(type(image_data_1))
print(image_data_1.shape)

print(type(image_data_2))
print(image_data_2.shape)

print(type(image_data_3))
print(image_data_3.shape)

print(type(image_data_4))
print(image_data_4.shape)

print(type(image_data_5))
print(image_data_5.shape)

#print(type(image_data_6))
#print(image_data_6.shape)

print(type(image_data_7))
print(image_data_7.shape)

#print(type(image_data_8))
#print(image_data_8.shape)
#
#print(type(image_data_9))
#print(image_data_9.shape)


fig = plt.figure()
########################
a = [0,301,0,301]
b = 14
c = 'white'
#########################################################################
#ax1a = fig.add_subplot(431)
#######
#ax1a.text(147.0+4, 162.0, '133 mas', color='black', size=8)
#ax1a.plot([149+4, 159+4], [161, 161], color='black')
#
#ax1a.arrow(165, 170, -10 , 0, head_width=2, head_length=4, fc= 'black', ec= 'black')
#ax1a.arrow(165, 170, 0 , 10, head_width=2, head_length=4, fc= 'black', ec= 'black')
#
#ax1a.text(150.0, 172.0, 'East', color='black', size=8)
#ax1a.text(154.0, 182.0, 'North', color='black', size=8)
#
#######
#image_data_10a = np.sqrt(image_data_1a**2)/4239.16 # Normalize it
#
#image_data_100a = image_data_10a-image_data_10a
#
#ax1a.imshow(image_data_100a, cmap='hot', norm=LogNorm(vmin=0.002, vmax=.4), origin='lower', interpolation='none', extent=a)
#
#ax1a.text(62.0, 23.5, 'X8', color='white', size=14)
#
#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
#
#ax1a.spines['top'].set_visible(False)
#ax1a.spines['right'].set_visible(False)
#ax1a.spines['bottom'].set_visible(False)
#ax1a.spines['left'].set_visible(False)
#
#plt.xlim(145,178)
#plt.ylim(160,188)
#########################################################################
aaa1 = 145 # delta x = 33 = 2*16.5
aaa2 = 178
bbb1 = 160 # delta y = 28 = 2*14
bbb2 = 188
######################################################################### 2002
#ax1b = fig.add_subplot(431)
#ax1b.text(147.0+6.43, 162.0+7.43, '2002', color='white', size=14)
#ax1b.plot(165+2.93, 183-1.57, "wx", markeredgewidth=2, color='black',markersize= b) 
##ax1b.plot(165+2.93, 183-5.26, "wx", markeredgewidth=2, color='white',markersize= b) #corrected 2006 SgrA* position
##ax1b.scatter(172.5, 179., s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
##ax1b.scatter(168.5, 186.5, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')  #2002_naco_f
#ax1b.scatter(171, 185.5, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')    #2002_naco_gg & 2002_naco_ggg
##ax1b.scatter(169.6, 181.0, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
#
#plt.ylabel('East', size=14)
#
#ax1b.set_title('North')
#
##ax1b.text(145.0+6.43, 182.0+3.74, '133 mas', color='white', size=8)
##ax1b.plot([147+6.43, 157+6.43], [181+3.74, 181+3.74], color='white')
#
##image_data_10b = np.sqrt(image_data_1b**2)/4239.16 # Normalize it
##image_data_10b = np.sqrt(image_data_1b**2)/757003 # Normalize it
##image_data_10b = np.sqrt(image_data_1b**2)/4902.04 # Normalize it
##image_data_10b = np.sqrt(image_data_1b**2)/13.7772 # Normalize it 2002_naco_gg
##image_data_10b = np.sqrt(image_data_1b**2)/757003 # Normalize it 2002_naco_f
##image_data_10b = np.sqrt(image_data_1b**2)/14.37 # Normalize it 2002_naco_ggg
#image_data_10b = np.sqrt(image_data_1b**2)/8.24616 # Normalize it 2002_naco_gggg
#
#ax1b.imshow(image_data_10b, cmap='hot', norm=LogNorm(vmin=0.1, vmax=.3), origin='lower', interpolation='none', extent=a)
##ax1b.imshow(image_data_10b, cmap='hot', vmin=0.01, vmax=.2, origin='lower', interpolation='none', extent=a)
##(vmin=0.001, vmax=.4)
##norm=LogNorm(vmin=0.085, vmax=.2)
#
#
#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
#
##plt.xlim(aaa1+6.43,aaa2+6.43)  #center 161.5
##plt.ylim(bbb1+3.74,bbb2+3.74)  #center 174
#plt.xlim(aaa1+6.43,aaa2+6.43)  #center 161.5
#plt.ylim(bbb1+7.43,bbb2+7.43)  #center 174
########################################################################## 2003
#ax1c = fig.add_subplot(432)
#ax1c.text(147.0+6.43, 162.0+3.74, '2003', color='white', size=14)
#ax1c.plot(165+2.93, 183-5.6, "wx", markeredgewidth=2, color='white',markersize= b) #corrected 2006 SgrA* position
#ax1c.scatter(169.5, 178.5, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
#
#image_data_10c = np.sqrt(image_data_1c**2)/1025.86 # Normalize it
#
#ax1c.imshow(image_data_10c, cmap='hot', norm=LogNorm(vmin=0.005, vmax=.4), origin='lower', interpolation='none', extent=a)
#
#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
#
#plt.xlim(aaa1+6.43,aaa2+6.43)  #center 161.5
#plt.ylim(bbb1+3.74,bbb2+3.74)  #center 174
#
#
#########################################################################  2004
ax1 = fig.add_subplot(431)

ax1.text(147.0+6.43, 162.0, '2004', color='white', size=14)

ax1.plot(165+2.48, 183-9, "wx", markeredgewidth=2, color='white',markersize= b) 

#ax1.scatter(171, 176, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax1.scatter(172.5, 178, s=350, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax1.scatter(161.75, 176.75, s=350, facecolors='none', color= c, linewidth=1, linestyle='dashed') # naco_gg


#image_data_10t = np.sqrt(image_data_1**2)/9465.67 # Normalize it
#image_data_10t = np.sqrt(image_data_1**2)/1160.11
image_data_10t = np.sqrt((image_data_1/1.997e+5)**2)
#image_data_10t = (image_data_1/3052)


image_data_10 = image_data_10t + image_data_10t[145:146,176:177]

ax1.imshow(image_data_10, cmap='hot', norm=LogNorm(vmin=0.00025, vmax=.35), origin='lower', interpolation='none', extent=a)

#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
ax1.axis('off')

plt.xlim(aaa1+6.43,aaa2+6.43)  #center 161.5
plt.ylim(bbb1,bbb2)  #center 174

############################################################################### 2005
ax2 = fig.add_subplot(432)
  
ax2.text(147.0+5.45, 162.0-1.37, '2005', color='white', size=14)

ax2.plot(165+1.95, 183-10.37, "wx", markeredgewidth=2, color='white',markersize= b)

#ax2.scatter(170, 176, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax2.scatter(171., 177.5, s=350, facecolors='none', color='lime', linewidth=1, linestyle='dashed') # naco_gg
ax2.scatter(161.75, 176.75, s=350, facecolors='none', color=c, linewidth=1, linestyle='dashed') # naco_gg

#ax2.scatter(171., 178.5, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed') # naco_g
#172.8, 178.5

#image_data_20 = image_data_2/356.595
#image_data_20 = image_data_2/2414.55
#image_data_20 = np.sqrt(image_data_2**2)  naco_f
#image_data_20 = image_data_2/12.57     # naco_g
#image_data_20 = image_data_2/6.62125     # naco_gg
#image_data_20 = image_data_2/11.6066     # naco_ggg
image_data_20 = image_data_2/9.77356     # naco_gggg

ax2.imshow(image_data_20, cmap='hot', vmin=0.065, vmax=.3 , origin='lower', interpolation='none', extent=a)
#norm=LogNorm(vmin=0.005, vmax=.4)
#norm=LogNorm(vmin=0.01, vmax=.4)
#norm=LogNorm(vmin=0.1, vmax=.6)
#vmin=0.065, vmax=.45 naco_gg

#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
ax2.axis('off')

plt.xlim(aaa1+5.45,aaa2+5.45)  #center 161.5
plt.ylim(bbb1-1.37,bbb2-1.37)  #center 174
############################################################################### 2006a
ax3 = fig.add_subplot(433)

ax3.text(147.0+4.47, 162.0-3.03, '2006.58', color='white', size=14)

ax3.plot(165+0.97, 183-12.03, "wx", markeredgewidth=2, color='white',markersize= b)

#ax3.scatter(170.25, 174, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
#ax3.scatter(172.47, 177.87, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax3.scatter(171.47, 177.37, s=350, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax3.scatter(159.5-1.5, 177.5-1.0, s=350, facecolors='none', color=c, linewidth=1, linestyle='dashed') # naco_gg

#image_data_30 = image_data_3/884.61
image_data_30 = np.sqrt((image_data_3/4.343e+4)**2)


#ax3.imshow(image_data_30, cmap='hot', norm=LogNorm(vmin=0.008, vmax=0.2) , origin='lower', interpolation='none', extent=a)
ax3.imshow(image_data_30, cmap='hot', norm=LogNorm(vmin=0.000075, vmax=0.05) , origin='lower', interpolation='none', extent=a)

#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
ax3.axis('off')

plt.xlim(aaa1+4.47,aaa2+4.47)  #center 161.5
plt.ylim(bbb1-3.03,bbb2-3.03)  #center 174
############################################################################### 2006b
ax4 = fig.add_subplot(434)

ax4.text(147.0+4.47, 162.0-3.03, '2006.72', color='white', size=14)

ax4.plot(165+0.97, 183-12.03, "wx", markeredgewidth=2, color='white',markersize= b)

#ax3.scatter(170.25, 174, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
#ax3.scatter(172.47, 177.87, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax4.scatter(171.47, 177.37, s=350, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax4.scatter(159.5-1.5, 177.5-.5, s=350, facecolors='none', color=c, linewidth=1, linestyle='dashed') # naco_gg

#image_data_30 = image_data_3/884.61
image_data_40 = np.sqrt((image_data_4/4.343e+4)**2)


#ax3.imshow(image_data_30, cmap='hot', norm=LogNorm(vmin=0.008, vmax=0.2) , origin='lower', interpolation='none', extent=a)
ax4.imshow(image_data_40, cmap='hot', norm=LogNorm(vmin=0.00075, vmax=0.05) , origin='lower', interpolation='none', extent=a)

#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
ax4.axis('off')

plt.xlim(aaa1+4.47,aaa2+4.47)  #center 161.5
plt.ylim(bbb1-3.03,bbb2-3.03)  #center 174
############################################################################### 2006c
ax5 = fig.add_subplot(435)

ax5.text(147.0+4.47, 162.0-3.03, '2006.78', color='white', size=14)

ax5.plot(165+0.97, 183-12.03, "wx", markeredgewidth=2, color='white',markersize= b)

#ax3.scatter(170.25, 174, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
#ax3.scatter(172.47, 177.87, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax5.scatter(171.47, 177.37, s=350, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax5.scatter(159.5+2., 177.5-1.5, s=350, facecolors='none', color=c, linewidth=1, linestyle='dashed') # naco_gg

#image_data_30 = image_data_3/884.61
image_data_50 = np.sqrt((image_data_5/4.343e+4)**2)


#ax3.imshow(image_data_30, cmap='hot', norm=LogNorm(vmin=0.008, vmax=0.2) , origin='lower', interpolation='none', extent=a)
ax5.imshow(image_data_50, cmap='hot', norm=LogNorm(vmin=0.0003, vmax=0.065) , origin='lower', interpolation='none', extent=a)

#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
ax5.axis('off')

plt.xlim(aaa1+4.47,aaa2+4.47)  #center 161.5
plt.ylim(bbb1-3.03,bbb2-3.03)  #center 174
############################################################################### 2006d
ax6 = fig.add_subplot(436)

ax6.text(147.0+4.47, 162.0-3.03, '2006.82', color='white', size=14)

ax6.plot(165+0.97, 183-12.03, "wx", markeredgewidth=2, color='white',markersize= b)

#ax3.scatter(170.25, 174, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
#ax3.scatter(172.47, 177.87, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax6.scatter(171.47, 177.37, s=350, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax6.scatter(159.5, 177.5, s=350, facecolors='none', color=c, linewidth=1, linestyle='dashed') # naco_gg

#image_data_30 = image_data_3/884.61
image_data_60 = np.sqrt((image_data_6/4.343e+4)**2)


#ax3.imshow(image_data_30, cmap='hot', norm=LogNorm(vmin=0.008, vmax=0.2) , origin='lower', interpolation='none', extent=a)
ax6.imshow(image_data_60, cmap='hot', norm=LogNorm(vmin=0.00007, vmax=0.05) , origin='lower', interpolation='none', extent=a)

#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
ax6.axis('off')

plt.xlim(aaa1+4.47,aaa2+4.47)  #center 161.5
plt.ylim(bbb1-3.03,bbb2-3.03)  #center 174
############################################################################### 2007a
ax7 = fig.add_subplot(437)

ax7.text(147.0+3.95, 162.0-3.7, '2007.20', color='white', size=14)

ax7.plot(165+0.45, 183-12.7, "wx", markeredgewidth=2, color='white',markersize= b)

#ax4.scatter(169.5, 174, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax7.scatter(170.-.5, 178.-1., s=350, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax7.scatter(160+1., 178.-1.5, s=350, facecolors='none', color=c, linewidth=1, linestyle='dashed') # naco_gg

#image_data_40 = image_data_4/5220.32
image_data_70 = np.sqrt((image_data_7/np.max(image_data_7))**2)

ax7.imshow(image_data_70, cmap='hot', norm=LogNorm(vmin=0.000075, vmax=0.5) , origin='lower', interpolation='none', extent=a)

#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
ax7.axis('off')

plt.xlim(aaa1+3.95,aaa2+3.95)  #center 161.5
plt.ylim(bbb1-3.7,bbb2-3.7)  #center 174
############################################################################### 2007b
ax8 = fig.add_subplot(438)

ax8.text(147.0+3.95, 162.0-3.7, '2007.21', color='white', size=14)

ax8.plot(165+0.45, 183-12.7, "wx", markeredgewidth=2, color='white',markersize= b)

#ax4.scatter(169.5, 174, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax8.scatter(170., 178.-.5, s=350, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax8.scatter(160, 178.-.75, s=350, facecolors='none', color=c, linewidth=1, linestyle='dashed') # naco_gg

#image_data_40 = image_data_4/5220.32
image_data_80 = np.sqrt((image_data_8/np.max(image_data_8))**2)

ax8.imshow(image_data_80, cmap='hot', norm=LogNorm(vmin=0.000075, vmax=0.5) , origin='lower', interpolation='none', extent=a)

#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
ax8.axis('off')

plt.xlim(aaa1+3.95,aaa2+3.95)  #center 161.5
plt.ylim(bbb1-3.7,bbb2-3.7)  #center 174
############################################################################### 2007c
ax9 = fig.add_subplot(439)

ax9.text(147.0+3.95, 162.0-3.7, '2007.25', color='white', size=14)

ax9.plot(165+0.45, 183-12.7, "wx", markeredgewidth=2, color='white',markersize= b)

#ax4.scatter(169.5, 174, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax9.scatter(170., 178., s=350, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax9.scatter(160, 178., s=350, facecolors='none', color=c, linewidth=1, linestyle='dashed') # naco_gg

#image_data_40 = image_data_4/5220.32
image_data_90 = image_data_9/300.521

ax9.imshow(image_data_90, cmap='hot', norm=LogNorm(vmin=0.009, vmax=0.5) , origin='lower', interpolation='none', extent=a)

#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
ax9.axis('off')

plt.xlim(aaa1+3.95,aaa2+3.95)  #center 161.5
plt.ylim(bbb1-3.7,bbb2-3.7)  #center 174
############################################################################### 2007d
ax10 = fig.add_subplot(4,3,10)

ax10.text(147.0+3.95, 162.0-3.7, '2007.45', color='white', size=14)

ax10.plot(165+0.45, 183-12.7, "wx", markeredgewidth=2, color='white',markersize= b)

#ax4.scatter(169.5, 174, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax10.scatter(170.+1.5, 178.+1, s=350, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax10.scatter(160+1, 178.-.5, s=350, facecolors='none', color=c, linewidth=1, linestyle='dashed') # naco_gg

#image_data_40 = image_data_4/5220.32
image_data_100 = image_data_10/np.max(image_data_10)

ax10.imshow(image_data_100, cmap='hot', norm=LogNorm(vmin=0.0002, vmax=0.1) , origin='lower', interpolation='none', extent=a)

#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
ax10.axis('off')

plt.xlim(aaa1+3.95,aaa2+3.95)  #center 161.5
plt.ylim(bbb1-3.7,bbb2-3.7)  #center 174
############################################################################### 2008
ax11 = fig.add_subplot(4,3,11)

ax11.text(147.0+2.83, 162.0-4.3, '2008', color='white', size=14)

ax11.plot(165-0.67, 183-13.3, "wx", markeredgewidth=2, color='white',markersize= b)

#ax5.scatter(169, 174, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax11.scatter(165-0.67+9.0, 183-13.3+8.0+1.0, s=350, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax11.scatter(160, 175., s=350, facecolors='none', color=c, linewidth=1, linestyle='dashed') # naco_gg

image_data_110 = np.sqrt(((image_data_11)/1.561e+5)**2)
#image_data_50 = image_data_5

ax11.imshow(image_data_110, cmap='hot', norm=LogNorm(vmin=0.000075, vmax=.7) , origin='lower', interpolation='none', extent=a)
#LogNorm(vmin=0.01, vmax=0.5)
#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
ax11.axis('off')

plt.xlim(aaa1+2.83,aaa2+2.83)  #center 161.5
plt.ylim(bbb1-4.3,bbb2-4.3)  #center 174
############################################################################## 2009
#ax6 = fig.add_subplot(438)
#
#ax6.text(147.0+1.85, 162.0-4.5, '2009', color='white', size=14)
#  
#ax6.plot(165-1.65, 183-13.5, "wx", markeredgewidth=2, color='white',markersize= b)
#
##ax6.scatter(171, 174.5, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
#ax6.scatter(165-1.65+6.42, 183-13.5+6.45, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
#
#image_data_60 = np.sqrt(image_data_6**2)/7066.96
#
#ax6.imshow(image_data_60, cmap='hot', norm=LogNorm(vmin=0.005, vmax=0.3), origin='lower', interpolation='none', extent=a)
#
#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
#
#plt.xlim(aaa1+1.85,aaa2+1.85)  #center 161.5
#plt.ylim(bbb1-4.5,bbb2-4.5)  #center 174
############################################################################## 2010
ax12 = fig.add_subplot(4,3,12)#4,3,9)

ax12.text(147.0+0.95, 162.0-4.3, '2010', color='white', size=14)

ax12.plot(165-2.55, 183-13.3, "wx", markeredgewidth=2, color='white',markersize= b)

#ax7.scatter(169, 174, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax12.scatter(165-2.55+6.0, 183-13.3+5.5, s=350, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
ax12.scatter(163, 173.5, s=350, facecolors='none', color=c, linewidth=1, linestyle='dashed') # naco_gg

image_data_120 = np.sqrt((image_data_12/1.602e+5)**2)

ax12.imshow(image_data_120, cmap='hot', norm=LogNorm(vmin=0.0002, vmax=.25), origin='lower', interpolation='none', extent=a)

#plt.tick_params()
#plt.tight_layout()
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
#
#ax7.spines['top'].set_visible(False)
#ax7.spines['right'].set_visible(False)
#ax7.spines['bottom'].set_visible(False)
#ax7.spines['left'].set_visible(False)

#plt.xticks([])
#plt.yticks([])

#fig.patch.set_visible(False)
ax12.axis('off')

plt.xlim(aaa1+0.95,aaa2+0.95)  #center 161.5
plt.ylim(bbb1-4.3,bbb2-4.3)  #center 174
############################################################################## 2011
#ax8 = fig.add_subplot(4,3,10)
#
#ax8.text(147.0+0.27, 162.0-3.7, '2011', color='white', size=14)
#
#ax8.plot(165-3.23, 183-12.7, "wx", markeredgewidth=2, color='white',markersize= b)
#
##ax8.scatter(166, 174.5, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
#ax8.scatter(165-3.23+4.32, 183-12.7+5.49, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
#
#image_data_80 = image_data_8/620.927
#
#ax8.imshow(image_data_80, cmap='hot', norm=LogNorm(vmin=0.05, vmax=0.5), origin='lower', interpolation='none', extent=a)
#
#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
#
#ax8.spines['top'].set_visible(False)
#ax8.spines['right'].set_visible(False)
#ax8.spines['bottom'].set_visible(False)
#ax8.spines['left'].set_visible(False)
#
#plt.xlim(aaa1+0.27,aaa2+0.27)  #center 161.5
#plt.ylim(bbb1-3.7,bbb2-3.7)  #center 174
############################################################################### 2012
#ax9 = fig.add_subplot(4,3,11)
#
#ax9.text(147.0-0.33, 162.0-3.1, '2012', color='white', size=14)
#
#ax9.plot(165-3.83, 183-12.1, "wx", markeredgewidth=2, color='white',markersize= b)
#
##ax9.scatter(164, 174.5, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
#ax9.scatter(165-3.83+2.8, 183-12.1+4.0, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
#
#image_data_90 = image_data_9/2110.73
#
#ax9.imshow(image_data_90, cmap='hot', norm=LogNorm(vmin=0.009, vmax=0.5), origin='lower', interpolation='none', extent=a)
#
#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
#
#ax9.spines['top'].set_visible(False)
#ax9.spines['right'].set_visible(False)
#ax9.spines['bottom'].set_visible(False)
#ax9.spines['left'].set_visible(False)
#
#plt.xlim(aaa1-0.33,aaa2-0.33)  #center 161.5
#plt.ylim(bbb1-3.1,bbb2-3.1)  #center 174
###############################################################################
##########################################################################
#ax1a = fig.add_subplot(4,3,12)
#######
##ax1a.text(147.0+4, 162.0, '133 mas', color='black', size=8)
##ax1a.plot([149+4, 159+4], [161, 161], color='black')
#
##ax1a.arrow(165, 170, -10 , 0, head_width=2, head_length=4, fc= 'black', ec= 'black')
##ax1a.arrow(165, 170, 0 , 10, head_width=2, head_length=4, fc= 'black', ec= 'black')
#
##ax1a.text(150.0, 172.0, 'East', color='black', size=8)
##ax1a.text(154.0, 182.0, 'North', color='black', size=8)
#
#######
#ax1a.text(147.0-1.03, 162.0-1.8, '2013', color='white', size=14)
#ax1a.plot(165-4.53, 183-10.8, "wx", markeredgewidth=2, color='white',markersize= b)
#
#
#image_data_10a = np.sqrt(image_data_1a**2)/1261.17 # Normalize it
#
#ax1a.scatter((165-4.53)+1.56, (183-10.8)+3.15, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
#
#
#ax1a.imshow(image_data_10a, cmap='hot', norm=LogNorm(vmin=0.009, vmax=.4), origin='lower', interpolation='none', extent=a)
#
#plt.tick_params(
#    axis='both',          # changes apply to the x-axis
#    which='both',      # both major and minor ticks are affected
#    bottom='off',      # ticks along the bottom edge are off
#    top='off',         # ticks along the top edge are off
#    labelbottom='off', # labels along the bottom edge are off
#right='off', left='off', labelleft='off')
#
#ax1a.spines['top'].set_visible(False)
#ax1a.spines['right'].set_visible(False)
#ax1a.spines['bottom'].set_visible(False)
#ax1a.spines['left'].set_visible(False)
#
#plt.xlim(aaa1-1.03,aaa2-1.03)  #center 161.5
#plt.ylim(bbb1-1.8,bbb2-1.8)  #center 174


#########################################################################
plt.tight_layout()
plt.subplots_adjust(wspace=-.6, hspace =.1)#,vspace= -.1)
#plt.tight_layout()
plt.savefig('overview_s4711_all.png', dpi=600)#, bbox_inches='tight')
plt.show()
plt.close()
