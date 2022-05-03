from encodings import utf_8
import json
def convert(file1,file2):
    with open('../Datasets/'+file1,'r') as f:
        j = json.load(f)
    with open('../Datasets/'+file2,'w',encoding="utf_8") as fw:
        fw.write(json.dumps(j,ensure_ascii=False,indent=4))

if __name__ == "__main__":
    convert('restaurants서대문3.json','신촌3.json')
