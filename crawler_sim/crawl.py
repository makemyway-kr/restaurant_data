import os
import sys
import urllib.request
from dotenv import dotenv_values
config = dotenv_values("../.env")
client_id = config["ID"]
client_secret = config["PW"]
def get_district():
    district = {}
    with open("../place.txt","rt",encoding= 'utf-8') as f :
        while True : 
            line = f.readline()
            if not line:
                break
            elif line == '':
                break
            encText = urllib.parse.quote(line)
            url = "https://openapi.naver.com/v1/search/blog?query=" + encText
            request = urllib.request.Request(url)
            request.add_header("X-Naver-Client-Id",client_id)
            request.add_header("X-Naver-Client-Secret",client_secret)
            response = urllib.request.urlopen(request)
            rescode = response.getcode()
            if(rescode==200):
                response_body = response.read()
                print(response_body.decode('utf-8'))
            else:
                print("Error Code:" + rescode)
