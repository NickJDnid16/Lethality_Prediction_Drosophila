All = open('./Gene&GO_F_With_Lethality.txt', mode='rb')
Mel = open('./Gene&GO_F_With_Lethality_Filtered.txt', mode='rb')
Out = open('./Missing_From_Filtered.txt', mode='wb')


MelList = []
for line in Mel:
    #line = line.split("\t")
    MelList.append(str(line))

for line in All:
    #line = line.split(",")
    g = line[0]
    line = str(line)
    if line not in MelList:
        #line = ','.join(line)
        Out.write(str(line))