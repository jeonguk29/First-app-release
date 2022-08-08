#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen

response =  urlopen('https://en.wikipedia.org/wiki/Main_Page') # url 주소를 열어서 response에 주소를 담겠다   아래 코드와 동일 
# with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response: 
soup = BeautifulSoup(response, 'html.parser') # 주소를 넣어주고 html.parser 을 이용해 soup 담아줌 
for anchor in soup.find_all('a'): # 모든 a 태그를 찾아서 
    print(anchor.get('href', '/')) #href 가지고 와서 프린트 해라 
