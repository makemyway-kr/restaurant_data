import json
def classifier():
    result = {}
    data = []
    with open ('./topmenus.json','r',encoding='utf-8') as f:
        data = json.load(f)
        f.close()
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
    with open ('./classified.json','w',encoding='utf-8') as f:
        f.write(json.dumps(result,ensure_ascii=False,indent=4))
classifier()