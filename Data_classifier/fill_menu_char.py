import openpyxl
from pprint import pprint

def get_keyword_charac():
    load_wb = openpyxl.load_workbook('./Menu_charac/data/menu_key.xlsx', data_only=True)
    load_ws = load_wb['menu_key']
    menu_keys = {}
    for row in load_ws.iter_rows(min_row=2):
        key_charac = []
        key_charac.append(['isSoup',row[1].value])
        key_charac.append(['isSpicy',row[2].value])
        key_charac.append(['isSweet',row[3].value])
        key_charac.append(['isHot',row[4].value])
        key_charac.append(['isMeet',row[5].value])
        key_charac.append(['isNoodle',row[6].value])
        key_charac.append(['isRice',row[7].value])
        key_charac.append(['isBread',row[8].value])
        menu_keys[row[0].value] = key_charac
    #pprint(menu_keys)
    return menu_keys

def get_menu():
    load_wb = openpyxl.load_workbook('../Datasets/menu_data.xlsx', data_only=True)
    load_ws = load_wb['menu']
    menu = []
    for row in load_ws['B']:
        menu.append(row.value)
    menu.pop(0)
    return menu;

def fill_charac(menu, menu_keys):
    menu_charac = {}
    for m in menu:
        has_key = False
        charac = []
        charac2 = [['isSoup',False],['isSpicy',False],['isSweet',False],['isHot',False],['isMeet',False],['isNoodle',False],['isRice',False],['isBread',False]]
        for k in menu_keys.keys():
            if m.find(k) != -1:
                has_key = True
                for i in menu_keys[k]:
                    if i[1] == 1:
                        charac.append(i[0])
                charac_s = set(charac)
                charac = list(charac_s)
                #print(charac)
        #if has_key == False:
        #    print(m)
        for i in charac2:
            for j in charac:
                if i[0] == j:
                    i[1] = True
        menu_charac[m] = charac2
    pprint(menu_charac)


if __name__ == "__main__":
    menu_keys = get_keyword_charac()
    menu = get_menu()
    fill_charac(menu, menu_keys)
