import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "myrootpassword",
    #database = "sotd"
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


#Still to come
#Add more than 1 record at a time
#Don't accept duplicate rows
#More than 1 table in a database
#Primary and Secondary keys
#SELECT with JOIN