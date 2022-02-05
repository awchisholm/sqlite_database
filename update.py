import sqlite3
database = 'college.db'

update_sql = 'UPDATE tutor set FirstName = "Felonius", Surname="Gru" where TutorId = 2'

con = sqlite3.connect(database)
cur = con.cursor()
cur.executescript(update_sql)
con.commit()
con.close()