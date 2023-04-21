#!/usr/bin/python3
# -*- coding: utf-8  -*-


#pip install pandas

import pandas as pd
import datetime
import os

print('XoXX' * 50)
df = pd.read_excel('file_name.xlsx',)
# df = pd.read_excel('file_name.xlsx',index=False)

print(df.head(20))

df.at[9,1] = 'Hello all'


df.to_excel('file_name.xlsx', index=False)
print('X'*50)
df = pd.read_excel('file_name.xlsx')
print(df.head(20))


"""
df.at[2, 'A'] = 'Hello'


print(df.head(20))
df.to_excel('my_excel_file.xlsx', index=False)

print('*' * 50)

now = datetime.datetime.now().strftime("%Y-%m-%d")
 

file_name = "my_excel_file.xlsx"
new_file_name = f"{now}_{file_name}"

os.rename(file_name, new_file_name)


df = pd.read_excel(new_file_name)
print(df.head(20))

"""