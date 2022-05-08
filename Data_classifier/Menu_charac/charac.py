import json
def read_json( filename ):
    data = {}
    with open ('../../Datasets/'+filename,'r',encoding='utf-8') as f:
        data = json.load(f)
        f.close()
    return data

def get_top_menus(filenames):
    data = {}
    for f in filenames:
        data.update(read_json(f))
    top_menus = []
    for d in data.keys():
        if data[d][-2][0] == "대표메뉴" and data[d][-2][1] != "대표메뉴 없음" and data[d][-2][1] not in top_menus:
            top_menus.append(data[d][-2][1])
    
