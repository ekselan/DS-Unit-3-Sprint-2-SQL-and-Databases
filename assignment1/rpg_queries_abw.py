import sqlite3
import os

DATABASE_FILEPATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "rpg_db.sqlite3")
connection = sqlite3.connect(DATABASE_FILEPATH)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

query1 = "SELECT count(DISTINCT character_id) as character_count FROM charactercreator_character"
result1 = cursor.execute(query1).fetchall()  # > LIST
for row in result1:
    print("RPG QUERIES:")
    print("-----")
    print('How many characters?', row[0])

query2 = "SELECT charactercreator_character.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT character_id) as character_count FROM charactercreator_character JOIN charactercreator_mage ON charactercreator_character.character_id = charactercreator_mage.character_ptr_id"
result2 = cursor.execute(query2).fetchall()  # > LIST
for row in result2:
    print("-----")
    print('How many Mages?', row[2])

query3 = "SELECT charactercreator_character.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT character_id) as character_count FROM charactercreator_character JOIN charactercreator_thief ON charactercreator_character.character_id = charactercreator_thief.character_ptr_id"
result3 = cursor.execute(query3).fetchall()  # > LIST
for row in result3:
    print("-----")
    print('How many Thieves?', row[2])