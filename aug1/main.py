import psycopg2

conn = psycopg2.connect(host = "localhost", dbname="testdb", user= "testuser", password = "root", port=5432)
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person (
id INT PRIMARY KEY,
name VARCHAR(255),
age INT,
gender CHAR
);
""")

cur.execute(""" INSERT INTO person(id, name, age, gender) VALUES
(1, 'Risav', 23, 'm'),
(12, 'Sam', 22, 'm'),
(13, 'riri', 26, 'f'),
(15, 'suds', 24, 'm');
""")



conn.commit()

cur.close()
conn.close()