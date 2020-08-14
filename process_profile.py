#
# Script to read data from odb file and save it to a csv file
#
from odbAccess import *
from abaqus import *
from abaqusConstants import * 
import sys
# odb = openOdb('output/coating-plastic-penalty-rough-mesh.odb')
odb = openOdb('output/test.odb')
# step1 = odb.steps['Step-1'].frames[-1]
step1 = odb.steps['Step-1']
# get displacements of all nodes

# print(step1.fieldOutputs)
# print(step1.historyRegions['ElementSet COATING_SURFACE-SET'])

# http://ivt-abaqusdoc.ivt.ntnu.no:2080/v6.14/pdf_books/SCRIPT_USER.pdf
# print(step1.fieldOutputs.nodeSets)

# print step1.historyRegions.keys()
# region_ball = step1.historyRegions['NodeSet BALL-SET']

lastFrame = odb.steps['Step-1'].frames[-1]

# for fieldName in lastFrame.fieldOutputs.keys():
#     print fieldName

# combine this with the previous
# should be able to get the noderegion we're interested in
# then apply that to the 
# print(odb.rootAssembly.instances['COATING-1'].nodeSets['COATING-SURFACE'])
# surface_region_nodes = surface_region.nodes
# print(surface_region)
# print(dir(surface_region))
# print(surface_region.nodes)
# print(step1.historyRegions)
# print(step1.getHistoryRegion(region=surface_region_nodes))

# print(step1.historyRegions)

# print(dispSubField.values[0])
# print(nodeLabel)
# print(odb.rootAssembly.instances['COATING-1'].getNodeFromLabel(nodeLabel).coordinates)

coating_instance = odb.rootAssembly.instances['COATING-1']
coating_surface_region = coating_instance.nodeSets['COATING-SURFACE']
coating_surface_dispSubField = step1.frames[-1].fieldOutputs['U'].getSubset(region=coating_surface_region)
length = len(coating_surface_dispSubField.values)

coating_outfile = open('out/coating_surface-profile.csv', 'w')
coating_outfile.write("#originalx originaly dispx dispy\n")
for i in range(0,length):
    coating_nodeLabel = coating_surface_dispSubField.values[i].nodeLabel
    coords = coating_instance.getNodeFromLabel(coating_nodeLabel)
    displacements = coating_surface_dispSubField.values[i].data
    # print(displacements)
    # print(displacements.data)
    # print(coords.coordinates[0], coords.coordinates[1], displacements[0], displacements[1])
    # print(coords['coordinates'])
    coating_outfile.write('%10.4E %10.4E %10.4E %10.4E\n'%(coords.coordinates[0], coords.coordinates[1], displacements[0], displacements[1]))

coating_outfile.close()

coating_lowersurface_region = coating_instance.nodeSets['COATING-LOWERSURFACE']
coating_lowersurface_dispSubField = step1.frames[-1].fieldOutputs['U'].getSubset(region=coating_lowersurface_region)
coating_outfile = open('out/coating_lowersurface-profile.csv', 'w')
coating_outfile.write("#originalx originaly dispx dispy\n")
for i in range(0,length):
    coating_nodeLabel = coating_lowersurface_dispSubField.values[i].nodeLabel
    coords = coating_instance.getNodeFromLabel(coating_nodeLabel)
    displacements = coating_lowersurface_dispSubField.values[i].data
    # print(displacements)
    # print(displacements.data)
    # print(coords.coordinates[0], coords.coordinates[1], displacements[0], displacements[1])
    # print(coords['coordinates'])
    coating_outfile.write('%10.4E %10.4E %10.4E %10.4E\n'%(coords.coordinates[0], coords.coordinates[1], displacements[0], displacements[1]))

coating_outfile.close()

plate_instance = odb.rootAssembly.instances['PLATE-1']
plate_surface_region = plate_instance.nodeSets['PLATE-SURFACE']
plate_surface_dispSubField = step1.frames[-1].fieldOutputs['U'].getSubset(region=plate_surface_region)
plate_outfile = open('out/plate_surface-profile.csv', 'w')
plate_outfile.write("#originalx originaly dispx dispy\n")
for i in range(0,length):
    plate_nodeLabel = plate_surface_dispSubField.values[i].nodeLabel
    coords = plate_instance.getNodeFromLabel(plate_nodeLabel)
    displacements = plate_surface_dispSubField.values[i].data
    # print(displacements)
    # print(displacements.data)
    # print(coords.coordinates[0], coords.coordinates[1], displacements[0], displacements[1])
    # print(coords['coordinates'])
    plate_outfile.write('%10.4E %10.4E %10.4E %10.4E\n'%(coords.coordinates[0], coords.coordinates[1], displacements[0], displacements[1]))

plate_outfile.close()

# step1
