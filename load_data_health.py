import psycopg2
import psycopg2.extras
from psycopg2 import IntegrityError
import csv
from progress.bar import Bar

def run():

	conn_string = "host='localhost' dbname='health' user='health' password='health'"
	conn = psycopg2.connect(conn_string)
	cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

	with open('Healthy_Aging_Data.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		line_count = 0
		for row in csv_reader:
			line_count += 1
			if(line_count == 1):
				continue
			year = row[0]
			state = row[2]
			disability = row[6]
			age = row[20]
			if state in ('SOU', 'NRE', 'WEST', 'MDW', 'US') or len(state) > 2:
				continue
			sql = "INSERT INTO state_health (year, disability_type, state, age_group) VALUES ('{}', '{}', '{}', '{}');".format(year, disability, state, age)
			cursor.execute(sql)
	conn.commit()