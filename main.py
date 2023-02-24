import sqlite3

# conn = sqlite3.connect('test_sqlite.db')
conn = sqlite3.connect(':memory')
curs = conn.cursor()
curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
conn.commit()

curs.execute(
    'INSERT INTO persons(name) values("MIKE")'
)
conn.commit()

curs.execute('SELECT * FROM persons')
print(curs.fetchall())

curs.execute(
    'INSERT INTO persons(name) values("NANCY")'
)
curs.execute(
    'INSERT INTO persons(name) values("TOM")'
)
conn.commit()

curs.execute('UPDATE persons set name = "MICHEL" WHERE name = "MIKE"')
conn.commit()

curs.execute('DELETE FROM persons WHERE name = "MICHEL"')
conn.commit()
curs.close()
conn.close()