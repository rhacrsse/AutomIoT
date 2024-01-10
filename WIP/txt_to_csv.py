#!/usr/bin/python3

import re
import sys

if len(sys.argv) != 3:
    raise ValueError('You need to specify 2 variables: ./txt_to_csv.py SOURCE_PATH DESTINATION_PATH')

srcp = sys.argv[1]
destp = sys.argv[2]

file1 = open(srcp, 'r')
#file1 = open('/Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/WIP/gtfile.txt', 'r')
lines = file1.readlines()
lines = [re.sub("\n","",r) for r in lines]
x = re.findall("(\[.+\])", lines[1])[0]
y = list(filter(lambda r: r != "" and "NOP" not in r, lines))
#y = list(map(lambda r: re.findall("(\[.+\])", r)[0], y))
z=[re.sub("(\[|\]|TIMESTAMP: |EVENT COUNTER: |APP: |DEVICE: |ACTION: )","", re.sub("\]\s\[",",",r)) for r in y]
z.insert(0,"TIMESTAMP,EVENT COUNTER,APP,DEVICE,ACTION")
file2 = open(destp, 'w')
#file2 = open('/Users/angelo/workspace/IOT-Forensics-Android-UI-Automation-Testing/linksys_analysis/gtfile.csv', 'w')
[file2.writelines(r + "\n") for r in z]
file2.close()
file1.close()
