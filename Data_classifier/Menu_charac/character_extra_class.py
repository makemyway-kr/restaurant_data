import json
import openpyxl
from pprint import pprint

def get_keyword_charac():
    load_wb = openpyxl.load_workbook('../../DB_cell/menu_key.xlsx', data_only=True)
    load_ws = load_wb['menu_key']
    menu_keys = {}
    for row in load_ws.iter_rows(min_row=2):
        key_charac = []
        key_charac.append(['isSoup',row[1].value])
        key_charac.append(['isSpicy',row[2].value])
        key_charac.append(['isSweet',row[3].value])
        key_charac.append(['isHot',row[4].value])
        key_charac.append(['isMeat',row[5].value])
        key_charac.append(['isNoodle',row[6].value])
        key_charac.append(['isRice',row[7].value])
        key_charac.append(['isBread',row[8].value])
        menu_keys[row[0].value] = key_charac
    #pprint(menu_keys)
    return menu_keys

def get_all_menus():
    data = []
    with open ('./allmenus.json','r',encoding='utf-8') as f:
        data = json.load(f)
        f.close()
    #pprint(data)
    return data

def filtering_charac(menu, menu_keys):
    extra_menu = []
    for m in menu:
        has_key = 0
        for k in menu_keys.keys():
            if m.find(k) != -1:
                has_key = 1

        if has_key == False:
            extra_menu.append(m)
            #print(m)
    return extra_menu

def classifier(data):
    result = {}
    for d in data:
        temp= d.split(' ')
        for t in temp:
            if t[0] == '(':
                continue
            for i in range(2,len(t)):
                for k in range(len(t)-i+1):
                    if '(' not in t[k:k+i] and ')' not in t[k:k+i] and '\n' not in t[k:k+i]:
                        if t[k:k+i] not in result.keys():
                            result[t[k:k+i]] = 1
                        else :
                            result[t[k:k+i]] += 1
    result = [ j for j in result if result[j] >= 2]
    return result

def get_top_menu_key():
    key = []
    filenames = ['classified.json','c2.json','c3.json']
    for i in filenames:
        with open ('./data/'+i,'r',encoding='utf-8') as f:
            data = json.load(f)
            key += data[1]
            f.close()
    return key

def remove_duplicated_key(menu_key,top_key):
    for m in menu_key:
        for t in top_key:
            if m == t:
                menu_key.remove(m)
                print(m)
    return menu_key

def write_json(data):
    with open ('./data/classified2.json','w',encoding='utf-8') as f:
        f.write(json.dumps(data,ensure_ascii=False,indent=4))

if __name__ == "__main__":
    menu_keys = get_keyword_charac()
    menu = get_all_menus()
    extra_menu = filtering_charac(menu,menu_keys)
    menu_key = classifier(extra_menu)
    top_key = get_top_menu_key()
    extra_key = remove_duplicated_key(menu_key,top_key)
    write_json(extra_key)
