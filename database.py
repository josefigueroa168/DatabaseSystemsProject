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

    def get_category_ids(self):
        self.cursor.execute("select * from survey_categories;")
        records = self.cursor.fetchall()
        return records

    def search_by_catagory_type_state(self, catagoryid, year, state):
        query = '''
        select avg(average), question from question_data, survey_categories, master
        where question_data.categoryid = survey_categories.id and categoryid ILIKE %s and master.questionid = question_data.questionid and year = %s and state ILIKE %s
        group by question;
        '''
        self.cursor.execute(query, [catagoryid, year, state])
        records = self.cursor.fetchall()
        return records

    def search_us_by_disease_stats(self, disease):
        query = '''
        select state, avg(average), question from master, 
            (select question from question_data
            where questionid ILIKE %s) questiontxt
        where questionid ILIKE %s
        group by state, question;
        '''
        self.cursor.execute(query, [disease, disease])
        records = self.cursor.fetchall()
        return records

    def quit(self):
        self.cursor.close()