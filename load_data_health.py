import csv

def run(args, cursor):
    filename = args.csv+'/Healthy_Aging_Data.csv'
    with open(filename) as csv_file:
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
        print('state_health insertions complete.')