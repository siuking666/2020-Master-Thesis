file = open("candidate list.txt", "r") 
out = open("appendix orbit and timeline.txt", "a") 

candidate_list = []

for line in file.readlines():
    line_entries = line.replace("\n", "")
    candidate_list.append(line_entries)
    
print(candidate_list)

for item in candidate_list:
    out.writelines("\subsection{Candidate \#" + str(item) + "}" + "\n")
    out.writelines("\\begin{figure}[H]" + "\n")
    out.writelines("\t\\centering" + "\n")
    out.writelines("\t\\begin{subfigure}[b]{\\textwidth}" + "\n")
    out.writelines("\t\t\\centering" + "\n")
    out.writelines("\t\t\\includegraphics[width=\\textwidth]{./ALL Orbit Plots/" + str(item) +"}" + "\n")
    out.writelines("\t\t\\caption{Orbital Plot between 2000-2020}" + "\n")
    out.writelines("\t\\end{subfigure}" + "\n")
    out.writelines("\t\\hfill" + "\n")
    
    out.writelines("\t\\begin{subfigure}[b]{\\textwidth}" + "\n")
    out.writelines("\t\t\\centering" + "\n")
    out.writelines("\t\t\\includegraphics[width=\\textwidth]{./ALL Orbit Plots/" + str(item) + "a}" + "\n")
    out.writelines("\t\t\\caption{Orbital Plot for a Full Orbit}" + "\n")
    out.writelines("\t\\end{subfigure}" + "\n")
    out.writelines("\t\\hfill" + "\n")
    out.writelines("\t\\caption{Orbital Plots of Candidate \#" + str(item) + "}" + "\n")
    out.writelines("\end{figure}" + "\n")
    
    out.writelines("\\begin{figure}[H]" + "\n")
    out.writelines("\t\\includegraphics[width=\\linewidth]{./ALL Timeline Plots/" + str(item) + " Timeline}" + "\n")
    out.writelines("\t\\caption[T]{Timeline Plot of Candidate \#" + str(item) + "}" + "\n")
    out.writelines("\\end{figure}" + "\n")
    out.writelines("\n")

    
file.close()
out.close()    
    
# \subsection{Candidate \#1}
# \begin{figure}[H]
# 	\centering
# 	\begin{subfigure}[b]{\textwidth}
# 		\centering
# 		\includegraphics[width=\textwidth]{./ALL Orbit Plots/5/1}
# 		\caption{Orbital Plot between 2000-2020}
# 	\end{subfigure}
# 	\hfill

# 	\begin{subfigure}[b]{\textwidth}
# 		\centering
# 		\includegraphics[width=\textwidth]{./ALL Orbit Plots/5/1a}
# 		\caption{Orbital Plot for a Full Orbit}
# 	\end{subfigure}
# 	\hfill
# 	\caption{Orbital Plots of Candidate \#1}
# \end{figure}

# \begin{figure}[H]
# 	\includegraphics[width=\linewidth]{./ALL Timeline Plots/1 Timeline}
# 	\caption[T]{Timeline Plot of Candidate \#1}
# \end{figure}
# \pagebreak

# ===========================
# Example input:

# 1
# 2
# 3
# 4
# 5
# 8
# 9