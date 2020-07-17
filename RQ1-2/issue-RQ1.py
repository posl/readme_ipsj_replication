import csv
import os
import string
import linecache

csv_file1 = open('based_list.csv','r',encoding='utf-8', errors="", newline="")
infile = csv.reader(csv_file1,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

csv_file2 = open('first_list.csv','r',encoding='utf-8', errors="", newline="")
infile2 = csv.reader(csv_file2,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

csv_file3 = open('RQ1_result.csv','w')
outfile = csv.writer(csv_file3)

header = next(infile)
header = next(infile2)



what1 = 0
why1 = 0
how1 = 0
when1 = 0
who1 = 0
references1 = 0
contribution1 = 0
other1 = 0

what2 = 0
why2 = 0
how2 = 0
when2 = 0
who2 = 0
references2 = 0
contribution2 = 0
other2 = 0

for row in infile:
    if row[2].find('1') != -1:
        what1 += 1
    
    if row[2].find('2') != -1:
        why1 += 1
    
    if row[2].find('3') != -1:
        how1 += 1
    
    if row[2].find('4') != -1:
        when1 += 1

    if row[2].find('5') != -1:
        who1 += 1
    
    if row[2].find('6') != -1:
        references1 += 1

    if row[2].find('7') != -1:
        contribution1 += 1
    
    if row[2].find('8') != -1:
        other1 += 1


for row2 in infile2:
 
    if row2[2].find('1') != -1:
        what2 += 1
    
    if row2[2].find('2') != -1:
        why2 += 1
    
    if row2[2].find('3') != -1:
        how2 += 1
    
    if row2[2].find('4') != -1:
        when2 += 1

    if row2[2].find('5') != -1:
        who2 += 1
    
    if row2[2].find('6') != -1:
        references2 += 1

    if row2[2].find('7') != -1:
        contribution2 += 1
    
    if row2[2].find('8') != -1:
        other2 += 1

what3 = what1 - what2
why3 = why1 - why2
how3 = how1 - how2
when3 = when1 - when2
who3 = who1 - who2
who3 = who1 - who2
references3 = references1 - references2
contribution3 = contribution1 - contribution2
other3 = other1 - other2

title = ['category','first','addition','last']
what = ['what',what2,what3,what1]
why = ['why',why2,why3,why1]
how = ['how',how2,how3,how1]
when = ['when',when2,when3,when1]
who = ['who',who2,who3,who1]
references = ['references',references2,references3,references1]
contribution = ['contribution',contribution2,contribution3,contribution1]
other = ['other',other2,other3,other1]

outfile.writerow(title)
outfile.writerow(what)
outfile.writerow(why)
outfile.writerow(how)
outfile.writerow(when)
outfile.writerow(who)
outfile.writerow(references)
outfile.writerow(contribution)
outfile.writerow(other)


nc = int(linecache.getline('no_category.csv',1))
print(nc)
nc = str(nc)
no_category = ['no category',nc,'-','-']
outfile.writerow(no_category)

csv_file1.close()
csv_file2.close()
csv_file3.close()