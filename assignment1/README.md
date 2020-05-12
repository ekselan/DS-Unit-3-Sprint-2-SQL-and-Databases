# 3.2.1 Assignment Prompt

## TODO

### How many total Characters are there? (302)

```
SELECT 
	count(DISTINCT character_id) as character_count -- 302 characters
FROM charactercreator_character
```

### How many of each specific subclass?

#### Mage: 108
```
SELECT 
	charactercreator_character.character_id
	,charactercreator_character.'Name' as CharacterName
	,count(DISTINCT character_id) as character_count -- 108 characters (subclass: mage)
FROM charactercreator_character
JOIN charactercreator_mage ON charactercreator_character.character_id = charactercreator_mage.character_ptr_id
```
#### Thief: 51
```
SELECT 
	charactercreator_character.character_id
	,charactercreator_character.'Name' as CharacterName
	,count(DISTINCT character_id) as character_count -- 51 characters (subclass: thief)
FROM charactercreator_character
JOIN charactercreator_thief ON charactercreator_character.character_id = charactercreator_thief.character_ptr_id
```
#### Cleric: 75
```
SELECT 
	charactercreator_character.character_id
	,charactercreator_character.'Name' as CharacterName
	,count(DISTINCT character_id) as character_count -- 51 characters (subclass: thief)
FROM charactercreator_character
JOIN charactercreator_cleric ON charactercreator_character.character_id = charactercreator_cleric.character_ptr_id
```
#### Fighter: 68
```
SELECT 
	charactercreator_character.character_id
	,charactercreator_character.'Name' as CharacterName
	,count(DISTINCT character_id) as character_count -- 51 characters (subclass: thief)
FROM charactercreator_character
JOIN charactercreator_fighter ON charactercreator_character.character_id = charactercreator_fighter.character_ptr_id
```
#### Necromancer: 11
```
SELECT 
	charactercreator_character.character_id
	,charactercreator_character.'Name' as CharacterName
	,count(DISTINCT character_id) as character_count -- 51 characters (subclass: thief)
FROM charactercreator_character
JOIN charactercreator_necromancer ON charactercreator_character.character_id = charactercreator_necromancer.mage_ptr_id
```

### How many total Items? (174)
```
SELECT
	count(DISTINCT item_id) as item_count --174 items
FROM armory_item
```

### How many of the Items are weapons? How many are not?

#### Weapons: 37
```
SELECT
	count(DISTINCT item_id) as item_count --37 items are weapons
FROM armory_item
JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
```
#### Not weapons: 137
```
SELECT
	count(DISTINCT item_id) as item_count --137 items are not weapons
	,(count(DISTINCT item_id)) - (count(DISTINCT item_ptr_id)) as non_weapon_count
FROM armory_item
LEFT JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
```

### How many Items does each character have? (Return first 20 rows)
```
SELECT
	charactercreator_character_inventory.character_id
	,charactercreator_character.'Name' as CharacterName
	,count(DISTINCT item_id) as item_count 
FROM charactercreator_character
LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
GROUP BY charactercreator_character.character_id
LIMIT 20
```
Returns output of character_id, CharacterName, and item_count columns,
with item_count being the number of items each character has.

### How many Weapons does each character have? (Return first 20 rows)
```
SELECT
		charactercreator_character_inventory.character_id
		,charactercreator_character.'Name' as CharacterName
		,count(DISTINCT item_id) as item_count
		,count(DISTINCT item_ptr_id) as weapon_count 
	FROM charactercreator_character
	LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
	LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
	GROUP BY charactercreator_character.character_id
	LIMIT 20
```
Returns output of character_id, CharacterName, item_count and  weapon_count
columns, with weapon_count being the number of weapons each character has.
 
### On average, how many Items does each Character have? (2.97)
```
SELECT
	AVG(item_count)
FROM (
	SELECT
		charactercreator_character_inventory.character_id
		,charactercreator_character.'Name' as CharacterName
		,count(DISTINCT item_id) as item_count 
	FROM charactercreator_character
	LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
	GROUP BY charactercreator_character.character_id
)
```
 
### On average, how many Weapons does each character have? (0.67)
```
SELECT
	AVG(item_count)
	,AVG(weapon_count)
FROM (
	SELECT
		charactercreator_character_inventory.character_id
		,charactercreator_character.'Name' as CharacterName
		,count(DISTINCT item_id) as item_count
		,count(DISTINCT item_ptr_id) as weapon_count 
	FROM charactercreator_character
	LEFT JOIN charactercreator_character_inventory ON charactercreator_character.character_id = charactercreator_character_inventory.character_id
	LEFT JOIN armory_weapon ON charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
	GROUP BY charactercreator_character.character_id
	--LIMIT 20
)
```

## Methodology

You do not need all the tables - in particular, the account_*, auth_*, django_*, and socialaccount_* tables are for the application and do not have the data you need. the charactercreator_* and armory_* tables and where you should focus your attention. armory_item and charactercreator_character are the main tables for Items and Characters respectively - the other tables are subsets of them by type (i.e. subclasses), connected via a key (item_id and character_id).

## Submission

You can use the DB Browser or other tools to explore the data and work on your queries if you wish, but to complete the assignment you should write a file rpg_queries.py that imports sqlite3 and programmatically executes and reports results for the above queries.

``` py
rpg_queries_abw.py
```

# Notes on PART II
All code is available in ```buddymove_holidayiq_abw.py```  but markdown version of
SQL prompts and code are also available in ```PART2.md```. (SQL commands are commented out in ```buddymove_holidayiq_abw.py```)