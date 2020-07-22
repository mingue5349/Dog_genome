f1 = open('CDS FASTA IPD.fa', 'r')
f2 = open('DLA-88 from Kennedy parsed.fa', 'r')


f1set = set()
f2set = set()

for f1line in f1:
    if '>' in f1line:
        nomen = f1line.split("|")
        f1set.add(nomen[1])

for f2line in f2:
    if '>' in f2line:
        nomen = f2line.split("_")
        f2set.add(nomen[1])

#print(f1set-f2set)
print(f2set-f1set)

