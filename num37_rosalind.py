from collections import Counter

def Expand(Peptide_masses, amino_acids_masses):
    expanded_peptide = []
    for peptide_mass in Peptide_masses:
        if peptide_mass == 0:
            for amino in amino_acids_masses:
                num = []
                num.append(peptide_mass)
                num.append(amino)
                expanded_peptide.append(num)
        else:
            temp_pep = peptide_mass[:]
            for amino in amino_acids_masses:
                temp_pep.append(amino)
                expanded_peptide.append(temp_pep)
                temp_pep = peptide_mass[:]

    return(sorted(expanded_peptide))

def cyclicSpec(peptide):

    mass_array = [0, sum(peptide)]

    peptide_2 = (2*peptide)

    for i in range(1, len(peptide)):
        for j in range(len(peptide)):
            mass_array.append(sum(peptide_2[j:j+i]))

    return(mass_array)

def Score(Peptide, Spectrum):
    score = 0;

    for m in Counter(Peptide):
        if m in Counter(Spectrum):
            score += 1
    return(score)

def Cut(Leader, Spec, N):

    if(len(Leader) <= int(N)):
        return(Leader)
    else:
        score = 0
        temp_n = int(N)
        leader_score = {}
        for l in Leader:
            score = Score(cyclicSpec(l), Spec)
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

        return(sorted(output_array))

def ConvolutionCyclopeptideSequencing(Spectrum, M):
    Spectrum_array = []
    return_array = []
    final_array = []

    x = 0
    temp_int = 0
    
    for i in range(len(Spectrum)):
        for j in range(len(Spectrum)):
            new_num = (Spectrum[j]-Spectrum[i])
            if(new_num >= 57 and new_num <= 200):
                Spectrum_array.append(new_num)

    #print(Counter(Spectrum_array))

    for i in sorted(Counter(Spectrum_array), key=Counter(Spectrum_array).get, reverse = True):
        if(x > int(M) and (temp_int != Counter(Spectrum_array)[i])):
            break
        for j in range(Counter(Spectrum_array)[i]):
            if i not in final_array:
                final_array.append(i)
        x += 1
        
        if (x > int(M)):
            temp_int = Counter(Spectrum_array)[i]

    for k in sorted(final_array):
        return_array.append(k)

    return(return_array)

def leaderBoardCyclopeptideSequencing(Spectrum, parent_mass, N, Spec_int_array):
    Leaderboard = [0]
    LeaderPeptide = 0
    LeaderScore = 0
    x = 0
    while Leaderboard[:]:
        Leaderboard = Expand(Leaderboard, Spectrum)
        for peptide_mass in Leaderboard[:]:
            if sum(peptide_mass) == parent_mass:
                curr_score = Score(cyclicSpec(peptide_mass), Spec_int_array)
                if curr_score > LeaderScore:
                    LeaderPeptide = peptide_mass
                    LeaderScore = curr_score
            elif(sum(peptide_mass) > parent_mass):
                Leaderboard.remove(peptide_mass)
                
        Leaderboard = Cut(Leaderboard, Spec_int_array, N)

    return(LeaderPeptide)

f = open("example.txt", "r")

M = f.readline().strip()
N = f.readline().strip()
Spectrum = f.readline().strip().split(' ')

Spec_int_array = []

for s in Spectrum:
    Spec_int_array.append(int(s))

f.close()

cyclo_spec = ConvolutionCyclopeptideSequencing(Spec_int_array, M)

parent_mass = max(Spec_int_array)

finally_array = leaderBoardCyclopeptideSequencing(cyclo_spec, parent_mass, N, Spec_int_array)
print(finally_array)
output_test = ""

for i in finally_array:
    if i != 0:
        output_test += str(i) + '-'

print(output_test[:-1])
