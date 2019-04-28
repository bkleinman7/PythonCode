from collections import Counter

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

    for i in range(1, len(peptide)):
        for j in range(len(peptide)):
            mass_array.append(str(Mass(peptide_2[j:j+i])))
    return(sorted(mass_array))

def Score(Peptide, Spectrum):
    score = 0;
    for m in Counter(Peptide):
        if m in Counter(Spectrum):
            score += 1
    return(score)

def Cut(Leader, Spec, N):

    leader_score = {}
    temp_n = int(N)
    for l in Leader:
        score = Score(cyclicSpec(l), Spec)
        #print(linearSpec(l), Spec, score)
        if score in leader_score:
            leader_score[score].append(l)
        else:
            leader_score[score] = [l]

    output_array = []

    for score in sorted(leader_score.keys(), reverse = True):
        output_array.extend(leader_score[score])
        temp_n -= int(len(leader_score[score]))
        if temp_n < 0:
            break

    return(output_array)

def leaderBoardCyclopeptideSequencing(Spectrum, N):
    Leaderboard = [""]
    LeaderPeptide = ''
    LeaderScore = 0
    while Leaderboard[:]:
        Leaderboard = Expand(Leaderboard)
        for Peptide in Leaderboard[:]:
            if int(Mass(Peptide)) == int(ParentMass(Spectrum)):
                #print("FOUND!")
                curr_score = Score(cyclicSpec(Peptide), Spectrum)
                if curr_score > LeaderScore:
                    LeaderPeptide = Peptide
                    LeaderScore = curr_score
            elif(int(Mass(Peptide)) > int(ParentMass(Spectrum))):
                Leaderboard.remove(Peptide)
        Leaderboard = Cut(Leaderboard, Spectrum, N)

    return(LeaderPeptide)

f = open("example.txt", "r")

Spectrum = f.readline().strip().split(' ')

f.close()

for N in range(1,100):

    finally_array = leaderBoardCyclopeptideSequencing(Spectrum, N)

    print(N, finally_array)

'''for i in finally_array:
    output_test += str(masses[i]) + '-'

print(output_test[:-1])'''
