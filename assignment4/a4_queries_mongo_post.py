import pymongo
import os
from dotenv import load_dotenv

### ESTABLISH POSTGRES CONNECTION
 
load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")
connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
# print("----------------")
# print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
# print("----------------")
# print("CLIENT:", type(client), client)
# print("DB NAMES:", client.list_database_names())

db = client.rpg_data_db 
print("----------------")
# print("DB:", type(db), db)
# print(db.list_collection_names()) 
## Output:
# ['thief_collection', 'mancer_collection', 
# 'fighter_collection', 'weapons_collection', 
# 'mage_collection', 'items_collection', 
# 'inventory_collection', 'cleric_collection', 
# 'character_collection']

# NUM CHARACTERS
coll = db.character_collection
print("Num Thieves:", coll.count_documents({}))

## NUM THIEVES
coll = db.thief_collection
print("------------------")
print("Num Thieves:", coll.count_documents({}))

## NUM MAGES
coll = db.mage_collection
print("Num Mages:", coll.count_documents({}))

## NUM CLERICS
coll = db.cleric_collection
print("Num Clerics:", coll.count_documents({}))

## NUM FIGHTERS
coll = db.fighter_collection
print("Num Fighters:", coll.count_documents({}))

## NUM MANCERS
coll = db.mancer_collection
print("Num Necromancers:", coll.count_documents({}))

## NUM ITEMS
coll = db.items_collection
print("Num Items:", coll.count_documents({}))

## NUM WEAPONS
coll = db.weapons_collection
print("Num Weapons:", coll.count_documents({}))

## NUM ITEMS NOT WEAPONS
a = db.items_collection
n_items = a.count_documents({})

b = db.weapons_collection
n_weapons = b.count_documents({})

print("NUM ITEMS NOT WEAPONS:", n_items - n_weapons)



## AVG NUM ITEMS PER CHARACTER
a = db.character_collection
n_characters = a.count_documents({})

b = db.items_collection
n_items = b.count_documents({})

print("AVG NUM ITEMS PER CHAR:", n_items / n_characters)