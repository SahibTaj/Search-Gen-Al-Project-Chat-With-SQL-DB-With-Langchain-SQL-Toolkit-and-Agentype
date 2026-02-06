import sqlite3

connection = sqlite3.connect("student.db")

cursor=connection.cursor()

table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
"""

cursor.execute(table_info)

cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Aarav', 'Data Science', 'B', 85)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Diya', 'Data Science', 'A', 95)''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Maya', 'Data Science', 'C', 80)''')

print("The inserted records are:")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()