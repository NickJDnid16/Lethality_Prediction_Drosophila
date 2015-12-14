'''
Created on 23 Oct 2015

@author: nid16
'''


import codecs
data = {}


inputfile = open('/home/nid16/workspace/Project_With_New_Data/Gene_With_Lethal&Viable_Only.txt', mode='r')
outputfile = open('/home/nid16/workspace/Project_With_New_Data/Genes_With_All_Lethality.txt', mode='w')
  
for line in inputfile:
    split_string = line.split(",")
    genome = split_string [0]
    lethalNotation = split_string [1]
    data [genome] = data.get(genome,"")+lethalNotation.rstrip('\r\n')+","


for x in data:
        #print (x+","+data[x]+"\n")
    outputfile.write(x+","+data[x]+"\n")   
           
outputfile.close()