import psycopg2
import sqlite3
import os.path

### Establish PostgreSQL connection
DB_NAME = 'axajhxor'
DB_USER = 'axajhxor'
DB_PW = 'jon9BPw8JOK1xjzsunZhv3xsdPTmLLuB'
DB_HOST = 'rajje.db.elephantsql.com'

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PW, host=DB_HOST)
# print(type(conn))

cur = conn.cursor()
# print(type(cur))


### Establish sqlite3 connection
sl_conn = sqlite3.connect("data/rpg_db_original.sqlite3")
sl_curs = sl_conn.cursor()
# print(type(sl_conn))
# print(type(sl_curs))
# row_count = 'SELECT COUNT(*) FROM charactercreator_character'
# print(sl_curs.execute(row_count).fetchall()} characters)


###################### INSERTS ###########################


### Get and insert data for charcreator_characters
get_characters = 'SELECT * FROM charactercreator_character'
chars = sl_curs.execute(get_characters).fetchall()

show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE pg_tables.schemaname != 'pg_catalog' AND 'pg_tables.schemename' != 'information_schema'
"""
# cur.execute(show_tables)
# print(cur.fetchall())
# print(chars[0])

for character in chars:
    insert_character = """
    INSERT INTO charcreator_character
    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
    VALUES """ + str(character[1:]) + ";"
    cur.execute(insert_character)
# conn.commit()

# cur.execute('SELECT * FROM charcreator_character')
# cur.fetchall()


###################### SUBCLASS: CLERIC #####################

# Create cleric table
cur.execute(
    """
    CREATE TABLE clerics (
    character_ptr_id SERIAL PRIMARY KEY,
    using_shield INTEGER NOT NULL,
    mana INTEGER NOT NULL
    );
    """
)
conn.commit()

### Get and insert data for charcreator_cleric
# get_characters = 'SELECT * FROM charactercreator_cleric'
# chars = sl_curs.execute(get_characters).fetchall()

# for character in chars:
#     insert_character = """
#     INSERT INTO clerics
#     (using_shield, mana)
#     VALUES """ + str(character[1:]) + ";"
#     cur.execute(insert_character)
# conn.commit()

# cur.execute('SELECT * FROM charcreator_cleric')
# cur.fetchall()
