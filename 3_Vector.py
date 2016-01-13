from datetime import datetime

startTime = datetime.now()

# Unicode Characters from text file
import codecs
import json
import sys
import time

counter = 1

from pygraph.classes.digraph import digraph

# Graph creation

gr = digraph()
count = 0

# Input
GraphInput = codecs.open('./Refined_GO_Nodes.txt', encoding='utf-8', mode='r')

EdgesInput = codecs.open('./GO_Children&Parents.txt', encoding='utf-8', mode='r')

with open('./GO_Children&Parents.txt') as json_file:
    json_data = json.load(json_file)
    # print(json_data, "\n")

    for key in json_data.keys():
        ##print ("key:", key, " parents:",json_data[key]['p'], " children:",json_data[key]['c'])#("key:",key,"\n")
        node = key.replace(":", "")
        gr.add_node(node)
        print ("Added ", node)

    for key in json_data.keys():
        print (count)
        ##print ("key:", key, " parents:",json_data[key]['p'], " children:",json_data[key]['c'])#("key:",key,"\n")
        node = key.replace(":", "")
        # gr.add_node(node)
        for parent in json_data[key]['p']:
            print("PARENT")
            pt = parent.replace(":", "")
            # print(node, " - ", pt)
            if gr.has_node(node) and gr.has_node(pt):
                if not gr.has_edge((pt, node)):
                    gr.add_edge((pt, node))
        for child in json_data[key]['c']:
            print("CHILD")
            cd = child.replace(":", "")
            if gr.has_node(node) and gr.has_node(cd):
                if not gr.has_edge((node, cd)):
                    gr.add_edge((node, cd))
        count += 1
# print(GraphInput)

counter = 0

count = 0

with open('./Refined_GO_Nodes.txt') as input:
    tempVec = []
    BinVec = []
    vec = []
    for line in input:
        tempVec.append(line.strip())
        BinVec.append(0)
    for item in tempVec:
        print("Item")
        print(item)
        tempItem = item.replace(":", "")
        vec.append(tempItem)
        print(tempItem)

Missing = []


def Incidents(Up):
    i = 0

    for key in Up:
        # print(i)
        # print(key)
        if key not in Seen:
            tempy = []
            try:
                tempy.extend(gr.incidents(key))
                Seen.append(key)
            except (KeyError, ValueError):
                OutMissing.write("Tempy Missing")
                # print(len(tempy))
            if len(tempy) > 0:
                i = i + 1
                if i > 0:
                    return False
                else:
                    return True


def Duplicates(Up):
    NewUp = []
    NodesSeen = []
    for node in Up:
        if node not in NodesSeen:  # not a duplicate
            NewUp.append(node)
            NodesSeen.append(node)
    return NewUp


debug = 0
# outputfile = open('/home/mint/git/prediction-of-Lethality-in-Fly-Mutants-using-Machine-Learning/Workspace/Lethality Extraction/Vector.txt')
data = open('./Gene&GO_F_With_Lethality.txt')
# data = open('./Gene&GO_F_No_ISS.txt')#NO ISS
# data = open('./Gene&GO_F_No_IMP.txt')#NO IMP

outputfile = open('./BinVec.txt', mode='w')
OutMissing = open('./Missing.txt', mode='w')
OutParents = open('./Parents.txt', mode='w')
Genes = open('./Genes.txt', mode='w')
for line in data:
    debug = debug + 1
    csv = line.split(",")
    Gene = csv[0]
    print(csv[0])

    Continue = True
    csvCount = 0
    Ancestors = []
    # Ancestors.append(temp)
    Seen = []
    Up = []
    for t in range(1, len(csv)):
        csvCount = csvCount +1
        if "GO" in csv[csvCount]:
            print(csv[csvCount])
            print "Here"

            temp = csv[csvCount]
            temp = temp.replace(":", "")
            # print ("Ancestors")
            # print(gr.incidents(temp))

            Up.append(temp)



            # Ancestors.extend(Up)
            print("Up")
            Continue = True
            Nodes = []
            while Continue == True:
                l = 0
                if Incidents(Up) == False:
                    # print("GO in Incidents")

                    for node in Up:
                        if node not in Nodes:
                            Nodes.append(node)
                            try:
                                Up.extend(gr.incidents(node))
                                l = l + 1
                                if l == 1000000:
                                    Up = Duplicates(Up)
                                    # print("Parents Added")
                            except (KeyError, ValueError):
                                print("Error")

                                # print("Node Size")
                                # print(len(Nodes))


                else:
                    Continue = False
                    print("Root")

    Ancestors.extend(Up)
    print("Ancestors")
    # print(Ancestors)
    # print(vec)
    ModifiedAncestors = []
    NodesSeen = []
    for node in Ancestors:
        if node not in NodesSeen:  # not a duplicate
            ModifiedAncestors.append(node)
            NodesSeen.append(node)

    print ModifiedAncestors

    del Ancestors[:]
    for Node in ModifiedAncestors:

        # OutParents.write(Node)
        try:

            print(vec.index(Node))

            BinVec[vec.index(Node)] = 1
        # Parents = gr.incidents(temp)

        except (KeyError, ValueError):
            print("Missing")
            try:
                Missing.index(Node)
                print("Already Missing")
            except (KeyError, ValueError):
                Missing.append(Node)
# ##################################################################################
#     GO_Terms = []
#     Leaf_1 = []
#     Leaf_2 = []
#     Leaf_3 = []
#     Leaf_4 = []
#     Leaf_5 = []
#     Leaf_6 = []
#     Leaf_7 = []
#     Leaf_8 = []
#     Leaf_9 = []
#     Leaf_10 = []
#     Leaf_11 = []
#     Leaf_12 = []
#     Leaf_13 = []
#     Leaf_14 = []
#     Leaf_15 = []
#     Leaf_16 = []
#     print Gene
#     print ModifiedAncestors
#     # sys.exit("dff")
#     #for GO in ModifiedAncestors:
#
#     if "GO0022008" in ModifiedAncestors:
#         GO_Terms.append(Gene + " GO0022008")
#         Leaf_1.append(Gene + ",")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO:0022008" + " ")
#         Genes.write(csv[-1])
#
#
#     if "GO0009792" in ModifiedAncestors and Gene not in GO_Terms:
#         GO_Terms.append(Gene + " GO0009792")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO:0009792" + " ")
#         Genes.write(csv[-1])
#     #####
#     if "GO0010631" in ModifiedAncestors and Gene not in GO_Terms:
#         GO_Terms.append(Gene + " GO0010631")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO:0010631" + " ")
#         Genes.write(csv[-1])
#     #####
#
#     if "GO0048598" in ModifiedAncestors and Gene not in GO_Terms:
#         GO_Terms.append(Gene + " GO0048598")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO:0048598" + " ")
#         Genes.write(csv[-1])
#     #####
#     if "GO0048731" in ModifiedAncestors and Gene not in GO_Terms:
#         GO_Terms.append(Gene + " GO0048731")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO:0048731" + " ")
#         Genes.write(csv[-1])
#         #print "GENES"
#         #print GO_Terms
#         #sys.exit("STOPPED")
#         # time.sleep(5)
#     #####
#     if "GO0048646" in ModifiedAncestors and Gene not in GO_Terms:
#         GO_Terms.append(Gene + " GO0048646")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO:0048646" + " ")
#         Genes.write(csv[-1])
#     #####
#     if "GO0048477" in ModifiedAncestors and Gene not in GO_Terms:
#         GO_Terms.append(Gene + " GO0048477")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO:0048477" + " ")
#         Genes.write(csv[-1])
#     #####
#     if "GO0009886" in ModifiedAncestors and Gene not in GO_Terms:
#         GO_Terms.append(Gene + " GO0009886")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO:0009886" + " ")
#         Genes.write(csv[-1])
#     #####
#     if "GO1903047" in ModifiedAncestors and Gene not in GO_Terms:
#         GO_Terms.append(Gene + " GO1903047")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO:1903047" + " ")
#         Genes.write(csv[-1])
#     #####
#     if "GO0048513" in ModifiedAncestors and Gene not in GO_Terms:
#         GO_Terms.append(Gene + " GO0048513")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO:0048513" + " ")
#         Genes.write(csv[-1])
#     #####
#     if "GO0098796" in ModifiedAncestors and Gene not in GO_Terms:
#         GO_Terms.append(Gene + " GO0098796")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO:0098796" + " ")
#         Genes.write(csv[-1])
#     #####
#     if "GO0006357" in ModifiedAncestors and Gene not in GO_Terms:
#         GO_Terms.append(Gene + "GO0006357")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO:0006357" + " ")
#         Genes.write(csv[-1])
#     #####
#     if "GO0006357" in ModifiedAncestors and Gene not in GO_Terms:
#         GO_Terms.append(Gene + " GO0006357")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO:0006357" + " ")
#         Genes.write(csv[-1])
#     #####
#     if "GO0032991" in ModifiedAncestors and "GO0044446" in ModifiedAncestors and Gene not in GO_Terms:
#         GO_Terms.append(Gene + " GO0032991 With GO:0044446")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO0032991 With GO:0044446 ")
#         Genes.write(csv[-1])
#     #####
#     if "GO0032991" in ModifiedAncestors and not "GO0044446" in ModifiedAncestors and Gene not in GO_Terms:
#         GO_Terms.append(Gene + " GO0032991 Without GO:0044446")
#         print counter
#         Genes.write(Gene + " ")
#         Genes.write("GO0032991 Without GO:0044446 ")
#         Genes.write(csv[-1])
#     if any(ModifiedAncestors) not in GO_Terms or Gene not in GO_Terms:
#         print "Left Overs"
#         Leaf_16.append(Gene + ",")
#         Genes.write(Gene + " ")
#         Genes.write("Without Any Identified GO Terms ")
#         Genes.write(csv[-1])
#
#
#     print GO_Terms
#
#     count = count + 1
#
#     ##################################################################################
    outputfile.write(Gene)
    outputfile.write(',')

    for key in BinVec:
        outputfile.write(str(key))
    outputfile.write('\n')

    print(Gene, BinVec)

    for t in range(0, len(BinVec)):
        BinVec[t] = 0
    print("Loop")
    try:
        del Seen[:]
        del Up[:]
        del Ancestors[:]
        del ModifiedAncestors[:]
        del Nodes[:]
    except NameError:
        print "NameError"

print("Missing")
print(len(Missing))
for key in Missing:
    OutMissing.write(str(Missing))
    OutMissing.write('\n')

print(datetime.now() - startTime)
