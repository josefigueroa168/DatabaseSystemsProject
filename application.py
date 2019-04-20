import database
import gui
import pandas as pd

if __name__ == "__main__":
    db = database.database()

    US_DISEASE_SEARCH = 1
    SOMETHING = 2
    CORRELATION = 3
    HELP = 8
    QUIT = 9

    print("Welcome to the US health database")

    while True:
        print("{}) Search the US by disease code".format(US_DISEASE_SEARCH))
        print("{}) ".format(SOMETHING))
        print("{}) See correlation between insurance and elder health.".format(CORRELATION))
        print("{}) help".format(HELP))
        print("{}) close the US health database".format(QUIT))
        query_type = int(input("Enter query type: "))
        if query_type == US_DISEASE_SEARCH:
            disease = input("Enter disease code: ")
            rec = db.search_us_by_disease_stats(disease)
            if(len(rec) == 0):
                print('No results found, disease code not present')
            else:
                data = dict()
                question = rec[0][2]
                for i in range(len(rec)):
                    data[rec[i][0]] = rec[i][1]
                gui.plot1(data, disease)
       
        elif query_type == SOMETHING:
            category_id = input('Enter catagory type: ')
            year = input('Enter year: ')
            state = input('Enter state: ')
            rec = db.search_by_catagory_type_state(category_id, year, state)
            data = dict()
            for i in range(len(rec)):
                data[rec[i][1]] = rec[i][0]
            gui.plot2(data)      


        elif query_type == CORRELATION:
            question = input("Enter question code: ")
            rec = db.insurance_correlation(question)
            if(len(rec) == 0):
                print('No results found, question code not present.')
            else:
                gui.plot3(pd.DataFrame(rec))
                
        elif query_type == HELP:
            print('1) get category codes')
            command = int(input('Enter command: '))
            if command == 1:
                rec = db.get_category_ids()
                for i in range(len(rec)):
                    print('Code: {} -> English: {}'.format(rec[i][0], rec[i][1]))
                
        elif query_type == QUIT:
            db.quit()
            break
        
        
    
    