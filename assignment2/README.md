## Assignment 2

Reproduce (debugging as needed) the live lecture task of setting up and
inserting the RPG data into a PostgreSQL database, and add the code you write to
do so.

Then, set up a new table for the Titanic data (`titanic.csv`) - spend some time
thinking about the schema to make sure it is appropriate for the columns.
[Enumerated types](https://www.postgresql.org/docs/9.1/datatype-enum.html) may
be useful. Once it is set up, write a `insert_titanic.py` script that uses
`psycopg2` to connect to and upload the data from the csv, and add the file to
your repo. Then start writing PostgreSQL queries to explore the data!



# ALTERNATE TITANIC SOLUTIONS:

### df.astype() approach (for lecture example)
```
df["Survived"] = df["Survived"].values.astype(bool) # do this before converting to native types, because this actually converts to np.bool
df = df.astype("object") # converts numpy dtypes to native python dtypes (avoids psycopg2.ProgrammingError: can't adapt type 'numpy.int64')
```

### SQLALCHEMY APPROACH:
```
import os
from sqlalchemy import create_engine
import sqlite3
from dotenv import load_dotenv
import pandas as pd
# Instantiate titanic data
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv")
df = pd.read_csv(CSV_FILEPATH)
# Change the columns to be more sql friendly
df.columns = ['survived', 'pclass', 'name', 'sex', 'age',
'siblings_spouses_aboard', 'parents_children_aboard', 'fare']
print(df.columns)
# Set up .env variables to connect to postgres later
envpath = os.path.join(os.getcwd(), '.env')
# print(envpath)
load_dotenv()
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
# Set connection to PostgreSQL
sql_url = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
engine = create_engine(sql_url)
# Copy df to new table in PostgreSQL
df.to_sql('titanic_data', engine, if_exists='replace')
```
