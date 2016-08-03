from abaqus import *
from abaqusConstants import *
from odbAccess import *
import os

odb = session.openOdb('Cube_V0075_D12_ZZ_AB_SoftContact.odb')

FileName = 'Cube_V0075_D12_ZZ_AB_SoftContact_FvsD.txt'

with open(FileName,'w') as saveFile:	
	for step in odb.steps.values():
		for frame in step.frames:
			RFTop = odb.rootAssembly.instances['MATRIX-1'].nodeSets['REFNODE']
			RFTopDisplacement = frame.fieldOutputs['U'].getSubset(region=RFTop)
			RFTopForce = frame.fieldOutputs['RF'].getSubset(region=RFTop)
			Dy = RFTopDisplacement.values[0].data[1]
			Fy = RFTopForce.values[0].data[1]
			FileResultsX.write('%10.8E\t %10.8E\t\n' % (Dy,Fy))