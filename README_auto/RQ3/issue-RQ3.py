import csv
import os
import string

csv_file0 = open('based_list.csv','r',encoding='utf-8', errors="", newline="")
infile = csv.reader(csv_file0,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

csv_file1 = open('first_list.csv','r',encoding='utf-8', errors="", newline="")
infile1 = csv.reader(csv_file1,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

csv_file2 = open('second_list.csv','r',encoding='utf-8', errors="", newline="")
infile2 = csv.reader(csv_file2,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

csv_file3 = open('third_list.csv','r',encoding='utf-8', errors="", newline="")
infile3 = csv.reader(csv_file3,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

csv_file4 = open('fourth_list.csv','r',encoding='utf-8', errors="", newline="")
infile4 = csv.reader(csv_file4,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

csv_file = open('RQ3_result.csv','w')
outfile = csv.writer(csv_file)

header = next(infile)
header = next(infile2)



what = 0
why = 0
how = 0
when = 0
who = 0
references = 0
contribution = 0
other = 0

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

what3 = 0
why3 = 0
how3 = 0
when3 = 0
who3 = 0
references3 = 0
contribution3 = 0
other3 = 0

what4 = 0
why4 = 0
how4 = 0
when4 = 0
who4 = 0
references4 = 0
contribution4 = 0
other4 = 0

for row in infile:
    if row[2].find('1') != -1:
        what += 1
    
    if row[2].find('2') != -1:
        why += 1
    
    if row[2].find('3') != -1:
        how += 1
    
    if row[2].find('4') != -1:
        when += 1

    if row[2].find('5') != -1:
        who += 1
    
    if row[2].find('6') != -1:
        references += 1

    if row[2].find('7') != -1:
        contribution += 1
    
    if row[2].find('8') != -1:
        other += 1


for row1 in infile1:
 
    if row1[2].find('1') != -1:
        what1 += 1
    
    if row1[2].find('2') != -1:
        why1 += 1
    
    if row1[2].find('3') != -1:
        how1 += 1
    
    if row1[2].find('4') != -1:
        when1 += 1

    if row1[2].find('5') != -1:
        who1 += 1
    
    if row1[2].find('6') != -1:
        references1 += 1

    if row1[2].find('7') != -1:
        contribution1 += 1
    
    if row1[2].find('8') != -1:
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

for row3 in infile3:
 
    if row3[2].find('1') != -1:
        what3 += 1
    
    if row3[2].find('2') != -1:
        why3 += 1
    
    if row3[2].find('3') != -1:
        how3 += 1
    
    if row3[2].find('4') != -1:
        when3 += 1

    if row3[2].find('5') != -1:
        who3 += 1
    
    if row3[2].find('6') != -1:
        references3 += 1

    if row3[2].find('7') != -1:
        contribution3 += 1
    
    if row3[2].find('8') != -1:
        other3 += 1

for row4 in infile4:
 
    if row4[2].find('1') != -1:
        what4 += 1
    
    if row4[2].find('2') != -1:
        why4 += 1
    
    if row4[2].find('3') != -1:
        how4 += 1
    
    if row4[2].find('4') != -1:
        when4 += 1

    if row4[2].find('5') != -1:
        who4 += 1
    
    if row4[2].find('6') != -1:
        references4 += 1

    if row4[2].find('7') != -1:
        contribution4 += 1
    
    if row4[2].find('8') != -1:
        other4 += 1

title = ['category','first','second','third','last']
what = ['what',what2 - what1,what3 - what2,what4 - what3,what - what4]
why = ['why',why2 - why1,why3 - why2,why4 - why3,why - why4]
how = ['how',how2 - how1,how3 - how2,how4 - how3,how - how4]
when = ['when',when2 - when1,when3 - when2,when4 - when3,when - when4]
who = ['who',who2 - who1,who3 - who2,who4 - who3,who - who4]
references = ['references',references2 - references1,references3 - references2,references4 - references3,references - references4]
contribution = ['contribution',contribution2 - contribution1,contribution3 - contribution2,contribution4 - contribution3,contribution - contribution4]
other = ['other',other2 - other1,other3 - other2,other4 - other3,other - other4]

outfile.writerow(title)
outfile.writerow(what)
outfile.writerow(why)
outfile.writerow(how)
outfile.writerow(when)
outfile.writerow(who)
outfile.writerow(references)
outfile.writerow(contribution)
outfile.writerow(other)

csv_file0.close()
csv_file1.close()
csv_file2.close()
csv_file3.close()
csv_file4.close()
csv_file.close()
