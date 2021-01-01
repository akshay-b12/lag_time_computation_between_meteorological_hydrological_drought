'''
import re
f1 = open("daddi.txt", "r")
f2 = open("daddi.csv", "a")
lines = f1.readlines()
for line in lines:
    f2.write(re.sub(' +', ',', line))
f1.close()
f2.close()
'''
import csv
import sys

with open(sys.argv[1]) as fin, open(sys.argv[2], 'w') as fout:
    o=csv.writer(fout)
    for line in fin:
        o.writerow(line.split())
