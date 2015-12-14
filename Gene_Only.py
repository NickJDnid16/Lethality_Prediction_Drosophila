'''
Created on 23 Oct 2015

@author: nid16
'''

import csv
import codecs
from itertools import repeat
quoting=csv.QUOTE_NONE
inputfile = open('/home/nid16/workspace/Project_With_New_Data/Converted_Alleles_To_Genes.txt', mode='r')
outputfile = open('/home/nid16/workspace/Project_With_New_Data/Gene_Only.txt', mode='w')

inputfile = csv.reader(inputfile, delimiter='\t')

for row in inputfile:
    
   
    #del row[1]
    Temp = (str(row[3]))
    
    Temp = Temp.replace(',','')
    outputfile.write(Temp)
    outputfile.write('\n')
