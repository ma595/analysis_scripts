#
# Script to read data from odb file and save it to a csv file
#
from odbAccess import *
from abaqus import *
from abaqusConstants import * 
import sys
odb = openOdb('output/coating-plastic-penalty-rough-mesh.odb')
# step1 = odb.steps['Step-1'].frames[-1]
step1 = odb.steps['Step-1']

ball_instance = odb.rootAssembly.instances['BALL-1']
first_node = ball_instance.nodes[0]
first_node_label = first_node.label

print(ball_instance.elementSets['BALL-SET'])

# for i in range(0,len(step1.frames)):
#     print(step1.frames[i].fieldOutputs['U'].getSubset(node=first_node))


# nodeHistory = odb.steps['Step-1'].getHistoryRegion(point=first_node)
# this Node Ball-1.1 doesn't exist
region = step1.historyRegions['Node BALL-1.65']

# print(step1.frames[-1].fieldOutputs)
# # print(odb.rootAssembly.instances['BALL-1'])
# print(region.historyOutputs['U2'].data)

print(odb.materials['BALL'])
# print(odb.parts['BALL'].engineeringFeatures)
region_ball = step1.historyRegions['ElementSet BALL-SET']
region_all = step1.historyRegions['Assembly ASSEMBLY']
print(region_all)


# alldata = region.historyOutputs['U'].data

# print(step1.historyRegions['ElementSet BALL-SET'])
# print(step1.historyRegions['ElementSet BALL-SET'].historyOutputs)
region_ball = step1.historyRegions['ElementSet BALL-SET']
print(region_ball)
