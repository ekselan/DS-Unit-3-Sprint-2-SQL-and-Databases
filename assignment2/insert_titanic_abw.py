import psycopg2
import os
from dotenv import load_dotenv

# ESTABLISH POSTGRES CONNECTION
load_dotenv()

PRAC_NAME = os.getenv("PRAC_NAME", default="OOPS")
PRAC_USER = os.getenv("PRAC_USER", default="OOPS")
PRAC_PW = os.getenv("PRAC_PW", default="OOPS")
PRAC_HOST = os.getenv("PRAC_HOST", default="OOPS")

conn = psycopg2.connect(
    dbname=PRAC_NAME,
    user=PRAC_USER,
    password=PRAC_PW,
    host=PRAC_HOST)
print("------------------")
print("CONNECTION:", type(conn))

cur = conn.cursor()
print("------------------")
print("CURSOR:", type(cur))

print("-------------------")
print("Congrats! You've Sueccessfully connected to a PostgreSQL instance!")


# Review shape of titanic.csv in terminal
# to determine schema
# 8 columns:
"""
Survived INT
Pclass INT
Name VARCHAR(40) NOT NULL
Sex ENUM
Age INT
Siblings/Spouses Aboard INT
Parents/Children Aboard INT
Fare NUMERIC
"""

# Create titanic table
# cur.execute(
#     """
#     --CREATE TYPE sex AS ENUM ('male', 'female');
#     CREATE TABLE titanic (
#         Survived INTEGER NOT NULL,
#         Pclass INTEGER NOT NULL,
#         Name TEXT NOT NULL,
#         Sex sex,
#         Age NUMERIC NOT NULL,
#         "Siblings/Spouses Aboard" INTEGER NOT NULL,
#         "Parents/Children Aboard" INTEGER NOT NULL,
#         Fare NUMERIC NOT NULL
#     );
#     """
# )
# conn.commit()

# Insert titanic data
# with open('module2-sql-for-analysis/titanic.csv', 'r') as f:
#     next(f)  # Skip header row
#     cur.copy_from(f, 'titanic', sep=',')

# conn.commit()
# #(https://www.dataquest.io/blog/loading-data-into-postgres/)
