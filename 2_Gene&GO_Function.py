__author__ = 'nid16'

import codecs
import csv
import sys
data = {}
import pprint
outputfile = open('./Gene&GO_F.txt', mode='w')
GOoutputfile = open('./Gene_With_Only_GO.txt', mode='w')
FUNCoutputfile = open('./Gene_With_GO_FUNC .txt', mode='w')
Seen =[]
FUNC = []
<<<<<<< HEAD
geneAssociation = open('./gene_association.fb')
geneAssociation = csv.reader(geneAssociation, delimiter='\t')
for rows in geneAssociation:

    if(rows[0] == "FB"):
        genome = rows[2]
        print genome
        GO = rows[4]
        dataMarker = rows[6]
=======
for line in open('./gene_association.fb'):

    if(line[:2] == "FB"):#FlyBase = FB
        split_string = line.split("\t")
        genome = split_string [2]
        GO = split_string [4]
        dataMarker = split_string [6]
>>>>>>> origin/master
        data[genome] = data.get(genome,"")+GO+","+dataMarker+","
        if genome not in Seen:
            Seen.append(genome)
            GOoutputfile.write(genome + "\n")
        FUNC.append(genome + "\t" + GO  + "\n")
<<<<<<< HEAD

=======
>>>>>>> origin/master
for line in open('./Single_Lethality_Genes.txt', mode='r'):
    line = line.rstrip()
    split_line = line.split(",")
    gene = split_line[0]
    data[gene] = data.get(gene,"")+str(split_line[1])


################################################################

# newFUNC = []
#
# geneSeen = []
# for line in open('./Single_Lethality_Genes.txt', mode='r'):
#     line = line.rstrip()
#     split_line = line.split(",")
#     gene = split_line[0]
#     lethality = split_line[1]
#     if (lethality == "lethal"):
#         for line in FUNC:
#             tempFUNC = []
#             if gene in line and line not in geneSeen:
#                 geneSeen.append(line)
#                 line = line.strip()
#                 tempFUNC.append(str(line) + "\t1")
#                 print tempFUNC
#                 newFUNC.append(tempFUNC)
#     if (lethality == "viable"):
#         for line in FUNC:
#             tempFUNC = []
#             if gene in line and line not in geneSeen:
#                 geneSeen.append(line)
#                 line = line.replace('\n','')
#                 tempFUNC.append(str(line) + "\t0")
#
#                 print tempFUNC
#                 newFUNC.append(tempFUNC)
#
#         print "Something"
#         print tempFUNC
# # #FUNCoutputfile.write("\n".join(newFUNC))
#
#
# for element in newFUNC:
#     #FUNCoutputfile.writelines(str(element)+"\n")
#     FUNCoutputfile.write(" ".join(element) + "\n")

###############################################################



########################################################

for x in data:
    print (x,data[x])
    outputfile.write(x+","+data[x]+"\n")
  #  FUNCoutputfile.write()
outputfile.close()


newFUNC = []
#Test
geneSeen = []
for line in open('./Single_Lethality_Genes.txt', mode='r'):
    line = line.rstrip()
    split_line = line.split(",")
    gene = split_line[0]
    lethality = split_line[1]
    #print "Lethality is " + lethality
    if "lethal" in lethality:
        for line in FUNC:
            tempFUNC = []
            if gene in line and line not in geneSeen:
                geneSeen.append(line)
                line = line.strip()
                tempFUNC.append(str(line) + "\t1")
                #print tempFUNC
                newFUNC.append(tempFUNC)
    if "viable" in lethality:
        for line in FUNC:
            tempFUNC = []
            if gene in line and line not in geneSeen:
                geneSeen.append(line)
                line = line.replace('\n','')
                tempFUNC.append(str(line) + "\t0")

                #print tempFUNC
                newFUNC.append(tempFUNC)

        #print "Something"
        #print tempFUNC
#FUNCoutputfile.write("\n".join(newFUNC))


for element in newFUNC:
    #FUNCoutputfile.writelines(str(element)+"\n")
    FUNCoutputfile.write(" ".join(element) + "\n")

########################################################


inputfile = open('./Gene&GO_F.txt', mode='rb')
outputfile = open('./Gene&GO_F_With_Lethality.txt', mode='wb')
LethalOutput = open('./Lethal_Fly.txt', mode='w')
Viable_LethalOutput= open('./Lethal&Viable_Fly.txt', mode='w')
inputfile = csv.reader(inputfile, delimiter=',')

previous = None


writer = csv.writer(outputfile)
<<<<<<< HEAD
Lethalwriter = csv.writer(LethalOutput)
VLwriter = csv.writer(Viable_LethalOutput)

=======
# lethalwriter = csv.writer(lethaloutfile)
# allwriter = csv.writer(alloutfile)
>>>>>>> origin/master

for rows in inputfile:

        if "viable" in str(rows[-1]) or "lethal" in str(rows[-1]):

            if "GO" in str(rows):
                writer.writerow(rows)
<<<<<<< HEAD
                VLwriter.writerow(rows[0:1])
                if "lethal" in str(rows[-1]):
                    Lethalwriter.writerow(rows[0:1])

                print rows
=======
                print rows
########################################################

outputfile.close()
inputfile = open('./Gene&GO_F_With_Lethality.txt', mode='r')
lethaloutfile = open('./Fly_Gene_Lethal.txt', mode='w')
alloutfile = open('./Fly_Gene_Viable_Lethal.txt', mode='w')
inputfile = csv.reader(inputfile, delimiter=',')
for line in inputfile:
    if "lethal" in line[-1]:
        lethaloutfile.write(line[0] + "\n")
    alloutfile.write(line[0] + "\n")





>>>>>>> origin/master
