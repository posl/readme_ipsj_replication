import csv
import os
import codecs
import linecache
import string

csv_file1 = open('dataset_combined.csv','r',encoding='utf-8', errors="", newline="")
infile = csv.reader(csv_file1,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
csv_file2 = open('dataset_combined_cp.csv','w')
outfile = csv.writer(csv_file2)
header = next(infile)

pn = []
pname = []
head = []

#a = 0

#i = 0
#j = 0
#k = 0

last_file_id = 1
flag = False

top = ["section-id","file-id","url","heading","Codes with >= 2 votes"]
outfile.writerow(top)

last_pname = []

rmlist = []

for line in open("project_name.csv"):
    pname = line.strip("\n")

    try:
        F_IN = open("repos/" + pname + "/README.md",'r',encoding='utf_8')
        if pname == 'fig':
            print('USA')

    except:
        
        try:
            F_IN = open("repos/" + pname + "/README.md",'r', encoding='shift_jis')
            

        except:
            try:
                F_IN = open("repos/" + pname + "/README.md",'r', encoding='cp932')
                
            except:
                if file_id not in rmlist:
                    rmlist.append(file_id)
                continue

    try:
        for line2 in F_IN:
            if "#" in line2:
                x = line2.strip("\n")
                y = line2.strip("#")
                head.append(y)
        
            elif ("---" in line2 or "===" in line2):
                x = last_line.strip("\n")
                head.append(x)
            
            last_line = line2
        
        for row in infile:
            if pname in row[2]:
                pn = row[3].strip("#")
                if pn in head:
                    outfile.writerow(row)
    
    except UnicodeDecodeError:
        continue
    head = []
    F_IN.close()        



csv_file1.close()
csv_file2.close()