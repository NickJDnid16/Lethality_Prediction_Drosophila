'''
Created on 23 Oct 2015

@author: nid16
'''

import codecs



outputfile = open('/home/nid16/workspace/Project_With_New_Data/Single_Lethality_Genes.txt', mode='w')
inputfile = open('/home/nid16/workspace/Project_With_New_Data/Genes_With_All_Lethality.txt', mode='r')

for line in inputfile:
    v = "viable" in line
    l = "lethal" in line

    if (l and v):
        print ("Ignoring Line")
    else:
        line = line.rstrip()
        bits = line.split(',')
        if(v):
            bit = bits[0]+",viable\n"
            print (bit)
            outputfile.write(bit)
        if(l):
            bit = bits[0]+",lethal\n"
            print (bit)
            outputfile.write(bit)
        if ((not l) and (not v)):
            print("Not Viable OR Lethal")
            
            
outputfile.close()
            