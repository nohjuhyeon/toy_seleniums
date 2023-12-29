# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time


def getBrowserFromURI(uri):
    webdriver_manager_directory = ChromeDriverManager().install()
    # ChromeDriver 실행
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
    # Chrome WebDriver의 capabilities 속성 사용
    capabilities = browser.capabilities
    # - 주소 입력(https://www.w3schools.com/)
    browser.get(uri)
    pass

    return browser
def mongodb(client,DB,collection_name):                         # mongodb 연결
    from pymongo import MongoClient
    mongo_client = MongoClient(client)
    Database = mongo_client[DB] 
    collection = Database[collection_name] 
    collection.delete_many({})
    return collection       
def page_shift(browser,collection):  
        from selenium.webdriver.common.by import By
        for i in range(5):
            try:
                item_name = browser.find_element(by=By.CSS_SELECTOR,value = "#product-atf > section > div.css-1qy9c46.ezpe9l12 > h1").text                  # 제품 이름 찾기
                item_list = browser.find_elements(by=By.CSS_SELECTOR, value="#review > section > div:nth-child(3) > div.css-169773r.e36z05c8")
                for item in item_list:
                    user_name = item.find_element(by=By.CSS_SELECTOR,value = "span.css-f3vz0n.e36z05c5").text                                           # 사용자 이름 찾기
                    item_type = item.find_element(by=By.CSS_SELECTOR,value = "div.css-18pn4xv.e36z05c9 > h3").text                                      # 제품 종류 찾기
                    item_content = item.find_element(by=By.CSS_SELECTOR,value = "article > div > p").text                                               # 리뷰 내용 찾기
                    review_date= item.find_element(by=By.CSS_SELECTOR,value = "article > div > footer > div > span").text                               # 리뷰 날짜 찾기
                    try:
                        recommend = item.find_element(by=By.CSS_SELECTOR,value=" footer > button > span:nth-child(2)").text.split()[1]                  # 추천 수 찾기
                    except: 
                        recommend = 0                                                                                                                   # 추천 수가 없으면 0 
                    collection.insert_one({"제품 이름" : item_name,                                                                                      # DB에 전송
                                            "사용자":user_name,
                                            "제품 종류": item_type,
                                    "등록 날짜": review_date,
                                    "내용": item_content,
                                    "추천 수": recommend}
                                    )
                browser.find_element(by=By.CSS_SELECTOR,value="#review > section > div:nth-child(3) > div.css-jz9m4p.ebs5rpx3 > button.css-1orps7k.ebs5rpx0").click()       # 다음 페이지 이동
                time.sleep(1)
            except:
                break
        return 0

if __name__ == "__main__":
    try: 
        browser = getBrowserFromURI("https://www.kurly.com/goods/5086757")
        collection = mongodb("mongodb://192.168.10.184:27017/","toy_seleniums","kurly_review" )
        page_shift(browser,collection)
        pass
    except:
        pass        # 업무 코드 문제 발생 시 대처 코드
    finally:
        pass        # try나 except이 끝난 후 무조건 실행 코드

    pass

