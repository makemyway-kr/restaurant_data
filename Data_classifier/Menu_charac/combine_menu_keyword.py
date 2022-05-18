import json
from openpyxl import Workbook

def get_keyword(filename):
    with open('./data/'+filename,'r',encoding='utf_8') as f:
        data = json.load(f)
        f.close()
    return data

def extract_keyword(key_list):
    write_wb = Workbook()
    write_ws = write_wb.create_sheet('menu_key')

    write_ws = write_wb.active
    write_ws = write_wb['menu_key']
    write_ws.append(['name','isSoup','isSpicy','isSweet','isHot','isMeat','isNoodle','isRice','isBread'])

    for i in key_list:
        write_ws.append([i])
    write_wb.save('./data/menu_key.xlsx')

if __name__ == "__main__":
    keyword = []
    data = {}
    file = ['result1.json','result2.json','result3.json']
    for f in file:
        temp = get_keyword(f)
        keyword += temp[1]
    keyword_set = set(keyword)
    keyword = list(keyword_set)
    extract_keyword(keyword)
