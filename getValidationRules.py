import xml.etree.ElementTree as ET
import os
import csv

vrList = [['Object', 'Rule Name', 'Active', 'Description', 'Error Condition Formula', 'Error Displayed Field', 'Error Message']]
vrFields = ['fullName', 'active', 'description', 'errorConditionFormula', 'errorDisplayField', 'errorMessage']

def findField(fieldName):
    for i in range(root.__len__()):
        if root[i].tag.__contains__(fieldName):
            return root[i].text
        
objects = [folder for folder in os.listdir() if os.path.isdir(os.path.join(os.getcwd(), folder))]
objectsWithVr = [obj for obj in objects if 'validationRules' in os.listdir(obj)]

for obj in objectsWithVr:
    vrFileNames = os.listdir(obj+'/validationRules/')
    for vr in vrFileNames:
        root = ET.parse(obj+'/validationRules/'+vr).getroot()
        vrList.append([obj] + [findField(field) for field in vrFields])

with open('ValidationRules.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(vrList)