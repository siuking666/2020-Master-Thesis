#### This code generates the repeating section for timeline_plot_code:
## MAIN plot code goes to Code_output.py
## Orbital trajectory code goes to Code_overlay_output.py
## Summary of values imported goes to Code_summary_output.txt

#### REQUIRED INPUT FILES:
## 1) list of FITS filenames used in the timeline for this object (use "make #_FITS_filenames_list.txt.py")
## 2) decimal dates & coordinates (x, y) for Sag A*  (use "make #_sagA_coordinates.txt.py")
## 3) decimal dates & offsets from Sag A* (x, y) in marcsec for obj (#_best_points_v2.txt)
## 4) For orbit overlay, decimal dates & extrapolated offsets data set (#_inquired_pos_for_orbital_plot.txt) 

import glob
import os
import re

#### SETTINGS:
## Object name/number:
object_name = 101

## Output code file names:
code_output = open("Code_output.py", "w+")
overlay_output = open("Code_overlay_output.py", "w+")
summary_output = open("Code_summary_output.txt", "w+")

## number of subplot rows (--) & columns (||)
subplot_rows = 8
subplot_columns = 6

## Display radial distance around Sag A, in pixels
radius = 30

## Size of green cicle object marker & cross-shaped Sag A marker
circle_size = "s=180"
SagA_marker_size = "markersize = 7"

## Size & Color of orbit trajectory; within timeline plot range & outside range
pt_size = "s=0.5"    
in_range_color = 'cyan'
out_range_color = 'paleturquoise'

#=======================================================================
#=======================================================================
#### Main Output Code v4 Sample:
# image_data_1 = fits.getdata('2016_03_23.fits')    
# image_2003_06_15t = np.sqrt((image_2003_06_15/np.max(image_2003_06_15))**2) + 1e-20
# ax1 = fig.add_subplot(6, 4, 1)
# ax1.set_title('2003.452')
# ax1.plot(168-1, 159-1, 'x', markeredgewidth=1, color='blue',markersize= 7)
# ax1.set_xlim(148-1, 188-1)
# ax1.set_ylim(139-1, 179-1)
# ax1.scatter(173.83-1, 158.53-1, s=250, facecolors='none', color='lime', linewidth=1, linestyle='dashed')
# ax1.imshow(image_2003_06_15t, cmap='hot', norm=LogNorm(vmin=0.00005, vmax=.01), origin='lower', interpolation='none')
# ax1.axis('off')
#=======================================================================

## Import necessary files, flexible file name

fits_list_input = open(str(object_name)+"_FITS_filenames_list.txt", "r") 
sagA = open(str(object_name)+"_sagA_coordinates.txt", "r") 
best_point_v2 = open(str(object_name)+"_best_points v2.txt", "r")

## v7 update: for orbit overlay
perfect_offsets_pix = open(str(object_name)+"_inquired_pos_for_orbital_plot.txt", "r") 

#=======================================================================

## import a list of FITS filenames used in the timeline for this object

files = []

for fits_filename in fits_list_input.readlines():
    files.append(fits_filename.replace("\n", ""))

# print(files)

## detects ALL FITS files in this folder, use them ALL for timeline
## AND output all the filenames as list (from output_FITS_filenames_in_folder.py)

# # print directory
# print(os.getcwd())

# for file in glob.glob("*.fits"):
#     files.append(file)
# # print(files)

# fits_list_output = open("FITS_filenames_list.txt", "w+") 
# for item in files:
#     fits_list_output.writelines(item + "\n")
# fits_list_output.close()

#=======================================================================

## Import and set up dates, Sag A coordinate & object coordinate

decimal_date = []
sagA_coord_x = []
sagA_coord_y = []

for line_a in sagA.readlines():
    date_sagA = line_a.split("\t")
    #print(date_sagA)
    decimal_date.append(date_sagA[0])
    # Appended as float instead of string, as string cannot do math operations below
    sagA_coord_x.append(float(date_sagA[1]))
    sagA_coord_y.append(float(date_sagA[2].replace("\n", "")))
    
# print(decimal_date) 
# print(sagA_coord_x)
# print(sagA_coord_y) 

#=======================================================================

## Now the object coordinates are calculated within the code from offsets, 
## importing coordinates file manually created from Excel is no longer needed
#
# coordinates = open(str(object_name)+"_timeline_coordinates.txt", "r") 
#
# obj_coord_x = []
# obj_coord_y = []
#
# for line in coordinates.readlines():
#     date_coord = line.split("\t")
#     #print(date_coord)    
#     obj_coord_x.append((float(date_coord[1])))
#     obj_coord_y.append((float(date_coord[2].replace("\n", ""))))
#
# # print(obj_coord_x)
# # print(obj_coord_y)    

# coordinates.close()

#=======================================================================

## v5 Update: Auto Object coordinates calculation from Offset

offset_pix_x = []
offset_pix_y = []

## best_points_v2 contains the offset of object in marcsec
## Import the offsets as pixel unit

for line in best_point_v2.readlines():
    date_offset_mas = line.split("\t")
    #print(date_offset_mas)    
    offset_pix_x.append((((float(date_offset_mas[1]))/-13.3)))
    offset_pix_y.append((((float(date_offset_mas[2]))/13.3)))
    
## Calculate the object coordinates:
## Results are verified to be almost identical to Excel values (raw Gaussian extraction)

calculated_obj_coord_x = []
calculated_obj_coord_y = []

i = 0
for item in offset_pix_x:
    calc_x = sagA_coord_x[i] + offset_pix_x[i]
    calc_y = sagA_coord_y[i] + offset_pix_y[i]
    calculated_obj_coord_x.append(round(calc_x, 2))
    calculated_obj_coord_y.append(round(calc_y, 2))
    i += 1

    
# ## Verification that the offsets + Sag A coordinate = obj coordinate imported from Excel
#
# temp_test_x = []
# temp_test_y = []
# i = 0
# for item in offset_pix_x:
#     verify_x = sagA_coord_x[i] + offset_pix_x[i] - obj_coord_x[i]
#     verify_y = sagA_coord_y[i] + offset_pix_y[i] - obj_coord_y[i]
#     temp_test_x.append(round(verify_x, 2))
#     temp_test_y.append(round(verify_y, 2))
#     i += 1
# 
# print(temp_test_x)    
# print(temp_test_y)  

#=======================================================================

## generate the content lines in timeline code

n = 1
for item in files:
    date = item[0:10]
    code_output.writelines('image_' + date + " = fits.getdata('" + item + "')" + '\n')
    # print('image_' + date + " = fits.getdata('" + item + "')")
code_output.writelines("\n")    

## v3 Update: IF USING THE COORDINATES FROM QFitsView (Hence, also from Excel)
# Origin is set as (0,0) in matplotlib for the first pixel of the image, instead of (1,1) in QFitsView!
# the code-generator needs to deduct 1 pixel for all coordinates-specified objects:
# -That of Sag A* 
# -The x-limit and y-limit of the subplot since we want Sag A* as the center
# -That of the star-marker (circle) since it is calculated from Sag A*
# This will fix the systematic 1-pix deviation for markers in every subplot.

## v4 Update: adding the minimal 1e-20 intensity fixes blank/white holes bug in the plot

## v6 Update: Brightness/Contrast adjustments automation

for item in files:
    date = item[0:10]
    # 'item' full FITS image file name: 2003_06_15_mosaic.fits
    # 'date' format: 2003_06_15
    
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
        code_output.writelines('image_2008_08_07t = np.sqrt((image_2008_08_07/3e+5)**2) + 1e-20' + '\n')
    elif item == '2009_04_21_mosaic.fits':
        code_output.writelines('image_2009_04_21t = np.sqrt((image_2009_04_21/2e+5)**2) + 1e-20' + '\n')
    elif item == '2009_05_03_mosaic.fits':
        code_output.writelines('image_2009_05_03t = np.sqrt((image_2009_05_03/2e+5)**2) + 1e-20' + '\n')
    elif item == '2009_08_12_mosaic.fits':
        code_output.writelines('image_2009_08_12t = np.sqrt((image_2009_08_12/2e+5)**2) + 1e-20' + '\n')
    elif item == '2009_09_19_S13_mosaic.fits':
        code_output.writelines('image_2009_09_19t = np.sqrt((image_2009_09_19/3e+5)**2) + 1e-20' + '\n')
    elif item == '2009_09_20_S13_mosaic.fits':
        code_output.writelines('image_2009_09_20t = np.sqrt((image_2009_09_20/3e+5)**2) + 1e-20' + '\n')
    elif item == '2010_03_29_mosaic.fits':
        code_output.writelines('image_2010_03_29t = np.sqrt((image_2010_03_29/3e+5)**2) + 1e-20' + '\n')
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
        
    code_output.writelines('ax' + str(n) + ' = fig.add_subplot(' + str(subplot_rows) + ', ' + str(subplot_columns) + ', ' + str(n) + ')' + "\n")   
    code_output.writelines('ax' + str(n) + ".set_title('" + decimal_date[n-1] + "')" + "\n")
    code_output.writelines('ax' + str(n) + ".plot(" + str(sagA_coord_x[n-1]) + "-1, " + str(sagA_coord_y[n-1]) + "-1, 'x', markeredgewidth=1, color='blue'," + SagA_marker_size + ")" + "\n")    
    # sagA_coord imported as integer, did the +-radius then write out as string
    code_output.writelines('ax' + str(n) + ".set_xlim(" + str(sagA_coord_x[n-1]-radius) + "-1, " + str(sagA_coord_x[n-1]+radius) + "-1)" + "\n")
    code_output.writelines('ax' + str(n) + ".set_ylim(" + str(sagA_coord_y[n-1]-radius) + "-1, " + str(sagA_coord_y[n-1]+radius) + "-1)" + "\n")
    # calculated_obj_coord imported as string
    code_output.writelines('ax' + str(n) + ".scatter(" + str(calculated_obj_coord_x[n-1]) + "-1, " + str(calculated_obj_coord_y[n-1]) + "-1, " + circle_size + ", facecolors='none', color='lime', linewidth=1, linestyle='dashed')" + "\n") 
    
    if item == '2011_05_27_median.nice.fits':
        code_output.writelines('ax' + str(n) + ".imshow(image_" + date + "t, cmap='hot', norm=LogNorm(vmin=0.00005, vmax=.001), origin='lower', interpolation='none')" + "\n")
    else:
        code_output.writelines('ax' + str(n) + ".imshow(image_" + date + "t, cmap='hot', norm=LogNorm(vmin=0.00005, vmax=.01), origin='lower', interpolation='none')" + "\n")
    
    code_output.writelines('ax' + str(n) + ".axis('off')" + "\n")
    code_output.writelines("\n")          
    n += 1
    
#=======================================================================

## v7 Update: Experimental orbit trail overlay
## Each point-marker coordinate = Each extrapolated offset + SagA coord for one subplot;
## Calculate and apply that to every subplots

## v7b Update: Using extrapolated, inquired offsets/data points
## Input file "#_inquired_pos_for_orbital_plot.txt" is needed
## Generate this set of extrapolated offsets from "Inquire_positions.py" and "convert marcsec to pix.py"

## v9 Update: Different, custom colors for orbit section covered by timeline plot

## Moved to top of the code
# perfect_offsets_pix = open("8_inquired_pos_for_orbital_plot.txt", "r") 
# overlay_output = open("Code_overlay_output.py", "w+")
# in_range_color = 'cyan'
# out_range_color = 'paleturquoise'
# pt_size = "s=1"  

perfect_offsets_date = []
perfect_offsets_x = []
perfect_offsets_y = []

for line in perfect_offsets_pix.readlines():
    date_perf = line.split("\t")
    perfect_offsets_date.append(float(date_perf[0]))
    perfect_offsets_x.append(float(date_perf[1]))
    perfect_offsets_y.append(float(date_perf[2].replace("\n", "")))    
    
print("Offsets")
print(perfect_offsets_x)
print(perfect_offsets_y) 
print("\n")
    
orbit_x_1 = []
orbit_y_1 = []  

# k = subplot index
k=0
for subplot in decimal_date:
    print(decimal_date[k])
    print(sagA_coord_x[k], sagA_coord_y[k])
    
# generate list of orbital positions l for k=0
    l = 0
    for offset in perfect_offsets_x:
        orb_x = perfect_offsets_x[l] + sagA_coord_x[k]
        orb_y = perfect_offsets_y[l] + sagA_coord_y[k]
        orbit_x_1.append(round(orb_x, 2))
        orbit_y_1.append(round(orb_y, 2))
        l+=1  
    print("\n" + "Points to show orbit")    
    print(orbit_x_1)
    print(orbit_y_1)
    print("\n")
    
# j = loop to write the line to plot each orbit pos
    j = 1
    for item in orbit_x_1:        
# time period included inside and outside timeline use different colors
        if perfect_offsets_date[j-1] <= 2002 or perfect_offsets_date[j-1] >= 2016:
            overlay_output.writelines('ax' + str(k+1) + ".scatter(" + str(orbit_x_1[j-1]) + "-1, " + str(orbit_y_1[j-1]) + "-1, " + pt_size + ", facecolors='none', color='" + out_range_color + "', marker='o')" + "\n")
        else:
            overlay_output.writelines('ax' + str(k+1) + ".scatter(" + str(orbit_x_1[j-1]) + "-1, " + str(orbit_y_1[j-1]) + "-1, " + pt_size + ", facecolors='none', color='" + in_range_color + "', marker='o')" + "\n")
        j+=1
    
    orbit_x_1.clear()
    orbit_y_1.clear()          
    k+=1

################################################    
    
## v7a Update: Using all other subplots' offsets/data points
## Result is not satisfactory

# # subplot index
# k=0
# print(decimal_date[k])
# print(sagA_coord_x[k], sagA_coord_y[k])

# print("\n" + "Offsets")
# print(offset_pix_x)
# print(offset_pix_y)

# orbit_x_1 = []
# orbit_y_1 = []

# # generate list of orbital pos in k=0
# l = 0
# for offset in offset_pix_x:
#     orb_x = offset_pix_x[l] + sagA_coord_x[k]
#     orb_y = offset_pix_y[l] + sagA_coord_y[k]
#     orbit_x_1.append(round(orb_x, 2))
#     orbit_y_1.append(round(orb_y, 2))
#     l+=1
# print("\n" + "Points to show orbit")    
# print(orbit_x_1)
# print(orbit_y_1)
# print("\n")

# # k = subplot index
# # mm = loop the orbit points
# pt_size = "s=1"
# mm = 1
# for item in orbit_x_1:
#     print('ax' + str(k+1) + ".scatter(" + str(orbit_x_1[mm-1]) + "-1, " + str(orbit_y_1[mm-1]) + "-1, " + pt_size + ", facecolors='none', color='aqua', marker='o')" + "\n")
#     mm+=1

#=======================================================================

## v8 Update: Summary of all values used in the code for potential double-checking

# There are these values in records:
# decimal_date 
# FITS file names
# sagA_coord_x
# sagA_coord_y 
# offset_pix_x 
# offset_pix_y 
# calculated_obj_coord_x
# calculated_obj_coord_y

summary_output.writelines("Summary of all values used in Object " + str(object_name) + " timeline plot code:" + "\n")
summary_output.writelines("Check with other records, ie: Excel to verify all the related inputs are correct" + "\n")
summary_output.writelines("Date\tDecimal_date\tSagA x\ty\tObj_offset_pix x\ty\tCalc_obj coord x\ty\tFITS filename" + "\n")

summary_index = 0
for entry in files:
    date_yyyy = entry[0:10]
    summary_output.writelines(date_yyyy + "\t")
    summary_output.writelines(str(decimal_date[summary_index]) + "\t")
    summary_output.writelines(str(sagA_coord_x[summary_index]) + "\t")
    summary_output.writelines(str(sagA_coord_y[summary_index]) + "\t")
    summary_output.writelines(str(round(offset_pix_x[summary_index],2)) + "\t")
    summary_output.writelines(str(round(offset_pix_y[summary_index],2)) + "\t")
    summary_output.writelines(str(calculated_obj_coord_x[summary_index]) + "\t")
    summary_output.writelines(str(calculated_obj_coord_y[summary_index]) + "\t")
    summary_output.writelines(files[summary_index] + "\t")    
    summary_output.writelines("\n")
    summary_index+=1

#=======================================================================
#=======================================================================

print("Generate Timeline Plot Code Successful")
print("Generate Timeline Orbit Trajectory Code Successful")
print("Summarize Timeline Plot Values Successful")
    
fits_list_input.close()
sagA.close()
best_point_v2.close()
perfect_offsets_pix.close()
code_output.close()  
overlay_output.close()  
summary_output.close()


# #=======================================================================
# #=======================================================================

# #### The stuff outside main body in Timeline_code.py, in case the example file was lost

# # Code that generates a progressive timeline map from FITS files and given positions

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

# # Main Body, paste everything from Code_output.py in here
# # Paste everything from code_overlay_output.py in here for orbital trajectory

# ########################

# plt.tight_layout()
# plt.subplots_adjust(wspace=-.6, hspace =.2)#,vspace= -.1)
# plt.savefig('test.png', dpi=500)#, bbox_inches='tight')
# plt.show()
# plt.close()
