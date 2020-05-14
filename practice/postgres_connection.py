import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

PRAC_NAME = os.getenv("PRAC_NAME", default="OOPS")
PRAC_USER = os.getenv("PRAC_USER", default="OOPS")
PRAC_PW = os.getenv("PRAC_PW", default="OOPS")
PRAC_HOST = os.getenv("PRAC_HOST", default="OOPS")

# TODO: get credentials in .env file for use in connecting
# Establish PostgreSQL connection
# DB_NAME = 'axajhxor'
# DB_USER = 'axajhxor'
# DB_PW = 'jon9BPw8JOK1xjzsunZhv3xsdPTmLLuB'
# DB_HOST = 'rajje.db.elephantsql.com'

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

