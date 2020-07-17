import sys
import pandas as pd 
import os

input_path = "./dataset_combined.csv"
repo_path = "./repos/"

df_in = pd.read_csv(input_path, sep = ',')
cloned = os.listdir(repo_path)

eng_repo = []

for filenum in range(len(df_in["file-id"])):
    eng_repo.append(df_in["url"][filenum].split('/')[4])
eng_repo = list(dict.fromkeys(eng_repo))

num = 0
for i in range(len(eng_repo)):
    if (eng_repo[i] in cloned) == 0:
        print(eng_repo[i])
        num = num + 1

print("num:" + str(num))

print(len(cloned))
print(len(eng_repo))
