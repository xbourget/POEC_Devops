#pip install panda
import pandas as pd

df = pd.read_excel("file_name.xlsx")

print(df.head(20))

df.at[2, 'A'] = 'Hello'

print(df.head(20))

df.to_excel('my_excel_file.xlsx', index=False)