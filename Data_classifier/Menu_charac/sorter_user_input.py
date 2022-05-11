import json
from operator import indexOf
def ui():
    filename = input("데이터를 끌어올 파일명을 입력하세요: ")
    data = []
    try:
        with open('./data/'+filename,'r',encoding = 'utf-8') as f:
            data = json.load(f)
            f.close()
    except Exception as ex:
        filename = input("오류발생 . 데이터를 끌어올 파일명을 입력하세요 : ")
    to_erase = []
    start = indexOf(data[1],data[0])
    for i in range(start,len(data[1])):
        selection = input("해당 키워드를 삭제할까요? (y/n) , 입력없음은 n처리. c 는 중단하고 임시저장.\n "+data[1][i] + ':')
        if selection == 'y':
            data[0] = data[1][i]
        elif selection == "c":
            break
        else:
            to_erase.append(data[1][i])
    savefile = input('결과를 저장할 파일명을 입력하세요: ')
    data[1] = [ data[1][i] for i in range (len(data[1])) if data[1][i] not in to_erase] 
    savefile = input('결과를 저장할 파일명을 입력하세요: ')
    with open ('./data/'+savefile,'w',encoding='utf-8') as f:
        f.write(json.dumps(data,ensure_ascii=False,indent=4))
        f.close()

if __name__ == "__main__":
    ui()
