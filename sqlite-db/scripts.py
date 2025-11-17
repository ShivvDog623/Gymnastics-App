from sqlite_db_con import SqliteDBCon

db = SqliteDBCon()
cur = db.getCursor()

def createGymnastsTable():
    cur.execute('''CREATE TABLE IF NOT EXISTS gymnasts(
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gym TEXT NOT NULL,
    level INTEGER NOT NULL
)''')
    db.getConnection().commit()

def insertGymnast(first_name, last_name, gym, level):
    cur.execute(f'''INSERT INTO gymnasts (first_name, last_name, gym, level)
                VALUES ('{first_name}', '{last_name}', '{gym}', {level})''')
    print(f"Created Gymnast {first_name}, {last_name}")
    
    db.getConnection().commit()

def getAllGymnasts():
    cur.execute('SELECT * FROM gymnasts')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    

def getGymnastById(id):
    cur.execute(f"SELECT * FROM gymnasts WHERE id = ?", (id,))
    row = cur.fetchone()
    if row == None:
        print("Gymnast is not registered")
    else:
        print(row)
    return row
    


def deleteOneGymnast(id):
    cur.execute(f"DELETE FROM gymnasts WHERE id = ?", (id,))
    print("Deleted Gymnast")
    db.getConnection().commit()

            
            
        


if __name__ == "__main__":
    # createGymnastsTable()
    # insertGymnast("Luigi", "Plumber", "Mushroom Gym", 8)
    # getAllGymnasts()
    # deleteOneGymnast(8)
    getGymnastById(7)