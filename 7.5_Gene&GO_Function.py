__author__ = 'nid16'

import codecs
data = {}

outputfile = open('/home/nid16/workspace/Project_With_New_Data/Gene&GO_F.txt', mode='w')

for line in open('/home/nid16/workspace/Project_With_New_Data/New_gene_association.fb'):

    if(line[:2] == "FB"):
        split_string = line.split("\t")
        genome = split_string [2]
        GO = split_string [4]
        dataMarker = split_string [6]
        data[genome] = data.get(genome,"")+GO+","+dataMarker+","

for line in open('/home/nid16/workspace/Project_With_New_Data/Single_Lethality_Genes.txt', mode='r'):
    line = line.rstrip()
    split_line = line.split(",")
    gene = split_line[0]
    data[gene] = data.get(gene,"")+str(split_line[1])

for x in data:
    print (x,data[x])
    outputfile.write(x+","+data[x]+"\n")

outputfile.close()