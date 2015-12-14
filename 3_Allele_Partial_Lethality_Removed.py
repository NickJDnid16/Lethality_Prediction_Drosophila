'''
Created on 23 Oct 2015

@author: nid16
'''

import codecs

outputfile = open('/home/nid16/workspace/Project_With_New_Data/Removed_Partial_Lethality.txt', mode='w')

P_Temp = []
W_Temp = []

for line in codecs.open('/home/nid16/workspace/Project_With_New_Data/Allele&Lethality_Rows.txt', mode ='r'):
    if not "partially" in line: 
        print (line)
        P_Temp.append(line)
        
for line in P_Temp:
    if not "with" in line:
            print(line)
            W_Temp.append(line)

for line in W_Temp:
    if not "poor" in line :
        print(line)
        outputfile.write(line)   

outputfile.close()