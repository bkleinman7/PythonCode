DNA_A = 0
DNA_C = 0
DNA_G = 0
DNA_T = 0
x = " "
for c in "":
	if c == "A":
		DNA_A += 1
	elif c == "C":
		DNA_C += 1
	elif c == "G":
		DNA_G += 1
	elif c == "T":
		DNA_T += 1
print(DNA_A, x, DNA_C, x, DNA_G, x, DNA_T)