import sqlite3

# Establish sqlite3 connection
sl_conn = sqlite3.connect("data/rpg_db_original.sqlite3")
sl_curs = sl_conn.cursor()
# print(type(sl_conn))
# print(type(sl_curs))
row_count = 'SELECT COUNT(*) FROM charactercreator_character'
# print(sl_curs.execute(row_count).fetchall())

rpg_characters = 'SELECT * FROM charactercreator_character'
# print(sl_curs.execute(rpg_characters).fetchall())
# breakpoint()

# desc = sl_curs.description # tuple of column names from RPG db (sqlite3)
# breakpoint()
# col_names = [col[0] for col in desc]
# data = [dict(zip(col_names, row))
#         for row in sl_curs.fetchall()]

# breakpoint()


def all_chars():
    query = rpg_characters
    chars = sl_curs.execute(query)
    pass
    char_data = []
    for row in chars:
        character = {
            "character_id": row[0],
            "name": row[1],
            "level": row[2],
            "exp": row[3],
            "hp": row[4],
            "strength": row[5],
            "intelligence": row[6],
            "dexterity": row[7],
            "wisdom": row[8]
        }
        char_data.append(character)
    result = char_data
    return result


a = all_chars()
print(a)
