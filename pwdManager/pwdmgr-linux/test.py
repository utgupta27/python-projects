import sqlite3
conn = sqlite3.connect("data.db")
cursor = conn.cursor()
# cursor.execute("CREATE TABLE EMP(NAME CHAR(20),ADDRESS CHAR(50))")
# cursor.execute("INSERT INTO EMP(NAME,ADDRESS) values ('AMARESH','GORAKHPUR')")
result = cursor.execute("SELECT * FROM EMP")
for i in result:
    print(i)
conn.commit()
conn.close()
