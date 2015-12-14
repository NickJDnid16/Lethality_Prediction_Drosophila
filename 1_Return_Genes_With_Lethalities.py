'''
Created on 23 Oct 2015

@author: nid16
'''

import codecs
from itertools import repeat
import csv
inputfile = open('./allele_phenotypic_data_fb_2015_04.tsv', mode='r')
outputfile = open('./Lethal&Viable_Alleles.txt', mode='w')

for line in inputfile:
    if "lethal" in line or "viable" in line:
        outputfile.write(line)
        
inputfile.close()
outputfile.close()


inputfile = open('./Lethal&Viable_Alleles.txt', mode='r')
outputfile = open('./Allele&Lethality_Rows.txt', mode='w')

inputfile = csv.reader(inputfile, delimiter='\t')
outputfile = csv.writer(outputfile)

for row in inputfile:
    count = int (1)
    del row[1]
    if count > 0:
        outputfile.writerows(repeat(row[0:2], count))




outputfile = open('./Removed_Partial_Lethality.txt', mode='w')

P_Temp = []
W_Temp = []

for line in codecs.open('./Allele&Lethality_Rows.txt', mode ='r'):
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


inputfile = open('./Removed_Partial_Lethality.txt', mode='r')
outputfile = open('./Gene&Lethality_Only.txt', mode='w')

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
