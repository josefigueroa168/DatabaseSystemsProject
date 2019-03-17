import csv
import psycopg2
import psycopg2.extras

'''
DROP DATABASE IF EXISTS health;
CREATE DATABASE restaurant;

DROP USER IF EXISTS health;
CREATE USER health WITH PASSWORD 'health';

GRANT ALL PRIVILEGES ON DATABASE health TO health;
'''


connection_string = "host='localhost' dbname='restaurant' user='health' password='health'"
conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)

with open('Healthy_Aging_Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            year = row[0]
            location = row[2]
            classType = row[5]
            topic = row[6]
            question = row[7]
            answer = row[12]
            print(year, location, classType, topic, question, answer)
            
            #print(f'\t{row[0]}, {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')