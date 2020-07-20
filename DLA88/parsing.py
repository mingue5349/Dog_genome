f1 = open('DLA-88_from_Kennedy', 'r')
f2 = open('output1.txt', 'w')


for f1line in f1:
    if '>' in f1line:
        f2.write('\n'+ f1line)
    else:
        f2.write(f1line.strip())

f1.close()
f2.close()

f3 = open('output1.txt', 'r')
f4 = open('output2.txt', 'w')

for f3line in f3:
    if '>' in f3line:
        header = f3line.split('\t')
        joinheader = '_'.join(header)
        if header[2] == 'exon2\n':
            f4.write(joinheader.strip() + '+exon3' + '\n')
            f4.write(f3.readline().strip())
            f3.readline()
            f4.write(f3.readline())
        elif header[2] == 'exon3':
            continue
        else:
            f4.write(joinheader)
            f4.write(f3.readline())
f3.close()
f4.close()





f3.close()
f4.close()

