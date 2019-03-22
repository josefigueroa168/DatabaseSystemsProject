#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:04:39 2019

@author: josefigueroa
"""

import pandas as pd
import psycopg2
import psycopg2.extras
from psycopg2 import IntegrityError
import sys

conn_string = "host='localhost' dbname='health' user='health' password='health'"

conn = psycopg2.connect(conn_string)
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
conn.autocommit = True

cursor.execute(open("Schema.sql", "r").read())
conn.autocommit = True
sql = ""
with open('500_Cities__Local_Data_for_Better_Health__2018_release.csv') as csv_file:
    #Relevant Features
    cities_df = pd.read_csv(csv_file, usecols=['Year','StateDesc', 'StateAbbr','CityName', 'CityFIPS','PopulationCount','Category',
                                               'CategoryID', 'MeasureId', 'Measure','Short_Question_Text', 'Data_Value_Type',
                                               'Low_Confidence_Limit','High_Confidence_Limit','Data_Value'])
    cities_df = cities_df.dropna()
    cities_df.CityFIPS = cities_df.CityFIPS.astype(int)
    cities_df.CityName = cities_df.CityName.apply(lambda x: x.replace("'",""))
    #Parsing for tables
    
    #States: Dropped repeats as we only need one instance of each state.
    state = cities_df.loc[:,['StateAbbr','StateDesc']].drop_duplicates('StateAbbr')
    
    #CityState: Dropped repeats as we only need one instance of each city.
    city_state = cities_df.loc[:, ['CityFIPS', 'CityName', 'StateAbbr']].drop_duplicates('CityFIPS')
    #city_state = city_state.dropna()
    #city_state.CityFIPS = city_state.CityFIPS.astype(int)
    #city_state.CityName = city_state.CityName.apply(lambda x: x.replace("'",""))
    
    #Census: Used groupby to aggregate by state and year, summing city populations
    #Not sure how accurate this data would be for us.
    census = cities_df.loc[:, ['Year', 'StateAbbr', 'PopulationCount']].groupby(['Year', 'StateAbbr']).sum()
    
    #Survey Categories: dropped duplicates just cuz
    survey_categories = cities_df.loc[:,['CategoryID','Category']].drop_duplicates('CategoryID')
    
    question_data = cities_df.loc[:,['MeasureId','Measure','CategoryID','Short_Question_Text' ]].drop_duplicates('MeasureId')
    
    for index, row in state.iterrows():
        sql = """INSERT INTO state (stateAbbr, stateName) 
        VALUES ('{0}', '{1}')
        """.format(row['StateAbbr'], row['StateDesc'])
        try:
            cursor.execute(sql)
        except IntegrityError:
            print("Integrity Error: Key {0} already exists".format(row['StateAbbr']))
    
    for index, row in city_state.iterrows():
        sql = """INSERT INTO city_state (cityID, city, state)
        VALUES ('{0}', '{1}', '{2}')
        """.format(row['CityFIPS'], row['CityName'], row['StateAbbr'])
        try:
            cursor.execute(sql)
        except IntegrityError:
            print("Integrity Error: Key {0} already exists".format(row['CityFIPS']))
     
    for index, row in census.iterrows():
        sql = """
        INSERT INTO census (year, state, population) 
        VALUES ('{0}', '{1}', '{2}')
        """.format(index[0], index[1], row['PopulationCount'])
        try:
            cursor.execute(sql)
        except IntegrityError:
            print("Integrity Error: Key ({0},{1}) already exists".format(index[0],index[1]))
    
    for index, row in survey_categories.iterrows():
        sql = """INSERT INTO survey_categories (ID, category) 
        VALUES ('{0}', '{1}')
        """.format(row['CategoryID'], row['Category'])
        try:
            cursor.execute(sql)
        except IntegrityError:
            print("Integrity Error: Key {0} already exists".format(row['CategoryID']))
    
    for index, row in question_data.iterrows():
        sql = """INSERT INTO question_data (questionID, question, categoryID, topic) 
        VALUES ('{0}', '{1}', '{2}', '{3}')
        """.format(row['MeasureId'],  row['Measure'], row['CategoryID'], row['Short_Question_Text'])
        try:
            cursor.execute(sql)
        except IntegrityError:
            print("Integrity Error: Key {0} already exists".format(row['MeasureId']))
    
    for index, row in cities_df.iterrows():
        sql = """INSERT INTO master
        (year, state, cityID, questionID, data_type, low_con, high_con, average) 
        VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')
        """.format(row['Year'],  row['StateAbbr'], row['CityFIPS'], 
        row['MeasureId'],  row['Data_Value_Type'], row['Low_Confidence_Limit'], row['High_Confidence_Limit'], 
        row['Data_Value'])
        cursor.execute(sql)
    

cursor.close()