import json
import sqlite3

JSON_FILE = "/home/asad/Downloads/movies-master/movies/imdb.json"
DB_FILE = "/home/asad/Downloads/movies-master/MovieDatabase_V4.db"

traffic = json.load(open(JSON_FILE))
conn = sqlite3.connect(DB_FILE)

print traffic

count = 1
for x in traffic:
	count +=1
	data = [count,x['name'],'English',x['director'],x['genre'][0]]
	c = conn.cursor()
	c.execute('insert into MovieDB_movie values (?,?,?,?,?)', data)

conn.commit()
c.close()