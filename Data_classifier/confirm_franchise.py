import openpyxl
import json
from encodings import utf_8
import re
from difflib import SequenceMatcher

def get_restaurant(filename):
    data = {}
    with open ('../Datasets/'+filename,'r',encoding='utf-8') as f:
        data = json.load(f)
        f.close()
    return data

def get_franchise_restaurant():
    data = []
    sheet = ['한식','분식','중식','일식','양식','기타외국식','패스트푸드','치킨','피자','제과제빵','아이스크림빙수','커피', '음료_커피외','주점','기타외식']

    read_wb = openpyxl.load_workbook('../Datasets/전국프랜차이즈리스트.xlsx',data_only = True)
    for s in sheet:
        read_ws = read_wb[s]
        for row in read_ws['C']:
            temp = str(row.value).lower()
            if temp.find('(') == -1:
                data.append(temp)
            else:
                data.append(temp.split('(')[1].split(')')[0])
                data.append(temp.split('(')[0] + temp.split(')')[1])
    return data

def add_franchise(dict_of_res,franchise_list):
    for i in dict_of_res.keys():
        is_fr = False
        k=[]
        k.append('프랜차이즈')
        t = i.split(' ')
        del t[0]
        if len(t) > 1 and t[-1][-1] == '점':
            del t[-1]
        name = ' '.join(t)
        if name.find('(') != -1:
            name = name.split('(')[0] + name.split(')')[1]
        for j in franchise_list:
            if SequenceMatcher(None, j, name).ratio() > 0.8:
                is_fr = True
                print(j + ' / ' + name)
        if is_fr:
            k.append('True')
        else:
            k.append('False')
        dict_of_res[i].append(k)

def write_json(dict,filename):
    to_write = json.dumps(dict,ensure_ascii=False,indent=4)
    print("\n"+filename + "\n\n\n"+to_write)
    with open ('../Datasets/'+filename,'w',encoding='utf_8') as fw:
        fw.write(to_write)
        fw.close()


if __name__ == "__main__":
    franchise_list = get_franchise_restaurant()
    restaurant_dic = {}
    file = ['설입.json','신촌1.json','신촌2.json','신촌3.json','상도동1.json','상도동2.json','상도동3.json']
    for f in file:
        temp = get_restaurant(f)
        add_franchise(temp,franchise_list)
        write_json(temp,f)
