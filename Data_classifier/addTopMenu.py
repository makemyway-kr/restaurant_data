import json

def get_restaurant(filename):
    data = {}
    with open ('../Datasets/'+filename,'r',encoding='utf-8') as f:
        data = json.load(f)
        f.close()
    return data

def add_top_menu(dict_of_res): #대표메뉴 뽑아넣기
    temp = {}
    for i in dict_of_res.keys():
        for l in dict_of_res[i]:
            if l[0] == "메뉴":
                t = []
                if l[1] != "메뉴 정보 없음":
                    menus = l[1]
                    keys = list(menus.keys())
                    temp[i] = keys[0]
                    t.append("대표메뉴")
                    t.append(keys[0])
                else:
                    t.append("대표메뉴")
                    t.append("대표메뉴 없음")
                dict_of_res[i].append(t)


def write_json(dict,filename):
    to_write = json.dumps(dict,ensure_ascii=False,indent=4)
    print("\n"+filename + "\n\n\n"+to_write)
    with open ('../Datasets/'+filename,'w',encoding='utf_8') as fw:
        fw.write(to_write)
        fw.close()

if __name__ == "__main__":
    file = ['설입.json','신촌1.json','신촌2.json','신촌3.json','상도동1.json','상도동2.json','상도동3.json']
    for f in file:
        temp = get_restaurant(f)
        add_top_menu(temp)
        write_json(temp,f)
