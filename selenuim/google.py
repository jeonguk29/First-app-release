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
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd") # 전체 이지미 리스트를 담아서 
count = 1 # 이미지 이름 1씩 증가시킬거임 

for image in images:  # 하나씩 이미지를 넣고
    image.click()   # 클릭 
    time.sleep(1)
    imgUrl = driver.find_element_by_css_selector(".n3VNCb.KAlRDb").get_attribute("src") # 3초뒤에 이미지 URL 다운 받아서 
    urllib.request.urlretrieve(imgUrl, str(count) + ".jpg") 
    count = count + 1




# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()