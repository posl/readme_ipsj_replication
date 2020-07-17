import csv
import os
#import subprocess as s
#import sys
#import io
import codecs

#sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
#sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

a = []
b = [['project_name', 'category', 'commits', 'first_category']]
c = []
d = 0 
e = []
last_num = []
num = []

csv_file = open("dataset_combined.csv", "r")
f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
header = next(f)
# print(header)
for row in f:
    if row[2] not in c:
        if len(c) != 0:
            last_num = list(set(num))
            c.append(last_num)
            b.append(c)
            c = []
        c.append(row[2])
        num = []
        # print(row[4])
        # print(type(row[4]))
        if row[-1] == '-':
            pass
        else:
            # print(row)
            n = int(row[-1])
            while n != 0:
                num.append(n % 10)
                n //= 10
    else:
        num2 = []
        if row[-1] == '-':
            pass
        else:
            # print(row)
            n = int(row[-1])
            while n != 0:
                # print(int(row[-1]))
                num2.append(n % 10)
                n //= 10
            num.extend(num2)
    # print(b[-1][-1])

last_num = list(set(num))
c.append(last_num)
b.append(c)

for line in open("./data.csv"):
    y = line.strip("\n")
    d = d + 1
    b[d].append(y)

d = 0 
y = 0
    
# print(b[2])

# os.system('sh git.sh')

for line2 in open ("project_name.csv"):
    x = line2.strip("\n")
#    x.parse("")
    num = []
    #print(x)
    try:
        F_IN = codecs.open("./repos/" + x + "/" + "README.md",'r',encoding='utf_8',errors='ignore')
    except:
        try:
            F_IN = codecs.open("./repos/" + x + "/" + "README.md", 'r', encoding='shift_jis')
        except:
            F_IN = codecs.open("./repos/" + x + "/" + "README.md", 'r', encoding='cp932')
    for line in F_IN:
        if "#" in line:
            y = y + 1
            g = line.strip("\n")
            #a = []
            #a.append(g)
            #print(g)
            csv_file = open("dataset_combined.csv", "r", encoding="utf-8", errors="", newline="" )
            f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
            header = next(f)
            for row in f:
                #print(row)
                #print(row[2])
                if x in row[2]:
                    #print("a")
                    #print(g)
                    #print(row[3])
                    if row[3] in g:
                        #print("b")
                        #print(row[-1])
                        if row[-1] == '-':
                            pass 
                        else:
                            n = int(row[-1])
                            while n != 0:
                                num.append(n % 10)
                                n //= 10
        elif ("===" in line or "---" in line):
            y = y + 1
            csv_file = open("dataset_combined.csv", "r", encoding="utf-8", errors="", newline="")
            f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
            header = next(f)
            for row in f:
                if x in row[2]:
                    # g = "#### " + g
                    print(g)
                    print(row[3])
                    if row[3] in g:
                        print("a")
                        if row[-1] == '-':
                            pass
                        else:
                            n = int(row[-1])
                            while n != 0:
                                num.append(n % 10)
                                n //= 10
        else: 
            g = line.strip("\n")
            g = "#### " + g
    last_num = list(set(num))
    d = d + 1
    b[d].append(last_num)

#print(b)
#print(y)

with open('new_result_last.csv','w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerows(b)
