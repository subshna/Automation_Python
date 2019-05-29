import pyodbc

dbpath = '../../Resources/Student_Information.accdb'

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
                      r'DBQ =E:/Subash/Python/SeleniumAutomation/Resources/Student_Information.accdb'
                      )
cursor = conn.cursor()

cursor.execute('Select * from students')

for row in cursor.fetchall():
    print (row)

cursor.close()
conn.close()