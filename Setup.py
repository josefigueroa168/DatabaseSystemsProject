import psycopg2
import psycopg2.extras

conn_string = "host='localhost' dbname='baseball' user='postgres' password='postgres'"

conn = psycopg2.connect(conn_string)
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
conn.autocommit = True

cursor.execute("DROP DATABASE IF EXISTS health;")
cursor.execute("CREATE DATABASE health;")

cursor.execute("DROP USER IF EXISTS health;")
cursor.execute("CREATE USER health WITH PASSWORD 'health';")

cursor.execute("GRANT ALL PRIVILEGES ON DATABASE health TO health;")