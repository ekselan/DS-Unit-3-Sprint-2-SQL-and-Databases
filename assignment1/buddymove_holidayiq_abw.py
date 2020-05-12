import sqlite3
import pandas as pd

PATH = '/Users/ekselan/Documents/GitHub/DS_3_2_1_SQL/DS-Unit-3-Sprint-2-SQL-and-Databases/module1-introduction-to-sql/buddymove_holidayiq.csv'
df = pd.read_csv(PATH)
print(df.shape)
# print(df.isnull().sum())
print(df.head())

# CREATE DATABASE
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
cursor = conn.cursor()
# Create review table
cursor.execute('DROP TABLE REVIEW')
cursor.execute('CREATE TABLE REVIEW (User Id text, Sports number, Religious number, Nature number, Theatre number, Shopping number, Picnic number)')
conn.commit()
# DF to SQL
df.to_sql('REVIEW', conn, if_exists='replace', index=False)

cursor.execute('SELECT * FROM REVIEW')
for row in cursor.fetchall():
    print(row)


# # BuddyMove Data Set

# ### Count how many rows you have (249)
# ```
# SELECT
# 	count(DISTINCT "User Id") as users_count
# FROM REVIEW
# ```

# ### How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category? (78)

# ```
# SELECT
# 	count(DISTINCT "User Id") as Nat_and_shop_count
# FROM REVIEW
# WHERE Nature>=100 and Shopping>=100
# ```

# (STRETCH) What are the average number of reviews for each category?
# ```
# SELECT
# 	AVG(Sports)
# 	,AVG(Religious)
# 	,AVG(Nature)
# 	,AVG(Theatre)
# 	,AVG(Shopping)
# 	,AVG(Picnic)
# FROM REVIEW
# ```
