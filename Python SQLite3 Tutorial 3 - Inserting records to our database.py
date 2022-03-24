import sqlite3

dbase = sqlite3.connect('Our_data.db') # Open a database File


dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_records(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    DIVISION TEXT NOT NULL,
    STARS INT NOT NULL) ''')


dbase.execute(''' INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
        VALUES(5,'James','Maintenance',4)
''')

dbase.commit()


dbase.close()

