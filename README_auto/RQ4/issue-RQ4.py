import csv
import os
import codecs
import linecache
import string

c_list1 = []
c_list2 = []
c_list3 = []
c_list4 = []
c_list5 = []
c_list6 = []
c_list7 = []
c_list8 = []

csv_file1 = open('based_list.csv','r',encoding='utf-8', errors="", newline="")
infile = csv.reader(csv_file1,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
csv_file2 = open('first_list.csv','r',encoding='utf-8', errors="", newline="")
infile2 = csv.reader(csv_file2,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
csv_file3 = open('based_list.csv','r',encoding='utf-8', errors="", newline="")
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


for n in range(392):
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
    
    n += 1

c1 = 0
c2 = 0
c3 = 0 
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0

ca1 = 0
ca2 = 0
ca3 = 0 
ca4 = 0
ca5 = 0
ca6 = 0
ca7 = 0
ca8 = 0

a1 = len(c_list1)
a2 = len(c_list2)
a3 = len(c_list3)
a4 = len(c_list4)
a5 = len(c_list5)
a6 = len(c_list6)
a7 = len(c_list7)
a8 = len(c_list8)

n = 0

for line2 in infile3:
    n += 1
    if n in c_list1:
        c1 += int(line2[4])
        ca1 += int(line2[5])
    elif n in c_list2:
        c2 += int(line2[4])
        ca2 += int(line2[5])
    elif n in c_list3:
        c3 += int(line2[4])
        ca3 += int(line2[5])
    elif n in c_list4:
        c4 += int(line2[4])
        ca4 += int(line2[5])
    elif n in c_list5:
        c5 += int(line2[4])
        ca5 += int(line2[5])
    elif n in c_list6:
        c6 += int(line2[4])
        ca6 += int(line2[5])
    elif n in c_list7:
        c7 += int(line2[4])
        ca7 += int(line2[5])
    elif n in c_list8:
        c8 += int(line2[4])
        ca8 += int(line2[5])


print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
print(a7)
print(a8)

print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)
print(c8)
   
print(ca1)
print(ca2)
print(ca3)
print(ca4)
print(ca5)
print(ca6)
print(ca7)
print(ca8)

title = ['categories','add num','commit ave README.md','commit ave ALL','README.md commit rate']
one = [1,a1,c1/a1,ca1/a1,c1/ca1*100]
two = [2,a2,c2/a2,ca2/a2,c2/ca2*100]
three = [3,a3,c3/a3,ca3/a3,c3/ca3*100]
four = [4,a4,c4/a4,ca4/a4,c4/ca4*100]
five = [5,a5,c5/a5,ca5/a5,c5/ca5*100]
six = [6,a6,c6/a6,ca6/a6,c6/ca6*100]
seven = [7,a7,c7/a7,ca7/a7,c7/ca7*100]
eight = [8,a8,c8/a8,ca8/a8,c8/ca8*100]
ave = ['ave',(a1+a2+a3+a4+a5+a6+a7+a8)/8,(c1/a1+c2/a2+c3/a3+c4/a4+c5/a5+c6/a6+c7/a7+c8/a8)/8,(ca1/a1+ca2/a2+ca3/a3+ca4/a4+ca5/a5+ca6/a6+ca7/a7+ca8/a8)/8,(c1/ca1*100+c2/ca2*100+c3/ca3*100+c4/ca4*100+c5/ca5*100+c6/ca6*100+c7/ca7*100+c8/ca8*100)/8]
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)
print(ave)

f = open('RQ4_result.csv','w')
F = csv.writer(f)

F.writerow(title)
F.writerow(one)
F.writerow(two)
F.writerow(three)
F.writerow(four)
F.writerow(five)
F.writerow(six)
F.writerow(seven)
F.writerow(eight)
F.writerow(ave)


csv_file1.close()
csv_file2.close()
csv_file3.close()
f.close()