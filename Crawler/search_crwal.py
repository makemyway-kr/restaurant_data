import openpyxl
import os
import sys
import time
import json
from urllib.parse import quote_plus
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import multiprocessing
from pprint import pprint

def save_images(images, save_path):
    try:
        for index, image in enumerate(images[:5000]):
            print(index)
            src = image.get_attribute('src')
            t = urlopen(src).read()
            file = open(os.path.join(save_path, str(index + 1) + ".jpg"),"wb")
            file.write(t)
            print("img save " + save_path + str(index + 1) + ".jpg")
    except Exception as e2:
        print(e2)

def create_folder_if_not_exists(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

def make_url(search_term):
    # 네이버 이미지 검색
    base_url = 'https://search.naver.com/search.naver?where=image&section=image&query='
    # CCL 상업적 이용 가능 옵션
    #end_url = '&res_fr=0&res_to=0&sm=tab_opt&color=&ccl=2' \
              #'&nso=so%3Ar%2Ca%3Aall%2Cp%3Aall&recent=0&datetype=0&startdate=0&enddate=0&gif=0&optStr=&nso_open=1'
    return base_url + quote_plus(search_term)

def crawl(search_term):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome('./101/chromedriver',options=options)

    url = make_url(search_term)

    driver.get(url)
    driver.implicitly_wait(time_to_wait=2)
    #elem =  driver.find_element(by=By.TAG_NAME, value = "body")
    #for i in range(10000):
    #    elem.send_keys(Keys.PAGE_DOWN)
    #    time.sleep(0.1)
    for _ in range(10000):
        driver.execute_script("window.scrollBy(0,20000)")
    images = driver.find_elements(by=By.CLASS_NAME, value = "_image._listImage")
    save_path = "../search_image/" + search_term + "/"
    create_folder_if_not_exists(save_path)
    save_images(images,save_path)

    time.sleep(3)

if __name__ == '__main__':
    crawl(input('원하는 검색어: '))
