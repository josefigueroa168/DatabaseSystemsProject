import csv
import pandas as pd
import psycopg2
import psycopg2.extras

def insertStates(cursor, conn):
    state_set = set()
    with open('500_Cities__Local_Data_for_Better_Health__2018_release.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            if row[1] == 'US':
                continue
            else:
                abbr = row[1]
                state_name = row[2]
                state_set.add((abbr, state_name))

    for (abbr, state_name) in state_set:
        sql = "insert into state VALUES('{}', '{}');".format(abbr, state_name)
        cursor.execute(sql)
    conn.commit()

conn_string = "host='localhost' dbname='health' user='health' password='health'"

conn = psycopg2.connect(conn_string)
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
conn.autocommit = True

cursor.execute(open("Schema.sql", "r").read())

conn.autocommit = False

with open('Healthy_Aging_Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
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

insertStates(cursor, conn)


cursor.close()