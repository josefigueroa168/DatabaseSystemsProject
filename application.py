import database

if __name__ == "__main__":
    db = database.database()
    sql = "select * from census where state = 'NY';"
    print(db.run_query(sql))