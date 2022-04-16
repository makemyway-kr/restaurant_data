import os
import requests
import json
def get_district():
    district = {}
    with open("../place.txt","rt",encoding= 'utf-8') as f :
        while True : 
            line = f.readline()
            if not line:
                break
            elif line == '':
                break
            else:
                tmp = line.split(',')
                if tmp[0] not in district.keys():
                    district[tmp[0]] = [tmp[1].replace('\n','')]
                else:
                    district[tmp[0]].append(tmp[1].replace('\n',''))
                