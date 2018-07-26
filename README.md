# parameter-determination

Purpose
=============

Calculate distance and angle parameters for a large-scale set of PDB protein structures

Overview
=============
All scripts and data structure to calculate structure parameters are contained in the provided python files and run from get_structure_parameters.py. The user must provide a parameters.txt file in the same format as the example file. The script assumes that the chain of interest is labeled chain "A". If multiple sets of atomic coordinates are present for a residue, the script will calculate distances with the final set of coordinates given.

The example folder includes all scripts, input PDB structures for the Aurora Kinase A, and the output file.

Method
=============
User must create parameters.txt file in the same format as the example. For each parameter, specify "distance" or "angle" (do not include quotes) and 2 residue numbers (for distance) or 3 residue numbers (for angle). For angles, the second residue is the vertex. All calculations are performed on the residue center of mass.

To calculate the parameters, simply run the get_structure_parameters.py file with python. Numpy is required for the script to work.

```bash
python get_structure_parameters.py
```
Measurements output in the output.txt file written by the script. Distances are reported in angstroms, angles are reported in degrees.

System Requirements
======
Python dependencies:

*numpy
