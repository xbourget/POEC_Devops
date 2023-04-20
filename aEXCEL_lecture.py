#!/usr/bin/python3
# -*- coding: utf-8  -*-

# http://www.python-simple.com/python-pandas/panda-intro.php
# pip install pandas
# pip install  openpyxl

import datetime
import pandas as pd

df = pd.read_excel('file_name.xlsx')

print(df)

print( 's' * 20 )
print(df.loc( 1 ))

print( 's' * 20 )
print(df.head( 3 ))

#print( 's' * 20 )
#print(df[0])

print( 's' * 20 )

df.at[1, 'nom'] = 'toto'
df.at[2, 'nom'] = 'titi'
df.at[2, 'A'] = 'Hello'
df.at[2, 1] = 'ABABAB'
print(df)

now = datetime.datetime.now().strftime("%Y-%m-%d")
df.to_excel('my_excel_file'+now+'.xlsx', index=False)