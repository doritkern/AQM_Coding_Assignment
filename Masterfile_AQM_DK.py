import requests
import pandas as pd

#Latest Microdata
URL_Latest_Data = "https://www.newyorkfed.org/medialibrary/Interactives/sce/sce/downloads/data/frbny-sce-public-microdata-latest"
open("Micro_Latest_Data.xlsx", "wb").write(requests.get(URL_Latest_Data).content)

#Microdata from 17 until 19
URL_17_19 = "https://www.newyorkfed.org/medialibrary/interactives/sce/sce/downloads/data/frbny-sce-public-microdata-complete-17-19.xlsx"
open("Micro_17_19.xlsx", "wb").write(requests.get(URL_17_19).content)

#Microdata from 13 to 16
URL_13_16 = "https://www.newyorkfed.org/medialibrary/interactives/sce/sce/downloads/data/frbny-sce-public-microdata-complete-13-16.xlsx"
open("Micro_13_16.xlsx", "wb").write(requests.get(URL_13_16).content)

#Put tables in a dataframe while skipping the first row (introduction line)
df1 = pd.read_excel('Micro_Latest_Data.xlsx', sheet_name='Data', skiprows=1)
df2 = pd.read_excel('Micro_17_19.xlsx', sheet_name='Data', skiprows=1)
df3 = pd.read_excel('Micro_13_16.xlsx', sheet_name='Data', skiprows=1)

#Check if all columns are identical (there is probably a smarter way of doing this ;-))
result = 0
for i in range(0,len(df1.columns)):
    if df1.columns[i] == df2.columns[i] == df3.columns[i]:
        result += 0
    else:
        result += 1
    i += 1
if result > 0:
    print("Attention: Not all tables are identical")

#Combine three tables into one dataframe
df_full = pd.concat([df1, df2, df3], axis=0)
print(df_full)

#Save combined data frame as xml
df_full.to_excel("Micro_Data_all.xlsx", sheet_name='Data')