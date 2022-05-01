from encodings import utf_8
import json
def convert(file1,file2):
    with open('./'+file1,'r') as f:
        j = json.load(f)
    with open('./'+file2,'w',encoding="utf_8") as fw:
        fw.write(json.dumps(j,ensure_ascii=False))

if __name__ == "__main__":
    convert('restaurants_bongcheon.json','설입.json')
