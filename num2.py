text = "GTATTGTAAGCGACATGAGCGACATGAGCGACATGACTTGGTAGAGCGACATGGTATTGTAAGCTCCAGTAAGCGACATGGTATTGTATCGGACTTGGTATTGTAAGCTCCAGTAACTTGGTAGGTATTGTATCGGACTTGACTTGGTAGACTTGGTAGGTATTGTAAGCGACATGAGCTCCAGTAAGCGACATGTCGGACTTGAGCGACATGGTATTGTAACTTGGTAGACTTGGTAGAGCTCCAGTAGTATTGTAAGCTCCAGTATCGGACTTGAGCTCCAGTAACTTGGTAGTCGGACTTGACTTGGTAGTCGGACTTGTCGGACTTGAGCGACATGACTTGGTAGTCGGACTTGTCGGACTTGAGCTCCAGTAACTTGGTAGAGCGACATGACTTGGTAGAGCTCCAGTAGTATTGTAAGCGACATGTCGGACTTGGTATTGTAGTATTGTAAGCTCCAGTAGTATTGTAGTATTGTAAGCTCCAGTATCGGACTTGAGCTCCAGTAAGCTCCAGTATCGGACTTGACTTGGTAGACTTGGTAGTCGGACTTGAGCGACATGGTATTGTATCGGACTTGGTATTGTAACTTGGTAGTCGGACTTGTCGGACTTGAGCTCCAGTAAGCGACATGACTTGGTAGAGCGACATGACTTGGTAGACTTGGTAGAGCGACATGGTATTGTAAGCGACATGAGCTCCAGTAAGCTCCAGTAACTTGGTAGAGCTCCAGTAACTTGGTAGGTATTGTAACTTGGTAGAGCGACATGTCGGACTTGACTTGGTAGAGCTCCAGTAGTATTGTAAGCGACATGAGCGACATGAGCTCCAGTAGTATTGTATCGGACTTGAGCTCCAGTAGTATTGTAGTATTGTAAGCTCCAGTAGTATTGTAAGCGACATGGTATTGTAACTTGGTAGAGCTCCAGTATCGGACTTGTCGGACTTGTCGGACTTGAGCTCCAGTAGTATTGTA"
size = 12
thislist = []
count = 0
maxcount = 0
maxlist = []
j = 0

for i in range(0,len(text)-size+1):
    text = list(text)
    kmer = ''.join(text[i:i+size])
    thislist.insert(i, kmer)

for i in range(0,len(text)-size+1):
    text = list(text)
    kmer = ''.join(text[i:i+size])
    count = 0
    for x in thislist:
        if kmer == x:
            count += 1
        if count > maxcount:
            maxcount = count

for i in range(0,len(text)-size+1):
    text = list(text)
    kmer = ''.join(text[i:i+size])
    count = 0
    for x in thislist:
        if kmer == x:
            thislist.remove(kmer)
            count += 1            
        if count == maxcount:
            if kmer not in maxlist:
                maxlist.append(kmer) 

for x in maxlist:
    print(x)