import sys
import os
import Atomtypes
import ResidueTypes

class Structure:
	#Structure class comprised of dictionary with residue number as the key and the residue object as the value

	def __init__(self, pdbList):
		self.residues = {}
		self.pdbLines = pdbList
		self.makeResidues()

	def __str__(self):
		return str(self.residues)

	def __getitem__(self, residueNum):
		try:
			return self.residues[residueNum]
		except KeyError:
			return None

	#static Structure functions
	@staticmethod
	def makeResidueList(inputPDB):
		"""creates list of lines containing residue atomic coordinates"""
		residueLineList = []
		for line in inputPDB:
			if line[0] == "ATOM" and line[4] == "A": #checks if line is a residue atom in the main PDB chain
				residueLineList.append(line)
			if line[0] == "HETATM" and line[3] == "TPO" and line[4] == "A": #gets phosphorylated threonines in main chain
				residueLineList.append(line)
		return residueLineList

	#non-static Structure functions
	def makeResidues(self):
		"makes dictionary of residue objects for structure object"
		residueLines = Structure.makeResidueList(self.pdbLines)
		residueLinesDict = {}
		currentResidueNum = residueLines[0][5] #gets residue number for first residue
		currentResidueAtomList = []
		for atom in residueLines:
			#for each atom in the chain, check if the residue it is part of is already in the dictionary. If so, add the atom line. If not, make a new entry in the dictionary
			if atom[5] == currentResidueNum:
				currentResidueAtomList.append(atom)
			else:
				residueLinesDict[currentResidueNum] = currentResidueAtomList #saves last residue's lines to dictionary
				currentResidueNum = atom[5] #updates residue number
				currentResidueAtomList = [atom]
		for residue in residueLinesDict:
			currentResidue = self.Residue(residueLinesDict[residue])
			self.residues[currentResidue.resNumber] = currentResidue


	class Residue:
		#Residue class comprised of list of atom objects, coordinates for the residue center of mass, and residue type

		residueDict = {'CYS': 'cysteine', 'ACYS': 'cysteine', 'BCYS': 'cysteine', 'ASP': 'aspartate', 'AASP': 'aspartate', 'BASP': 'aspartate', 'SER': 'serine', 'ASER': 'serine', 'BSER': 'serine', 'GLN': 'glutamine', 'AGLN': 'glutamine', 'BGLN': 'glutamine', 'LYS': 'lysine', 'ALYS': 'lysine', 'BLYS': 'lysine', 'ILE': 'isoleucine', 'AILE': 'isoleucine', 'BILE': 'isoleucine', 'PRO': 'proline', 'APRO': 'proline', 'BPRO': 'proline', 'THR': 'threonine', 'ATHR': 'threonine', 'BTHR': 'threonine', 'TPO': 'threonine', 'PHE': 'phenylalanine', 'APHE': 'phenylalanine', 'BPHE': 'phenylalanine', 'ASN': 'asparagine', 'AASN': 'asparagine', 'BASN': 'asparagine', 'GLY': 'glycine', 'AGLY': 'glycine', 'BGLY': 'glycine', 'HIS': 'histidine', 'AHIS': 'histidine', 'BHIS': 'histidine', 'LEU': 'leucine', 'ALEU': 'leucine', 'BLEU': 'leucine', 'ARG': 'arginine', 'AARG': 'arginine', 'BARG': 'arginine', 'TRP': 'tryptophan', 'ATRP': 'tryptophan', 'BTRP': 'tryptophan', 'ALA': 'alanine', 'AALA': 'alanine', 'BALA': 'alanine', 'VAL':'valine', 'AVAL':'valine', 'BVAL':'valine', 'GLU': 'glutamate', 'AGLU': 'glutamate', 'BGLU': 'glutamate', 'TYR': 'tyrosine', 'ATYR': 'tyrosine', 'BTYR': 'tyrosine', 'MET': 'methionine', 'AMET': 'methionine', 'BMET': 'methionine'}

		def __init__(self, inputAtomLinesList):
			self.resTypeString = inputAtomLinesList[0][3].upper()
			self.resTypeStringLong = self.residueDict[self.resTypeString].upper()
			self.resType = ResidueTypes.residueTypes[self.resTypeStringLong]
			self.resNumber = inputAtomLinesList[0][5]
			self.atomList = inputAtomLinesList
			self.atoms = []
			self.getAtoms()
			self.com_x = 0
			self.com_y = 0
			self.com_z = 0
			self.setCOM()

		def __repr__(self):
			return str([self.com_x, self.com_y, self.com_z])

		def __getitem__(self):
			return [self.com_x, self.com_y, self.com_z]

		def __getitem__(self, i):
			if i == 0:
				return self.com_x
			elif i ==1:
				return self.com_y
			elif i == 2:
				return self.com_z
			else:
				return 0

		#Residue non-static methods
		def getAtoms(self):
			for atom in self.atomList:
				currentAtom = self.Atom(atom)
			self.atoms.append(currentAtom)

		class Atom:
			#contains atom type and x,y,z coordinates

			atomDict = {'H':"hydrogen", 'C':'carbon', 'N':'nitrogen', 'O':'oxygen', 'O1-':'oxygen', 'O1+':'oxygen', 'F': 'fluorine', 'Si':'silicon', 'P': 'phosphorus', 'S': 'sulfur', 'Cl': 'chlorine', 'Se': 'selenium'}

			def __init__(self, atomLine):
				self.element = atomLine[-1]
				self.type = ""
				self.mass = 0
				self.x = float(atomLine[6])
				self.y = float(atomLine[7])
				self.z = float(atomLine[8])
				self.setTypeandMass(self.atomDict[self.element].upper())

			def setTypeandMass(self, inputType):
				self.type = Atomtypes.atomtypes[inputType].type
				self.mass = Atomtypes.atomtypes[inputType].mass

		#Residue non-static methods
		def getCOM(self):
			"""returns center of mass for residue"""
			sum_x = 0
			sum_y = 0
			sum_z = 0
			total_mass = 0
			for atom in self.atoms:
				sum_x = sum_x + (atom.x * atom.mass)
				sum_y = sum_y + (atom.y * atom.mass)
				sum_z = sum_z + (atom.z * atom.mass)
				total_mass = total_mass + atom.mass
			com_x = float(sum_x) / float(total_mass)
			com_y = float(sum_y) / float(total_mass)
			com_z = float(sum_z) / float(total_mass)
			return [com_x, com_y, com_z]

		def setCOM(self):
			com_coordinates = self.getCOM()
			self.com_x = com_coordinates[0]
			self.com_y = com_coordinates[1]
			self.com_z = com_coordinates[2]

