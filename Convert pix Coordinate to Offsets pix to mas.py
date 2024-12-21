# Calculate the offsets from Sgr A* in pixels, then convert offsets & errors in pixels to marcsec
# Expected to read the format in "Dates (3 decimals), X, Y, Error X, Error Y (in pixel unit)"
# Need a reference table of Sgr A* pixel coordinate positions

#=============================================================
#=============================================================

# reads the "found positions" file

# CHECK THE INPUT FILE NAME 
# FILE SHOULD BE PURELY NUMBERS
found_coordinates = open("test.txt", 'r')

SagA_pix_coordinates = open("Sag A Pixel Coordinates.txt", 'r')
output_offset_pixel_file = open("object offsets in pix.txt", 'w+')

list_found_coord_float = []
list_sagA_coord_float = []
list_offsets_pix = []

#=============================================================
# PROBLEMS:
# 1) NEED TO ADD ZEROES TO THE ERROR WHERE THERE IS EMPTY
# 2) NEED TO KEEP THE EMPTY DATES FOR CALCULATION ITERATION
# 3) DELETE THOSE EMPTY DATES AFTERWARDS

for line, found_coord in enumerate(found_coordinates.readlines()):
    split_found_coord = found_coord.replace('\n', '').split("\t")

# fill the empty entries with zeroes
# convert them to float for numerical operations
    for item in range(len(split_found_coord)):
        if split_found_coord[item] == str(''):
            split_found_coord[item] = str('0')                
    for item in split_found_coord:
        list_found_coord_float.append(float(item))
        
print("Imported Coord master list")     
print(list_found_coord_float)       

# Put the Sag A coordinates in a list                
# starting at 3rd line, ignore headers

for k, sagA_coord in enumerate(SagA_pix_coordinates.readlines()):
    if k >= 2:
        split_sagA_coord = sagA_coord.split("\t")    
        for SagA in split_sagA_coord:
            list_sagA_coord_float.append(float(SagA))  
            
# adding 2 zeros per date as Errors to make calculation simpler
        list_sagA_coord_float.append(float(0))
        list_sagA_coord_float.append(float(0))

print("Sag A Coord master list")        
print(list_sagA_coord_float)  
            
#=============================================================         
# using the pixel positions of Sgr A*, calculate the offset distances in pixel units
# iterate and deduct one list from another 
# NEED TO KEEP THE EMPTY DATES FOR CALCULATION ITERATION

for index, (a, b) in enumerate(zip(list_found_coord_float, list_sagA_coord_float)):
    index_per_line = 5
    
    # dont change the dates
    if index % index_per_line == 0:
        list_offsets_pix.append(a)
        
    # if position is empty, skip
    if index % index_per_line == 1:
        if a == 0:
            list_offsets_pix.append(a)
        else:
            list_offsets_pix.append(round((a-b), 3))
            
    if index % index_per_line == 2:
        if a == 0:
            list_offsets_pix.append(a)
        else:
            list_offsets_pix.append(round((a-b), 3))

    # No need to skip Errors as Sag A* errors are ZERO
    # errors, written to add for generalization
    if index % index_per_line == 3:
        list_offsets_pix.append(a+b)
            
    if index % index_per_line == 4:
        list_offsets_pix.append(a+b)             
            
print('calculated offsets in pix')        
print(list_offsets_pix) 

# write the result to output file
# Format: "Dates (3 decimals), X, Y (in pixel)"

for index, coordinate in enumerate(list_offsets_pix):
    new_line_every = 5
    if index % new_line_every == 4:
        output_offset_pixel_file.write("%s\n" % coordinate)
    else:
        output_offset_pixel_file.write("%s\t" % coordinate)
    
#=============================================================   
        
# close all files
found_coordinates.close()
SagA_pix_coordinates.close()
output_offset_pixel_file.close()

#=============================================================  
#=============================================================  

# converts the (X, Y) offsets & Errors to RA/DEC to marcsec unit 
# DELETE THOSE EMPTY DATES FROM OUTPUT

# CHECK THE INPUT FILE NAME 
# FILE SHOULD BE PURELY NUMBERS
offset_pixel_file = open("object offsets in pix.txt", 'r')
output_offset_marcsec_file = open("object offsets in marcsec.txt", 'w+')

list_offsets_errors_marcsec_float = []

#=============================================================  

# read the lines, whole line as one string needs to be split
for line, offsets in enumerate(offset_pixel_file.readlines()):
    split_offsets_pix = offsets.replace('\n', '').split("\t")
    print(split_offsets_pix)

# convert them to float for numerical operations
# if any offset is zero (empty) , ignore that date-line

    for j, item in enumerate(split_offsets_pix):
        if split_offsets_pix[1] == str('0.0'):
            split_offsets_pix.clear           
        elif split_offsets_pix[2] == str('0.0'):
            split_offsets_pix.clear
            
# if the date entry is valid, convert the units
# the dates do not need to be changed
        else:
            if j == 0:
                list_offsets_errors_marcsec_float.append(float(item))
                
# RA is inverted from X-axis             
            if j == 1:
                number_marcsec = round(float(item)*-13.3, 5) 
                list_offsets_errors_marcsec_float.append(number_marcsec)
            
# DEC is not inverted             
            if j == 2:
                number_marcsec = round(float(item)*13.3, 5)
                list_offsets_errors_marcsec_float.append(number_marcsec)   

# add 0.5 pix as systematic error then convert units                
            if j == 3:
                number_marcsec = round((float(item)+0.5)*13.3, 5)
                list_offsets_errors_marcsec_float.append(number_marcsec) 
                
            if j == 4:
                number_marcsec = round((float(item)+0.5)*13.3, 5)
                list_offsets_errors_marcsec_float.append(number_marcsec)                
                 
print("Imported offsets & errors pix master list")     
print(list_offsets_errors_marcsec_float)       

# write the result to output file
# Format: "Dates (3 decimals), RA, DEC, Error RA, Error DEC (in marcsec)"

for index, offset in enumerate(list_offsets_errors_marcsec_float):
    new_line_every = 5
    if index % new_line_every == 4:
        output_offset_marcsec_file.write("%s\n" % offset)
    else:
        output_offset_marcsec_file.write("%s\t" % offset)
        
#=============================================================   
        
# close all files
offset_pixel_file.close()
output_offset_marcsec_file.close()


