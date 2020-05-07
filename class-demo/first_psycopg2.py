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

# Practice 
name = input('Enter your name ... ')
age = int(input('How old are you ... '))
conn = psycopg2.connect('dbname=test user=az')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS test;')
cur.execute('''CREATE TABLE test(
               id INTEGER PRIMARY KEY,
               name VARCHAR
              );
''')
cur.execute('''INSERT INTO test
               (id, name)
               VALUES(%s, %s);''', (age, name)
)

cur.execute("SELECT * FROM test;")
result_4 = cur.fetchall()
for x in result_4:
  print(x)



conn.commit()
cur.close()
conn.close()