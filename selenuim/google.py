from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)


driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")  # 이름 혹은 클레스명 
elem.send_keys("명언") # 거기에 키보드 입력처럼 값 전달 가능 
elem.send_keys(Keys.RETURN) # 엔터키를 의미함 
driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click() # css 명을 가지고 선택  브라우저에서 rg_i Q4LuWd 이렇게 되어 있는걸 공백사이에 .으로 연결 그리고 맨앞에 클레스다 알려주는 . 입력
time.sleep(3)
imgUrl = driver.find_element_by_css_selector(".n3VNCb.KAlRDb").get_attribute("src")
urllib.request.urlretrieve(imgUrl, "test.jpg")
# 이러면 class를 가진 요소를 선택하는 선택자가 됨 



# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()