import sqlite3

database= sqlite3.connect("database.db")
cursor = database.cursor()

make_table = "CREATE TABLE IF NOT EXISTS personell(name TEXT,surname TEXT,department TEXT, salary INT )"

cursor.execute(make_table)

database.commit()

cursor.execute("INSERT INTO personell VALUES('Can','Dinler','Management','1000000000')")
cursor.execute("INSERT INTO personell VALUES('Can','Dinler','Management','1000000000')")
cursor.execute("INSERT INTO personell VALUES('Can','Dinler','Management','1000000000')")
cursor.execute("INSERT INTO personell VALUES('Can','Dinler','Management','1000000000')")
cursor.execute("INSERT INTO personell VALUES('Can','Dinler','Management','1000000000')")

database.commit()

def take_datas():
    cursor.execute("SELECT * FROM personell")
    list = cursor.fetchall()
    for i in list:
        print(i)
        
def take_persons():
    cursor.execute("SELECT Name,Surname FROM personell")
    list = cursor.fetchall()
    for i in list:
        print(i)

def take_department():
    cursor.execute("SELECT * FROM personell WHERE Department = 'Management' " )
    list = cursor.fetchall()
    for i in list:
        print(i)

take_department()



database.close()