import pandas as pd
import json
csv_file = pd.read_csv('restaurant_menu_data.csv', sep=',', encoding='cp949')
csv_file.to_json('restaurant_menu.json', orient='records', force_ascii=False)

with open('restaurant_menu.json', 'r', encoding='utf-8') as f:
    temp = json.load(f)
    with open('restaurant_menu.json', 'w', encoding='utf-8') as fw:
        fw.write(json.dumps(temp, indent=4, ensure_ascii=False))
