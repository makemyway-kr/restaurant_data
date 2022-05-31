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
    cursor.execute('INSERT INTO restaurant (id,name,external_star,restaurant_add,business_date,start_time,fin_time,best_menu,franchise,internal_star,restaurant_type) values(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);',
                   (restaurants[r]['id'], restaurants[r]['name'], restaurants[r]['external_star'], restaurants[r]['address_id'], restaurants[r]['business_date'], restaurants[r]['starttime'], restaurants[r]['fintime'], restaurants[r]['bestmenu_id'], restaurants[r]['franchise'], restaurants[r]['internal_star'], restaurants[r]['restaurant_type']))
    Database.commit()
cursor.fetchall()
Database.close()
