class ResidueTypes:
	def __init__(self, inputLetterCode, input3letterCode, inputName):
		self.letterCode = inputLetterCode
		self.letterCode3 = input3letterCode
		self.name = inputName

global residueTypes
residueTypes = {}

residueTypes["ALANINE"] = ResidueTypes("A", "ala", "alanine")
residueTypes["ARGININE"] = ResidueTypes("R", "arg", "arginine")
residueTypes["ASPARAGINE"] = ResidueTypes("N", "asn", "asparagine")
residueTypes["ASPARTATE"] = ResidueTypes("D", "asp", "aspartate")
residueTypes["CYSTEINE"] = ResidueTypes("C", "cys", "cysteine")
residueTypes["GLUTAMINE"] = ResidueTypes("Q", "gln", "glutamine")
residueTypes["GLUTAMATE"] = ResidueTypes("E", "glu", "glutamate")
residueTypes["GLYCINE"] = ResidueTypes("G", "gly", "glycine")
residueTypes["HISTIDINE"] = ResidueTypes("H", "his", "histidine")
residueTypes["ISOLEUCINE"] = ResidueTypes("I", "ile", "isoleucine")
residueTypes["LEUCINE"] = ResidueTypes("L", "leu", "leucine")
residueTypes["LYSINE"] = ResidueTypes("K", "lys", "lysine")
residueTypes["METHIONINE"] = ResidueTypes("M", "met", "methionine")
residueTypes["PHENYLALANINE"] = ResidueTypes("F", "phe", "phenylalanine")
residueTypes["PROLINE"] = ResidueTypes("P", "pro", "proline")
residueTypes["SERINE"] = ResidueTypes("S", "ser", "serine")
residueTypes["THREONINE"] = ResidueTypes("T", "thr", "threonine")
residueTypes["TRYPTOPHAN"] = ResidueTypes("W", "trp", "tryptophan")
residueTypes["TYROSINE"] = ResidueTypes("Y", "tyr", "tyrosine")
residueTypes["VALINE"] = ResidueTypes("V", "val", "valine")