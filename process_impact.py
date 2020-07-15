#
# Script to read data from odb file and save it to a csv file
#
from odbAccess import *
import sys
odb = openOdb('Job-1.odb')
step1 = odb.steps['Step-1']

f = open("demofile.txt", "a")
f.write("Now the file has one more line!")
# Edit the line below to enter the correct node number
# region = step1.historyRegions['Node Part-1-1.65']
# region = step1.historyRegions
# print(region)

region = step1.historyRegions['Node PART-1-1.65']
displacementData = region.historyOutputs['U2'].data
nn = len(displacementData)
dispFile = open('disp-steel.csv','w')

for i in range(0, nn):
     dispFile.write('%10.4E,%10.4E \n'%(displacementData[i][0], displacementData[i][1]))
dispFile.close()

# os.system('abaqus cae noGUI=C:\\Users\\Samuel\\abaqus-1\\script1.py')

