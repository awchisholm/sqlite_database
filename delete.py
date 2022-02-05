import sqlite3

database = 'college.db'

update_sql = 'DELETE FROM tutor where FirstName = "Felonius"'

con = sqlite3.connect(database)
cur = con.cursor()
cur.executescript(update_sql)
con.commit()
con.close()