file = open("epoch list.txt", "r") 
out = open("appendix finding chart.txt", "a") 

epoch_list = []

for line in file.readlines():
    line_entries = line.replace("\n", "")
    epoch_list.append(line_entries)
    
print(epoch_list)

for item in epoch_list:
    out.writelines("\\subsection{" + str(item) + "}" + "\n")
   
    out.writelines("\\begin{figure}[H]" + "\n")
    out.writelines("\t\\includegraphics[width=\\linewidth]{./ALL Finding Charts/" + str(item) + "}" + "\n")
    out.writelines("\t\\caption[T]{Finding Chart of " + str(item) + "}" + "\n")
    out.writelines("\\end{figure}" + "\n")
    out.writelines("\n")
    
file.close()
out.close()    


# \subsection{2002.578}
# 
# \begin{figure}[H]
# 	\includegraphics[width=\textwidth]{./Figures/5/2003.452}
# 	\caption[T]{Finding Chart of 2003.452}
# \end{figure}
# \pagebreak

# ===========================
# Example input:

# 2002.578
# 2003.446
# 2003.452
# 2003.455
# 2004.511
# 2004.516