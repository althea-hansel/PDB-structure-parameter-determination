class Atomtype:
	def __init__(self, inputType, inputMass):
		self.type = inputType
		self.mass = inputMass

global atomtypes
atomtypes = {}

atomtypes["HYDROGEN"] = Atomtype("H", 1.0079)
atomtypes["CARBON"] = Atomtype("C", 12.0107)
atomtypes["NITROGEN"] = Atomtype("N", 14.0067)
atomtypes["OXYGEN"] = Atomtype("O", 15.999)
atomtypes["FLUORINE"] = Atomtype("F", 18.9984)
atomtypes["SILICON"] = Atomtype("Si", 28.0855)
atomtypes["PHOSPHORUS"] = Atomtype("P", 30.9738)
atomtypes["SULFUR"] = Atomtype("S", 32.065)
atomtypes["CHLORINE"] = Atomtype("Cl", 35.453)
atomtypes["SELENIUM"] = Atomtype("Se", 78.96)