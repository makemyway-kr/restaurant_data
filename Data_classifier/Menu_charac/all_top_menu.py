import json
def read_json( filename ):
    data = {}
    with open ('../../Datasets/top_menus/'+filename+'.json','r',encoding='utf-8') as f:
        data = json.load(f)
        f.close()
    return data

def get_top_menus(filenames):
    data = {}
    for f in filenames:
        data.update(read_json(f))
    top_menus = []
    for d in data.keys():
            top_menus.append(data[d])
    with open ('./topmenus.json','w',encoding='utf-8') as f:
        f.write(json.dumps(top_menus,ensure_ascii=False,indent=4))

if __name__ == "__main__":
    get_top_menus(['상도동1대표메뉴','상도동2대표메뉴','상도동3대표메뉴','신촌1대표메뉴','신촌2대표메뉴','신촌3대표메뉴','설입대표메뉴'])
    
