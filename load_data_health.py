import pandas as pd
from progress.bar import Bar
from psycopg2 import IntegrityError

def run(args, cursor):
    filename = args.csv+'Healthy_Aging_Data.csv'
    with open(filename) as csv_file:
        health = pd.read_csv(csv_file, usecols=["YearStart", "LocationAbbr", "LocationDesc", "Class", "Topic", "Question",
                                                "Data_Value_Type", "Data_Value", "Low_Confidence_Limit", "High_Confidence_Limit",
                                                "Stratification1", "QuestionID", "ClassID"])
        
        #state_health = health.loc[:,["YearStart","ClassID","LocationAbbr","Stratification1"]]
        state = health.loc[:,["LocationAbbr", "LocationDesc"]].drop_duplicates("LocationAbbr")
        survey_categories = health.loc[:,["ClassID","Class"]].drop_duplicates("ClassID")
        question_data = health.loc[:,["QuestionID","Question","ClassID","Topic"]].drop_duplicates("QuestionID")
        master = health.loc[:,["YearStart","LocationAbbr","QuestionID","Data_Value_Type","Low_Confidence_Limit", "High_Confidence_Limit","Data_Value"]].dropna()
        sql = ""
        
        for index, row in state.iterrows():
            if row["LocationAbbr"] in ('SOU', 'NRE', 'WEST', 'MDW', 'US') or len(row["LocationAbbr"]) > 2:
                continue
            sql = """INSERT INTO state (stateAbbr, stateName) 
            VALUES ('{0}', '{1}')
            """.format(row["LocationAbbr"], row["LocationDesc"])
            try:
                cursor.execute(sql)
            except IntegrityError:
                print("Integrity Error: Key {0} already exists".format(row['LocationAbbr']))
        
        print('State insertions complete.')
        
        #for index, row in state_health.iterrows():
        #    if row["LocationAbbr"] in ('SOU', 'NRE', 'WEST', 'MDW', 'US') or len(row["LocationAbbr"]) > 2:
        #        continue
        #    sql = """INSERT INTO state_health (year, disability_type, state, age_group)
        #    VALUES ('{}', '{}', '{}', '{}');
        #    """.format(row["YearStart"], row["ClassID"], row["LocationAbbr"], row["Stratification1"])
        #    try:
        #        cursor.execute(sql)
        #    except IntegrityError:
        #        print("Integrity Error: Key {0} already exists".format(row['LocationAbbr']))
            
        #print('state_health insertions complete.')
        
        for index, row in survey_categories.iterrows():
            sql = """INSERT INTO survey_categories (ID, category) 
            VALUES ('{0}', '{1}')
            """.format(row['ClassID'], row['Class'])
            try:
                cursor.execute(sql)
            except IntegrityError:
                print("Integrity Error: Key {0} already exists".format(row['ClassID']))
        
        print('survey_categories insertions complete.')
        
        for index, row in question_data.iterrows():
            sql = """INSERT INTO question_data (questionID, question, categoryID, topic) 
            VALUES ('{0}', '{1}', '{2}', '{3}')
            """.format(row['QuestionID'],  row['Question'], row['ClassID'], row['Topic'])
            try:
                cursor.execute(sql)
            except IntegrityError:
                print("Integrity Error: Key {0} already exists".format(row['questionID']))
        
        print('question_data insertions complete.')
        
        with Bar('Processing master', max=master.shape[0]) as bar:
            for index, row in master.iterrows():
                if row["LocationAbbr"] in ('SOU', 'NRE', 'WEST', 'MDW', 'US') or len(row["LocationAbbr"]) > 2:
                    bar.next()
                    continue
                sql = """INSERT INTO master
                (year, state, questionID, data_type, low_con, high_con, average) 
                VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')
                """.format(row['YearStart'],  row['LocationAbbr'], row['QuestionID'],  
                row['Data_Value_Type'], row['Low_Confidence_Limit'], row['High_Confidence_Limit'], 
                row['Data_Value'])
                cursor.execute(sql)
                bar.next()  
        print('master insertions complete.')