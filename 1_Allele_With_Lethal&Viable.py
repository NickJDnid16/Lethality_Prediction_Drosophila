'''
Created on 23 Oct 2015

@author: nid16
'''

import codecs
inputfile = open('/home/nid16/workspace/Project_With_New_Data/allele_phenotypic_data_fb_2015_04.tsv', mode='r')
outputfile = open('/home/nid16/workspace/Project_With_New_Data/Lethal&Viable_Alleles.txt', mode='w')

for line in inputfile:
    if "lethal" in line or "viable" in line:
        outputfile.write(line)
        
inputfile.close()
outputfile.close()
