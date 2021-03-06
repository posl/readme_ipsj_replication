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
    infile = csv.reader(csv_file1,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    csv_file2 = open('based_list.csv','w')
    #csv_file2 = open('first_list.csv','w')
    outfile = csv.writer(csv_file2)

#csv_file3 = open('data.csv','r',encoding='utf-8', errors="", newline="")

elif(i == 1):
    csv_file1 = open('dataset_combined.csv','r',encoding='utf-8', errors="", newline="")
    infile = csv.reader(csv_file1,delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    csv_file2 = open('first_list.csv','w')
    outfile = csv.writer(csv_file2)

header = next(infile)
a = []

fname = []
f = []
title = ['project name','project url','category','commits']
name = ['https://github.com/aasm/aasm']
#name.append(linecache.getline('dataset_combined.csv', 1))
head = []
number = []
list = []
last_name = 'https://github.com/aasm/aasm'
now_file_id = 1
rmlist =[]

x = 0
y = 0
z = 0
num = 0


for line in open("project_name.csv"):
    num += 1
    n = line.strip("\n")

    try:
        f = open("repos/" + n + "/README.md",'r',encoding='utf_8')
        #x += 1

    except FileNotFoundError:
        
        try:
            f = open("repos/" + n + "/README.md", 'r', encoding='shift_jis')
            #y += 1
        except FileNotFoundError:

            try:
                f = open("repos/" + n + "/README.md", 'r', encoding='cp932')
                #z += 1
            except FileNotFoundError:
                rmlist.append(num)

    try:
        for line in f:
            x += 1

    except UnicodeDecodeError:
        rmlist.append(num)        

f.close()

print(rmlist)

outfile.writerow(title)


for row in infile:
    #新しいファイルを読み込み始めたので、今までに読んでlistを作っていたファイルの情報をoutfileに書き込む
    if row[2] not in name:
            #outfile第1項への書き込み
        f = linecache.getline('project_name.csv', now_file_id)
        fname = f.strip("\n")
        #print(fname)

        list.append(fname)
        list.append(last_name)
        name.append(row[2])
        #outfile第2項への書き込み
        head.sort()
        list.append(head)
        
        #outfile第3項への書き込み
        commit = linecache.getline('data.csv', now_file_id)
        c = commit.strip("\n")
        list.append(c)

        if now_file_id not in rmlist:
            print(now_file_id)
            outfile.writerow(list)
        
        head = []
        list = []
        last_name = row[2] 
        now_file_id += 1

    if row[-1] != '-':
        print("row[-1] =" + row[-1])
        number = int(row[-1])
        
        while number != 0:
            add =  number % 10
            if add not in head:
                head.append(add)
            number = int((number-add)/10)

#ループ内で書けなかった最終行の書き込み処理
f = linecache.getline('project_name.csv', now_file_id)
fname = f.strip("\n")
list.append(fname)
list.append(last_name)
list.append(head)
commit = linecache.getline('data.csv', now_file_id)
c = commit.strip("\n")
list.append(c)
outfile.writerow(list)

csv_file1.close()
csv_file2.close()


