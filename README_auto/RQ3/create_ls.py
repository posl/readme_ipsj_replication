import csv
import os
import codecs
import linecache
import string

I = linecache.getline('mode.csv',1)
i = I.strip("\n")
i = int(i)

if(i == 0):

    csv_file1 = open('dataset_combined.csv','r',encoding='utf-8', errors="", newline="")
    #csv_file1 = open('dataset_combined_cp.csv','r',encoding='utf-8', errors="", newline="")
    infile = csv.reader(csv_file1,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    csv_file3 = open('dataset_combined.csv','r',encoding='utf-8', errors="", newline="")
    #csv_file1 = open('dataset_combined_cp.csv','r',encoding='utf-8', errors="", newline="")
    infile2 = csv.reader(csv_file3,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    csv_file2 = open('based_list.csv','w')
    #csv_file2 = open('first_list.csv','w')
    outfile = csv.writer(csv_file2)

#csv_file3 = open('data.csv','r',encoding='utf-8', errors="", newline="")

else:
    csv_file1 = open('dataset_combined_cp.csv','r',encoding='utf-8', errors="", newline="")
    infile = csv.reader(csv_file1,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    csv_file3 = open('dataset_combined_cp.csv','r',encoding='utf-8', errors="", newline="")
    infile2 = csv.reader(csv_file3,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    
    if i == 1:
        csv_file2 = open('first_list.csv','w')
        outfile = csv.writer(csv_file2)
    elif i == 2:
        csv_file2 = open('second_list.csv','w')
        outfile = csv.writer(csv_file2)
    elif i == 3:
        csv_file2 = open('third_list.csv','w')
        outfile = csv.writer(csv_file2)
    elif i == 4:
        csv_file2 = open('fourth_list.csv','w')
        outfile = csv.writer(csv_file2)


header = next(infile)
header = next(infile2)
title = ['project name','project url','category','commits']
outfile.writerow(title)

#reject number which is file_id that is unable to read README.md
num = 0
rm_num = []

#the list of name which we can't read README.md
rm_list = []

last_i = 1
control_list = []
e_num = 0
place = 0

head = []

f = open("project_name.csv")
for line in open("project_name.csv"):
    num += 1
    n = line.strip("\n")

    try:
        f = open("repos/" + n + "/README.md",'r',encoding='utf_8')

    except FileNotFoundError:
        
        try:
            f = open("repos/" + n + "/README.md", 'r', encoding='shift_jis')

        except FileNotFoundError:

            try:
                f = open("repos/" + n + "/README.md", 'r', encoding='cp932')
            except FileNotFoundError:
                rm_num.append(num)

    try:
        x = 0
        for line in f:
            x += 1

    except UnicodeDecodeError:
        rm_num.append(num)        

f.close()

print(rm_num)

j = 0 #各id毎の要素数
for row in infile:
    #print('aaa')
    i = int(row[1])
    if last_i != i:
        control_list.append([last_i,j])
        j = 0

    if i in rm_num:
        rm_list.append(row[2])
    else:
        j += 1
    last_i = i


control_list.append([last_i,j])
#print(control_list)
#print(rm_list)
num = 0
list = []

#print(control_list[10][1])

for line in infile2:
    if line[2] in rm_list:
        continue
    
    if line[-1] != "-":
        number = int(line[-1])
        while number != 0:
            add =  number % 10
            if add not in head:
                head.append(add)
            number = int((number-add)/10)

    #print('aaa')
    now_id = int(line[1])

    num += 1
    
    length = len(control_list)
    k = 0
    for k in range(length):
        
        if control_list[k][0] == now_id:
            place = k
            break
        k += 1
        
    
    
    #print(control_list[place][1])
    
    if num == control_list[place][1]:
        #書き込み処理
        f = linecache.getline('project_name.csv', now_id)
        fname = f.strip("\n")
        list.append(fname)

        list.append(line[2])

        head.sort()
        list.append(head)

        commit = linecache.getline('data.csv', now_id)
        c = commit.strip("\n")
        list.append(c)

        #print(list)

        outfile.writerow(list)

        
        head = []
        list = []
        num = 0
        


#print(rm_list)
#print(control_list)

csv_file1.close()
csv_file2.close()


