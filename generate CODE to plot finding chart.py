#### This code generates the repeating section for finding chart code:
## MAIN plot code goes to Code_output.py

#### REQUIRED INPUT FILES:
## 1) FITS filename & SagA* coordinates for this epoch (use "Epoch to sagA_coord & FITS_filename.py")
## 2) candidate names & pixel-coordinates/offsets from Sag A* (#_candidate positions.txt)
## 3) known S-star names & pixel-coordinates/offsets from Sag A* (#_known stars positions.txt)

import glob
import os
import re

#### SETTINGS:
## Object name/number:
epoch = 2007.214

## Display radial distance around Sag A, in pixels; Color map & title text size
## Color-map catalogue: https://matplotlib.org/stable/tutorials/colors/colormaps.html
## xkcd-colors: https://xkcd.com/color/rgb/
radius = 50
color_map_gradient = "gray"
overhead_title_fontsize = 25

## SagA* & star circle marker settings: size, color, shape
SagA_marker_size = "20"
SagA_marker_color = "yellow"
SagA_marker_shape = "*"
star_circle_size = "1500"
star_circle_color = "lime"
star_circle_line_width = "1"
star_circle_line_style = "dashed"

## candidate star name label settings
## position of name label relative to star coordinate, xy in pixel
star_position_unit = "marcsec" # "pixel" or "marcsec"
star_text_fontsize = "15"
star_text_color = "lime"
star_text_offset_x = "2.5"
star_text_offset_y = "-1.5"

## known S-stars label settings
s_star_position_unit = "pixel" # "pixel" or "marcsec"
s_star_text_fontsize = "15"
s_star_text_color = "blue"
s_star_text_offset_x = "0"
s_star_text_offset_y = "0"

## set star name label position manually & enable pointer??
star_text_custom_position = "no" # yes or no
star_text_arrow_color = "lime"

#=======================================================================
#=======================================================================

## Import necessary files, flexible file name

cand_positions = open(str(epoch)+" candidates positions.txt", "r")
s_star_positions = open(str(epoch)+" known stars positions.txt", "r")
fits_list_input = open(str(epoch)+"_FITS_filenames_list.txt", "r") 
sagA = open(str(epoch)+"_sagA_coordinates.txt", "r") 

## Output code file names:
code_output = open("Code_output.py", "w+")

#=======================================================================

## import & set up the FITS filename, date, SagA* coordinate

files = []
decimal_date = []
sagA_coord_x = []
sagA_coord_y = []

for fits_filename in fits_list_input.readlines():
    files.append(fits_filename.replace("\n", ""))
    
for line_a in sagA.readlines():
    date_sagA = line_a.split("\t")
    decimal_date.append(date_sagA[0])
    # Appended as float instead of string, as string cannot do math operations below
    sagA_coord_x.append(float(date_sagA[1]))
    sagA_coord_y.append(float(date_sagA[2].replace("\n", "")))
    
#=======================================================================

## If position file contains the offset of object in marcsec
## Import the offsets and change to pixel unit & calculate the object coordinates:

offset_pix_x = []
offset_pix_y = []
candidate_name = []
calculated_obj_coord_x = []
calculated_obj_coord_y = []

if star_position_unit == "marcsec":
    for line in cand_positions.readlines():
        date_offset_mas = line.split("\t")
        candidate_name.append(str(date_offset_mas[0]))
        offset_pix_x.append((((float(date_offset_mas[1]))/-13.3)))
        offset_pix_y.append((((float(date_offset_mas[2]))/13.3)))

    i = 0
    for item in offset_pix_x:
        calc_x = sagA_coord_x[0] + offset_pix_x[i]
        calc_y = sagA_coord_y[0] + offset_pix_y[i]
        calculated_obj_coord_x.append(round(calc_x, 2))
        calculated_obj_coord_y.append(round(calc_y, 2))
        i += 1
    
if star_position_unit == "pixel":    
    for line11 in cand_positions.readlines():
        date_offset_mas11 = line11.replace("\n","").split("\t")
        candidate_name.append(str(date_offset_mas11[0]))
        calculated_obj_coord_x.append(float(date_offset_mas11[1]))
        calculated_obj_coord_y.append(float(date_offset_mas11[2])) 
    
## Known S-stars part:    
    
s_star_offset_pix_x = []
s_star_offset_pix_y = []
s_star_name = []    
s_star_calculated_obj_coord_x = []
s_star_calculated_obj_coord_y = []

if s_star_position_unit == "marcsec":
    for line2 in s_star_positions.readlines():
        date_offset_mas2 = line2.split("\t")
        s_star_name.append(str(date_offset_mas2[0]))
        s_star_offset_pix_x.append((((float(date_offset_mas2[1]))/-13.3)))
        s_star_offset_pix_y.append((((float(date_offset_mas2[2]))/13.3)))    

    j = 0
    for item2 in s_star_offset_pix_x:
        s_star_calc_x = sagA_coord_x[0] + s_star_offset_pix_x[j]
        s_star_calc_y = sagA_coord_y[0] + s_star_offset_pix_y[j]
        s_star_calculated_obj_coord_x.append(round(s_star_calc_x, 2))
        s_star_calculated_obj_coord_y.append(round(s_star_calc_y, 2))
        j += 1

if s_star_position_unit == "pixel":    
    for line3 in s_star_positions.readlines():
        date_offset_mas3 = line3.replace("\n","").split("\t")
        s_star_name.append(str(date_offset_mas3[0]))
        s_star_calculated_obj_coord_x.append(float(date_offset_mas3[1]))
        s_star_calculated_obj_coord_y.append(float(date_offset_mas3[2]))

#=======================================================================

## generate the content lines in timeline code

## v3 Update: IF USING THE COORDINATES FROM QFitsView (Hence, also from Excel)
# Origin is set as (0,0) in matplotlib for the first pixel of the image, instead of (1,1) in QFitsView!
# the code-generator needs to deduct 1 pixel for all coordinates-specified objects
## v4 Update: adding the minimal 1e-20 intensity fixes blank/white holes bug in the plot
## v6 Update: Brightness/Contrast adjustments automation

for item in files:
    # 'item' full FITS image file name: 2003_06_15_mosaic.fits
    # 'date' format: 2003_06_15
    date = item[0:10]
    code_output.writelines('image_' + date + " = fits.getdata('" + item + "')" + '\n')
    # Brightness/Contrast line for specific FITS images, might add more
    if item == '2002_07_31_98_subim42.nice.fits':
        code_output.writelines('image_2002_07_31t = np.sqrt((image_2002_07_31/8e+4)**2) + 1e-20' + '\n')
    elif item == '2004_07_06_561_subim14.nice.fits':
        code_output.writelines('image_2004_07_06t = np.sqrt((image_2004_07_06/5e+4)**2) + 1e-20' + '\n')
    elif item == '2004_07_29_48_mosaic.fits':
        code_output.writelines('image_2004_07_29t = np.sqrt((image_2004_07_29/4e+5)**2) + 1e-20' + '\n')
    elif item == '2005_05_16_mosaicc.fits':
        code_output.writelines('image_2005_05_16t = np.sqrt((image_2005_05_16/3e+4)**2) + 1e-20' + '\n')
    elif item == '2006_08_02_mosaic.fits':
        code_output.writelines('image_2006_08_02t = np.sqrt((image_2006_08_02/3e+4)**2) + 1e-20' + '\n')
    elif item == '2006_09_23_55_mosaic.fits':
        code_output.writelines('image_2006_09_23t = np.sqrt((image_2006_09_23/4e+5)**2) + 1e-20' + '\n')
    elif item == '2007_03_17_S13_mosaic.fits':
        code_output.writelines('image_2007_03_17t = np.sqrt((image_2007_03_17/3e+4)**2) + 1e-20' + '\n')
    elif item == '2008_08_07_mosaic.fits':
        code_output.writelines('image_2008_08_07t = np.sqrt((image_2008_08_07/1.5e+5)**2) + 1e-20' + '\n')
    elif item == '2009_04_21_mosaic.fits':
        code_output.writelines('image_2009_04_21t = np.sqrt((image_2009_04_21/2e+5)**2) + 1e-20' + '\n')
    elif item == '2009_05_03_mosaic.fits':
        code_output.writelines('image_2009_05_03t = np.sqrt((image_2009_05_03/2e+5)**2) + 1e-20' + '\n')
    elif item == '2009_08_12_mosaic.fits':
        code_output.writelines('image_2009_08_12t = np.sqrt((image_2009_08_12/2e+5)**2) + 1e-20' + '\n')
    elif item == '2009_09_19_S13_mosaic.fits':
        code_output.writelines('image_2009_09_19t = np.sqrt((image_2009_09_19/3e+5)**2) + 1e-20' + '\n')
    elif item == '2009_09_20_S13_mosaic.fits':
        code_output.writelines('image_2009_09_20t = np.sqrt((image_2009_09_20/1.3e+5)**2) + 1e-20' + '\n')
    elif item == '2010_03_29_mosaic.fits':
        code_output.writelines('image_2010_03_29t = np.sqrt((image_2010_03_29/1.5e+5)**2) + 1e-20' + '\n')
    elif item == '2010_06_12_mosaic.fits':
        code_output.writelines('image_2010_06_12t = np.sqrt((image_2010_06_12/2e+4)**2) + 1e-20' + '\n')
    elif item == '2010_06_16_mosaic.fits':
        code_output.writelines('image_2010_06_16t = np.sqrt((image_2010_06_16/1.5e+5)**2) + 1e-20' + '\n')
    elif item == '2011_05_27_median.nice.fits':
        code_output.writelines('image_2011_05_27t = np.sqrt((image_2011_05_27/3e+5)**2) + 1e-20' + '\n')
    elif item == '2012_05_17_median.nice.fits':
        code_output.writelines('image_2012_05_17t = np.sqrt((image_2012_05_17/8e+4)**2) + 1e-20' + '\n')
    elif item == '2015_08_01_median.nice.fits':
        code_output.writelines('image_2015_08_01t = np.sqrt((image_2015_08_01/2e+5)**2) + 1e-20' + '\n')
    elif item == '2016_3_22_decon.fits':
        code_output.writelines('image_2016_3_22_t = np.sqrt((image_2016_3_22_/2e+3)**2) + 1e-20' + '\n')
    elif item == '2017_6_16_decon.fits':
        code_output.writelines('image_2017_6_16_t = np.sqrt((image_2017_6_16_/2e+3)**2) + 1e-20' + '\n')        
    # Generic Brightness/Contrast line if adjustment unnecessary
    else:
        code_output.writelines('image_' + date + "t = np.sqrt((image_" + date + "/np.max(image_" + date + '))**2) + 1e-20' + "\n")
    
    # 'imshow' settings
    if item == '2011_05_27_median.nice.fits':
        code_output.writelines("plt.imshow(image_" + date + "t, cmap='"+str(color_map_gradient)+"', norm=LogNorm(vmin=0.00005, vmax=.001), origin='lower', interpolation='none')" + "\n")
    if item == '2010_03_29_mosaic.fits':
        code_output.writelines("plt.imshow(image_" + date + "t, cmap='"+str(color_map_gradient)+"', norm=LogNorm(vmin=0.0002, vmax=.002), origin='lower', interpolation='none')" + "\n")
    if item == '2009_09_20_S13_mosaic.fits':
        code_output.writelines("plt.imshow(image_" + date + "t, cmap='"+str(color_map_gradient)+"', norm=LogNorm(vmin=0.00015, vmax=.004), origin='lower', interpolation='none')" + "\n")
    else:
        code_output.writelines("plt.imshow(image_" + date + "t, cmap='"+str(color_map_gradient)+"', norm=LogNorm(vmin=0.0002, vmax=.002), origin='lower', interpolation='none')" + "\n")
    
code_output.writelines("plt.axis('off')" + "\n")    
code_output.writelines("\n")
code_output.writelines("plt.title('" + decimal_date[0] + "', fontsize = "+str(overhead_title_fontsize)+")" + "\n")
code_output.writelines("plt.plot(" + str(sagA_coord_x[0]) + "-1, " + str(sagA_coord_y[0]) + "-1, '"+SagA_marker_shape+"', markeredgewidth=1, color='"+SagA_marker_color+"', markersize="+str(SagA_marker_size)+ ")" + "\n")    
code_output.writelines("plt.xlim(" + str(sagA_coord_x[0]-radius) + "-1, " + str(sagA_coord_x[0]+radius) + "-1)" + "\n")
code_output.writelines("plt.ylim(" + str(sagA_coord_y[0]-radius) + "-1, " + str(sagA_coord_y[0]+radius) + "-1)" + "\n")
code_output.writelines("\n")   

# Looping for Star markers and labels

n = 1
for name in candidate_name:
    code_output.writelines("plt.scatter(" + str(calculated_obj_coord_x[n-1]) + "-1, " + str(calculated_obj_coord_y[n-1]) + "-1, s="+str(star_circle_size)+", facecolors='none', color='"+str(star_circle_color)+"', linewidth="+str(star_circle_line_width)+", linestyle='"+str(star_circle_line_style)+"')" + "\n") 
    if star_text_custom_position == "no":
        code_output.writelines("plt.annotate('"+str(name)+"', xy=("+str(calculated_obj_coord_x[n-1]) + "-1, " + str(calculated_obj_coord_y[n-1]) + "-1), xytext=("+str(calculated_obj_coord_x[n-1]) + "-1+" + str(star_text_offset_x) + ", " + str(calculated_obj_coord_y[n-1])+"-1+" + str(star_text_offset_y) + "), color='"+str(star_text_color)+"', fontsize="+str(star_text_fontsize)+", fontstyle='normal')" + "\n")
    if star_text_custom_position == "yes":
        code_output.writelines("plt.annotate('"+str(name)+"', xy=("+str(calculated_obj_coord_x[n-1]) + "-1, " + str(calculated_obj_coord_y[n-1]) + "-1), xytext=("+str(calculated_obj_coord_x[n-1]) + "-1, " + str(calculated_obj_coord_y[n-1])+"-1), arrowprops=dict(arrowstyle='-', color='" + str(star_text_arrow_color) + "'), color='"+str(star_text_color)+"', fontsize="+str(star_text_fontsize)+", fontstyle='normal')" + "\n")
    n+=1

code_output.writelines("\n\n")
    
m = 1
for name in s_star_name:
    #code_output.writelines("plt.scatter(" + str(calculated_obj_coord_x[n-1]) + "-1, " + str(calculated_obj_coord_y[n-1]) + "-1, s="+str(star_circle_size)+", facecolors='none', color='"+str(star_circle_color)+"', linewidth="+str(star_circle_line_width)+", linestyle='"+str(star_circle_line_style)+"')" + "\n") 
    code_output.writelines("plt.annotate('"+str(name)+"', xy=("+str(s_star_calculated_obj_coord_x[m-1]) + "-1, " + str(s_star_calculated_obj_coord_y[m-1]) + "-1), xytext=("+str(s_star_calculated_obj_coord_x[m-1]) + "-1+" + str(s_star_text_offset_x) + ", " + str(s_star_calculated_obj_coord_y[m-1])+"-1+" + str(s_star_text_offset_y) + "), color='"+str(s_star_text_color)+"', fontsize="+str(s_star_text_fontsize)+", fontstyle='normal')" + "\n")
    m+=1
    
#=======================================================================

print("Generate Finding Chart Code Successful")
   
fits_list_input.close()
sagA.close()
cand_positions.close()
s_star_positions.close()
code_output.close()

# #=======================================================================
# #=======================================================================
# #### The stuff outside main body in Timeline_code.py

# ## Code that generates a progressive timeline map from FITS files and given positions
# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# import matplotlib.mlab as mlab
# import matplotlib.cm as cm
# import matplotlib.image as mpimg
# import matplotlib.patches as patches
# from astropy.utils.data import download_file
# from astropy.io import fits
# from pylab import *
# from optparse import OptionParser
# from matplotlib import gridspec
# from matplotlib.colors import LogNorm
# from matplotlib.patches import ConnectionPatch
# from mpl_toolkits.axes_grid1 import ImageGrid
# from PIL import Image
# import copy

# fig = plt.figure(figsize=(12, 12))

# ########################

# ## Main Body, paste everything from Code_output.py in here

# ## Main Output Code Example:
# ## non-variable lines, depends on epoch only
# # open FITS file and brightness, colormap settings
# image_2010_03_29 = fits.getdata('2010_03_29_mosaic.fits')
# image_2010_03_29t = np.sqrt((image_2010_03_29/3e+5)**2) + 1e-20
# plt.imshow(image_2010_03_29t, cmap='gray', norm=LogNorm(vmin=0.00005, vmax=.01), origin='lower', interpolation='none')
# plt.axis('off')
# # overhead title, SagA* marker, displayed area
# plt.title('2010.238', fontsize = 25)
# plt.plot(162.96-1, 152.43-1, marker='*', markeredgewidth=2, color='blue', markersize=20)
# plt.xlim(112.96000000000001-1, 212.96-1)
# plt.ylim(102.43-1, 202.43-1)
# # the markers and labels
# plt.scatter(163.41-1, 155.83-1, s=1500, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
# plt.annotate("S4711", xy=(163.41-1, 155.83-1), xytext=(163.41-1, 155.83-1), arrowprops=dict(arrowstyle="-", color='lime'), color='lime', fontsize=15, fontstyle='normal')

# ########################

# plt.tight_layout()
# plt.subplots_adjust(wspace=-.6, hspace =.2)#,vspace= -.1)
# plt.savefig('test.png', dpi=500)#, bbox_inches='tight')
# plt.show()
# plt.close()
