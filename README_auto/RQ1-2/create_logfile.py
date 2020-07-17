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


last_line = []

a = 0

i = 0
j = 0
k = 0

nc = 0

last_file_id = 1
flag = False

top = ["section-id","file-id","url","heading","Codes with >= 2 votes"]
outfile.writerow(top)

last_pname = []

rmlist = []

for row in infile:
    
    file_id = int(row[1])
    
    if file_id != last_file_id:
        if flag != True:
            if last_file_id not in rmlist:
                outfile.writerow(['',last_file_id,last_pname,'','-'])
                nc += 1
                print(last_file_id)
        flag = False
    
    pn = linecache.getline('project_name.csv', file_id)
    pname = pn.strip("\n")

    try:
        F_IN = open("repos/" + pname + "/README.md",'r',encoding='utf_8')
        '''
        if file_id == 127:
            print('aaa')
        '''
    except FileNotFoundError:
        
        try:
            F_IN = open("repos/" + pname + "/README.md",'r', encoding='shift_jis')
            

        except FileNotFoundError:
            try:
                F_IN = open("repos/" + pname + "/README.md",'r', encoding='cp932')
                
            except FileNotFoundError:
                if file_id not in rmlist:
                    rmlist.append(file_id)
                    last_file_id = file_id
                    last_pname = row[2]
                continue

    try:
        for line in F_IN:

            if "#" in line:
                x = line.strip("#")
                y = x.strip("\n")
                z = y.strip(' ')
                head.append(z)
                #print(y)
                #print(head)
            elif ("==="in line or "---" in line):
                x = str(last_line).strip("\n")
                y = x.strip(' ')
                head.append(y)
            last_line = line

        x = row[3].strip("#")
        y = x.strip(' ')

        #print(row)

        if y in head:
            #print(aaa)
            outfile.writerow(row)
            #print(row)
            flag = True

        

    except UnicodeDecodeError:
        if file_id not in rmlist:
            rmlist.append(file_id)
        continue  

    head = []
    last_file_id = file_id
    last_pname = row[2]
    F_IN.close()

print(rmlist)
#print(a)    
print(str(nc))



csv_file1.close()
csv_file2.close()

with open('no_category.csv','w') as f:
    f.write(str(nc))
