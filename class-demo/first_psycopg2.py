import psycopg2

conn = psycopg2.connect('dbname=foo user=az')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
    CREATE TABLE table2 (
      id INTEGER PRIMARY KEY,
      completed BOOLEAN NOT NULL DEFAULT False
    );
''')


cursor.execute('''
    INSERT INTO table2 (id, completed) VALUES (1, true);
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (2, True))
cursor.execute('INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);', {
  'id': 3,
  'completed': False
})

sql = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'
data = {
  'id': 4,
  'completed': False
}
cursor.execute(sql, data)


# select

cursor.execute('SELECT * FROM table2;')
result = cursor.fetchall()
print(result)
cursor.execute('SELECT * FROM table2;')
result_2 = cursor.fetchone()
print(result_2)
cursor.execute('SELECT * FROM table2;')
result_3 = cursor.fetchmany(2)
print(result_3)


conn.commit()
cursor.close()
conn.close()