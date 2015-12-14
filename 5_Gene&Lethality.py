'''
Created on 23 Oct 2015

@author: nid16
'''

import csv


inputfile = open('/home/nid16/workspace/Project_With_New_Data/Removed_Partial_Lethality.txt', mode='r')
outputfile = open('/home/nid16/workspace/Project_With_New_Data/Gene&Lethality_Only.txt', mode='w')

inputfile = csv.reader(inputfile, delimiter=',')

for row in inputfile:
    
   
    #del row[1]
    Temp = (str(row[0]))
    Temp = Temp.split('[')[0].strip()
    #Temp = Temp.replace(',','')
    print Temp 
    print 
    outputfile.write(Temp)
    outputfile.write(',')
    outputfile.write(str(row[1]))
    outputfile.write('\n')
