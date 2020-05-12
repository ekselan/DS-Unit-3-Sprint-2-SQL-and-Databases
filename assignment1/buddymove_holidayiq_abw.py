import pandas as pd

PATH = '/Users/ekselan/Documents/GitHub/DS_3_2_1_SQL/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv'
df = pd.read_csv(PATH)
print(df.shape)
# print(df.isnull().sum())
print(df.head())

# CREATE DATABASE
import sqlite3
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
cursor = conn.cursor()
# Create review table
cursor.execute('CREATE TABLE REVIEW (User Id text, Sports number, Religious number, Nature number, Theatre number, Shopping number, Picnic number)')
conn.commit()
# DF to SQL
df.to_sql('REVIEW', conn, if_exists='replace', index=False)

cursor.execute('SELECT * FROM REVIEW')
for row in cursor.fetchall():
    print(row)