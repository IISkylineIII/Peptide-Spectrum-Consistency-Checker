spectrum = {0, 71, 99, 101, 103, 128, 129, 199, 200, 204, 227, 230, 231, 298, 303, 328, 330, 332, 333}

peptides = ["TVQ", "AVQ", "ETC", "TCQ", "QCV", "TCE"]

def calculate_mass(peptide):
    mass_table = {
        'A': 71, 'C': 103, 'E': 129, 'G': 57, 'H': 137,
        'I': 113, 'K': 128, 'L': 113, 'M': 131, 'N': 114,
        'P': 97, 'Q': 128, 'R': 156, 'S': 87, 'T': 101,
        'V': 99, 'W': 186, 'Y': 163
    }
    return sum([mass_table[aa] for aa in peptide])

consistent_peptides = []

for peptide in peptides:
    mass = calculate_mass(peptide)
    if mass in spectrum:
        consistent_peptides.append(peptide)

print("Peptídeos consistentes com o espectro:")
for peptide in consistent_peptides:
    print(peptide)
