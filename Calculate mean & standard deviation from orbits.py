import math

file = open("input.txt", "r") 
out = open("temp.txt", "a") 

lines = []
output= []

for line in file.readlines():
    line_entries = line.replace("\n", "").replace("Minimized variables result: ", "")
    lines.append(line_entries)

standard = (lines[2]) #standard
odd = (lines[5]) #odd
even = (lines[8]) #even

standard_s = standard.split(" , ")
odd_s = odd.split(" , ")
even_s = even.split(" , ")

standard_ss = []
odd_ss = []
even_ss = []
for item in standard_s:
    standard_ss.append(float(item))
for item in odd_s:
    odd_ss.append(float(item))    
for item in even_s:
    even_ss.append(float(item))

print(standard_ss)
print(odd_ss)
print(even_ss)
print('\n')

#==================================================================

# # Calculate the difference between standard result AND odd & even
# # Return the larger difference as error

# i = 0
# for item in standard_ss:
#     error_odd = abs(odd_ss[i] - standard_ss[i])
#     error_even = abs(even_ss[i] - standard_ss[i])
    
#     print(item)
#     print(max(error_odd, error_even))
    
#     output.append(round(item,3))
#     output.append(round(max(error_odd, error_even),3))

#     print('\n')
#     i+=1

# print(output)

# for item in output:
#     out.writelines(str(item) + "\t")
# out.writelines("\n")

#==================================================================

# Calculate the Mean & standard deviation from standard result AND odd & even
# Return them

i = 0
for item in standard_ss:
    mean = (standard_ss[i] + odd_ss[i] + even_ss[i])/3
    standard_deviation = math.sqrt( ( (standard_ss[i]-mean)**2 + (odd_ss[i]-mean)**2 + (even_ss[i]-mean)**2) /3)
    
    print(item)
    print(mean)
    print(standard_deviation)
    
    output.append(round(item,3))
    output.append(round(mean,3))
    output.append(round(standard_deviation,3))

    print('\n')
    i+=1

print(output)

for item in output:
    out.writelines(str(item) + "\t")
out.writelines("\n")

file.close()
out.close()

#=========================================
# Example input file

# #11
# likelihood: 498.1664422481465
# Minimized variables result: 40.54110307985115 , 0.8985669141432097 , 1.4226570255697937 , 0.6597333059145707 , 5.36571504487573 , 2029.697127162629
 
# likelihood: 213.5629822450236
# Minimized variables result: 40.28779651156245 , 0.8496920048917918 , 1.4022343490453084 , 0.4851962225518836 , 5.30882209539255 , 2030.361145449309

# likelihood: 192.54180274894995
# Minimized variables result: 40.656513361875284 , 0.962700833553225 , 1.472904620699895 , 0.9472700929362511 , 5.524465955664864 , 2029.399152266973
