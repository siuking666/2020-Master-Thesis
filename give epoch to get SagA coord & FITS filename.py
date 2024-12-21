#### this code takes the EPOCH (and positions file if you wish), returns the SagA* coordinates & FITS filenames
## input file: EPOCH POSITIONS file where decimal dates are placed at the second of line
## output files: #_sagA_coordinates.txt where the decimal dates, and SagA x, y coordinates are listed
## output files: #_FITS_filenames_list.txt where the date-corresponding FITS filenames are listed
## the output file can then be used in the "generate codes of finding chart code.py"

#### Obviously modified from my previous codes used for making the timelines

## GIVE EPOCH HERE
epoch = 2010.238

#=======================================================================
## Input file:
# timeline_dates_input = open(str(epoch)+" candidates positions.txt", "r") 

## Output files:
sagA_coord_output = open(str(epoch)+"_sagA_coordinates.txt", "w+")
fits_list_output = open(str(epoch)+"_FITS_filenames_list.txt", "w+") 

epochl = []
epochl.append(str(epoch))
print("Epoch/Date given:", str(epoch))
output = []

for item in epochl:
	if item == '2002.578':
		output.append('2002.578\t167.09\t181.54')
	elif item == '2003.446':
		output.append('2003.446\t102.98\t106.44')
	elif item == '2003.452':
		output.append('2003.452\t168.32\t159.26')
	elif item == '2003.455':
		output.append('2003.455\t169.13\t160.16')
	elif item == '2004.511':
		output.append('2004.511\t168.85\t182.76')
	elif item == '2004.516':
		output.append('2004.516\t165.86\t176.08')
	elif item == '2004.574':
		output.append('2004.574\t1022.27\t1028.88')
	elif item == '2004.669':
		output.append('2004.669\t166.55\t154.88')
	elif item == '2004.727':
		output.append('2004.727\t166.50\t156.81')
	elif item == '2005.268':
		output.append('2005.268\t1014.95\t1008.81')
	elif item == '2005.37':
		output.append('2005.37\t166.13\t153.79')
	elif item == '2005.370':
		output.append('2005.37\t166.13\t153.79')       
	elif item == '2005.466':
		output.append('2005.466\t167.34\t154.48')
	elif item == '2005.562':
		output.append('2005.562\t167.09\t179.13')
	elif item == '2005.583':
		output.append('2005.583\t166.41\t178.72')
	elif item == '2006.49':
		output.append('2006.49\t166.99\t179.43')
	elif item == '2006.490':
		output.append('2006.49\t166.99\t179.43')
	elif item == '2006.583':
		output.append('2006.583\t769.11\t766.59')
	elif item == '2006.726':
		output.append('2006.726\t857.50\t799.51')
	elif item == '2006.729':
		output.append('2006.729\t796.16\t764.93')
	elif item == '2006.753':
		output.append('2006.753\t803.04\t719.73')
	elif item == '2007.205':
		output.append('2007.205\t740.80\t710.49')
	elif item == '2007.214':
		output.append('2007.214\t732.15\t713.51')
	elif item == '2007.255':
		output.append('2007.255\t734.92\t715.12')
	elif item == '2007.455':
		output.append('2007.455\t747.44\t767.27')
	elif item == '2008.145':
		output.append('2008.145\t728.17\t682.03')
	elif item == '2008.197':
		output.append('2008.197\t716.03\t753.99')
	elif item == '2008.268':
		output.append('2008.268\t725.01\t733.05')
	elif item == '2008.456':
		output.append('2008.456\t734.96\t752.21')
	elif item == '2008.598':
		output.append('2008.598\t709.78\t722.53')
	elif item == '2008.708':
		output.append('2008.708\t737.28\t779.38')
	elif item == '2009.299':
		output.append('2009.299\t725.50\t755.82')
	elif item == '2009.301':
		output.append('2009.301\t740.05\t756.85')
	elif item == '2009.334':
		output.append('2009.334\t712.00\t750.15')
	elif item == '2009.37':
		output.append('2009.37\t727.66\t756.64')
	elif item == '2009.370':
		output.append('2009.37\t727.66\t756.64')  
	elif item == '2009.501':
		output.append('2009.501\t711.62\t757.59')
	elif item == '2009.605':
		output.append('2009.605\t756.92\t758.94')
	elif item == '2009.611':
		output.append('2009.611\t723.17\t757.55')
	elif item == '2009.715':
		output.append('2009.715\t743.62\t727.44')
	elif item == '2009.718':
		output.append('2009.718\t748.41\t751.19')
	elif item == '2010.238':
		output.append('2010.238\t162.96\t152.43')
	elif item == '2010.351':
		output.append('2010.351\t737.54\t759.23')
	elif item == '2010.444':
		output.append('2010.444\t726.92\t754.19')
	elif item == '2010.455':
		output.append('2010.455\t745.92\t747.02')
	elif item == '2010.46':
		output.append('2010.46\t725.73\t748.22')
	elif item == '2010.460':
		output.append('2010.46\t725.73\t748.22')
	elif item == '2011.4':
		output.append('2011.4\t91.32\t102.49')
	elif item == '2011.400':
		output.append('2011.4\t91.32\t102.49')
	elif item == '2012.374':
		output.append('2012.374\t100.29\t96.86')
	elif item == '2013.488':
		output.append('2013.488\t97.77\t93.20')
	elif item == '2013.666':
		output.append('2013.666\t160.88\t155.32')
	elif item == '2015.581':
		output.append('2015.581\t59.15\t91.13')
	elif item == '2016.221':
		output.append('2016.221\t35.88\t34.83')
	elif item == '2017.455':
		output.append('2017.455\t36.68\t38.27')
	elif item == '2018.309':
		output.append('2018.309\t161.10\t162.21')

print("Output SagA* coordinates:", str(output))

for file in output:
    sagA_coord_output.writelines(file + "\n")
output.clear()

#=======================================================================
# FITS filename part

for item in epochl:
	if item == '2002.578':
		output.append('2002_07_31_98_subim42.nice.fits')
	elif item == '2003.446':
		output.append('2003_06_13_mosaic.nice.fits')
	elif item == '2003.452':
		output.append('2003_06_15_mosaic.fits')
	elif item == '2003.455':
		output.append('2003_06_16_mosaic.fits')
	elif item == '2004.511':
		output.append('2004_07_06_561_subim14.nice.fits')
	elif item == '2004.516':
		output.append('2004_07_08_255_subim105.nice.fits')
	elif item == '2004.574':
		output.append('2004_07_29_48_mosaic.fits')
	elif item == '2004.669':
		output.append('2004_09_02_mosaic.fits')
	elif item == '2004.727':
		output.append('2004_09_23_mosaic.fits')
	elif item == '2005.268':
		output.append('2005_04_09_mosaic.fits')
	elif item == '2005.37':
		output.append('2005_05_16_mosaicc.fits')
	elif item == '2005.370':
		output.append('2005_05_16_mosaicc.fits')    
	elif item == '2005.466':
		output.append('2005_06_20_mosaic.fits')
	elif item == '2005.562':
		output.append('2005_07_25_subim90.nice.fits')
	elif item == '2005.583':
		output.append('2005_08_02_subim19.nice.fits')
	elif item == '2006.49':
		output.append('2006_06_29_111_subim56.nice.fits')
	elif item == '2006.490':
		output.append('2006_06_29_111_subim56.nice.fits')        
	elif item == '2006.583':
		output.append('2006_08_02_mosaic.fits')
	elif item == '2006.726':
		output.append('2006_09_23_55_mosaic.fits')
	elif item == '2006.729':
		output.append('2006_09_24_65_mosaic.fits')
	elif item == '2006.753':
		output.append('2006_10_03_mosaic.fits')
	elif item == '2007.205':
		output.append('2007_03_17_S13_mosaic.fits')
	elif item == '2007.214':
		output.append('2007_03_20_20_mosaic.fits')
	elif item == '2007.255':
		output.append('2007_04_04_mosaic.fits')
	elif item == '2007.455':
		output.append('2007_06_16_A_mosaic.fits')
	elif item == '2008.145':
		output.append('2008_02_23_mosaic.fits')
	elif item == '2008.197':
		output.append('2008_03_13_mosaic.fits')
	elif item == '2008.268':
		output.append('2008_04_08_mosaic.fits')
	elif item == '2008.456':
		output.append('2008_06_16_mosaic.fits')
	elif item == '2008.598':
		output.append('2008_08_07_mosaic.fits')
	elif item == '2008.708':
		output.append('2008_09_16_mosaic.fits')
	elif item == '2009.299':
		output.append('2009_04_20_mosaic.fits')
	elif item == '2009.301':
		output.append('2009_04_21_mosaic.fits')
	elif item == '2009.334':
		output.append('2009_05_03_mosaic.fits')
	elif item == '2009.37':
		output.append('2009_05_16_mosaic.fits')
	elif item == '2009.370':
		output.append('2009_05_16_mosaic.fits')
	elif item == '2009.501':
		output.append('2009_07_03_mosaic.fits')
	elif item == '2009.605':
		output.append('2009_08_10_mosaic.fits')
	elif item == '2009.611':
		output.append('2009_08_12_mosaic.fits')
	elif item == '2009.715':
		output.append('2009_09_19_S13_mosaic.fits')
	elif item == '2009.718':
		output.append('2009_09_20_S13_mosaic.fits')
	elif item == '2010.238':
		output.append('2010_03_29_mosaic.fits')
	elif item == '2010.351':
		output.append('2010_05_09_42_mosaic.fits')
	elif item == '2010.444':
		output.append('2010_06_12_mosaic.fits')
	elif item == '2010.455':
		output.append('2010_06_16_mosaic.fits')
	elif item == '2010.46':
		output.append('2010_06_18_mosaic.fits')
	elif item == '2010.460':
		output.append('2010_06_18_mosaic.fits')
	elif item == '2011.4':
		output.append('2011_05_27_median.nice.fits')
	elif item == '2011.400':
		output.append('2011_05_27_median.nice.fits')
	elif item == '2012.374':
		output.append('2012_05_17_median.nice.fits')
	elif item == '2013.488':
		output.append('2013_06_28_median.nice.fits')
	elif item == '2013.666':
		output.append('2013_09_01_mosaic.fits')
	elif item == '2015.581':
		output.append('2015_08_01_median.nice.fits')
	elif item == '2016.221':
		output.append('2016_3_22_decon.fits')
	elif item == '2017.455':
		output.append('2017_6_16_decon.fits')
	elif item == '2018.309':
		output.append('2018_04_24_mosaic.fits')

print("Output FITS filenames:", str(output))        

for file in output:
    fits_list_output.writelines(file + "\n")
output.clear()   
    
# # count useless occurances of given epoch in input file, good for...checking consistency, I guess?
# dates = []
# for line in timeline_dates_input.readlines():
#     line_entries = line.replace("\n", "").split("\t")
#     #print(line_entries)    
#     dates.append(line_entries[1])
# print("Dates & Counts detected in the input file: ", str(epoch), str(dates.count(str(epoch))))

# timeline_dates_input.close()

sagA_coord_output.close()
fits_list_output.close()