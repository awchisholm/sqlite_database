import sqlite3
import os
database = 'example.db'
if os.path.exists(database):
    os.remove(database)

sql = '''
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "recipe" (
	"recipe_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"pizza_id"	INTEGER NOT NULL,
	"ingredient_id"	INTEGER NOT NULL,
	FOREIGN KEY("ingredient_id") REFERENCES "ingredient"("ingredient_id"),
	FOREIGN KEY("pizza_id") REFERENCES "pizza"("pizza_id")
);
CREATE TABLE IF NOT EXISTS "ingredient" (
	"ingredient_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"ingredient_name"	TEXT
);
CREATE TABLE IF NOT EXISTS "pizza" (
	"pizza_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"pizza_name"	TEXT
);
INSERT INTO "recipe" ("recipe_id","pizza_id","ingredient_id") VALUES (1,1,1),
 (2,1,2),
 (3,1,3),
 (4,1,6),
 (5,2,1),
 (6,2,2),
 (7,2,3),
 (8,2,4),
 (9,3,1),
 (10,3,2),
 (11,3,6),
 (12,3,5);
INSERT INTO "ingredient" ("ingredient_id","ingredient_name") VALUES (1,'Cheese'),
 (2,'Tomato'),
 (3,'Pepperoni'),
 (4,'Barbeque Sauce'),
 (5,'Pineapple'),
 (6,'Mushroom');
INSERT INTO "pizza" ("pizza_id","pizza_name") VALUES (1,'Calzone'),
 (2,'Texan Barbeque'),
 (3,'Hawaiian');
COMMIT;
'''

con = sqlite3.connect(database)
cur = con.cursor()
cur.executescript(sql)
con.commit()
con.close()

# This finds what a Calzone is made of
query = '''
select pizza.pizza_name, ingredient.ingredient_name from pizza 
left join recipe 
  on pizza.pizza_id = recipe.pizza_id 
left join ingredient 
  on recipe.ingredient_id = ingredient.ingredient_id
where pizza.pizza_name = 'Calzone' 
'''
con = sqlite3.connect(database)
cur = con.cursor()
rows = cur.execute(query).fetchall()
print(rows)
con.close()
