# Assignment III

Full Assignment III code (including mongoDB instance connection) is available in ```mongo_queries_abw.py```. Below is response to question prompt as well as code to insert RPG data into MongoDB.

## "How was working with MongoDB different from working with PostgreSQL? What was easier, and what was harder?"

I thought MongoDB was quite different because I feel it's much easier to make mistakes in mongo than PostgreSQL. Particularly in terms of bringing data in, mongoDB lets you put just about anything, so I was more than half way done before I realized I probably should have been putting each SQL table into its own collection. Alternati vely, bringing data into postgreSQL was more like playing a game of "Emergency," where the computer yells at you pretty quickly if it sees anything that doesn't add up.

Having said that, mongoDB makes it a bit easier to import data into. If all things were equal, I'd probably choose to use a SQL database because
1) it will help ensure data is being brought in appropriately (albeit risk of duplicates still exists)
2) it has multiple GUIs (that I'm familiar with) that make interaction and experimentation more intuitive

Overall I'd say SQL is great for beginners (like myself), but I could imagine more-skilled users preferring mongoDB.

## RPG to MongoDB
```
################## ASSIGNMENT III #############################

# INSERT RPG DATA INTO MONGODB INSTANCE


## Establish sqlite3 connection to access rpg data
sl_conn = sqlite3.connect("data/rpg_db_original.sqlite3")
sl_curs = sl_conn.cursor()

## Create new collection for RPG data
collection2 = db.rpg_collection
print("-------------------")
print("COLLECTION 2:", type(collection2), collection2)
# print("COLLECTIONS:")
# print(db.list_collection_names())


################# CHARACTERS ###########################


## Establish SQL syntax for query
# rpg_characters = 'SELECT * FROM charactercreator_character'


## Function to loop through characters and return list of dictionaries
# def all_chars():
#     query = rpg_characters
#     chars = sl_curs.execute(query)
#     char_data = []
#     for row in chars:
#         character = {
#             "character_id": row[0], 
#             "name": row[1],
#             "level": row[2],
#             "exp": row[3],
#             "hp": row[4],
#             "strength": row[5],
#             "intelligence": row[6],
#             "dexterity": row[7],
#             "wisdom": row[8]
#             }
#         char_data.append(character)
#     result = char_data
#     return result 

# character_dict_list = all_chars()
# # print(character_dict_list)

# collection2.insert_many(character_dict_list)
# print("DOCS(Num Characters):", collection2.count_documents({})) # SELECT count(distinct id) from characters


################# MAGES ###########################


# mages = 'SELECT * FROM charactercreator_mage'
# def all_chars():
#     query = mages
#     chars = sl_curs.execute(query)
#     char_data = []
#     for row in chars:
#         character = {
#             "character_ptr_id": row[0], 
#             "has_pet": row[1],
#             "mana": row[2],
#             }
#         char_data.append(character)
#     result = char_data
#     return result 

# character_dict_list = all_chars()

# collection2.insert_many(character_dict_list)
# print("DOCS:", collection2.count_documents({}))


################# THIEVES ###########################


# thieves = 'SELECT * FROM charactercreator_thief'
# def all_chars():
#     query = thieves
#     chars = sl_curs.execute(query)
#     char_data = []
#     for row in chars:
#         character = {
#             "character_ptr_id": row[0], 
#             "is_sneaking": row[1],
#             "energy": row[2],
#             }
#         char_data.append(character)
#     result = char_data
#     return result 

# character_dict_list = all_chars()

# collection2.insert_many(character_dict_list)
# print("DOCS:", collection2.count_documents({}))


################# CLERICS ###########################

# clerics = 'SELECT * FROM charactercreator_cleric'
# def all_chars():
#     query = clerics
#     chars = sl_curs.execute(query)
#     char_data = []
#     for row in chars:
#         character = {
#             "character_ptr_id": row[0], 
#             "using_shield": row[1],
#             "mana": row[2],
#             }
#         char_data.append(character)
#     result = char_data
#     return result 

# character_dict_list = all_chars()

# collection2.insert_many(character_dict_list)
# print("DOCS:", collection2.count_documents({}))


################# FIGHTERS ###########################

# fighters = 'SELECT * FROM charactercreator_fighter'
# def all_chars():
#     query = fighters
#     chars = sl_curs.execute(query)
#     char_data = []
#     for row in chars:
#         character = {
#             "character_ptr_id": row[0], 
#             "using_shield": row[1],
#             "rage": row[2],
#             }
#         char_data.append(character)
#     result = char_data
#     return result 

# character_dict_list = all_chars()

# collection2.insert_many(character_dict_list)
# print("DOCS:", collection2.count_documents({}))


################# NECROMANCERS ###########################

# mancers = 'SELECT * FROM charactercreator_necromancer'
# def all_chars():
#     query = mancers
#     chars = sl_curs.execute(query)
#     char_data = []
#     for row in chars:
#         character = {
#             "mage_ptr_id": row[0], 
#             "talisman_charged": row[1],
#             }
#         char_data.append(character)
#     result = char_data
#     return result 

# character_dict_list = all_chars()

# collection2.insert_many(character_dict_list)
# print("DOCS:", collection2.count_documents({}))


################# ITEMS ###########################

# items = 'SELECT * FROM armory_item'
# def all_chars():
#     query = items
#     chars = sl_curs.execute(query)
#     char_data = []
#     for row in chars:
#         character = {
#             "item_id": row[0], 
#             "name": row[1],
#             "value": row[2],
#             "weight": row[3]
#             }
#         char_data.append(character)
#     result = char_data
#     return result 

# character_dict_list = all_chars()

# collection2.insert_many(character_dict_list)
# print("DOCS:", collection2.count_documents({}))


################# WEAPONS ###########################

# weapons = 'SELECT * FROM armory_weapon'
# def all_chars():
#     query = weapons
#     chars = sl_curs.execute(query)
#     char_data = []
#     for row in chars:
#         character = {
#             "item_ptr_id": row[0], 
#             "power": row[1]
#             }
#         char_data.append(character)
#     result = char_data
#     return result 

# character_dict_list = all_chars()

# collection2.insert_many(character_dict_list)
# print("DOCS:", collection2.count_documents({}))


################# INVENTORY ###########################

# records = 'SELECT * FROM charactercreator_character_inventory'
# def all_chars():
#     query = records
#     chars = sl_curs.execute(query)
#     char_data = []
#     for row in chars:
#         character = {
#             "id": row[0], 
#             "character_id": row[1],
#             "item_id": row[2]
#             }
#         char_data.append(character)
#     result = char_data
#     return result 

# character_dict_list = all_chars()

# collection2.insert_many(character_dict_list)
print("DOCS:", collection2.count_documents({}))
print("COLLECTIONS:")
print(db.list_collection_names())

### Got the result of 1724 documents in collection2 which was as expected,
### but later realized it would have been better to create collection for 
### each of these as opposed to just putting them all in one collection,
### since collections == tables
```