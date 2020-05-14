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
print(db.list_collection_names()) #[character_collection]

coll = db.character_collection
print("------------------")
print("Num Characters:", coll.count_documents({}))
