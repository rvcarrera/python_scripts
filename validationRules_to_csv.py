import xml.etree.ElementTree as ET
import os
import csv

vrFileNames = os.listdir('validationRules')

xmlFields = ['fullName', 'active', 'description', 'errorConditionFormula', 'errorDisplayField', 'errorMessage']

def findField(x):
    for i in range(root.__len__()):
        if root[i].tag.__contains__(x):
            return root[i].text

vrList = [['Rule Name', 'Active', 'Description', 'Error Condition Formula', 'Error Displayed Field', 'Error Message']]

for vr in vrFileNames:
    tree = ET.parse('validationRules/'+vr)
    root = tree.getroot()
    vrLine = []
    for field in xmlFields:
         vrLine.append(findField(field))
    vrList.append(vrLine)

csvFile = os.path.basename(os.getcwd()) + 'ValidationRules.csv'

with open(csvFile, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(vrList)