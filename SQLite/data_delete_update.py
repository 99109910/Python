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
        
def update(old_department,new_department):
    cursor.execute("UPDATE personell SET Department=? WHERE Department=?" ,(new_department,old_department))
    database.commit()
    
update("Management","Management")

def delete(department):
    cursor.execute("DELETE FROM personell WHERE Department=?", (department,))
    database.commit()
    
delete("Management")

take_datas()
        
database.close()