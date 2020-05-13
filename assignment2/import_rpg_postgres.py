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

# for character in chars:
#     insert_character = """
#     INSERT INTO charcreator_character
#     (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
#     VALUES """ + str(character[1:]) + ";"
#     cur.execute(insert_character)
# conn.commit()

# cur.execute('SELECT * FROM charcreator_character')
# cur.fetchall()


###################### SUBCLASS: CLERIC #####################

### Create cleric table
# cur.execute(
#     """
#     CREATE TABLE clerics (
#     character_ptr_id SERIAL PRIMARY KEY,
#     using_shield INTEGER NOT NULL,
#     mana INTEGER NOT NULL
#     );
#     """
# )
# conn.commit()

### Get and insert data for clerics
get_characters = 'SELECT * FROM charactercreator_cleric'
chars = sl_curs.execute(get_characters).fetchall()

# for character in chars:
#     insert_character = """
#     INSERT INTO clerics
#     (using_shield, mana)
#     VALUES """ + str(character[1:]) + ";"
#     cur.execute(insert_character)
# conn.commit()

# cur.execute('SELECT * FROM clerics')
# cur.fetchall()


###################### SUBCLASS: MAGE #####################

### Create mage table
# cur.execute(
#     """
#     CREATE TABLE mages (
#     character_ptr_id SERIAL PRIMARY KEY,
#     has_pet INTEGER NOT NULL,
#     mana INTEGER NOT NULL
#     );
#     """
# )
# conn.commit()

### Get and insert data for mages
get_characters = 'SELECT * FROM charactercreator_mage'
chars = sl_curs.execute(get_characters).fetchall()

# for character in chars:
#     insert_character = """
#     INSERT INTO mages
#     (has_pet, mana)
#     VALUES """ + str(character[1:]) + ";"
#     cur.execute(insert_character)
# conn.commit()

# cur.execute('SELECT * FROM mages')
# cur.fetchall()


###################### SUBCLASS: THIEF #####################

### Create thieves table
# cur.execute(
#     """
#     CREATE TABLE thieves (
#     character_ptr_id SERIAL PRIMARY KEY,
#     is_sneaking INTEGER NOT NULL,
#     energy INTEGER NOT NULL
#     );
#     """
# )
# conn.commit()

# ### Get and insert data for thieves
# get_characters = 'SELECT * FROM charactercreator_thief'
# chars = sl_curs.execute(get_characters).fetchall()

# for character in chars:
#     insert_character = """
#     INSERT INTO thieves
#     (is_sneaking, energy)
#     VALUES """ + str(character[1:]) + ";"
#     cur.execute(insert_character)
# conn.commit()

# cur.execute('SELECT * FROM thieves')
# cur.fetchall()


###################### SUBCLASS: FIGTHER #####################

### Create fighters table
# cur.execute(
#     """
#     CREATE TABLE fighters (
#     character_ptr_id SERIAL PRIMARY KEY,
#     using_shield INTEGER NOT NULL,
#     rage INTEGER NOT NULL
#     );
#     """
# )
# conn.commit()

# ### Get and insert data for fighters
# get_characters = 'SELECT * FROM charactercreator_fighter'
# chars = sl_curs.execute(get_characters).fetchall()

# for character in chars:
#     insert_character = """
#     INSERT INTO fighters
#     (using_shield, rage)
#     VALUES """ + str(character[1:]) + ";"
#     cur.execute(insert_character)
# conn.commit()

# cur.execute('SELECT * FROM fighters')
# cur.fetchall()


###################### SUBCLASS: NECROMANCERS #####################

### Create necromancers table
# cur.execute(
#     """
#     CREATE TABLE necromancers (
#     character_ptr_id SERIAL PRIMARY KEY,
#     talisman_charged INTEGER NOT NULL
#     );
#     """
# )
# conn.commit()

### Get and insert data for necromancers
# get_characters = 'SELECT * FROM charactercreator_necromancer'
# chars = sl_curs.execute(get_characters).fetchall()

# for character in chars:
#     insert_character = """
#     INSERT INTO necromancers
#     (talisman_charged)
#     VALUES """ + str(character[1]) + ";"
#     # breakpoint()
#     cur.execute(insert_character)
# conn.commit()

# cur.execute('SELECT * FROM necromancers')
# cur.fetchall()
# # Was actually unable to get this one to work - continued to get error
# # regarding line 198 having a SyntaxError: at or near "1"


###################### ITEMS #####################


### Get and insert data for items
# get_itms = 'SELECT * FROM armory_item'
# itms = sl_curs.execute(get_itms).fetchall()

# for itm in itms:
#     insert_item = """
#     INSERT INTO items
#     (name, "value", weight)
#     VALUES """ + str(itm[1:]) + ";"
#     cur.execute(insert_item)
# conn.commit()

# cur.execute('SELECT * FROM items')
# cur.fetchall()


###################### SUBCLASS: WEAPONS #####################


### Get and insert data for weapons
# get_itms = 'SELECT * FROM armory_weapon'
# itms = sl_curs.execute(get_itms).fetchall()

# for itm in itms:
#     insert_item = """
#     INSERT INTO weapons
#     (power)
#     VALUES """ + str(itm[1:]) + ";"
#     cur.execute(insert_item)
# conn.commit()

# cur.execute('SELECT * FROM weapons')
# cur.fetchall()

# # Ran into same error as necromancer subclass - must have
# # something to do with itm[1:]


###################### INVENTORY #####################


### Get and insert data for char_inventory
get_itms = 'SELECT * FROM charactercreator_character_inventory'
itms = sl_curs.execute(get_itms).fetchall()

for itm in itms:
    insert_item = """
    INSERT INTO char_inventory
    (character_id, item_id)
    VALUES """ + str(itm[1:]) + ";"
    cur.execute(insert_item)
conn.commit()

cur.execute('SELECT * FROM char_inventory')
cur.fetchall()