from collections import Counter

f = open("example.txt", "r")

Spectrum = f.readline().strip().split(' ')

Spectrum_array = []

for i in range(len(Spectrum)):
    for j in range(len(Spectrum)):
        new_num = (int(Spectrum[j])-int(Spectrum[i]))
        print(int(Spectrum[i]), int(Spectrum[j]), new_num)
        if(new_num >= 57 and new_num <= 200):
            Spectrum_array.append(new_num)

final_string = ""

print(Counter(Spectrum_array))

for i in Counter(Spectrum_array):
    for j in range(Counter(Spectrum_array)[i]):
        final_string += str(i) + ' '

print(final_string)
        
