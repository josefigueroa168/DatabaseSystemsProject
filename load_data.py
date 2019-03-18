import csv
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

conn.autocommit = False

with open('Healthy_Aging_Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            year = row[0]
            location = row[2]
            classType = row[5]
            topic = row[6]
            question = row[7]
            answer = row[12]
            line_count += 1

cursor.close()