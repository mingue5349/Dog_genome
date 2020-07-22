#!/usr/bin/env python 3


f1 = open("Kennedy 2007", 'r')
f2 = open("output.txt", 'w')

haplist = []
SampleSize = 0

for line in f1:
    linelist = line.rstrip().split('\t')
    num_sample = int(linelist[2])
    SampleSize += num_sample

    if '1' in linelist[1] :
        #f2.write(f"SampleName={linelist[0]}\n")
        f2.write('SampleName = "' + linelist[0] + '"' + '\n')
        f2.write(f"SampleSize={SampleSize}\n")
        f2.write("SampleData= {\n")

        # Write haplotype
        # id = 1
        f2.write('\t'.join(linelist[1:]) + '\n')
        # id > 1
        for hap_line in haplist:
            f2.write(f"{hap_line}\n")
        f2.write("}" + '\n')

        # Initialize variables
        SampleSize = 0
        haplist = []

    else:
        haplist.append('\t'.join(linelist[1:]))

f2.close()
f1.close()