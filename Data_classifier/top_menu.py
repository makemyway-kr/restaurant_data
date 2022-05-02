import json
import jellyfish

def get_restaurant(filename):
    data = {}
    with open ('../Datasets/'+filename,'r',encoding='utf-8') as f:
        data = json.load(f)
    return data

def top_menu(dict_of_res): #대표메뉴 뽑아넣기
    temp = {}
    for i in dict_of_res.keys():
        for l in dict_of_res[i]:
            if l[0] == "메뉴" and l[1] != "메뉴 정보 없음":
                menus = l[1]
                keys = list(menus.keys())
                temp[i] = keys[0]
    return temp

def write_json(dict,filename):
    with open ('../Datasets/top_menus/'+filename.split('.')[0]+'대표메뉴'+'.json','w',encoding='utf-8') as f:
        print(filename+'\n',dict)
        j_ob = json.dumps(dict,ensure_ascii=False)
        f.write(j_ob)

if __name__ == "__main__":
    file = ['설입.json','신촌1.json','신촌2.json','신촌3.json','상도동1.json','상도동2.json','상도동3.json']
    for f in file:
        temp = get_restaurant(f)
        towrite = top_menu(temp)
        write_json(towrite,f)