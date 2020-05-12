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

# ***** CHARACTERS *****

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

query4 = "SELECT charactercreator_character.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT character_id) as character_count FROM charactercreator_character JOIN charactercreator_cleric ON charactercreator_character.character_id = charactercreator_cleric.character_ptr_id"
result4 = cursor.execute(query4).fetchall()  # > LIST
for row in result4:
    print("-----")
    print('How many Clerics?', row[2])

query5 = "SELECT charactercreator_character.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT character_id) as character_count FROM charactercreator_character JOIN charactercreator_fighter ON charactercreator_character.character_id = charactercreator_fighter.character_ptr_id"
result5 = cursor.execute(query5).fetchall()  # > LIST
for row in result5:
    print("-----")
    print('How many Fighters?', row[2])

query6 = "SELECT charactercreator_character.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT character_id) as character_count FROM charactercreator_character JOIN charactercreator_necromancer ON charactercreator_character.character_id = charactercreator_necromancer.mage_ptr_id"
result6 = cursor.execute(query6).fetchall()  # > LIST
for row in result6:
    print("-----")
    print('How many Necromancers?', row[2])

# ***** ITEMS *****

query7 = "SELECT charactercreator_character.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT character_id) as character_count FROM charactercreator_character JOIN charactercreator_necromancer ON charactercreator_character.character_id = charactercreator_necromancer.mage_ptr_id"
result7 = cursor.execute(query7).fetchall()  # > LIST
for row in result7:
    print("-----")
    print('How many total Items?', row[2])