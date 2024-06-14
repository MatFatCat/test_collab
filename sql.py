import psycopg2

connection = psycopg2.connect(
    user='postgres',
    password='estonia12345',
    host='127.0.0.1',
    port=5432,
    database='Persons'
)

cursor = connection.cursor()

query = f"INSERT INTO customers (id, name, age, email) VALUES (%s, %s, %s, %s)"

cursor.execute(query, (9, "Idris", 25, "jidris@gmail.com"))

connection.commit()

cursor.execute("SELECT * FROM customers")
records = cursor.fetchall()

for record in records:
    print(record)
