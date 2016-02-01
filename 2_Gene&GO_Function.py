__author__ = 'nid16'

import codecs
import csv

data = {}

outputfile = open('./Gene&GO_F.txt', mode='w')
GOoutputfile = open('./Gene_With_Only_GO.txt', mode='w')
FUNCoutputfile = open('./Gene_With_GO_FUNC .txt', mode='w')
Seen =[]
FUNC = []
for line in open('./gene_association.fb'):

    if(line[:2] == "FB"):#FlyBase = FB
        split_string = line.split("\t")
        genome = split_string [2]
        GO = split_string [4]
        dataMarker = split_string [6]
        data[genome] = data.get(genome,"")+GO+","+dataMarker+","
        if genome not in Seen:
            Seen.append(genome)
            GOoutputfile.write(genome + "\n")
        FUNC.append(genome + "\t" + GO  + "\n")
for line in open('./Single_Lethality_Genes.txt', mode='r'):
    line = line.rstrip()
    split_line = line.split(",")
    gene = split_line[0]
    data[gene] = data.get(gene,"")+str(split_line[1])
################################################################
    #for element in FUNC:
    split_string = element.split("\t")
    if split_line[1] is "lethal" and gene is split_string[0]:
        FUNC.append("\t" + "1")
        print "Something"
    elif split_line[1] is "viable" and gene is split_string[0]:
        FUNC.append("\t" + "0")
        print "Something"
    FUNCoutputfile.write(str(FUNC))
for x in data:
    print (x,data[x])
    outputfile.write(x+","+data[x]+"\n")
  #  FUNCoutputfile.write()
outputfile.close()


########################################################


inputfile = open('./Gene&GO_F.txt', mode='r')
outputfile = open('./Gene&GO_F_With_Lethality.txt', mode='w')

inputfile = csv.reader(inputfile, delimiter=',')

previous = None


writer = csv.writer(outputfile)



for rows in inputfile:

        if "viable" in str(rows[-1]) or "lethal" in str(rows[-1]):

            if "GO" in str(rows):
                writer.writerow(rows)
                print rows
