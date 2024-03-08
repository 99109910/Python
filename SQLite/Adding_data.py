import sqlite3

database= sqlite3.connect("database.db")
cursor = database.cursor()

make_table = "CREATE TABLE IF NOT EXISTS personell(name TEXT,surname TEXT,department TEXT, salary INT )"

cursor.execute(make_table)

database.commit()

cursor.execute("INSERT INTO personell VALUES('Can','Dinler','Management','1000000000')")
cursor.execute("INSERT INTO personell VALUES('Can','Dinler','Management','1000000000')")
cursor.execute("INSERT INTO personell VALUES('Can','Dinler','Management','1000000000')")

database.commit()

name = input("Name:")
Surname = input("Surname:")
Department = input("Department:")
Salary = int(input("Salary:"))

cursor.execute("INSERT INTO personell VALUES(?,?,?,?)",(name,Surname,Department,Salary))

database.commit()
database.close()