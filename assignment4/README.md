# Assignment IV

## mongoDB 

Practice! Go back to both your deployed PostgreSQL (Titanic data) and MongoDB
(RPG data) instances - use [MongoDB
queries](https://docs.mongodb.com/manual/tutorial/query-documents/) to answer
the same questions as you did from the first module (when the RPG data was in
SQLite). 

### How many total Characters are there? (302)
```
coll = db.character_collection
print("Num Characters:", coll.count_documents({}))
```
### How many of each specific subclass?
#### Mage: 108
```
coll = db.mage_collection
print("Num Mages:", coll.count_documents({}))
```
#### Thief: 51
```
coll = db.thief_collection
print("Num Thieves:", coll.count_documents({}))
```
#### Cleric: 75
```
coll = db.cleric_collection
print("Num Clerics:", coll.count_documents({}))
```
#### Fighter: 68
```
coll = db.fighter_collection
print("Num Fighters:", coll.count_documents({}))
```
#### Necromancer: 11
```
coll = db.mancer_collection
print("Num Mancers:", coll.count_documents({}))
```
### How many total Items? (174)
```
coll = db.items_collection
print("Num Items:", coll.count_documents({}))
```
### How many of the Items are weapons? How many are not?
#### Weapons: 37
```
coll = db.weapons_collection
print("Num Weapons:", coll.count_documents({
```
#### Not weapons: 137
```
a = db.items_collection
n_items = a.count_documents({})

b = db.weapons_collection
n_weapons = b.count_documents({})

print("NUM ITEMS NOT WEAPONS:", n_items - n_weapons)
```
### How many Items does each character have? (Return first 20 rows)
*"The following aggregation operation on the orders
collection joins the documents from orders with 
the documents from the inventory collection using
the fields item from the orders collection and 
the sku field from the inventory collection:"*
```
db.ORDERS.aggregate([
   {
     $lookup:
       {
         from: "INVENTORY",
         localField: "item",
         foreignField: "sku",
         as: "inventory_docs"
       }
  }
])
```
... This was about the closest I found for
joins in mongoDB, though I'm pretty sure that
syntax above is for use in a mongo shell.
In the interest of focusing on SQL queries for 
sprint challenge prep, I decided to forgo 
replicating the last 4 queries for now :(

### How many Weapons does each character have? (Return first 20 rows)
```

```
### On average, how many Items does each Character have? (2.97)
```

```
### On average, how many Weapons does each character have? (0.67)
```

```
## PostgreSQL 

With PostgreSQL, answer the following:

- How many passengers survived, and how many died?
- How many passengers were in each class?
- How many passengers survived/died within each class?
- What was the average age of survivors vs nonsurvivors?
- What was the average age of each passenger class?
- What was the average fare by passenger class? By survival?
- How many siblings/spouses aboard on average, by passenger class? By survival?
- How many parents/children aboard on average, by passenger class? By survival?
- Do any passengers have the same name?
- (Bonus! Hard, may require pulling and processing with Python) How many married
  couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  a married couple.