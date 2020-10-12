import csv
import statistics
import math
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
from scipy import stats
import collections
import pandas as pd
import numpy as np

commits_main = []
files_main = []
loc_main = []
lang_main = []

fp = FontProperties(fname=r'./yugothib.ttf', size=14)

with open('main.csv') as mainf:
    reader = csv.reader(mainf)
    header =next(reader)
    for row in reader:
        if(row[1] == "not found"):
            continue
        commits_main.append(int(row[2]))
        files_main.append(int(row[3]))
        loc_main.append(int(row[4]))
        lang_main.append(row[1])
mainf.close()

print("コミット数平均: " + str(statistics.mean(commits_main)))
print("コミット数中央値: " + str(statistics.median(commits_main)))
print("コミット数標準偏差: " + str(statistics.stdev(commits_main)))
print("コミット数最大値: " + str(max(commits_main)))
print("コミット数最小値: " + str(min(commits_main)))
print("ファイル数平均: " + str(statistics.mean(files_main)))
print("ファイル数中央値: " + str(statistics.median(files_main)))
print("ファイル数標準偏差: " + str(statistics.stdev(files_main)))
print("ファイル数数最大値: " + str(max(files_main)))
print("ファイル数最小値: " + str(min(files_main)))
print("論理行数平均: " + str(statistics.mean(loc_main)))
print("論理行数中央値: " + str(statistics.median(loc_main)))
print("論理行数標準偏差: " + str(statistics.stdev(loc_main)))
print("論理行数最大値: " + str(max(loc_main)))
print("論理行数最小値: " + str(min(loc_main)))
print("言語: " + str(collections.Counter(lang_main)))


fig, (axc, axf, axl) = plt.subplots(ncols=3, figsize=(10,4))
plt.suptitle('本実験', fontproperties=fp)
axc.boxplot(np.log(commits_main))
axc.set_xticklabels(["コミット数"], fontproperties=fp) 

axf.boxplot(np.log(files_main))
axf.set_xticklabels(["ファイル数"], fontproperties=fp) 

axl.boxplot(np.log(loc_main))
axl.set_xticklabels(["論理行数"], fontproperties=fp) 
plt.savefig("boxplot_main.pdf",dpi=100)
plt.grid()
plt.show()

lang_count = collections.Counter(lang_main)
df = pd.DataFrame.from_dict(lang_count, orient='index')
df.plot(kind='bar')
plt.savefig('lang_main_hist.pdf')


commits_add = []
files_add = []
loc_add = []
lang_add = []

with open('additional.csv') as additionalf:
    reader = csv.reader(additionalf)
    header =next(reader)
    for row in reader:
        if(row[1] == "not found"):
            continue
        commits_add.append(int(row[2]))
        files_add.append(int(row[3]))
        loc_add.append(int(row[4]))
        lang_add.append(row[1])
additionalf.close()

print("コミット数平均: " + str(statistics.mean(commits_add)))
print("コミット数中央値: " + str(statistics.median(commits_add)))
print("コミット数標準偏差: " + str(statistics.stdev(commits_add)))
print("コミット数最大値: " + str(max(commits_add)))
print("コミット数最小値: " + str(min(commits_add)))
print("ファイル数平均: " + str(statistics.mean(files_add)))
print("ファイル数中央値: " + str(statistics.median(files_add)))
print("ファイル数標準偏差: " + str(statistics.stdev(files_add)))
print("ファイル数数最大値: " + str(max(files_add)))
print("ファイル数最小値: " + str(min(files_add)))
print("論理行数平均: " + str(statistics.mean(loc_add)))
print("論理行数中央値: " + str(statistics.median(loc_add)))
print("論理行数標準偏差: " + str(statistics.stdev(loc_add)))
print("論理行数最大値: " + str(max(loc_add)))
print("論理行数最小値: " + str(min(loc_add)))
print("言語: " + str(collections.Counter(lang_add)))


fig, (axc, axf, axl) = plt.subplots(ncols=3, figsize=(10,4))
plt.suptitle('追加実験', fontproperties=fp)
axc.boxplot(np.log(commits_add))
axc.set_xticklabels(["コミット数"], fontproperties=fp) 

axf.boxplot(np.log(files_add))
axf.set_xticklabels(["ファイル数"], fontproperties=fp) 

axl.boxplot(np.log(files_add))
axl.set_xticklabels(["論理行数"], fontproperties=fp) 
plt.savefig("boxplot_addtional.pdf",dpi=100)
plt.grid()
plt.show()

lang_count = collections.Counter(lang_add)
df = pd.DataFrame.from_dict(lang_count, orient='index')
df.plot(kind='bar')
plt.savefig('lang_add_hist.pdf')

result_commits, p1 = stats.mannwhitneyu(commits_main,commits_add)
result_files, p2 = stats.mannwhitneyu(files_main,files_add)
result_loc, p3 = stats.mannwhitneyu(loc_main,loc_add)

print("コミット数t検定p値: " + str(result_commits) + ", "  + str(p1))
print("ファイル数t検定p値: " + str(result_files) + ", "+ str(p2))
print("論理行数t検定p値: " + str(result_loc) + "," +str(p3))