# 업무 : function 1(클릭해서 상세 정보 들어가기), function 2(나가기) function 3(페이지 넘기기)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import kurly_get_review_function as review
import kurly_get_review_function as review
import kurly_select_item_function as select
def main(): # self 키워드 필요 (class 소속 확인용)
    try: 
        url = "https://www.kurly.com/collection-groups/market-best?page=1&collection=market-best"
        browser = select.getbrowserfromuri(url)
        collection = review.mongodb("mongodb://192.168.10.240:27017/","toy_seleniums","kurly_review" )
        select.get_items(browser,collection)
        pass        # 업무 코드
    except:
        pass        # 업무 코드 문제 발생 시 대처 코드
    finally:
        pass       # try나 except이 끝난 후 무조건 실행 코드
    pass    # 내용 넣기
    return 0

if __name__ == "__main__":
    try: 
        main()        # 업무 코드
    except:
        pass        # 업무 코드 문제 발생 시 대처 코드
    finally:
        pass        # try나 except이 끝난 후 무조건 실행 코드

    pass

