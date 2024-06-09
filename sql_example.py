import psycopg2

connection = psycopg2.connect(
    user='matthewpopov',
    password='12345678',
    host='127.0.0.1',
    port=5432,
    database='test'
)

cursor = connection.cursor()

query = f"INSERT INTO customers (id, name, age, email) VALUES (%s, %s, %s, %s)"

cursor.execute(query, (4, "Nicko", 25, "example@gmail.com"))

connection.commit()

cursor.execute("SELECT * FROM customers")
records = cursor.fetchall()

for record in records:
    print(record)
