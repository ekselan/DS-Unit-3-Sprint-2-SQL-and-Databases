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
result1 = cursor.execute(query1).fetchall()  
for row in result1:
    print("RPG QUERIES:")
    print("-----")
    print('How many characters?', row[0])

query2 = "SELECT charactercreator_character.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT character_id) as character_count FROM charactercreator_character JOIN charactercreator_mage ON charactercreator_character.character_id = charactercreator_mage.character_ptr_id"
result2 = cursor.execute(query2).fetchall()  
for row in result2:
    print("-----")
    print('How many Mages?', row[2])

query3 = "SELECT charactercreator_character.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT character_id) as character_count FROM charactercreator_character JOIN charactercreator_thief ON charactercreator_character.character_id = charactercreator_thief.character_ptr_id"
result3 = cursor.execute(query3).fetchall() 
for row in result3:
    print("-----")
    print('How many Thieves?', row[2])

query4 = "SELECT charactercreator_character.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT character_id) as character_count FROM charactercreator_character JOIN charactercreator_cleric ON charactercreator_character.character_id = charactercreator_cleric.character_ptr_id"
result4 = cursor.execute(query4).fetchall() 
for row in result4:
    print("-----")
    print('How many Clerics?', row[2])

query5 = "SELECT charactercreator_character.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT character_id) as character_count FROM charactercreator_character JOIN charactercreator_fighter ON charactercreator_character.character_id = charactercreator_fighter.character_ptr_id"
result5 = cursor.execute(query5).fetchall()  
for row in result5:
    print("-----")
    print('How many Fighters?', row[2])

query6 = "SELECT charactercreator_character.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT character_id) as character_count FROM charactercreator_character JOIN charactercreator_necromancer ON charactercreator_character.character_id = charactercreator_necromancer.mage_ptr_id"
result6 = cursor.execute(query6).fetchall()  
for row in result6:
    print("-----")
    print('How many Necromancers?', row[2])

# ***** ITEMS *****

query7 = "SELECT count(DISTINCT item_id) as item_count FROM armory_item"
result7 = cursor.execute(query7).fetchall()  
for row in result7:
    print("-----")
    print('How many total Items?', row[0])

query8 = "SELECT count(DISTINCT item_id) as item_count FROM armory_item JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id"
result8 = cursor.execute(query8).fetchall()  
for row in result8:
    print("-----")
    print('How many of the items are weapons?', row[0])

query9 = "SELECT count(DISTINCT item_id) as item_count ,(count(DISTINCT item_id)) - (count(DISTINCT item_ptr_id)) as non_weapon_count FROM armory_item LEFT JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id"
result9 = cursor.execute(query9).fetchall() 
for row in result9:
    print("-----")
    print('How many of the items are NOT weapons?', row[1])

query10 = "SELECT charactercreator_character_inventory.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT item_id) as item_count FROM charactercreator_character LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id GROUP BY charactercreator_character.character_id LIMIT 20"
result10 = cursor.execute(query10).fetchall() 
print("-----")
print('How many items does each character have (first 20)?')
for row in result10:
    print(row[2])

query11 = "SELECT charactercreator_character_inventory.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT item_id) as item_count ,count(DISTINCT item_ptr_id) as weapon_count FROM charactercreator_character LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id GROUP BY charactercreator_character.character_id LIMIT 20"
result11 = cursor.execute(query11).fetchall() 
print("-----")
print('How many weapons does each character have (first 20)?')
for row in result11:
    print(row[3])

query12 = "SELECT AVG(item_count) FROM (SELECT charactercreator_character_inventory.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT item_id) as item_count FROM charactercreator_character LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id GROUP BY charactercreator_character.character_id)"
result12 = cursor.execute(query12).fetchall() 
for row in result12:
    print("-----")
    print('On average, how many items does each character have?', round(row[0], 2))

query13 = "SELECT AVG(item_count) ,AVG(weapon_count) FROM (SELECT charactercreator_character_inventory.character_id ,charactercreator_character.'Name' as CharacterName ,count(DISTINCT item_id) as item_count ,count(DISTINCT item_ptr_id) as weapon_count FROM charactercreator_character LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id GROUP BY charactercreator_character.character_id)"
result13 = cursor.execute(query13).fetchall() 
for row in result13:
    print("-----")
    print('On average, how many weapons does each character have?', round(row[1], 2))