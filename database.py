import psycopg2
import psycopg2.extras

class database(object):
    def __init__(self):
        conn_string = "host='localhost' dbname='health' user='health' password='health'"
        conn = psycopg2.connect(conn_string)
        self.cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def run_query(self, sql):
        self.cursor.execute(sql)
        records = self.cursor.fetchall()
        return records