__author__ = 'nid16'



import csv
import codecs
from theano.sandbox.cuda.basic_ops import row

inputfile = open('./Gene&GO_F.txt', mode='r')
outputfile = open('/home/nid16/workspace/Project_With_New_Data/Fixed_Gene&GO_F.txt', mode='w')

inputfile = csv.reader(inputfile, delimiter=',')

previous = None


writer = csv.writer(outputfile)



for rows in inputfile:
        #for index, words in enumerate(rows):
          #  previous = rows[index-1]
         #   current = rows[index]
           # if index-1 != -1:
            #    if "viable" in rows[-1] or "lethal" in rows[-1]:# and "GO" in rows:
                    #while "IMP" in rows[index] and "GO" in previous:
                     #       rows.pop(index-1)
                      #      if "GO" != rows:
                       #         break
             #   else:
                #    Null = "Null"
        #if rows[-1] == "viable" or rows[-1] == "lethal":
        if "viable" in str(rows[-1]) or "lethal" in str(rows[-1]):

            if "GO" in str(rows):
                writer.writerow(rows)
                print rows
