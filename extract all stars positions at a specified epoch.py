## This code checks all candidates' position files and output the positions for the given epoch

## Give the epoch to extract
epoch = "2008.598"

#==============================================
candidates = open("candidates.txt", "r") 
out = open(str(epoch) + " candidates positions.txt", "w+") 


for cand in candidates.readlines():
    cand1 = cand.replace("\n", "")
    file = open(str(cand1) + "_condensed.txt", "r") 

    for line in file.readlines():
        line_entries = line.split("\t")
        if line_entries[0] == epoch:
            break
    
    if line_entries[0] == epoch:
        print(cand.replace("\n", "\t") + line_entries[0], line_entries[1], line_entries[2])
        out.writelines(cand.replace("\n", "\t") + line_entries[0] + "\t" + line_entries[1] + "\t" + line_entries[2] + "\n")
    else:
        print(cand.replace("\n", "\t"))
        out.writelines(cand.replace("\n", "\t") + "\n")
        
    file.close()
    
candidates.close()
out.close()    

#==============================================
# candidate.txt input
# 1
# 2
# 3
# 4
# 5
# 115