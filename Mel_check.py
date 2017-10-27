SL = open('./Single_Lethality_Genes.txt', mode='rb')
Mel = open('./Melanogaster.txt', mode='rb')
Out = open('./Single_Melanogaster_Genes.txt', mode='wb')


MelList = []
for line in Mel:
    line = line.split("\t")
    MelList.append(line[0])

for line in SL:
    line = line.split(",")
    g = line[0]
    if g in MelList:
        gene = ','.join(line)
        Out.write(str(gene))