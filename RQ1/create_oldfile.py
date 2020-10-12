import csv
import os
import codecs
import linecache
import string

with open('./dataset_combined.csv') as f:
    reader = csv.reader(f)
    l = [row for row in reader]

tmp = []
s = set(tmp)

for data in l:
    if data[4] != '-':
        data = None

for data in l:
    s.add(data[2]);

print(len(s))

with open('repos.csv', 'w') as f1:
    for ss in s:
        f1.write(ss + '\n')