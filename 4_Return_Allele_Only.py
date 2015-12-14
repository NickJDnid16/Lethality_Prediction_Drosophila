'''
Created on 23 Oct 2015

@author: nid16
'''

import csv
import codecs
from itertools import repeat
quoting=csv.QUOTE_NONE
inputfile = open('/home/nid16/workspace/Project_With_New_Data/Removed_Partial_Lethality.txt', mode='r')
outputfile = open('/home/nid16/workspace/Project_With_New_Data/Allele_Only.txt', mode='w')

inputfile = csv.reader(inputfile, delimiter=',')
for row in inputfile:
    
   
    del row[1]
    Temp = (str(row[0]))
    
    Temp = Temp.replace(',','')
    outputfile.write(Temp)
    outputfile.write('\n')

    