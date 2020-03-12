import mysql.connector
import csv
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Sp323823906",
    database="runescapeIDs"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE runescapeIDs") creates database


# mycursor.execute("SHOW DATABASES")  #show database
# for db in mycursor:
#     print(db)

#mycursor.execute("CREATE TABLE items (name VARCHAR(255), ID INTEGER(255))") #create a table

# mycursor.execute("SHOW TABLES") #show table
# for tb in mycursor:
#     print(tb)


# sqlFormula = "INSERT INTO items (name,ID) VALUES (%s,%s)"
# items = [("Cannonball",2), ("Cannon base",6),("Cannon stand",8),("Cannon barrels",10),("Cannon furnace",12),("Candle",36)]
# mycursor.executemany(sqlFormula,items)
# mydb.commit() #have to commit to your database to save changes

fname ="RuneScape Item List (by ID).csv"
with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        name=row[1]
        ID=int(row[0])
        mycursor.execute('''INSERT INTO items(name,ID) VALUES (%s,%s)''',(name,ID))
        mydb.commit()
