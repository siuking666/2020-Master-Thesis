# Input a file of positions, Output two files consisting of odd-index and even-index entries respectively.
# For use of scrambling a data set and investigating fits/uncertainties

## GIVE OBJECT NUMBER HERE
#object_names = ['8', '9', '10', '11', '12', '13', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '201', '202', '203', '204', '301', '302', '303', '304', '305', '306', '307']
object_names = ['108']
data_pts = []

for obj in object_names:
    data_set_input = open(str(obj)+"_mediocre.txt", "r")
    odd_points_output = open(str(obj)+"_odd.txt", "w+")
    even_points_output = open(str(obj)+"_even.txt", "w+")

    for line in data_set_input.readlines():
        data_pts.append(line)
    
    i = 0
    for item in data_pts:
        if i % 2 == 0:
            odd_points_output.writelines(item)
        if i % 2 == 1:
            even_points_output.writelines(item)
        i += 1
    
    print(data_pts)
    data_pts.clear()
    
    data_set_input.close()
    odd_points_output.close()
    even_points_output.close()
    
#=======================================   
# Example text file input
# 2004.511	7.557634123	16.02590317	0.399	1.197
# 2004.516	8.710958609	-20.52916625	26.6	26.6
# 2006.726	104.6626268	57.67280311	6.251	17.423
# 2006.753	62.44516047	63.33742702	1.6226	0.798
# 2007.205	52.75919804	87.6520888	1.197	1.33
# 2007.214	62.89162902	79.6306014	0.665	0.399
# 2007.255	78.75588858	78.18007753	26.6	26.6
# 2007.455	58.38483397	110.917674	3.724	12.768
# 2008.145	70.13274563	62.01533061	1.995	0.931
# 2008.197	57.93561705	64.02624854	0.399	0.399    
    