import collections

masses = {"G": 57,
"A": 71,
"S": 87,
"P": 97,
"V": 99,
"T": 101,
"C": 103,
"I": 113,
"L": 113,
"N": 114,
"D": 115,
"K": 128,
"Q": 128,
"E": 129,
"M": 131,
"H": 137,
"F": 147,
"R": 156,
"Y": 163,
"W": 186}

amino_acids = ["G", "A", "S", "P", "V"
, "T", "C", "I", "L", "N", "D", "K", "Q", "E", "M"
, "H", "F", "R", "Y", "W"]

def ParentMass(Spectrum):
    myMax = Spectrum[0]
    for num in Spectrum:
        if int(myMax) < int(num):
            myMax = int(num)
    return(myMax)


def Mass(peptide):
	total = 0
	for amino_acid in peptide:
		total += masses[amino_acid]
	return total

def Expand(Peptides):
    expanded_peptide = []
    for peptide in Peptides:
        for amino in amino_acids:
            expanded_peptide.append(peptide + amino)
    return(expanded_peptide)

def cyclicSpec(peptide):
    mass_array = ['0', str(Mass(peptide))]
    peptide_2 = (2*peptide)
    #print(peptide_2)
    for i in range(1, len(peptide)):
        for j in range(len(peptide)):
            mass_array.append(str(Mass(peptide_2[j:j+i])))
    return(sorted(mass_array))

def linearSpec(peptide):
	mass_array = ['0']

	for i in range(0, len(peptide)):
	    for j in range(i, len(peptide)):
	        mass_array.append(str(Mass(peptide[i:j+1])))

	return(sorted(mass_array))

def consistent(current, final):

    if not set(current).issubset(set(final)):
        return(False)

    return(True)


def cycloPeptideSequencing(Spectrum):
    Peptides = [""]
    out_array = []
    max_value = int(ParentMass(Spectrum))
    while Peptides:
        Peptides = Expand(Peptides)
        #print(len(Peptides))
        for Peptide in Peptides[:]:
            total_m = int(Mass(Peptide))
            total_p = max_value
            if(total_m == total_p):
                out_array.append(Peptide)
                Peptides.remove(Peptide)
            elif consistent(linearSpec(Peptide), Spectrum) == False:
                Peptides.remove(Peptide)

    return(sorted(out_array))

f = open("example.txt", "r")

Spectrum = f.readline().strip().split(' ')

f.close()

finally_array = cycloPeptideSequencing(Spectrum)

#print(finally_array)

final_set = set()

for i in finally_array:
    output = ""
    max = len(finally_array[0])
    max_count = 0
    for j in i:
        if max_count == max-1:
            output += str(masses[j])
        elif max_count < max:
            output += str(masses[j]) + '-'
        max_count += 1
    final_set.add(output)

final_string = ""

for l in sorted(final_set):
    final_string += l + ' '

print(final_string)
