# BuddyMove Data Set

### Count how many rows you have (249)
```
SELECT 
	count(DISTINCT "User Id") as users_count
FROM REVIEW
```

### How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category? (78)

```
SELECT 
	count(DISTINCT "User Id") as Nat_and_shop_count
FROM REVIEW
WHERE Nature>=100 and Shopping>=100
```

### (STRETCH) What are the average number of reviews for each category?
```
SELECT 
	AVG(Sports)
	,AVG(Religious)
	,AVG(Nature)
	,AVG(Theatre)
	,AVG(Shopping)
	,AVG(Picnic)
FROM REVIEW
```
Returns 6 columns (AVG(Sports), AVG(Religious) etc ...) with average number (score/value?) of each category