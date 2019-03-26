import psycopg2
import psycopg2.extras
import argparse

def __main__():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username",action="store",dest="un", default="postgres"
                        , help="Username of a postgres superuser. Default value is postgres.")
    parser.add_argument("-p", "--password",action="store", dest="pw", default="postgres", 
                        help="Password of respective postgress superuser. Default value is postgres.")
    parser.add_argument("-d", "--database",action="store", dest="db", default="postgres", 
                        help="Database to be used during session. Default value is postgres.")
    args = parser.parse_args()
    conn_string = "host='localhost' dbname='"+args.db+"' user='"+args.un+"' password='"+args.pw+"'"
    conn = psycopg2.connect(conn_string)
    conn.autocommit = True
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("DROP DATABASE IF EXISTS health;")
    cursor.execute("CREATE DATABASE health;")
    cursor.execute("DROP USER IF EXISTS health;")
    cursor.execute("CREATE USER health WITH PASSWORD 'health';")
    cursor.execute("GRANT ALL PRIVILEGES ON DATABASE health TO health;")
    cursor.close()
    print('Successfully closed cursor.')
    
if (__name__=="__main__"):
    __main__()