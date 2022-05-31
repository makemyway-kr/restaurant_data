import json
import pymysql

data = {}

Database = pymysql.connect(
    user='admin',
    passwd='',
    host='',
    db='test_db',
)

with open('restaurant_menu2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

cursor = Database.cursor()

for r in range(len(data)):
    try:
        cursor.execute('INSERT into restaurant_menu (restaurants_id,menus_menu_id) values(' +
                       str(data[r]['restaurant_id']) + ',' + str(data[r]['menu_id']) + ');')
        Database.commit()
    except Exception as e:
        print(e)
        Database.rollback()
        break
Database.close()
