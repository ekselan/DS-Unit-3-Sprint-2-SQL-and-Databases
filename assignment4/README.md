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

```
#### Thief: 51
```

```
#### Cleric: 75
```

```
#### Fighter: 68
```

```
#### Necromancer: 11
```

```
### How many total Items? (174)
```

```
### How many of the Items are weapons? How many are not?
```

```
#### Weapons: 37
```

```
#### Not weapons: 137
```

```
### How many Items does each character have? (Return first 20 rows)
```

```
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