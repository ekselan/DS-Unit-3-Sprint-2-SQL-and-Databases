import psycopg2
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# RE-IMPORT TITANIC DATA

PATH = os.path.join(os.path.dirname(__file__), "titanic.csv")

df = pd.read_csv(PATH)
df.columns = ['survived', 'pclass', 'name', 'sex', 'age',
'siblings_spouses_aboard', 'parents_children_aboard', 'fare']
# print(df.columns)

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
# print("CONNECTION:", type(conn))

cur = conn.cursor()
print("------------------")
# print("CURSOR:", type(cur))

print("-------------------")
# print("Congrats! You've Successfully connected to a PostgreSQL instance!")

# cur.execute(
#     """
#     DROP TYPE sex
#     """
# )
# conn.commit()

# print("-----------")
# print("DONE")
# print("-----------")

# breakpoint()


# Set PostgreSQL engine
sql_url = f'postgresql://{PRAC_USER}:{PRAC_PW}@{PRAC_HOST}/{PRAC_NAME}'
engine = create_engine(sql_url)
# Copy df to new table in PostgreSQL
df.to_sql('titanic3', engine, if_exists='replace')
conn.commit()
print("DONE")
cur.close()
conn.close()
print("--------------------")
