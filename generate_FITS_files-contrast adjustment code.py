#### generate code that identify a FITS file and respective brightness/contrast adjustments

filename_n_brightness = open("filename_brightness.txt", "r") 
out = open("out.txt", "w+")

fits_file = []
brightness_code = []

for line in filename_n_brightness.readlines():
    line_entries = line.replace("\n", "").split("\t")
    fits_file.append(line_entries[0])
    brightness_code.append(line_entries[1])
     
print(fits_file)
print(brightness_code)

i=0
for item in fits_file:
    out.writelines("\t" + "elif item == '" + fits_file[i] + "':" + "\n")
    out.writelines("\t" + "\t" + "code_output.writelines('" + brightness_code[i] + "'" + " + '\\n')" + "\n")
    i += 1
    
#     if item == '2002_07_31_98_subim42.nice.fits':
#         code_output.writelines('image_2002_07_31t = np.sqrt((image_2002_07_31/8e+4)**2) + 1e-20' + "\n")

filename_n_brightness.close()
out.close()

