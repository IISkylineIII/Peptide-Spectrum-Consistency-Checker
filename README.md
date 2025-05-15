# Peptide-Spectrum-Consistency-Checker

This Python script identifies linear peptides that are consistent with a given experimental mass spectrum, a common task in computational proteomics.

# Overview
Given:

* A set of peptide candidates (amino acid sequences);

* An experimental mass spectrum (a set of integer mass values);

The script checks which peptides have a total mass matching one of the values in the spectrum.

How It Works
* Each peptide is translated into its total monoisotopic mass, using a standard amino acid mass table.

* The total mass is compared against the given spectrum.

* Peptides with matching masses are considered consistent.

# Example
```
spectrum = {0, 71, 99, 101, 103, 128, 129, 199, 200, 204, 227, 230, 231, 298, 303, 328, 330, 332, 333}

peptides = ["TVQ", "AVQ", "ETC", "TCQ", "QCV", "TCE"]
```

# Output:

TVQ
AVQ
ETC
TCQ
QCV
TCE 


Mass Table Used
Amino Acid	Mass		Amino Acid	Mass
A	          71		       N	    114
C	          103		       P	    97
E	          129	       	 Q   	  128
G	          57	         R	    156
H	          137		       S	    87
I/L	        113	      	 T	    101
K         	128		       V    	99
M	          131		       W	    186
Y	          163			

# Running the Script
To run the script:

python peptide_checker.py


#Applications
* Mass spectrometry-based peptide identification
* Peptide sequencing algorithms
* Bioinformatics education

# License
This project is licensed under the MIT License – see the LICENSE file for more details.
