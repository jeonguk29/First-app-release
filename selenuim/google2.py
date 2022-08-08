from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
elem = driver.find_element_by_name("q") # 검색창 찾아서
elem.send_keys("우기플리")  # 우기플리
elem.send_keys(Keys.RETURN) # 엔터 입력

SCROLL_PAUSE_TIME = 1 # 스크롤 높이 저장 
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height: # 이전스크롤 높이 랑 새로운 스크롤 높이가똑같으면 더이상 내려 갈 곳이 없음 
        try:
            driver.find_element_by_css_selector(".mye4qd").click() # 결과 더 보기 버튼이 있으면 계속 내려고
        except:
            break # 더 없으면 종료 
    last_height = new_height  


# 이후 작은 이미지 들을 묶어 저장한다음 
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") 
count = 1

for image in images: # 하나씩 빼서 
    try:
        image.click() # 클릭 해서 큰 이미지 선택한후 
        time.sleep(2)
        # url 저장후 
        imgUrl = driver.find_element_by_xpath('/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute("src")
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)

        # 파일 이름 바꿔서 저장 
        urllib.request.urlretrieve(imgUrl, str(count) + ".jpg")
        count = count + 1
        if count == 20 :
            break
    except:
        pass

driver.close()
