import database
import gui

if __name__ == "__main__":
    db = database.database()
    
    print("Welcome to the US health database")

    while True:
        print("1) Search the US by disease code")
        print("3) Insurance Correlation:")
        print("4) Close the US health database")
        query_type = int(input("Enter query type: "))
        if query_type == 1:
            disease = input("Enter disease code: ")
            rec = db.search_us_by_disease_stats(disease)
            if(len(rec) == 0):
                print('No results found, disease code not present')
            else:
                data = dict()
                for i in range(len(rec)):
                    data[rec[i][0]] = rec[i][1]
                gui.plot1(data, disease)
        if query_type == 3:
            question = input("Enter question code: ")
            rec = db.insurance_correlation(question)
            if(len(rec) == 0):
                print('No results found, question code not present.')
            
        elif query_type == 4:
            db.quit()
            break
        
        
    
    