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

def get_restaurant_info():
    restaurant_data = []
    address_data = []
    data = []
    load_wb = openpyxl.load_workbook('../DB_cell/restaurant_data.xlsx', data_only=True)
    load_ws = load_wb['restaurant']
    for row in load_ws.iter_rows(min_row=2):
        restaurant_data.append([row[1].value,row[3].value]) #식당명, 주소Id

    load_wb2 = openpyxl.load_workbook('../DB_cell/address_data.xlsx', data_only=True)
    load_ws2 = load_wb2['address']
    for row in load_ws2.iter_rows(min_row=2):
        address_data.append([row[0].value,row[2].value]) #주소Id, district

    for r in restaurant_data:
        for a in address_data:
            if r[1] == a[0]:
                data.append(a[1] + ' ' + r[0])
                break
    #pprint(data)
    return data

def save_images(images, save_path):
    try:
        for index, image in enumerate(images[:10]):
            print(index)
            src = image.get_attribute('src')
            t = urlopen(src).read()
            file = open(os.path.join(save_path, str(index + 1) + ".jpg"),"wb")
            file.write(t)
            print("img save " + save_path + str(index + 1) + ".jpg")
    except Exception as e2:
        print('tt')

def create_folder_if_not_exists(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

def crawl_restaurant_image(restaurants):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome('./101/chromedriver',options=options)

    for r in restaurants:
        try:
            driver.get("https://naver.com")
            driver.implicitly_wait(time_to_wait=2)
            search_box = driver.find_element(by=By.ID, value = "query")
            search_box.send_keys(r)
            search_box.send_keys(Keys.ENTER)
            driver.implicitly_wait(time_to_wait=2)

            try:
                #restaurantlist = driver.find_element(by=By.CLASS_NAME, value = "_3smbt")
                driver.find_element(by=By.CLASS_NAME, value = "XNxh9").click()
            except Exception as e2:
                driver.find_element(by=By.CLASS_NAME, value = "_2opOK").click()

            driver.switch_to.window(driver.window_handles[-1])
            driver.switch_to.frame("entryIframe")

            try:
                img_type1 = driver.find_element(by='xpath',value = '//*[@id="app-root"]/div/div/div/div[7]/div[2]/div/div/div/div/div[1]/a')
                t = img_type1.text
                img_type1.click()

                save_path = "../restaurant_image/" + r + "/" + t + "/"
                images = driver.find_elements(by=By.CLASS_NAME, value = "_img")
                create_folder_if_not_exists(save_path)
                save_images(images,save_path)
            except Exception as e2:
                pass

            try:
                img_type2 = driver.find_element(by='xpath',value = '//*[@id="app-root"]/div/div/div/div[7]/div[2]/div/div/div/div/div[2]/a')
                t = img_type2.text
                img_type2.click()

                save_path = "../restaurant_image/" + r + "/" + t + "/"
                images = driver.find_elements(by=By.CLASS_NAME, value = "_img")
                create_folder_if_not_exists(save_path)
                save_images(images,save_path)
            except Exception as e2:
                pass

            '''
            try:
                img_type3 = driver.find_element(by='xpath',value = '//*[@id="app-root"]/div/div/div/div[7]/div[2]/div/div/div/div/div[5]/a')
                t = img_type3.text
                img_type2.click()

                save_path = "../restaurant_image/" + r + "/" + t + "/"
                images = driver.find_elements(by=By.CLASS_NAME, value = "_img")
                create_folder_if_not_exists(save_path)
                save_images(images,save_path)
            except Exception as e2:
                print(e2)
                pass
            '''

            time.sleep(3)

            driver.close()
            driver.switch_to.window(driver.window_handles[0]);

        except Exception as e1:
            print(e1)
            print(r + " 정보 없음")
            #driver.switch_to.window(driver.window_handles[0]);
            #pass

if __name__ == '__main__':
    restaurants = ["동작구 마루스시", "동작구 내가 찜한 찜닭", " 동작구 맘스터치"];
    #restaurants = get_restaurant_info()
    crawl_restaurant_image(restaurants)
