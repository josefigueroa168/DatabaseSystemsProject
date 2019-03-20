#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:04:39 2019

@author: josefigueroa
"""

import pandas as pd
import psycopg2
import psycopg2.extras

conn_string = "host='localhost' dbname='health' user='josefigueroa' password=''"

conn = psycopg2.connect(conn_string)
cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
conn.autocommit = True

cursor.execute(open("Schema.sql", "r").read())
conn.autocommit = True

with open('500_Cities__Local_Data_for_Better_Health__2018_release.csv') as csv_file:
    cities_df = pd.read_csv(csv_file, usecols=['Year','StateDesc', 'StateAbbr','CityName', 'CityFIPS','PopulationCount','Category','CategoryID', 'MeasureId', 'Measure','Short_Question_Text'  ])
    #Insert to state column
    state = cities_df.loc[:,['StateAbbr','StateDesc']].drop_duplicates('StateAbbr')
    #Insert to cities.. so on. Should clean US dates.
    city_state = cities_df.loc[:, ['CityFIPS', 'CityName', 'StateAbbr']].drop_duplicates('CityFIPS')
    for index, row in state.iterrows():
        if row['StateAbbr'] == 'US':
                continue
        cursor.execute("INSERT INTO state (stateAbbr, stateName) VALUES ('{0}', '{1}')".format(row['StateAbbr'], row['StateDesc']))
    #Some cities have exclamation points to clean for...
    for index, row in city_state.iterrows():
        if row['StateAbbr'] == 'US':
                continue

cursor.close()