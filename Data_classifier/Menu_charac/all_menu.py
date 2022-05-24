import json
def get_menu_data(filename):
    data = {}
    menu_data = []
    with open ('../../Datasets/'+filename,'r',encoding='utf-8') as f:
        data = json.load(f)
        f.close()
    for i in data.keys():
        if data[i][4][1] != '메뉴 정보 없음':
            menu_data += list(data[i][4][1].keys())
    return menu_data

def write_menu_json(menu_data):
    with open ('./allmenus.json','w',encoding='utf-8') as f:
        f.write(json.dumps(menu_data,ensure_ascii=False,indent=4))

if __name__ == "__main__":
    menu_data = []
    filenames = ['상도동1.json','상도동2.json','상도동3.json','신촌1.json','신촌2.json','신촌3.json','설입.json']
    for f in filenames:
        menu_data += get_menu_data(f)
    menu_set = set(menu_data)
    menu_data = list(menu_set)
    write_menu_json(menu_data)
    print(len(menu_data))
