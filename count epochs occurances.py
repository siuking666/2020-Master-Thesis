## count the occurances of epochs in all position files
## hence giving a way to determine which epochs are most ideal as finding chart overview

candidates = open("candidates.txt", "r") 
all_epochs = open("all epochs.txt", "r") 
out = open("epoch occurance.txt", "w+") 

occured_epoch = []
all_epochsl = []

for item in candidates.readlines():
    item1 = item.replace("\n", "")
    file = open(str(item1) + "_condensed.txt", "r") 
    
    for line in file.readlines():
        line_entries = line.split("\t")
        occured_epoch.append(line_entries[0])
        
    file.close()
    
#print(occured_epoch)

for item11 in all_epochs.readlines():
    all_epochsl.append(item11.replace("\n", ""))
    
#print(all_epochsl)

for x in all_epochsl:
    print(x, occured_epoch.count(x))
    out.writelines(str(x) + "\t" + str(occured_epoch.count(x)) + "\n")

candidates.close()
all_epochs.close()   
out.close()    

# =====================================
# candidates.txt input
# 1
# 2
# 3
# 4
# 5

# all epochs.txt input
# 2002.578
# 2003.446
# 2003.452
# 2003.455
# 2004.511