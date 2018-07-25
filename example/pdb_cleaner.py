def cleaner(pdbFilePath):
	outputList = []
	with open(pdbFilePath, 'r') as f:
		pdb = [ line.split() for line in f.readlines()]
	for line in pdb:
		outputLine = []
		if line[0] == "ATOM":
			for column in line:
				outputColumn = column[0]
				for i in range(len(column))[1:]:
					if column[i] == "-":
						outputColumn = outputColumn + " " + column[i]
					else:
						outputColumn = outputColumn + column[i]
				outputLine.append(outputColumn)
		else:
			outputLine = line
		outputList.append(outputLine)

	with open(pdbFilePath, 'w') as f:
		for line in outputList:
			for column in line:
				f.write(column + " ")
			f.write("\n")