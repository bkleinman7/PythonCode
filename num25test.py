import collections
import itertools
in_file = open('example.txt', 'r')
line = 1
in_adjacency=[]
lpos = 0
for in_data in in_file:
    ldata = in_data.strip(' \t\n\r')
    if (len(ldata)==0):
        break
    else:
        ls = ldata.split()
        in_adjacency.append(ls[0]+ls[2][-1])

# in_adjacency => ['CTTA', 'ACCA', 'TACC', 'GGCT', 'GCTT', 'TTAC']
lpos = len(in_adjacency[0])-2
i=0
tot_iadj = len(in_adjacency)
pos =1

while (1<tot_iadj):
    ia = in_adjacency[i]
    end_ia = ia[pos:len(ia)]
    match=False
    for j,ja in enumerate(in_adjacency):
        sta_ja = ja[0:len(ia)-pos]
        if (end_ia==sta_ja and ja != ia and len(end_ia)>lpos):
            in_adjacency.remove(ja)
            in_adjacency.remove(ia)
            in_adjacency.append(ia +  ja[len(sta_ja):len(ja)])
            i=-1
            tot_iadj = len(in_adjacency)
            match=True
            pos = 1
            break
    if(not match):
        pos+=1
        if (len(end_ia)==0):
            i+=1
            pos=1
    else:
        i+=1
for i,d in enumerate(in_adjacency):
   print(d)
