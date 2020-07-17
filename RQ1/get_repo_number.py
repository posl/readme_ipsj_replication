import sys
import pandas as pd 

input_path = "./dataset_combined_2.csv"
output_path = "./dataset_combinedx.csv"
df_in = pd.read_csv(input_path, sep = ',')
i = 0;
j = 0;

df_out = pd.DataFrame(columns = ["section-id", "file-id","url", "heading", "Codes with >= 2 votes"])
df_out.to_csv(output_path)

for sections in range(len(df_in['section-id'])):
    if(df_in['Codes with >= 2 votes'][sections] != '-'):
        i = i + 1
        url = str(df_in["url"][sections])
        url = '"' +  url + '"'
        print(url)
        heading = str(df_in["heading"][sections])
        heading = '"' + heading + '"'
        Codes = str(df_in["Codes with >= 2 votes"][sections])
        Codes  = '"' + Codes + '"'
        if(df_in['file-id'][sections] != df_in['file-id'][sections - 1]):
            j = j + 1
        S = pd.DataFrame({"section-id":[i], "file-id":[j], "url":[url], "heading":[heading], "Codes with >= 2 votes":[Codes]})
        print(S)
        df_out = df_out.append(S)
        df_out.to_csv(output_path)

df_out = df_out.set_index("section-id")
df_out.to_csv(output_path)
