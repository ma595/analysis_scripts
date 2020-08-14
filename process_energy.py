#
# Script to read data from odb file and save it to a csv file
#
from odbAccess import *
from abaqus import *
from abaqusConstants import * 
import sys, os

outpath = os.getenv('OUTPATH')
outfile = open(outpath,'w')
print("outpath ", outpath)

output=os.getenv('ROOTODB')
print("output directory ", output)
odb = openOdb(output)

step1 = odb.steps['Step-1']

# output_ie='Internal energy: ALLIE PI: COATING-1 in ELSET COATING-SET'

print(dir(step1))
# do this to get the history regions:
print(step1.historyRegions)

region_coating = step1.historyRegions['ElementSet COATING-SET']
region_ball = step1.historyRegions['ElementSet BALL-SET']
region_plate = step1.historyRegions['ElementSet PLATE-SET']
region_all = step1.historyRegions['Assembly ASSEMBLY']
# print(region.historyOutputs)

coating_ie = region_coating.historyOutputs['ALLIE'].data
ball_ie = region_ball.historyOutputs['ALLIE'].data
plate_ie = region_plate.historyOutputs['ALLIE'].data

coating_ke = region_coating.historyOutputs['ALLKE'].data
ball_ke = region_ball.historyOutputs['ALLKE'].data
plate_ke = region_plate.historyOutputs['ALLKE'].data

coating_pd = region_coating.historyOutputs['ALLPD'].data
ball_pd = region_ball.historyOutputs['ALLPD'].data
plate_pd = region_plate.historyOutputs['ALLPD'].data

coating_se = region_coating.historyOutputs['ALLSE'].data
ball_se = region_ball.historyOutputs['ALLSE'].data
plate_se = region_plate.historyOutputs['ALLSE'].data

ETOTAL = region_all.historyOutputs['ETOTAL'].data

nn = len(coating_ie)
outfile.write('#t ball_ke ball_ie coating_ke coating_ie plate_ke plate_ie\n')
for i in range(0,nn):
    outfile.write('%10.4E %10.4E %10.4E %10.4E %10.4E %10.4E %10.4E\n'%(coating_ie[i][0], ball_ke[i][1], ball_ie[i][1], coating_ke[i][1], coating_ie[i][1], plate_ke[i][1], plate_ie[i][1]) )

outfile.close()    
print(coating_ie)
# SET = 'ElementSet . ALL ELEMENTS'
# SET = 'COATING-1 in ELSET COATING-SET'
# region = step1.historyRegions[SET]
# region = step1.historyRegions
# region = step1.historyRegions
# xy2 = xyPlot.XYDataFromHistory(odb=odb, 
#     outputVariableName='Internal energy: ALLIE PI: COATING-1 in ELSET COATING-SET', steps=('Step-1', ), suppressQuery=True)



# for i in range(0, nn):
#      dispFile.write('%10.4E,%10.4E \n'%(displacementData[i][0], displacementData[i][1]))
# dispFile.close()

# os.system('abaqus cae noGUI=C:\\Users\\Samuel\\abaqus-1\\script1.py')

