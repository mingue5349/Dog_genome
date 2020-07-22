f1 = open('DLA-88_from_Kennedy', 'r')
f2 = open('DLA-88_from_Kennedy_parsed', 'w')

DLA88dic = {}
f1linelist = f1.readlines()
for i in range(len(f1linelist)):
    if '>' in f1linelist[i]:
# 시퀀스가 2줄 나오면 하나로 묶기
        DLAnamelist = f1linelist[i].split('\t')
        DLAnamelist_2 = f1linelist[i + 2].split('\t')
        DLAnamelist_m2 = f1linelist[i-2].split('\t')
        if '>' not in (f1linelist[i+1] and f1linelist[i+2]):
            f2.write('>' + DLAnamelist[1].strip() + '\n' + f1linelist[i+1].strip() + f1linelist[i+2])

# 한 줄 시퀀스 추리기
        for i in range(f1linelist):
            if '>' in i:



# 나머지 시퀀스 묶기
        else:
            if DLAnamelist[1] == DLAnamelist_2[1]:
                f2.write('>' + DLAnamelist[1].strip() + '\n' + f1linelist[i+1].strip() + f1linelist[i+3])


f1.close()
f2.close()