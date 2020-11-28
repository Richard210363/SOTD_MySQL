import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "myrootpassword",
    database = "sotd"
)

print(db)

#You always need this
cursor = db.cursor()


#1
######################################################################################################
##Create a database
#cursor.execute("CREATE DATABASE sotd")

#2
######################################################################################################
##Display the databases in the MYSQL instence
#cursor.execute("SHOW DATABASES")  # Sends a command to the database
#databases = cursor.fetchall() #Fetches all the rows returned by the prevouse command

#print(databases) #Print All at once

#for database in databases: # Print 1 at a time
#    print(database)

#3
######################################################################################################
##Create a table in a database
#cursor.execute("CREATE TABLE entities (name VARCHAR(255), type VARCHAR(255), lives INT(10))")

#4
######################################################################################################
##show Tables in a database  RESTORE LINE 7
#cursor.execute("SHOW TABLES")

#tables = cursor.fetchall()

#for table in tables:
#    print(table)

#5
######################################################################################################
#Add data   NOTICE WHAT HAPPENS IF WE RUN THIS TWICE
#query = "INSERT INTO entities (name, type, lives) VALUES (%s, %s, %s)"
#values = ("Shaun", "Player", 10)

#cursor.execute(query, values) #execute the command
#db.commit() # Tell the database to commit

#print(cursor.rowcount, "record inserted")

#6
#####################################################################################################
#Get the data back.  All columns
#query = "SELECT * FROM entities"

#cursor.execute(query)

#records = cursor.fetchall()

#print("=========================================")
#print("All columns")

#for record in records:
#    print(record)

#7
#######################################################################################################
#Get the data back.  Single column
#query = "SELECT type FROM entities"

#cursor.execute(query)

#records = cursor.fetchall()

#print("=========================================")
#print("Single column by name - type")

#for record in records:
#    print(record)

#8
#######################################################################################################
#Get the data back.  More than 1 but not all columns
#query = "SELECT name, lives FROM entities"

#cursor.execute(query)

#records = cursor.fetchall()

#print("=========================================")
#print("Multiple columns by name - name, lives")

#for record in records:
#    print(record)

#9
######################################################################################################
##Delete records
#query = "DELETE FROM entities"
#cursor.execute(query)
#db.commit()  #NOTE commit is for when we change data

#10
######################################################################################################
##Add data
#query = "INSERT INTO entities (name, type, lives) VALUES (%s, %s, %s)"
#values = ("Shaun", "Player", 10)

#cursor.execute(query, values) #execute the command
#db.commit() # Tell the database to commit

#print(cursor.rowcount, "record inserted")

#query = "INSERT INTO entities (name, type, lives) VALUES (%s, %s, %s)"
#values = ("Zombie01", "Enemy", 8)

#cursor.execute(query, values) #execute the command
#db.commit() # Tell the database to commit

#print(cursor.rowcount, "record inserted")

#query = "INSERT INTO entities (name, type, lives) VALUES (%s, %s, %s)"
#values = ("Ed", "NPC", 20)

#cursor.execute(query, values) #execute the command
#db.commit() # Tell the database to commit

#print(cursor.rowcount, "record inserted")

#11
######################################################################################################
## Return selected item with WHERE
#query = "SELECT * FROM entities WHERE name = 'Shaun'"

#cursor.execute(query)
#records = cursor.fetchall()

#print("=========================================")
#print("WHERE name= Shaun")

#for record in records:
#    print(record)

#12
######################################################################################################
## Return selected items with WHERE
#query = "SELECT * FROM entities WHERE lives >8"

#cursor.execute(query)
#records = cursor.fetchall()

#print("=========================================")
#print("WHERE lives > 8")

### Showing the data
#for record in records:
#    print(record)


#13
######################################################################################################
## Return selected items with WHERE
#query = "SELECT * FROM entities WHERE lives >8 ORDER by lives DESC"

#cursor.execute(query)
#records = cursor.fetchall()

#print("=========================================")
#print("WHERE lives > 8 - Decending")

### Showing the data
#for record in records:
#    print(record)

#14
######################################################################################################
## Update
#query = "UPDATE entities SET lives = 9 WHERE name = 'Shaun'"

##WHAT GOES HERE?

#15
######################################################################################################
## Delete JUST Zombie01
#query = "DELETE FROM entities WHAT GOES HERE?"

##WHAT GOES HERE?

#16
######################################################################################################
#Delete a table
#cursor.execute("DROP TABLE entities")




######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################

#Still to come
#Add more than 1 record at a time
#Don't accept duplicate rows
#More than 1 table in a database
#Primary and Secondary keys
#SELECT with JOIN

#17
######################################################################################################
#Reset the table to new state.  Pick how you do this


#18
######################################################################################################
##Add data in bulk
#query = "INSERT INTO entities (name, type, lives) VALUES (%s, %s, %s)"

#values = [
#    ("Zombie01", "Enemy", 5),
#    ("Shaun", "Player", 10),
#    ("Zombie02", "Enemy", 5),
#    ("Ed", "NPC", 8)
#]


#cursor.executemany(query, values) #execute the command
#db.commit() # Tell the database to commit

#if cursor.rowcount > 1:
#    print(cursor.rowcount, "records inserted")
#else:
#    print(cursor.rowcount, "record inserted")  #<???

#if cursor.rowcount > 1:
#    outputText="records inserted"
#else:
#    outputText="record inserted"
#print(cursor.rowcount, outputText)

#19
######################################################################################################
#Delete the table
#cursor.execute("DROP TABLE entities")

#20
######################################################################################################
##A table with unique record IDs

#cursor.execute("CREATE TABLE entities (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), type VARCHAR(255), lives INT(10))")

#Add several records.  Look at records in SQL Workbench

#21
######################################################################################################
#Delete the table
#cursor.execute("DROP TABLE entities")

#22
######################################################################################################
#A table with unique records by single column

#cursor.execute("""
#        CREATE TABLE entities (
#            id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
#            name VARCHAR(255) UNIQUE, type VARCHAR(255), 
#            lives INT(10))
#            """)

#Try to add several records.

#query = "INSERT INTO entities (name, type, lives) VALUES (%s, %s, %s)"

#values = [
#    ("Zombie01", "Enemy", 5),
#    ("Shaun", "Player", 10),
#    ("Zombie01", "Enemy", 5),  #<----NOTE
#    ("Ed", "NPC", 8)
#]

#cursor.executemany(query, values)
#db.commit() 

#23
######################################################################################################
#Delete the table
#cursor.execute("DROP TABLE entities")


#24
######################################################################################################
#A table with unique records by multiple columns

#cursor.execute("""
#        CREATE TABLE entities (
#            id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
#            name VARCHAR(255), type VARCHAR(255), 
#            lives INT(10),
#            CONSTRAINT uc_name_type UNIQUE (name , type))
#            """)

#Try to add several records.

#query = "INSERT INTO entities (name, type, lives) VALUES (%s, %s, %s)"

#values = [
#    ("Zombie01", "Enemy", 5),
#    ("Shaun", "Player", 10),
#    ("Shaun", "Enemy", 5),  #<----NOTE
#    ("Ed", "NPC", 8)
#]

#cursor.executemany(query, values)
#db.commit() 


#############################################################################################################################
#############################################################################################################################
#############################################################################################################################

#Use of multiple tables

#25
######################################################################################################
#Delete the table
#cursor.execute("DROP TABLE entities")
#cursor.execute("DROP TABLE npc")

##26
#######################################################################################################
##Create Entity table - This is the same table we used above with UNIQUE name but missing lives
##Create new npc table

#cursor.execute("""
#        CREATE TABLE entities (
#            id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
#            name VARCHAR(255) UNIQUE, 
#            type VARCHAR(255))
#            """)

#cursor.execute("""
#        CREATE TABLE npc (
#            id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
#            name VARCHAR(255) UNIQUE, 
#            bullets VARCHAR(255), 
#            lives INT(10))
#            """)


#27
######################################################################################################
#Add data

#query = "INSERT INTO entities (name, type) VALUES (%s, %s)"

#values = [
#    ("Zombie01", "Enemy"),
#    ("Shaun", "Player"),
#    ("Zombie02", "Enemy"),
#    ("Ed", "NPC"),
#    ("Mum", "NPC")
#]

#cursor.executemany(query, values)
#db.commit() 

#query = "INSERT INTO npc (name, bullets, lives) VALUES (%s, %s, %s)"

#values = [
#    ("Ed", 50, 8),
#    ("Mum", 0, 5)
#]

#cursor.executemany(query, values)
#db.commit() 

#28
######################################################################################################
#Select with an INNER JOIN

#query = "SELECT \
#  entities.name AS name, \
#  npc.lives AS lives \
#  FROM entities \
#  INNER JOIN npc ON entities.name = npc.name"


#cursor.execute(query)
#records = cursor.fetchall()

##print("=========================================")
#print("Inner Join")
### Showing the data
#for record in records:
#    print(record)

##29
#######################################################################################################
##Select with a LEFT JOIN

#query = "SELECT \
#  entities.name AS name, \
#  npc.lives AS lives \
#  FROM entities \
#  LEFT JOIN npc ON entities.name = npc.name"


#cursor.execute(query)
#records = cursor.fetchall()

##print("=========================================")
#print("Left Join")
### Showing the data
#for record in records:
#    print(record)

##30
#######################################################################################################
##Select with a RIGHT JOIN

#query = "SELECT \
#  entities.name AS name, \
#  npc.lives AS lives \
#  FROM entities \
#  RIGHT JOIN npc ON entities.name = npc.name"


#cursor.execute(query)
#records = cursor.fetchall()

##print("=========================================")
#print("Right Join")
### Showing the data
#for record in records:
#    print(record)    #<----??