#### this code takes the best_points file, read the date entries, and return the list of FITS filenames.
## input file: #_best_points file where decimal dates are placed at the beginning of line
## output files: #_FITS_filenames_list.txt where the date-corresponding FITS filenames are listed
## the output file can then be used in the "generate codes of timeline code.py"

## GIVE OBJECT NUMBER HERE
object_name = 8

## Input file:
timeline_dates_input = open(str(object_name)+"_best_points v2.txt", "r") 
fits_list_output = open(str(object_name)+"_FITS_filenames_list.txt", "w+") 

#=======================================================================

dates =[]
line_entries = []
output = []

for line in timeline_dates_input.readlines():
    line_entries = line.replace("\n", "").split("\t")
    print(line_entries)    
    dates.append(line_entries[0])

print("List of dates detected in the input document:")
print(dates)

i=0

for item in dates:
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

        
print("List of FITS filenames:")        
print(output)


for file in output:
    fits_list_output.writelines(file + "\n")
        
timeline_dates_input.close()
fits_list_output.close()

#=======================================================================

# #### generate code for matching 51 dates and 51 files

# # datess = open("all_dates.txt", "r") 
# # fitss = open("all_fits.txt", "r") 
# out = open("out.txt", "w+")

# dates = ['2002.578', '2003.446', '2003.452', '2003.455', '2004.511', '2004.516', '2004.574', '2004.669', '2004.727', '2005.268', '2005.37', '2005.466', '2005.562', '2005.583', '2006.49', '2006.583', '2006.726', '2006.729', '2006.753', '2007.205', '2007.214', '2007.255', '2007.455', '2008.145', '2008.197', '2008.268', '2008.456', '2008.598', '2008.708', '2009.299', '2009.301', '2009.334', '2009.37', '2009.501', '2009.605', '2009.611', '2009.715', '2009.718', '2010.238', '2010.351', '2010.444', '2010.455', '2010.46', '2011.4', '2012.374', '2013.488', '2013.666', '2015.581', '2016.221', '2017.455', '2018.309']
# fits = ['2002_07_31_98_subim42.nice.fits', '2003_06_13_mosaic.nice.fits', '2003_06_15_mosaic.fits', '2003_06_16_mosaic.fits', '2004_07_06_561_subim14.nice.fits', '2004_07_08_255_subim105.nice.fits', '2004_07_29_48_mosaic.fits', '2004_09_02_mosaic.fits', '2004_09_23_mosaic.fits', '2005_04_09_mosaic.fits', '2005_05_16_mosaicc.fits', '2005_06_20_mosaic.fits', '2005_07_25_subim90.nice.fits', '2005_08_02_subim19.nice.fits', '2006_06_29_111_subim56.nice.fits', '2006_08_02_mosaic.fits', '2006_09_23_55_mosaic.fits', '2006_09_24_65_mosaic.fits', '2006_10_03_mosaic.fits', '2007_03_17_S13_mosaic.fits', '2007_03_20_20_mosaic.fits', '2007_04_04_mosaic.fits', '2007_06_16_A_mosaic.fits', '2008_02_23_mosaic.fits', '2008_03_13_mosaic.fits', '2008_04_08_mosaic.fits', '2008_06_16_mosaic.fits', '2008_08_07_mosaic.fits', '2008_09_16_mosaic.fits', '2009_04_20_mosaic.fits', '2009_04_21_mosaic.fits', '2009_05_03_mosaic.fits', '2009_05_16_mosaic.fits', '2009_07_03_mosaic.fits', '2009_08_10_mosaic.fits', '2009_08_12_mosaic.fits', '2009_09_19_S13_mosaic.fits', '2009_09_20_S13_mosaic.fits', '2010_03_29_mosaic.fits', '2010_05_09_42_mosaic.fits', '2010_06_12_mosaic.fits', '2010_06_16_mosaic.fits', '2010_06_18_mosaic.fits', '2011_05_27_median.nice.fits', '2012_05_17_median.nice.fits', '2013_06_28_median.nice.fits', '2013_09_01_mosaic.fits', '2015_08_01_median.nice.fits', '2016_3_22_decon.fits', '2017_6_16_decon.fits', '2018_04_24_mosaic.fits']

# # for item in datess.readlines():
# #     dates.append(item.replace("\n", ""))
    
# # for item in fitss.readlines():
# #     fits.append(item.replace("\n", ""))    

# i=0

# for item in dates:
#     out.writelines("\t" + "elif item == '" + dates[i] + "':" + "\n")
#     out.writelines("\t" + "\t" + "output.append('" + fits[i] + "')" + "\n")
#     i += 1
    
# #     if item == '2003.452':
# #         output.append('2003_06_15_mosaic.fits')

# # datess.close()
# # fitss.close()
# out.close()

