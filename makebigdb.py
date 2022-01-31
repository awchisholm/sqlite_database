#!/usr/bin/env python3
import random
import pandas as pd
import sqlite3
size = range(1,10000000)
index_values = [str(item).zfill(8) for item in size]
values = [random.random() for item in size]
bigdf = pd.DataFrame({'the_index': index_values, 'not_the_index': index_values, 'value': values})
con = sqlite3.connect('bigdb.db')
bigdf.to_sql('big_table', con=con, if_exists='replace', index=False)
cursor = con.cursor()
createIndexStatement = 'CREATE INDEX "pk_index" ON "big_table" ("the_index")'
cursor.execute(createIndexStatement)
con.commit()
con.close()
