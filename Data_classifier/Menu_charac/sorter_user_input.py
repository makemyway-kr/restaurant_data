import json
def ui():
    filename = input("데이터를 끌어올 파일명을 입력하세요: ")
    data = []
    metadata = [0,0]
    try:
        with open(filename,'r',encoding = 'utf-8') as f:
            data = json.load(f)
            f.close()
    except Exception as ex:
        filename = input("오류발생 . 데이터를 끌어올 파일명을 입력하세요 : ")
    to_erase = []
    temperary_save = False
    for i in data:
        selection = input("해당 키워드를 삭제할까요? (Y/N) , 입력없음은 Y처리. C 는 중단하고 임시저장. "+i + ':')
        if selection == 'N':
            to_erase.append(i)
        elif selection == "C":
            temperary_save = True
            break
    savefile = input('결과를 저장할 파일명을 입력하세요: ')
    if temperary_save == True:
        with open (savefile,'a',encoding='utf-8') as f:
            f.write(json.dumps())
    data = [ i for i in data if i not in to_erase ]
    savefile = input('결과를 저장할 파일명을 입력하세요: ')
    with open (savefile,'w',encoding='utf-8') as f:
        f.write(json.dumps(data,ensure_ascii=False,indent=4))
        f.close()

if __name__ == "__main__":
    ui()
