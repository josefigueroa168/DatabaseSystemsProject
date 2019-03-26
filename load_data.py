import argparse
import Setup
import psycopg2
import psycopg2.extras
import load_data_cities
import load_data_health

def com_line():    
    #Setup of command line interactions
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--csv-path",action="store",dest="csv", default=""
                        , help="Path of your csv files.")
    parser.add_argument("-s", "--sql-path",action="store", dest="sql", default="Schema.sql", 
                        help="Path of your sql file")
    #args variable
    return parser.parse_args()
    
def create_cursor():
    #Setup of connection and cursor object, using generic 'health' user
    conn_string = "host='localhost' dbname='health' user='health' password='health'"
    conn = psycopg2.connect(conn_string)
    conn.autocommit = True
    return conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

args = com_line()
cursor = create_cursor()
cursor.execute(open(args.sql,"r").read())
load_data_cities.run(args, cursor)
load_data_health.run(args, cursor)

cursor.close()
print('Successfully closed cursor connection.')