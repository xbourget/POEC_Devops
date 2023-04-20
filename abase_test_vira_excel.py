#pip install panda
import pandas as pd
import datetime
import os

df = pd.read_excel("file_name.xlsx")

print(df.head(20))

df.at[2, 'A'] = 'Hello'

print(df.head(20))

df.to_excel('my_excel_file.xlsx', index=False)

now = datetime.datetime.now().strftime("%Y-%m-%d")

file_name = "my_excel_file.xlsx"

new_file_name = f"{now}_{file_name}"

os.rename(file_name, new_file_name)