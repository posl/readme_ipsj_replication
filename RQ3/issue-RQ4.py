import csv
import os
import codecs
import linecache
import string
from statistics import median, mean

c_list1 = []
c_list2 = []
c_list3 = []
c_list4 = []
c_list5 = []
c_list6 = []
c_list7 = []
c_list8 = []
c_list0 = []

csv_file1 = open('based_list_.csv','r',encoding='utf-8', errors="", newline="")
infile = csv.reader(csv_file1,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
csv_file2 = open('first_list_.csv','r',encoding='utf-8', errors="", newline="")
infile2 = csv.reader(csv_file2,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
csv_file3 = open('based_list_.csv','r',encoding='utf-8', errors="", newline="")
infile3 = csv.reader(csv_file3,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

header = next(infile)
header = next(infile2)
header = next(infile3)

n = 0

bl = []
fl = []
margin = 0

for line in infile:
    bl.append(line[3])


for row in infile2:
    fl.append(row[3])


for n in range(49):
    margin = int(bl[n]) - int(fl[n])

    if margin == 1:
        c_list1.append(n+1)
    elif margin == 2:
        c_list2.append(n+1)
    elif margin == 3:
        c_list3.append(n+1)
    elif margin == 4:
        c_list4.append(n+1)
    elif margin == 5:
        c_list5.append(n+1)
    elif margin == 6:
        c_list6.append(n+1)
    elif margin == 7:
        c_list7.append(n+1)
    elif margin == 8:
        c_list8.append(n+1)
    elif margin == 0:
        c_list0.append(n+1)
    
    n += 1

c1 = []
c2 = []
c3 = [] 
c4 = []
c5 = []
c6 = []
c7 = []
c8 = []
c0 = []

ca1 = []
ca2 = []
ca3 = [] 
ca4 = []
ca5 = []
ca6 = []
ca7 = []
ca8 = []
ca0 = []

a1 = len(c_list1)
a2 = len(c_list2)
a3 = len(c_list3)
a4 = len(c_list4)
a5 = len(c_list5)
a6 = len(c_list6)
a7 = len(c_list7)
a8 = len(c_list8)
a0 = len(c_list0)

n = 0

for line2 in infile3:
    n += 1
    if n in c_list1:
        c1.append(int(line2[4]))
        ca1.append(int(line2[5]))
    elif n in c_list2:
        c2.append(int(line2[4]))
        ca2.append(int(line2[5]))
    elif n in c_list3:
        c3.append(int(line2[4]))
        ca3.append(int(line2[5]))
    elif n in c_list4:
        c4.append(int(line2[4]))
        ca4.append(int(line2[5]))
    elif n in c_list5:
        c5.append(int(line2[4]))
        ca5.append(int(line2[5]))
    elif n in c_list6:
        c6.append(int(line2[4]))
        ca6.append(int(line2[5]))
    elif n in c_list7:
        c7.append(int(line2[4]))
        ca7.append(int(line2[5]))
    elif n in c_list8:
        c8.append(int(line2[4]))
        ca8.append(int(line2[5]))
    elif n in c_list0:
        c0.append(int(line2[4]))
        ca0.append(int(line2[5]))

ave0 = []
ave1 = []
ave2 = []
ave3 = []
ave4 = []
ave5 = []
ave6 = []
ave7 = []
ave8 = []

for i in range(len(c1)):
    ave1.append(c1[i]/ca1[i])
for i in range(len(c2)):
    ave2.append(c2[i]/ca2[i])
for i in range(len(c3)):
    ave3.append(c3[i]/ca3[i])
for i in range(len(c4)):
    ave4.append(c4[i]/ca4[i])
for i in range(len(c5)):
    ave5.append(c5[i]/ca5[i])
for i in range(len(c6)):
    ave6.append(c6[i]/ca6[i])
for i in range(len(c7)):
    ave7.append(c7[i]/ca7[i])
for i in range(len(c8)):
    ave8.append(c8[i]/ca8[i])

print(mean(ave1))
print(mean(ave2))
print(mean(ave3))
print(mean(ave4))
print(mean(ave5))
print(mean(ave6))
print(mean(ave7))
#print(mean(ave8))



title = ['categories','add num','commit ave README.md','commit ave ALL','README.md commit rate']
'''
one = [1,a1,median(c1),ca1/a1,c1/ca1*100]
two = [2,a2,median(c2),ca2/a2,c2/ca2*100]
three = [3,a3,median(c3),ca3/a3,c3/ca3*100]
four = [4,a4,median(c4),ca4/a4,c4/ca4*100]
five = [5,a5,median(c5),ca5/a5,c5/ca5*100]
six = [6,a6,median(c6),ca6/a6,c6/ca6*100]
seven = [7,a7,median(c7),ca7/a7,c7/ca7*100]
if(a0 == 0):
    zero = [0, 0, 0, 0, 0]
else:
    zero = [0,a0,c0/a0,ca0/a0,c0/ca0*100]
if(a8 == 0):
    eight = [8, 0, 0, 0, 0]
else:
    eight = [8,a8,c8/a8,ca8/a8,c8/ca8*100]
if(a8 == 0):
    ave = ['ave',(a1+a2+a3+a4+a5+a6+a7+a0)/9,(c1/a1+c2/a2+c3/a3+c4/a4+c5/a5+c6/a6+c7/a7+c0/a0)/9,(ca1/a1+ca2/a2+ca3/a3+ca4/a4+ca5/a5+ca6/a6+ca7/a7+ca0/a0)/9,(c1/ca1*100+c2/ca2*100+c3/ca3*100+c4/ca4*100+c5/ca5*100+c6/ca6*100+c7/ca7*100+c0/ca0*100)/9]
else:
    ave = ['ave',(a1+a2+a3+a4+a5+a6+a7+a8+a0)/9,(c1/a1+c2/a2+c3/a3+c4/a4+c5/a5+c6/a6+c7/a7+c8/a8+c0/a0)/9,(ca1/a1+ca2/a2+ca3/a3+ca4/a4+ca5/a5+ca6/a6+ca7/a7+ca8/a8+ca0/a0)/9,(c1/ca1*100+c2/ca2*100+c3/ca3*100+c4/ca4*100+c5/ca5*100+c6/ca6*100+c7/ca7*100+c8/ca8*100+c0/ca0*100)/9]
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)
print(zero)
print(ave)
'''

f = open('RQ4_result.csv','w')
F = csv.writer(f)
'''
F.writerow(title)
F.writerow(one)
F.writerow(two)
F.writerow(three)
F.writerow(four)
F.writerow(five)
F.writerow(six)
F.writerow(seven)
F.writerow(eight)
F.writerow(zero)
F.writerow(ave)
'''

csv_file1.close()
csv_file2.close()
csv_file3.close()
f.close()

