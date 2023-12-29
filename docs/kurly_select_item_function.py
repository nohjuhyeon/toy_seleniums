# 업무 : function 1(클릭해서 상세 정보 들어가기), function 2(나가기) function 3(페이지 넘기기)

# 웹 크롤링 동작      # 셀레니움에서 웹드라이버 임포트
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
def getbrowserfromuri(uri):
    webdriver_manager_directory = ChromeDriverManager().install()
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

    # ChromeDriver 실행

    # Chrome WebDriver의 capabilities 속성 사용
    capabilities = browser.capabilities

    # - 주소 입력
    browser.get(uri)

    # - 가능 여부에 대한 OK 받음
    pass
    # - html 파일 받음(and 확인)
    browser.page_source
    return browser

# - 정보 획득
#container > div > div.css-1d3w5wq.ef36txc6 > div.css-rdz8z7.e82lnfz1 > a:nth-child(5)
def get_items(browser) :
    from selenium.webdriver.common.by import By
    # 다음페이지로 이동하기
    #container > div > div.css-1d3w5wq.ef36txc6 > div.css-rdz8z7.e82lnfz1 > a:nth-child(7)
    list_page = browser.find_elements(by=By.CSS_SELECTOR, value='div.css-rdz8z7.e82lnfz1 > a')
    for i in range(2,len(list_page)-2) :
        list_page = browser.find_elements(by=By.CSS_SELECTOR, value='div.css-rdz8z7.e82lnfz1 > a')
        list_page[i].click()
        time.sleep(2)    
        # 상품 리스트 : #container > div > div.css-1d3w5wq.ef36txc6 > div.css-11kh0cw.ef36txc5 > a:nth-child(1)
        element_lists_items = browser.find_elements(by=By.CSS_SELECTOR, value="div.css-11kh0cw.ef36txc5 > a")
        for item in range(len(element_lists_items)) :
            element_lists_items = browser.find_elements(by=By.CSS_SELECTOR, value="div.css-11kh0cw.ef36txc5 > a")
        # for item in range(3):
        # 상품 클릭해서 상세 정보 들어가기
        #container > div > div.css-1d3w5wq.ef36txc6 > div.css-11kh0cw.ef36txc5 > a:nth-child(1) > div.css-0.e1c07x4811 > div > span > img
            value_click = "div.css-11kh0cw.ef36txc5 > a:nth-child({})".format(item+1)
            browser.find_element(by=By.CSS_SELECTOR, value=value_click).click()
            time.sleep(1)

        # 제품 리스트로 이동(현재 브라우저 창에서 뒤로가기)
            browser.back()  
            time.sleep(1)
            pass

        pass
uri = "https://www.kurly.com/collection-groups/market-best?page=1&collection=market-best"
browser = getbrowserfromuri(uri)
get_items(browser)