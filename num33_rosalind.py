masses = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]

m = 57

def peptides(n, dictionary):
	for m in masses:
		if (n - m) in dictionary:
			dictionary[n] = dictionary.get(n, 0) + dictionary[n-m]
			print(dictionary[n])
	return dictionary


def pep_counter(m):
	dicc = {0:1}
	#recurssively update dictionary
	for i in range(m + 1):
		peptides(i, dicc)
	return dicc

print(pep_counter(m)[m])
