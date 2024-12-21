## Specify epoch & respective SagA* coordinates
## The code then converts all given objects' pixel-coordinates to marcsec offsets

epoch = 2010.238
sagA_coordinate_x = 162.955973
sagA_coordinate_y = 152.4342826

star_positions = open("convert.txt", "r")
output = open(str(epoch)+" star offsets.txt", "w+")

################################################

star_name = []
obj_coord_x = []
obj_coord_y = []
calculated_offset_pix_x = []
calculated_offset_pix_y = []
   
## Auto Object coordinates calculation from Offset

## position file contains the offset of object in marcsec
## Import the offsets as pixel unit

for line in star_positions.readlines():
    star_coord = line.replace("\n", "").split("\t")
    star_name.append(str(star_coord[0]))
    obj_coord_x.append((((float(star_coord[1])))))
    obj_coord_y.append((((float(star_coord[2])))))
    
## Calculate the object coordinates:

i = 0
for item in star_name:
    calc_x = (obj_coord_x[i] - sagA_coordinate_x)*-13.3
    calc_y = (obj_coord_y[i] - sagA_coordinate_y)*13.3
    calculated_offset_pix_x.append(round(calc_x, 2))
    calculated_offset_pix_y.append(round(calc_y, 2))
    i += 1    

j=0
for item in star_name:
    output.writelines(str(item) + "\t" + str(calculated_offset_pix_x[j]) + "\t" + str(calculated_offset_pix_y[j]) + "\n")
    j += 1
    
star_positions.close()
output.close()

################################################
# input example:
# S25	171	121
# S7	125.5	148
# S59	178	170
# S54	155	141.5