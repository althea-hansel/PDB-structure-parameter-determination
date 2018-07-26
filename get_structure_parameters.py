import sys
import os
import Structure
import glob
import pdb_cleaner
import math
import numpy as np

global structures
structures = {}
global parameters

def createStructureObject(pdbFilePath):
	with open(pdbFilePath, 'r') as f:
		pdb = [ line.split() for line in f.readlines()]
	structureObject = Structure.Structure(pdb)
	return structureObject

def createStructureDictionary():
	"""gets list of all PDB files in directory, creates structure object for them, and stores in global dictionary"""
	file_list = glob.glob("*.pdb")
	file_list.sort()
	for pdbFile in file_list:
		print "Importing " + pdbFile
		try:
			currentStructure = createStructureObject(pdbFile)
			structures[pdbFile[:4]] = currentStructure
		except ValueError:
			print pdbFile + "cleaned by pdb cleaner"
			pdb_cleaner.cleaner(pdbFile)
			currentStructure = createStructureObject(pdbFile)
			structures[pdbFile[:4]] = currentStructure

def read_parameters_list():
	with open("parameters.txt", 'r') as f:
		parameters = [ line.split() for line in f.readlines()]
	return parameters

def getStructure(pdbCode):
	return structures[pdbCode]

def getResidue(structure, resNumber):
	"""takes in structure object, residue number string"""
	return structure[str(resNumber)]

def getDistance(residue1, residue2):
	"""input residue coordinate lists [x, y, z]"""
	try:
		x_square = math.fabs(residue1[0] - residue2[0])**2
		y_square = math.fabs(residue1[1] - residue2[1])**2
		z_square = math.fabs(residue1[2] - residue2[2])**2
		return math.sqrt(x_square + y_square + z_square)
	except TypeError: #catch if residue does not exist in structure
		return " "

def getAngle(residue1, residue2, residue3):
	try:
		vector1 = [math.fabs(residue1[0] - residue2[0]), math.fabs(residue1[1] - residue2[1]), math.fabs(residue1[2] - residue2[2])]
		vector2 = [math.fabs(residue3[0] - residue2[0]), math.fabs(residue3[1] - residue2[1]), math.fabs(residue3[2] - residue2[2])]
		return np.arcsin(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))) * 180 / math.pi #converts to degrees
	except TypeError:
		return " "

def calcAllParameters():
	"""calculate all parameters in parameter file"""
	parametersInput = read_parameters_list()
	numberOfDistanceParameters = 0
	distanceParameters = []
	numberOfAngleParameters = 0
	angleParameters = []
	for line in parametersInput:
		if len(line) > 0:
			if line[0] == "distance":
				numberOfDistanceParameters += 1
				distanceParameters.append(line)
			elif line[0] == 'angle':
				numberOfAngleParameters += 1
				angleParameters.append(line)

	#make output list and header
	output = []
	output.append([" "])
	for i in range(numberOfDistanceParameters):
		output[0].append('r' + str(i))
	for j in range(numberOfAngleParameters):
		output[0]. append('a' + str(j))
	#calculate parameter values for each structure
	for structure in structures:
		currentStructure = getStructure(structure)
		currentStructure_parameters = [structure] #adds name of structure in first column
		for distance in distanceParameters:
			resNum1 = distance[1]
			resNum2 = distance[2]
			res1 = getResidue(currentStructure, resNum1)
			res2 = getResidue(currentStructure, resNum2)
			distanceMeasure = getDistance(res1, res2)
			currentStructure_parameters.append(distanceMeasure)
		for angle in angleParameters:
			resNum1 = angle[1]
			resNum2 = angle[2]
			resNum3 = angle[3]
			res1 = getResidue(currentStructure, resNum1)
			res2 = getResidue(currentStructure, resNum2)
			res3 = getResidue(currentStructure, resNum3)
			angleMeasure = getAngle(res1, res2, res3)
			currentStructure_parameters.append(angleMeasure)
		output.append(currentStructure_parameters)
	#write output file
	with open("output.txt", 'w') as f:
		for line in output:
			for word in line:
				f.write(str(word) + '\t')
			f.write('\n')

def main():
	createStructureDictionary()
	print "All pdb structure objects successfully created!"
	calcAllParameters()
	print "All structure parameters successfully calculated and written to output file"

main()