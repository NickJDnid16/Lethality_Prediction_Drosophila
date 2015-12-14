'''
Created on 23 Oct 2015

@author: nid16
'''

import csv

inputfile = open('/home/nid16/workspace/Project_With_New_Data/Gene&Lethality_Only.txt', mode='r')
outputfile = open('/home/nid16/workspace/Project_With_New_Data/Gene_With_Lethal&Viable_Only.txt', mode='w')

inputfile = csv.reader(inputfile, delimiter=',')

for row in inputfile:


    #del row[1]
    Temp = (str(row[1]))
    if "lethal" in Temp:
        Temp = "lethal"
    if "viable" in Temp:
        Temp = "viable"

    outputfile.write(str(row[0]))
    outputfile.write(",")
    outputfile.write(Temp)
    outputfile.write('\n')








