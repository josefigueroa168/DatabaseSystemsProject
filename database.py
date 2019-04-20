import psycopg2
import psycopg2.extras

class database(object):
    """
        A database interacting object that executes predifined queries with additional user input.
    """
    def __init__(self):
        conn_string = "host='localhost' dbname='health' user='health' password='health'"
        self.conn = psycopg2.connect(conn_string)
        self.cursor = self.conn.cursor()
    
    def run_query_c_y(self, year):
        self.cursor.execute("select * from census where year = %s;", [year])
        records = self.cursor.fetchall()
        return records

    def run_join_on_question(self):
        self.cursor.execute("select * from master, question_data where master.questionid = question_data.questionid;")

    def search_us_by_disease_stats(self, disease):
        '''
        valid disease: stroke, obesity, cholscreen, dental, cancer, kidney, mhlth
        '''
        query = '''
        select state, avg(average) from master
        where questionid ILIKE %s
        group by state;
        '''
        self.cursor.execute(query, [disease])
        records = self.cursor.fetchall()
        return records
    
    def insurance_correlation(self, question):
        """
        Pulls a join between question_data and master and maps correlation in each state between uninsured and elder health
        The goal is to observe correlations between insurance and health.
        @param question is a valid number from Q01-Q42
        """
        query = '''
            SELECT "state", question, AVG(average) 
            FROM master  
            JOIN question_data qd ON master.questionid=qd.questionid
            AND (master.questionid='ACCESS2' OR master.questionid='%s)
            GROUP BY ("state", question)
            ORDER BY "state";
            '''
        self.cursor.execute(query, [question])
        records = self.cursor.fetchall()
        return records
        
        
    def quit(self):
        self.cursor.close()