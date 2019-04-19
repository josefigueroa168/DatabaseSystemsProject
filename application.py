import database

#Steps to add a new generic query

def shell():
    command = input("health$ ")
    if command==commands[0]:
        return -1
    elif command==commands[1]:
        print("Commands:")
        for i in commands:
            print(" " + i)
    else:
        #Step 2: Write a new elif conditional below
        if command==commands[2]:
            abbr = input("Enter state abbreviation: ")
            sql = "select * from census where state = '" + abbr + "';"
        elif command==commands[3]:
            state = input("Enter state name: ")
            sql = "select stateAbbr from state where stateName = '" + state + "';"
        print(db.run_query(sql))
    return 0

#Step 1: Add query command name to this list
commands=["quit","help","abbr","state"]

if __name__ == "__main__":
    db = database.database()
    print("Health Application Shell")
    while shell()==0:
    	pass
    print("Shell Terminated")