import glob
import os

print(os.getcwd())

files = []
for file in glob.glob("*.fits"):
    files.append(file)
print(files)

fits_list_output = open("FITS_files_list.txt", "w+") 

for item in files:
    fits_list_output.writelines(item + "\n")

fits_list_output.close()

