import openpyxl
import os
import sys
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import multiprocessing
#엑셀에서 데이터 추출(형식 : ㅇㅇ동 ㅁㅁ식당)
def crawl(filename):
    restaurant_file = openpyxl.load_workbook(filename)
    restaurants = restaurant_file.worksheets[0]
    data = []

    for restaurant in restaurants.iter_rows(min_row=3):
        address = restaurant[16].value
        if address is not None:
            if address.split('(')[1].split(')')[0] == "상도동": #동 필터링
                data.append([
                    restaurant[16].value.split('(')[1].split(')')[0],
                    restaurant[18].value,
                    restaurant[16].value
                    ])

    #data = [['봉천동','삼우식당','주소1'],['중랑구','커피나무','주소2'],["숭실대","마루스시",'주소3']]

    json_data = {}
    file_path = "./restaurants"+filename+".json"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome('./100./chromedriver',options=options)

    '''
    #json에서 값 가져오는 코드
    with open(file_path,'r') as file:
        test_data = json.load(file)
    print(test_data)
    '''

    for i in data:
        keyword = i[0] + ' ' + i[1]
        print(keyword, end=" ")
        try:
            content = {}
            kakao_map_search_url = f"https://map.kakao.com/?q={keyword}"
            driver.get(kakao_map_search_url)
            driver.implicitly_wait(time_to_wait=2)

            #rateNum = driver.find_element(by='xpath',value = '//*[@id="info.search.place.list"]/li[1]/div[4]/span[1]/em').text
            #periodTime = driver.find_element(by='xpath',value = '//*[@id="info.search.place.list"]/li[1]/div[5]/div[3]/p/a').text
            #print("평점 " + rateNum + '\n영업시간 ' + periodTime)

            newlink = driver.find_element(by='xpath',value = '//*[@id="info.search.place.list"]/li[1]/div[5]/div[4]/a[1]').send_keys(Keys.ENTER)
            driver.switch_to.window(driver.window_handles[-1])

            try:
                rateNum = driver.find_element(by='xpath',value = '//*[@id="mArticle"]/div[1]/div[1]/div[2]/div/div/a[1]/span[1]').text
            except Exception as e1:
                rateNum = "평점 없음"
                pass

            try:
                callNum = driver.find_element(by=By.CLASS_NAME,value = 'txt_contact').text
            except Exception as e1:
                callNum = "전화번호 없음"
                pass

            time = ' '
            try:
                Timelist = driver.find_element(by=By.CLASS_NAME, value = 'list_operation')
                periodTime = Timelist.find_elements(by=By.CLASS_NAME, value = 'txt_operation')
                detailTime = Timelist.find_elements(by=By.CLASS_NAME, value = 'time_operation')
            except Exception as e1:
                time = '시간 정보 없음'

            menus_dic = {}
            try:
                menulist = driver.find_element(by=By.CLASS_NAME, value = 'list_menu')
                menus = menulist.find_elements(by=By.CLASS_NAME, value = 'loss_word')
                menus_price = menulist.find_elements(by=By.CLASS_NAME, value = 'price_menu')
                for a,b in zip(menus,menus_price):
                    menus_dic[a.text] = b.text
            except Exception as e1:
                pass


            print("평점 " + rateNum)
            content["평점"] = rateNum

            print("전화번호 " + callNum)
            content["전화번호"] = callNum

            print("주소 " + i[2])
            content["주소"] = i[2]
            if time == '시간 정보 없음':
                print("시간 정보 없음")
                content["영업 시간"] = "시간 정보 없음"
            else:
                if detailTime:
                    time = []
                    for i in periodTime:
                        time.append(i.text)
                        print(i.text)
                    content["영업 시간"] = time
                else:
                    print("시간 정보 없음")
                    content["영업 시간"] = "시간 정보 없음"

            if not menus_dic:
                print("메뉴 정보 없음")
                content["메뉴"] = "메뉴 정보 없음"
            else:
                for i in menus_dic:
                    print("key: {}, value: {}".format(i, menus_dic[i]))
                    content["메뉴"] = menus_dic

            json_data[keyword] = list(content.items())
            driver.close()
            driver.switch_to.window(driver.window_handles[0]);

        except Exception as e1:
            print("정보 없음")
            driver.switch_to.window(driver.window_handles[0]);
            pass

        print('\n')

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4)
    driver.close()

if __name__ == "__main__":
    start_time = time.time()
    f_list = ["동작구레스토랑1.xlsx","동작구레스토랑2.xlsx","동작구레스토랑3.xlsx"]
    pool = multiprocessing.Pool(processes=3)
    pool.map(crawl,f_list)
    pool.close()
    pool.join()
    print(time.time()-start_time)