#### this code takes the best_points file, read the date entries, and return the list of Sag A coordinates
## input file: #_best_points file where decimal dates are placed at the beginning of line
## output files: #_sagA_coordinates.txt where the decimal dates, and SagA x, y coordinates are listed
## the output file can then be used in the "generate codes of timeline code.py"


## GIVE OBJECT NUMBER HERE
object_name = 8

## Input file:
timeline_dates_input = open(str(object_name)+"_best_points v2.txt", "r") 
sagA_coord_output = open(str(object_name)+"_sagA_coordinates.txt", "w+")

#=======================================================================

dates = []
line_entries = []
output = []

for line in timeline_dates_input.readlines():
    line_entries = line.replace("\n", "").split("\t")
    print(line_entries)    
    dates.append(line_entries[0])

print("List of dates detected in the input document:")
print(dates)


for item in dates:
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
   
        
print("List of respective Sag A coordinates:")        
print(output)


for file in output:
    sagA_coord_output.writelines(file + "\n")
        
timeline_dates_input.close()
sagA_coord_output.close()

#=======================================================================

# #### generate code for matching 51 dates and 51 Sag A coordinates

# sagA_file = open("sagA_all.txt", "r") 
# out = open("out.txt", "w+")

# dates= []
# x = []
# y = []

# for line in sagA_file.readlines():
#     line_entries = line.replace("\n", "").split("\t")
#     dates.append(line_entries[0])
#     x.append(line_entries[1])
#     y.append(line_entries[2])
    
# # print(dates)
# # print(x)
# # print(y)

# i=0

# for item in dates:
#     out.writelines("\t" + "elif item == '" + dates[i] + "':" + "\n")
#     out.writelines("\t" + "\t" + "output.append('" + dates[i] + "\\t" + x[i] + "\\t" + y[i] + "')" + "\n")
#     i += 1
    
# # 	if item == '2003.452':
# # 		output.append('2003.452\t168.32\t159.26')

# sagA_file.close()
# out.close()

