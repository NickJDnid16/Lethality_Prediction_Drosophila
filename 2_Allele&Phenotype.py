'''
Created on 23 Oct 2015

@author: nid16
'''
from itertools import repeat
import csv
import codecs
inputfile = open('/home/nid16/workspace/Project_With_New_Data/Lethal&Viable_Alleles.txt', mode='r')
outputfile = open('/home/nid16/workspace/Project_With_New_Data/Allele&Lethality_Rows.txt', mode='w')

inputfile = csv.reader(inputfile, delimiter='\t')
outputfile = csv.writer(outputfile)

for row in inputfile:
    count = int (1)
    del row[1]
    if count > 0:
        outputfile.writerows(repeat(row[0:2], count))
        
#inputfile.close()
#outputfile.close()

