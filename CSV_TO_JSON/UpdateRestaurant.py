import json
import pymysql

restaurants = {}

Database = pymysql.connect(
    user='admin',
    passwd='',
    host='',
    db='test_db',
)

with open('restaurant2.json', 'r', encoding='utf-8') as f:
    restaurants = json.load(f)

cursor = Database.cursor()

for r in range(len(restaurants)):
    if restaurants[r]['franchise'] == 0:
        print(restaurants[r]['name'])
        cursor.execute('UPDATE restaurant SET franchise = 0 where id =' +
                       str(restaurants[r]['id']) + ';')
print(cursor.execute('SHOW TABLES;'))
Database.commit()
cursor.fetchall()
Database.close()
