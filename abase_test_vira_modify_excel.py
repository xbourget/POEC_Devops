#pip install panda
import pandas as pd
import datetime
import os
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

df = pd.read_excel("2023-04-20_my_excel_file.xlsx")

print(df.head(20))

df.loc[2, 'A'] = 'Hello Guys'

print(df)

df.to_excel('2023-04-20_my_excel_file.xlsx', index=False)

