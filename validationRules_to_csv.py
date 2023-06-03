import xml.etree.ElementTree as ET
import os
import csv

vrFileNames = os.listdir('validationRules')

vrList = [['Rule Name', 'Active', 'Error Condition Formula', 'Error Message']]

for vr in vrFileNames:
    tree = ET.parse('validationRules/'+vr)
    root = tree.getroot()
    vrLine = []
    for i in range(root.__len__()):
        if (root[i].tag.__contains__('fullName')):
            vrLine.append(root[i].text)
        elif (root[i].tag.__contains__('active')):
            vrLine.append(root[i].text)
        elif (root[i].tag.__contains__('errorConditionFormula')):
            vrLine.append(root[i].text)
        elif (root[i].tag.__contains__('errorMessage')):
            vrLine.append(root[i].text)
    vrList.append(vrLine)

csvFile = os.path.basename(os.getcwd()) + 'ValidationRules.csv'

with open(csvFile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(vrList)