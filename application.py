import database
import gui
import pandas as pd

if __name__ == "__main__":
    db = database.database()

    US_DISEASE_SEARCH = 1
    STATE_CATEGORY = 2
    CORRELATION = 3
    HELP = 8
    QUIT = 9

    print("Welcome to the US health database")

    while True:
        print("{}) Search the US by disease code".format(US_DISEASE_SEARCH))
        print("{}) Search by states per category".format(STATE_CATEGORY))
        print("{}) See correlation between insurance and elder health.".format(CORRELATION))
        print("{}) Help".format(HELP))
        print("{}) Close the US health database".format(QUIT))
        try:
            query_type = int(input("Enter query type: "))
        except ValueError:
            print("Invalid input, numeric query type only.")
            continue
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
       
        elif query_type == STATE_CATEGORY:
            category_id = input('Enter catagory type: ')
            year = input('Enter year: ')
            state = input('Enter state: ')
            rec = db.search_by_catagory_type_state(category_id, year, state)
            data = dict()
            for i in range(len(rec)):
                data[rec[i][1]] = rec[i][0]
            for key in data.keys():
                gui.binaryPieChart(key, data[key])   


        elif query_type == CORRELATION:
            question = input("Enter question code: ")
            rec = db.insurance_correlation(question)
            if(len(rec) <= 50):
                print('No results found, question code not present.')
            else:
                gui.plot3(pd.DataFrame(rec))
                
        elif query_type == HELP:
            print('1) Get category codes.')
            print('2) Get disease codes')
            print('3) Get question codes.')
            command = int(input('Enter command: '))
            if command == 1:
                rec = db.get_category_ids()
                for i in range(len(rec)):
                    print('Code: {} -> English: {}'.format(rec[i][0], rec[i][1]))
            elif command ==2:
                rec = db.getDiseaseID()
                for i in range(len(rec)):
                    print('DiseaseID: {} -> English: {}'.format(rec[i][0], rec[i][1]))
                print()
            elif command ==3:
                rec = db.getQuestionID()
                for i in range(len(rec)):
                    print('QuestionID: {} -> English: {}'.format(rec[i][0], rec[i][1]))
                print()
        elif query_type == QUIT:
            print("Bye!")
            db.quit()
            break
        
        
    
    