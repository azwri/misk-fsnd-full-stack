from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String

# engine = create_engine("postgresql://user:password@localhost/dbname")
engine = create_engine('postgres://az@localhost/test')

conn = engine.connect()


result = engine.execute('SELECT * FROM persons;')
for row in result:
  print(row)
conn.close()


engine_2 = create_engine('sqlite:///db.db', echo=True)
conn_2 = engine_2.connect()
# conn_2.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, name VAR);')
# conn_2.execute('INSERT INTO test (id, name) VALUES(1, "Eyas");')
test = conn_2.execute('SELECT * FROM test;')
for row in test:
  print(row)
conn_2.close()