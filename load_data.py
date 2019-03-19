import csv
# import pandas as pd
import psycopg2
import psycopg2.extras

def insertStates(cursor, conn):
    with open('states.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                state = row[0]
                abbr = row[1]
                sql = "insert into state VALUES('{}', '{}');".format(abbr, state)
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



# with open('500_Cities__Local_Data_for_Better_Health__2018_release.csv') as csv_file:
#     cities_df = pd.read_csv(csv_file, usecols=['Year','StateDesc', 'StateAbbr','CityName', 'CityFIPS','PopulationCount','Category','CategoryID', 'MeasureId', 'Measure','Short_Question_Text'  ])
#     #Insert to state column
#     state = cities_df.loc[:,['StateAbbr','StateDesc']].drop_duplicates('StateAbbr')
#     #Insert to cities.. so on. Should clean US dates.
#     city_state = cities_df.loc[:, ['CityFIPS', 'CityName', 'StateAbbr']].drop_duplicates('CityFIPS')
    

cursor.close()